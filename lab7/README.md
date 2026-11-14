# L6_L7_33 — Spam Scoring Filter

Lab 7: Fuzz Testing

## About

A small Python module that pulls apart sender addresses, finds links in messages and measures shouting.

## Files

| File | Description |
|------|-------------|
| `spam_scoring.py` | The code under test |
| `test_spam_scoring.py` | Hypothesis fuzz and behavior tests |
| `Lab7_FuzzTesting_Report_33.pdf` | Before/after test evidence and screenshots |

Install dependencies with `python -m pip install pytest hypothesis`, then run `python -m pytest -q test_spam_scoring.py` from this directory.

See `screenshots/` for the terminal result images included in the PDF. `fuzz_before_fix.txt` records the failing Hypothesis run; `fuzz_after_fix.txt` records the passing run.
