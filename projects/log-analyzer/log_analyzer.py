import sys

def parse_lines(lines) -> dict:
    invalid_format = 0
    empty = 0
    invalid_date = 0
    unknown_level = 0
    total_lines = 0
    levels = {"INFO", "WARNING", "ERROR"}
    entries = []
    for line in lines:
        total_lines += 1
        line = str(line).strip() 
        if line == "":
            empty += 1
            continue
        line = str(line).split()
        if len(line) < 3:
            invalid_format += 1
        else:
            date, level, *msg = line
            temporary_date = date.split("-")
            if len(temporary_date) == 3 and len(temporary_date[0]) == 4 and len(temporary_date[1]) == 2 and len(temporary_date[2]) == 2:
                try:
                    if int(temporary_date[0]) >= 0 and 0 < int(temporary_date[1]) < 13 and 0 < int(temporary_date[2]) < 32:
                        msg = " ".join(msg)
                        if level not in levels:
                            entries.append({"date" : date, "level": "OTHER", "msg": msg})
                            unknown_level += 1
                        else:
                            entries.append({"date" : date, "level": level, "msg": msg})
                    else:
                        invalid_date += 1
                except ValueError:
                    invalid_date += 1
            else:
                invalid_date += 1
    return {
            "entries": entries,
            "counts": {
                "invalid_format": invalid_format,
                "invalid_date": invalid_date,
                "unknown_level": unknown_level,
                "empty": empty,
                "total_lines": total_lines
                }
            }    

def analyze(parsed: dict) -> dict:
    total_non_empty_lines = parsed["counts"]["total_lines"] - parsed["counts"]["empty"]
    unique_days_set = set()
    worst_day = None
    worst_day_error_count = 0
    error_msg_counts = {}
    error_day_counts = {}
    level_counts = {"ERROR": 0, "WARNING": 0, "INFO": 0, "OTHER": 0}
    for line in parsed["entries"]:
        unique_days_set.add(line["date"])
        level = line["level"]
        level_counts[level] += 1
        if level == "ERROR":
            if line["date"] in error_day_counts:
                error_day_counts[line["date"]] += 1
            else:
                error_day_counts[line["date"]] = 1
            if line["msg"] in error_msg_counts:
                error_msg_counts[line["msg"]] += 1
            else:
                error_msg_counts[line["msg"]] = 1

    
    for i, j in error_day_counts.items():
        if j > worst_day_error_count:
            worst_day_error_count = j
            worst_day = i
        elif worst_day is not None and j == worst_day_error_count: # Tie-break: if same error count, choose the latest date
            if i > worst_day:
                worst_day_error_count = j
                worst_day = i
    
    top_errors_list = list(error_msg_counts.items())
    top_errors_list.sort(key=lambda item: item[1], reverse=True)
    top_errors_list = top_errors_list[:3]

    return {
        "total_non_empty_lines": total_non_empty_lines,
        "level_counts": level_counts,
        "unique_days": len(unique_days_set),
        "worst_day": worst_day,
        "worst_day_error_count": worst_day_error_count,
        "top_errors": top_errors_list
        }

def build_report(analysis, counts, path):
    n = 1
    lines = []
    if not analysis["top_errors"]:
        top_errors = "None"
    else:
        for i in analysis['top_errors']:
            lines.append(f"{n}) {i[0]} - {i[1]}")
            n += 1
        top_errors = "\n".join(lines)

    return (f"""File: {path}
Total lines: {counts['total_lines']}
Empty lines: {counts['empty']}
Total non-empty lines: {analysis['total_non_empty_lines']}
Invalid format lines: {counts['invalid_format']}
Invalid date lines: {counts['invalid_date']}
Unknown level lines: {counts['unknown_level']}
Level counts:
INFO: {analysis['level_counts']['INFO']}
WARNING: {analysis['level_counts']['WARNING']}
ERROR: {analysis['level_counts']['ERROR']}
OTHER: {analysis['level_counts']['OTHER']}
Unique days: {analysis['unique_days']}
Worst day (ERRORs): {analysis['worst_day']} ({analysis["worst_day_error_count"]})
Top 3 ERROR messages:
{top_errors}""")



def write_report(msg, stream):
     with open("report.txt", "w") as outfile:
        outfile.write(msg)
        print(msg, file=stream)

def main():
    if len(sys.argv) == 2:
        try: 
            with open(sys.argv[1]) as infile:
                parsed = parse_lines(infile)
            analysis = analyze(parsed)
            msg = build_report(analysis, parsed["counts"], sys.argv[1])
            write_report(msg, sys.stdout)
            sys.exit(0)
        except FileNotFoundError:
            msg = f"File '{sys.argv[1]}' not found.\nUsage: python log_analyzer.py <path_to_log_file>"
            write_report(msg, sys.stderr)
            sys.exit(1)
    else:
            msg = f"Expected 1 argument: path to log file. Got {len(sys.argv)-1}.\nUsage: python log_analyzer.py <path_to_log_file>"
            write_report(msg, sys.stderr)
            sys.exit(2)


if __name__ == "__main__":
    main()
