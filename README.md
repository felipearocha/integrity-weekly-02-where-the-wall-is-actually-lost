# Where the wall is actually lost

[![CI](https://github.com/felipearocha/integrity-weekly-02-where-the-wall-is-actually-lost/actions/workflows/ci.yml/badge.svg)](https://github.com/felipearocha/integrity-weekly-02-where-the-wall-is-actually-lost/actions/workflows/ci.yml)

Week of 2026-11-23 to 2026-11-27. Working notes on one integrity engineering problem: the posts, the code behind the numbers, and tests that hold the code to a hand calculation.

## Run it

```
pip install -r requirements-dev.txt
pytest -q
python code/cml_coverage.py
```

Python 3.11 or newer.

## Code

| File | What it computes |
|---|---|
| [`code/cml_coverage.py`](code/cml_coverage.py) | Chance that spot CMLs placed without mechanism knowledge touch the damaged area. |

Each script states its basis in the docstring, runs on synthetic data, and checks its own result against a hand calculation. The tests also confirm the printed output is the one published.

## Posts

| Day | Post | Format |
|---|---|---|
| Monday | [The Leak Was Not a Shortage of CMLs](posts/166_leak_was_not_a_cml_shortage.md) | text-only |
| Tuesday | [A P&ID Has No Elbows](posts/167_pid_has_no_elbows.md) | single image |
| Wednesday | [The Debottleneck Nobody Told the CMLs About](posts/168_debottleneck_and_the_elbow.md) | single image |
| Thursday | [Clean Because It Is Healthy, or Because of Where You Looked?](posts/169_clean_or_never_looked.md) | single image |
| Friday | [One Low Reading and a Morning Meeting](posts/170_one_low_reading.md) | single image |

## Scope and limits

- All data and drawings are synthetic. No plant, tag or operating data from any facility.
- The code is a worked example for engineers, not a certified calculation. Confirm every requirement against the edition of the standard that governs your equipment.
- Short quotations from standards are identified with their section. Standards are the property of their publishers and are not reproduced here.

## License

MIT for the code. See [LICENSE](LICENSE).
