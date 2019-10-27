# -*- coding: utf-8 -*-
import csv
from datetime import datetime

from PyQt5.QtSql import QSqlQuery

from Roadnet import database
from Roadnet.config import AsdTableEnum, RnReportFormat
from Roadnet.roadnet_dialog import StreetReportsAlert

__author__ = 'matthew.bradley'


class StreetReportsExport:
    def __init__(self, db, export_path, options, as_csv, params):
        self.db = db
        self.report_type = RnReportFormat.CSV if as_csv else RnReportFormat.TXT  # Text or CSV enum
        self.export_path = export_path + ".csv" if as_csv else export_path + ".txt"
        self.options = options
        self.report_title = "STREET CHANGES REPORT"
        self.no_content = "\n \nNO RECORDS FOUND \n \n"
        self.org = database.get_from_gaz_metadata(db, "owner")
        self.user = params['UserName']
        self.headers = {
            "streets": ["USRN", "TYPE", "DESCRIPTION", "LOCALITY", "TOWN", "COUNTY", "START DATE", "ENTRY DATE",
                        "UPDATE DATE", "CLOSURE DATE", "UPDATED BY", "CLOSED BY"],
            "srwr": ["USRN", "TYPE", "DESCRIPTION", "LOCALITY", "TOWN", "COUNTY", "CATEGORY", "LOCATION_TEXT"]
        }

    def run_export(self):
        # if the additional table option is selected and no
        # additional tables are selected warns the user
        if self.options['report'] == 'srwr':
            if len(self.options["categories"]) == 0:
                # Please select a category from an additional table
                self._show_alert()
                return False
            else:
                self.report_srwr()
        elif self.options['report'] == 'streets':
            self.report_streets()

        return True

    def report_srwr(self):

        report_fields = ["USRN", "Street_ref_type", "Description", "Locality", "Town", "County", "Category",
                         "location_text"]

        sqlgenericsel = "SELECT s.USRN, s.Description,s.Street_ref_type, l.Name AS Locality, " \
                        "t.Name AS Town, c.name AS County, s.Start_Date, s.Entry_Date, s.Update_Date, " \
                        "s.Closure_Date, s.Updated_By, s.Closed_By "

        sqlgenericfrom = "((tblSTREET s INNER JOIN tlkpTOWN t ON s.Town_Ref = t.Town_Ref) " \
                         "INNER JOIN tlkpCOUNTY c ON s.County_Ref = c.county_ref) " \
                         "INNER JOIN tlkpLOCALITY l ON s.Loc_Ref = l.Loc_Ref "

        # get comma-separated list of srwr categories selected on the form
        selected_categories = self._get_selected_categories(self.options["categories"])
        asd_table = AsdTableEnum(self.options["table"])

        qrys = {
            1: " {}, lrs.Description as Category, m.location_text FROM (( {} ) "
               "INNER JOIN tblMaint m on s.USRN = m.USRN) "
               "LEFT JOIN tlkpRoad_Status lrs on m.Road_Status_ref = lrs.Road_Status_Ref "
               "WHERE s.Currency_flag = 0 AND m.Currency_Flag = 0 AND m.Road_Status_Ref in ( {} ) "
               "ORDER BY s.Street_Ref_Type,s.USRN".format(sqlgenericsel, sqlgenericfrom, selected_categories),

            2: " {}, lrc.Description as Category, rc.location_text FROM (( {} ) "
               "INNER JOIN tblReins_Cat rc on s.USRN = rc.USRN) "
               "LEFT JOIN tlkpReins_Cat lrc on rc.Reinstatement_Code = lrc.Reinstatement_Code "
               "WHERE s.Currency_flag = 0 AND rc.Currency_Flag = 0 AND rc.Reinstatement_Code in ( {} ) "
               "ORDER BY s.Street_Ref_Type,s.USRN".format(sqlgenericsel, sqlgenericfrom, selected_categories),

            3: " {}, lsg.Designation_text as Category,sd.location_text FROM (( {} ) "
               "INNER JOIN tblSpec_Des sd on s.USRN = sd.USRN) "
               "LEFT JOIN tlkpSpec_Des lsg on sd.Designation_Code = lsg.Designation_Code "
               "WHERE s.Currency_flag = 0 AND sd.Currency_Flag = 0 AND sd.Designation_Code in ( {} ) "
               "ORDER BY s.Street_Ref_Type,s.USRN".format(sqlgenericsel, sqlgenericfrom, selected_categories)
        }

        # Setup for writing to file
        section_header = "Street with {} Categories in {}".format(asd_table.name, selected_categories)

        # Run query
        sql = qrys.get(self.options["table"])
        query = QSqlQuery(self.db)
        query.exec_(sql)
        rec = query.record()

        # Get Field positions for avals field list above
        report_field_ids = self._get_report_field_ids(report_fields, rec)

        with open(self.export_path, 'w', newline='') as out_file:
            if self.report_type is RnReportFormat.CSV:
                output_file = self._get_csv_writer(out_file)
            else:
                output_file = out_file

            self.write_report_header(output_file, self.report_type)
            self.write_sub_report_headings(section_header, "", output_file, self.report_type)

            # Write column headers and results
            self.write_column_headers(self.headers['srwr'], output_file, self.report_type)
            self.report_results('srwr', report_field_ids, query, output_file, self.report_type)

            # Add any report footer
            self.write_report_footer(output_file, self.report_type)

    def report_streets(self):
        report_fields = ["USRN", "Street_ref_type", "Description", "Locality", "Town", "County", "Start_Date",
                         "Entry_Date", "Update_Date", "Closure_Date", "Updated_By", "Closed_By"]

        sql_get_streets = "SELECT tblSTREET.USRN, tblStreet.Description,tblSTREET.Street_ref_type, " \
                          "tlkpLOCALITY.Name AS Locality, tlkpTOWN.Name AS Town, tlkpCOUNTY.name AS County, " \
                          "tblStreet.Start_Date, tblStreet.Entry_Date, tblStreet.Update_Date, " \
                          "tblStreet.Closure_Date, tblStreet.Updated_By, tblStreet.Closed_By " \
                          "FROM ((tblSTREET INNER JOIN tlkpTOWN ON tblSTREET.Town_Ref = tlkpTOWN.Town_Ref) " \
                          "INNER JOIN tlkpCOUNTY ON tblSTREET.County_Ref = tlkpCOUNTY.county_ref) " \
                          "INNER JOIN tlkpLOCALITY ON tblSTREET.Loc_Ref = tlkpLOCALITY.Loc_Ref "
        changes_since = self.options["change_date"]
        entry_sql = sql_get_streets + "WHERE tblStreet.Entry_Date > " + changes_since + \
                                      " AND tblStreet.currency_flag = 0"
        closed_sql = sql_get_streets + "WHERE tblStreet.Closure_date > " + changes_since
        changed_sql = sql_get_streets + "WHERE tblStreet.Update_date > " + changes_since + \
                                        " AND tblStreet.currency_flag = 0 " \
                                        "AND tblStreet.Entry_date < " + changes_since

        reports = [
            {'heading': 'New Streets Since ',
             'query': entry_sql},
            {'heading': 'Closed Streets Since ',
             'query': closed_sql},
            {'heading': 'Changed Streets Since ',
             'query': changed_sql}
        ]

        formatted_date = self._format_date(str(changes_since))

        with open(self.export_path, 'w', newline='') as out_file:
            if self.report_type is RnReportFormat.CSV:
                output_file = self._get_csv_writer(out_file)
            else:
                output_file = out_file

            # Write report header
            self.write_report_header(output_file, self.report_type)

            # New records
            query = QSqlQuery(self.db)

            # Loop through New, Closed & Changed sub-reports
            for rep in reports:
                query.exec_(rep['query'])
                rec = query.record()

                # Write sub-report headings
                self.write_sub_report_headings(rep['heading'], formatted_date, output_file, self.report_type)

                # Get Field positions for avals field list above
                report_field_ids = self._get_report_field_ids(report_fields, rec)

                # Write results of query
                self.write_column_headers(self.headers['streets'], output_file, self.report_type)
                self.report_results('streets', report_field_ids, query, output_file, self.report_type)

            self.write_report_footer(output_file, self.report_type)

    def report_results(self, mode, report_field_ids, query, output_file, report_type):
        if report_type is RnReportFormat.CSV:
            self.results_to_csv_row(report_field_ids, query, mode, output_file)
        else:
            self.results_to_txt_row(report_field_ids, mode, query, output_file)

    def results_to_txt_row(self, field_ids, mode, query, output_file):
        has_rows = False
        while query.next():
            if mode == "streets":
                # write street content
                line = [query.value(field_ids[0]), query.value(field_ids[1]), query.value(field_ids[2]),
                        query.value(field_ids[3]), query.value(field_ids[4]), query.value(field_ids[5]),
                        self._format_date(str(query.value(field_ids[6]))),
                        self._format_date(str(query.value(field_ids[7]))),
                        self._format_date(str(query.value(field_ids[8]))),
                        self._format_date(str(query.value(field_ids[9]))),
                        query.value(field_ids[10]), query.value(field_ids[11])]
            else:
                # write srwr content
                line = [query.value(field_ids[0]), query.value(field_ids[1]), query.value(field_ids[2]),
                        query.value(field_ids[3]), query.value(field_ids[4]), query.value(field_ids[5]),
                        query.value(field_ids[6]), query.value(field_ids[7])]

            has_rows = True
            num_cols = len(line)
            for idx, val in enumerate(line):
                output_file.write(str(val))
                if idx < num_cols - 1:
                    output_file.write(" , ")
            output_file.write("\n")
        output_file.write("\n")

        # Empty result set message
        if not has_rows:
            output_file.write(self.no_content)

    def results_to_csv_row(self, field_ids, query, mode, output_csv):
        if mode == "streets":
            # write street content
            while query.next():
                line = [query.value(field_ids[0]), query.value(field_ids[1]), query.value(field_ids[2]),
                        query.value(field_ids[3]), query.value(field_ids[4]), query.value(field_ids[5]),
                        self._format_date(str(query.value(field_ids[6]))),
                        self._format_date(str(query.value(field_ids[7]))),
                        self._format_date(str(query.value(field_ids[8]))),
                        self._format_date(str(query.value(field_ids[9]))),
                        query.value(field_ids[10]), query.value(field_ids[11])]
                output_csv.writerow(line)
        else:
            while query.next():
                line = [query.value(field_ids[0]), query.value(field_ids[1]), query.value(field_ids[2]),
                        query.value(field_ids[3]), query.value(field_ids[4]), query.value(field_ids[5]),
                        query.value(field_ids[6]), query.value(field_ids[7])]

                output_csv.writerow(line)

    @staticmethod
    def write_column_headers(headers, output_file, file_format):
        # write column header row
        if file_format is RnReportFormat.CSV:
            output_file.writerow(headers)
        else:
            for head in headers:
                output_file.write(head + " ")
            output_file.write("\n")

    @staticmethod
    def write_sub_report_headings(heading, formatted_date, output_file, report_type):
        if report_type is RnReportFormat.CSV:
            output_file.writerow([heading, formatted_date])
        else:
            header = heading + formatted_date
            output_file.write(header + "\n")
            line_length = len(header)
            output_file.write('-' * line_length + "\n \n")

    def write_report_header(self, output_file, file_format):
        # Only have a header for text format for now
        if file_format.name == RnReportFormat.TXT.name:
            output_file.write(str(self.report_title) + ' for {0} \n'.format(self.org))
            output_file.write('Created on : {0} at {1} By : {2} \n'.format(datetime.today().strftime("%d/%m/%Y"),
                                                                           datetime.now().strftime("%H:%M"),
                                                                           str(self.user)))
            output_file.write(
                "----------------------------------------------------------------------------------------- \n \n \n \n")

    @staticmethod
    def write_report_footer(output_file, file_format):
        # Only have a report footer for text format for now
        if file_format.name == RnReportFormat.TXT.name:
            output_file.write("\n \n \n")
            output_file.write("---------- End of Report ----------- \n")

    @staticmethod
    def _format_date(input_date):
        if input_date is "NULL" or input_date == "0":
            output_date = ""
            return output_date
        else:
            try:
                in_date_obj = datetime.strptime(input_date, "%Y%m%d")
                output_date = str((in_date_obj.strftime("%d/%m/%Y")))
            except ValueError:
                output_date = ""
            return output_date

    @staticmethod
    def _get_csv_writer(file):
        return csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, lineterminator='\r')

    @staticmethod
    def _get_report_field_ids(report_fields, rec):
        """
        Takes alist of field names and a record
        returns a list of field positions for the given names
        :param report_fields: list of field names to find in record
        :param rec: qsqlrecord
        :return: list of field position ids corresponding to the report_fields supplied
        """
        field_ids = []
        for field in report_fields:
            field_ids.append(rec.indexOf(field))
        return field_ids

    @staticmethod
    def _get_selected_categories(selected_options):
        # Build a list of selected values from the listWidget
        list_selected = list()

        # Extract option id from option text e.g. "1: option one"
        for opt in selected_options:
            sep = str(opt).find(":", 0, len(opt))
            list_selected.append(opt[:sep])
            list_selected.sort()

        # create comma sep list of values for query from an array
        selected_categories = ",".join(map(str, list_selected))
        return selected_categories

    @staticmethod
    def _show_alert():
        # trigger a dialog box but remain in the street reports menu
        error_alert = StreetReportsAlert()
        error_alert.ui.cancelPushButton.clicked.connect(error_alert.close)
        error_alert.exec_()
