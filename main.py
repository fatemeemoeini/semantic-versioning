def parse_input(input_str):
    if ">=" in input_str:
        num = input_str.split(">=")[1].strip()
        return ('>=', num, True)
    elif "<=" in input_str:
        num = input_str.split("<=")[1].strip()
        return ('<=', num, True)
    elif ">" in input_str:
        num = input_str.split(">")[1].strip()
        return ('>', num, False)
    elif "<" in input_str:
        num = input_str.split("<")[1].strip()
        return ('<', num, False)
    elif "=" in input_str:
        num = input_str.split("=")[1].strip()
        return ('=', num, True)
    else:
        num = input_str.strip()
        return ('=', num, True)


def version_to_tuple(version):
    parts = version.split(".")
    if not all(part.isdigit() for part in parts):
        raise ValueError(f"Invalid version part: {version}")
    return tuple(map(int, parts))


def create_range(input_str):
    input_str = input_str.strip()
    if not input_str:
        raise ValueError("Input cannot be empty")

    conditions = input_str.split(',')
    lower_bound = None
    upper_bound = None
    lower_bracket = '['
    upper_bracket = ']'

    for condition in conditions:
        condition = condition.strip()
        operator, num, has_equal = parse_input(condition)

        if num:
            num_tuple = version_to_tuple(num)
        else:
            num_tuple = None

        if operator == '>=':
            if lower_bound is None or (num_tuple is not None and num_tuple > lower_bound) or (
                    num_tuple == lower_bound and has_equal):
                lower_bound = num_tuple
                lower_bracket = '[' if has_equal else '('
        elif operator == '>':
            if lower_bound is None or (num_tuple is not None and num_tuple >= lower_bound):
                lower_bound = num_tuple
                lower_bracket = '('
        elif operator == '<=':
            if upper_bound is None or (num_tuple is not None and num_tuple < upper_bound) or (
                    num_tuple == upper_bound and has_equal):
                upper_bound = num_tuple
                upper_bracket = ']' if has_equal else ')'
        elif operator == '<':
            if upper_bound is None or (num_tuple is not None and num_tuple <= upper_bound):
                upper_bound = num_tuple
                upper_bracket = ')'
        elif operator == '=':
            lower_bound = num_tuple
            upper_bound = num_tuple
            lower_bracket = '['
            upper_bracket = ']'

    result = ""
    if lower_bound is None and upper_bound is not None:
        result = f"[ , {'.'.join(map(str, upper_bound))}]"
    elif upper_bound is None and lower_bound is not None:
        result = f"[{'.'.join(map(str, lower_bound))}, ]"
    elif lower_bound is not None and upper_bound is not None:
        if lower_bound == upper_bound:
            result = f"[{'.'.join(map(str, lower_bound))}, {'.'.join(map(str, upper_bound))}]"
        else:
            result = f"[{'.'.join(map(str, lower_bound))}, {'.'.join(map(str, upper_bound))}]"

    return result


# Test cases

input_str = "=>3.1.0"
print(create_range(input_str))
