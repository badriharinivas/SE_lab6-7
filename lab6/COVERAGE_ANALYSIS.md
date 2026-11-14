# Lab 6 coverage analysis

Coverage was measured for `spam_scoring.py` with the dedicated Lab 6 test suites.

## Code coverage

Command: `python -m coverage run --source=spam_scoring -m pytest -q CodeCoverageTest_33_application.py`

Result: 12 tests passed. `spam_scoring.py` executed all 39 statements (100% line coverage).

## Branch coverage

Command: `python -m coverage run --branch --source=spam_scoring -m pytest -q BranchCoverageTest_33_application.py`

Result: 6 tests passed. All 39 statements and all 26 branch outcomes were covered, with 0 partial branches (100% branch coverage).

The tests exercise both outcomes for the word scoring, link-count, sender-known, score-floor, classification, inbox iteration, and spam-ratio decisions. They also include empty inputs and exact classification and ratio boundaries.

Terminal result images are in `screenshots/`.
