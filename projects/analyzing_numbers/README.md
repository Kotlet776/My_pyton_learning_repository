# Numbers Report (CLI)

Small Python CLI tool that reads a text file with values (one per line), converts valid integers, ignores empty lines,
counts invalid lines, and generates a report (printed to terminal + saved to `report.txt`).

## Requirements
- Python 3.10+ (recommended: 3.12+)

## Input format
`numbers.txt` example:

10
3
-2
abc

15

8

Rules:
- empty lines are ignored
- valid integers are collected
- non-integer lines are counted as invalid

## Usage

Run from the folder where the script is located:

```bash
python analyzer.py numbers.txt
