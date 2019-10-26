import unittest
from mock import patch, Mock
from admin.street_report import StreetReportsExport


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