# Log Analyzer

A simple log analyzer written in Python.

## What does the script do?

`log_analyzer.py`:
- reads a log file,
- validates each line,
- counts log levels (`INFO`, `WARNING`, `ERROR`, and unknown ones as `OTHER`),
- detects invalid lines (empty, invalid format, invalid date),
- finds the "worst day" (the day with the highest number of `ERROR` entries),
- generates a text report and saves it to `report.txt`.

## Expected line format

Each valid log line should look like this:

```text
YYYY-MM-DD LEVEL message...
```

Example:

```text
2025-01-17 ERROR Database connection failed
```

Where:
- `YYYY-MM-DD` — date,
- `LEVEL` — one of: `INFO`, `WARNING`, `ERROR`,
- `message` — any text.

If a level is not one of the values above, the entry is counted as `OTHER` and increases the `unknown_level` counter.

## Data validation

The script marks a line as invalid when:
- it is empty (`empty`),
- it has fewer than 3 tokens after splitting by spaces (`invalid_format`),
- its date fails basic validation (`invalid_date`):
  - the format is not `YYYY-MM-DD`,
  - month is outside `1-12`,
  - day is outside `1-31`,
  - date parts are not numeric values.

> Note: date validation is simplified (for example, it does not verify month-specific day counts or leap years).

## Running the script

From the `projects/log-analyzer` directory:

```bash
python log_analyzer.py <path_to_log_file>
```

Example with the sample file:

```bash
python log_analyzer.py examples/sample.log
```

## Exit codes

- `0` — success,
- `1` — file not found,
- `2` — invalid number of arguments.

## Output

The script:
1. prints the report to standard output,
2. saves the same report to `report.txt` (in the current working directory).

The report includes:
- total and empty line counts,
- invalid line counters,
- log level statistics,
- number of unique days,
- the "worst day" by `ERROR` count,
- top 3 most frequent `ERROR` messages.

## Example files

In the `examples/` directory you can find:
- `sample.log` — sample input log,
- `report_example.txt` — sample report output.
