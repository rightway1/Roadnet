import unittest
from datetime import datetime
from mock import patch, MagicMock, call
from admin.street_report import StreetReportsExport
from config import RnReportFormat


class TestStreetReport(unittest.TestCase):
    def test_get_selected_categories(self):
        test_options = {"report": "srwr",
                        "categories": ["1: Test One", "3: Test Three"],
                        "table": 1
                        }
        expected_categories = "1,3"

        selected_categories = StreetReportsExport._get_selected_categories(test_options['categories'])

        self.assertEqual(expected_categories, selected_categories)

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
        test_date = "my test string"

        result = StreetReportsExport._format_date(test_date)
        self.assertEqual('', result)

    @patch('Roadnet.database.get_from_gaz_metadata')
    def test_write_report_header_txt(self, _):
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
        # Arrange
        test_params = {'UserName': 'test user'}
        test_report = StreetReportsExport(None, "", None, False, test_params)
        mock_output = MagicMock()

        # Act
        test_report.write_report_header(mock_output, RnReportFormat.CSV)

        # Assert
        self.assertEqual(0, mock_output.write.call_count, "No lines written for CSV")

    def test_write_report_footer_txt(self):
        test_file_format = RnReportFormat.TXT
        mock_output = MagicMock()
        expected_calls = [call("\n \n \n"),
                          call("---------- End of Report ----------- \n")]

        # Act
        StreetReportsExport.write_report_footer(mock_output, test_file_format)

        self.assertEqual(2, mock_output.write.call_count, "Two lines written")
        mock_output.write.assert_has_calls(expected_calls)

    def test_write_report_footer_csv(self):
        test_file_format = RnReportFormat.CSV
        mock_output = MagicMock()

        # Act
        StreetReportsExport.write_report_footer(mock_output, test_file_format)

        self.assertEqual(0, mock_output.write.call_count, "No footer written for CSV")
