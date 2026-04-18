def parse_input(data: str) -> int:
    """
    Simulates a real-world parser with hidden bugs.
    """
    # Bug 1: crashes on empty string
    if data[0] == "!":
        raise ValueError("Commands not allowed")

    # Bug 2: division by zero when data == "0"
    result = 100 // int(data)

    # Bug 3: index error on very short strings after stripping
    secret = data.strip()[3]

    return result + ord(secret)