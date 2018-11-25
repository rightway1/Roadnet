import datetime
import unittest
from mock import patch, Mock

import exports.export_csv as csv_export


class TestExportCSV(unittest.TestCase):
    def test_convert_floats_and_strings(self):
        org_name = "test org"
        code_num = 1234
        today = datetime.datetime.strptime('Jun 1 2018  1:33PM', '%b %d %Y %I:%M%p')
        today_date = today.date()
        today_time = today.time().strftime('%H%M%S')
        volnum = 1
        file_type = "F"
        float_no = 123.456789

        opts = {
            75: [10, org_name, code_num, today_date, volnum, today_date, today_time, "1.0", file_type, float_no]
        }
        expected = {
            75: [10, "Test Org", 1234, "2018-06-01", 1, "2018-06-01", "133300", "1.0", "F", 123.46]
        }

        version = 75
        aheader = opts.get(version)
        aheader = csv_export.format_floats_and_strings(aheader)

        self.assertListEqual(aheader, expected.get(version), "List {} did not match expected {}"
                             .format(str(aheader), str(expected[75])))
