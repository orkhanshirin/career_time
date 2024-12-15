import re

def parse_duration(duration_str: str) -> float:
    """
    Converting experience duration string into a float for more accurate calculation.
    
    Examples:
    - "2 years 7 months" -> 2 + (7/12) ≈ 2.58
    - "3 years" -> 3.0
    - "" or None -> 0.0 (no duration)
    """
    if not duration_str:
        return 0.0

    # Pattern matches "<number> <unit>" where unit is year/years/month/months
    pattern = re.compile(r'(\d+)\s+(year|years|month|months)', re.IGNORECASE)
    matches = pattern.findall(duration_str)

    years = 0
    months = 0
    for number_str, unit in matches:
        number = int(number_str)
        if 'year' in unit.lower():
            years += number
        elif 'month' in unit.lower():
            months += number

    return years + (months / 12.0)


def calculate_total_years(experiences: list[dict]) -> float:
    """
    Calculate total work experience in years by summing up the durations given in the data.
    """
    total = 0.0
    for exp in experiences:
        duration_str = exp.get("duration", "")
        total += parse_duration(duration_str)
    return total
