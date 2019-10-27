import unittest
from datetime import datetime

from PyQt5.QtCore import QVariant
from mock import patch, MagicMock, call, Mock
from PyQt5.QtSql import QSqlRecord, QSqlField

from admin.street_report import StreetReportsExport
from config import RnReportFormat


class TestStreetReport(unittest.TestCase):
    @patch('Roadnet.database.get_from_gaz_metadata')
    def test_report_results_output_csv(self, _):
        """Verifies correct results output method called for csv output"""
        # Arrange
        test_mode = 'srwr'
        test_fieldids = [1, 3, 5, 7, 9]
        test_query = Mock()
        mock_output = Mock()
        test_params = {'UserName': 'test_user'}
        report_type = RnReportFormat.CSV
        test_report = StreetReportsExport(None, "", None, True, test_params)
        test_report.results_to_csv_row = MagicMock()

        # Act
        test_report.report_results(test_mode, test_fieldids, test_query, mock_output, report_type)

        # Assert
        self.assertEqual(1, test_report.results_to_csv_row.call_count)
        test_report.results_to_csv_row.assert_called_with(test_fieldids, test_mode, test_query, mock_output)

    @patch('Roadnet.database.get_from_gaz_metadata')
    def test_report_results_output_txt(self, _):
        """Verifies correct results output method called for txt output"""
        # Arrange
        test_mode = 'srwr'
        test_fieldids = [1, 3, 5, 7, 9]
        test_query = Mock()
        mock_output = Mock()
        test_params = {'UserName': 'test_user'}
        report_type = RnReportFormat.TXT
        test_report = StreetReportsExport(None, "", None, True, test_params)
        test_report.results_to_txt_row = MagicMock()

        # Act
        test_report.report_results(test_mode, test_fieldids, test_query, mock_output, report_type)

        # Assert
        self.assertEqual(1, test_report.results_to_txt_row.call_count)
        test_report.results_to_txt_row.assert_called_with(test_fieldids, test_mode, test_query, mock_output)

    def test_write_column_headers_csv(self):
        """Verify correct column headers written for TXT format files"""
        # Arrange
        test_headers = ['Field 1', 'Field2', 'Field_3']
        mock_output = Mock()
        report_type = RnReportFormat.CSV

        # Act
        StreetReportsExport.write_column_headers(test_headers, mock_output, report_type)

        # Assert
        self.assertEqual(1, mock_output.writerow.call_count)
        mock_output.writerow.assert_called_with(test_headers)

    def test_write_column_headers_txt(self):
        """Verify correct column headers written for TXT format files"""
        # Arrange
        test_headers = ['Field 1', 'Field2', 'Field_3']
        mock_output = Mock()
        report_type = RnReportFormat.TXT
        expected_header1 = 'Field 1 Field2 Field_3 \n'

        # Act
        StreetReportsExport.write_column_headers(test_headers, mock_output, report_type)

        # Assert
        self.assertEqual(1, mock_output.write.call_count)
        mock_output.write.assert_called_with(expected_header1)

    def test_write_sub_report_headings_csv(self):
        """Verify correct sub headings written for CSV format files"""
        # Arrange
        test_heading = 'Test Heading'
        test_date = '01/02/2019'
        mock_output = Mock()
        report_type = RnReportFormat.CSV
        expected_call = [test_heading, test_date]

        # Act
        StreetReportsExport.write_sub_report_headings(test_heading, test_date,
                                                      mock_output, report_type)
        # Assert
        self.assertEqual(1, mock_output.writerow.call_count, 'One row written to csv')
        mock_output.writerow.assert_called_with(expected_call)

    def test_write_sub_report_headings_txt(self):
        """Verify correct sub headings written for TXT format files"""
        # Arrange
        test_heading = 'Test Heading '
        test_date = '01/02/2019'
        mock_output = Mock()
        report_type = RnReportFormat.TXT
        expected_line1 = test_heading + test_date + '\n'
        expected_line2 = '-----------------------\n\n'
        expected_calls = (call(expected_line1), call(expected_line2))

        # Act
        StreetReportsExport.write_sub_report_headings(test_heading, test_date,
                                                      mock_output, report_type)
        # Assert
        self.assertEqual(2, mock_output.write.call_count, 'Two rows written to csv')
        mock_output.write.assert_has_calls(expected_calls)

    @patch('Roadnet.database.get_from_gaz_metadata')
    def test_write_report_header_txt(self, _):
        """Verify correct headers written for TXT format files"""
        # Arrange
        test_report_title = 'test_title'
        test_org = 'test org'
        test_user = 'test user'
        test_params = {'UserName': test_user}
        test_report = StreetReportsExport(None, "", None, False, test_params)
        test_report.org = test_org
        test_report.report_title = test_report_title
        expected_header_1 = '{} for {} \n'.format(test_report_title, test_org)
        expected_header_2 = 'Created on : {} at {} By : {} \n'.format(datetime.today().strftime("%d/%m/%Y"),
                                                                      datetime.now().strftime("%H:%M"),
                                                                      test_user)
        expected_header_3 = '----------------------------------------------------------------------------' + \
                            '------------- \n \n \n \n'
        expected_calls = (call(expected_header_1), call(expected_header_2), call(expected_header_3))
        mock_output = MagicMock()

        # Act
        test_report.write_report_header(mock_output, RnReportFormat.TXT)

        # Assert
        self.assertEqual(3, mock_output.write.call_count, "Three lines written")
        mock_output.write.assert_has_calls(expected_calls)

    @patch('Roadnet.database.get_from_gaz_metadata')
    def test_write_report_header_csv(self, _):
        """Currently no header text written for CSV format reports"""
        # Arrange
        test_params = {'UserName': 'test user'}
        test_report = StreetReportsExport(None, "", None, False, test_params)
        mock_output = MagicMock()

        # Act
        test_report.write_report_header(mock_output, RnReportFormat.CSV)

        # Assert
        self.assertEqual(0, mock_output.write.call_count, "No lines written for CSV")

    def test_write_report_footer_txt(self):
        """Checks correct footer text written to text format files"""
        test_file_format = RnReportFormat.TXT
        mock_output = MagicMock()
        expected_calls = [call("\n \n \n"),
                          call("---------- End of Report ----------- \n")]

        # Act
        StreetReportsExport.write_report_footer(mock_output, test_file_format)

        self.assertEqual(2, mock_output.write.call_count, "Two lines written")
        mock_output.write.assert_has_calls(expected_calls)

    def test_write_report_footer_csv(self):
        """Currently no footer written for CSV format files"""
        test_file_format = RnReportFormat.CSV
        mock_output = MagicMock()

        # Act
        StreetReportsExport.write_report_footer(mock_output, test_file_format)

        self.assertEqual(0, mock_output.write.call_count, "No footer written for CSV")

    def test_format_date_valid(self):
        """Formatting a valid date string"""
        date_unformatted = '20190401'
        expected_date_formatted = '01/04/2019'

        result = StreetReportsExport._format_date(date_unformatted)
        self.assertEqual(expected_date_formatted, result)

    def test_format_date_null_or_0(self):
        """Formatting Null or 0 as a date string returns empty string"""
        expected_date_formatted = ""

        self.assertEqual(expected_date_formatted, StreetReportsExport._format_date('NULL'))
        self.assertEqual(expected_date_formatted, StreetReportsExport._format_date('0'))

    def test_format_date_invalid_returns_empty_string(self):
        """Formatting an invalid date string returns empty string"""
        test_date = "my test string"

        result = StreetReportsExport._format_date(test_date)
        self.assertEqual('', result)

    def test_get_report_field_ids(self):
        """Gets field IDs by name from a qSqlRecord object"""
        # Arrange
        test_record = QSqlRecord()
        test_record.append(QSqlField('fld1', QVariant.Int))
        test_record.append(QSqlField('fld2', QVariant.Int))
        test_record.append(QSqlField('fld3', QVariant.Int))
        test_record.append(QSqlField('fld4', QVariant.Int))

        test_report_fields = ['fld4', 'fld2']
        expected_results = [3, 1]

        # Act
        field_ids = StreetReportsExport._get_report_field_ids(test_report_fields, test_record)

        # Assert
        self.assertEqual(expected_results, field_ids)

    def test_get_selected_categories(self):
        """Selected category IDs extracted from text and returned as comma delimited string"""
        test_options = {"report": "srwr",
                        "categories": ["1: Test One", "3: Test Three"],
                        "table": 1
                        }
        expected_categories = "1,3"

        selected_categories = StreetReportsExport._get_selected_categories(test_options['categories'])

        self.assertEqual(expected_categories, selected_categories)
