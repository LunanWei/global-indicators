"""
Tests for the Global Healthy and Sustainable City Indicator software workflow.

This module may be run from the process directory as follows:

    python -m unittest -v tests/tests.py

For example, from within process directory:

>docker compose -f .test-compose.yml run ghsci
test_global_indicators_shell (tests.tests.tests)
Unix shell script should only have unix-style line endings. ... ok
test_project_setup (tests.tests.tests)
Check if _project_setup.py imported successfully. ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK

Successful running of all tests may require running of tests within the global-indicators Docker container, hence the use of a custom .test-compose.yml for this purpose.
"""

import sys
import unittest

try:
    import subprocesses.ghsci

    project_setup = True
except ImportError as e:
    project_setup = f'ghsci.py import error: {e}'


class tests(unittest.TestCase):
    """A collection of tests to help ensure functionality."""

    def test_global_indicators_shell(self):
        """Unix shell script should only have unix-style line endings."""
        counts = calculate_line_endings('../global-indicators.sh')
        lf = counts.pop(b'\n')
        self.assertTrue(sum(counts.values()) == 0 and lf > 0)

    def test_project_setup(self):
        """Check if _project_setup.py imported successfully."""
        self.assertTrue(project_setup)


def calculate_line_endings(path):
    """
    Tally line endings of different types, returning dictionary of counts.

    Based on code posted at https://stackoverflow.com/questions/29695861/get-newline-stats-for-a-text-file-in-python.
    """
    # order matters!
    endings = [
        b'\r\n',
        b'\n\r',
        b'\n',
        b'\r',
    ]
    counts = dict.fromkeys(endings, 0)

    with open(path, 'rb') as fp:
        for line in fp:
            for x in endings:
                if line.endswith(x):
                    counts[x] += 1
                    break
    return counts


if __name__ == '__main__':
    unittest.main()
