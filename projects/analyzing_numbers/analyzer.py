import sys
def read_numbers(lines) -> tuple:
    """
    Docstring for read_numbers
    Function checks if the value is a number.
    Returns a list of numbers.
    """
    
    numbers = []
    count_unable_to_convert = 0
    for i in lines:
        try:
            i = str(i).strip()
            if i == "":
                continue
            i = int(i)
            numbers.append(i)
        except ValueError:
            count_unable_to_convert +=1
            continue

    return(numbers, count_unable_to_convert)

def analyze_numbers(numbers: list) -> dict:
    """
    Docstring for analyze_numbers
    Funcion analyzes numberlist.
    Returns a dictionary with the output of the analization.
    """
    both_count = 0
    div3_count = 0
    even_count = 0
    sum_of_numbers = 0
    num_count = 0
    try:
        min_num = numbers[0]
        max_num = numbers[0]
    except IndexError:
        return {"min": None, "max": None, "avg": None, "even": 0, "div3": 0, "both": 0}
    
    for i in numbers:
        is_div3 = i % 3 == 0
        is_even = i % 2 == 0
        sum_of_numbers += i
        num_count += 1
        if i > max_num:
            max_num = i
        elif min_num > i:
            min_num = i
        if is_div3 and is_even:
            both_count +=1
        if is_even:
            even_count += 1
        if is_div3:
            div3_count += 1
    average = sum_of_numbers / num_count
    return{"min": min_num, "max": max_num, "avg": round(average, 2), "even": even_count, "div3": div3_count, "both": both_count}
    

def build_report(analyzed_result, bad_count) -> str:
    """
    Docstring for build_report
    Function returns a string with name value pairs, if there where enough numbers to analyze.
    """
    if analyzed_result['min'] is None:
        return("Not enough numbers to analyze.")
    else:
        return (f"Lowest number: {analyzed_result['min']}\n" +  f"Highest number: {analyzed_result['max']}\n" +
                f"Average: {analyzed_result['avg']}\n" + f"Even numbers: {analyzed_result['even']}\n" +
                f"Divisible by 3: {analyzed_result['div3']}\n" + f"Both: {analyzed_result['both']}\n" + f"Invalid lines: {bad_count}")

if len(sys.argv) == 2:
    try:
        with open(sys.argv[1]) as f:
            output_readlines = read_numbers(f)
            analyzed = analyze_numbers(output_readlines[0])
            txt = build_report(analyzed, output_readlines[1])
            print(txt)
            with open("report.txt", "w") as file:
                file.write(txt)
    except FileNotFoundError:
        msg = f"File '{sys.argv[1]}' not found."
        print(msg)
        with open("report.txt", "w") as file:
            file.write(msg)
else:
    msg = f"Expected 1 argument, got {len(sys.argv)-1}"
    print(msg)
    with open("report.txt", "w") as file:
        file.write(msg)
    sys.exit()