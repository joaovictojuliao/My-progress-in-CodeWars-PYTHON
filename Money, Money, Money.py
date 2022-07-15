def calculate_years(principal, interest, tax, desired):
    if principal >= desired:
        return 0
    result = principal * interest * (1 - tax) + principal
    return 1 if result >= desired else 1 + calculate_years(result, interest, tax, desired)
