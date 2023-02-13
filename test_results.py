import io
import csv
import unittest
from results import write_file 
import os

class TestWriteFile(unittest.TestCase):
    #testing write_file function
    def setUp(self):
        self.file = "testResult.csv"

    def test_write_file(self):
        with open('test.csv', 'r') as fh:
            csv_reader = csv.reader(fh)
            with open(self.file, 'w', newline='', ) as f:
                writer = csv.writer(f, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
                writer.writerow(['email_hash', 'category','filename'])
                write_file(writer, csv_reader, self.file)
        with open(self.file, 'r') as f:
            result = f.read()
        self.assertEqual(result, '"email_hash","category","filename"\n"name1","category1","testResult.csv"\n"name2","category2","testResult.csv"\n')

        # delete the file after the test
        if os.path.exists('testResult.csv'):
            os.remove('testResult.csv')


if __name__ == '__main__':
    unittest.main()



