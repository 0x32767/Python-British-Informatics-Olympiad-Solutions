from enum import StrEnum, auto


def split_brackets(pattern: str):
    idx = 0
    
    while idx < len(pattern):
        char = pattern[idx]
        
        if char == "(":
            idx += 1
            seq = ""

            while pattern[idx] != ")":
                seq += pattern[idx]
                idx += 1
            
            yield seq
        
        else:
            yield char
        
        idx += 1


def structure_pattern(pattern: str):
    structured_pattern = []
    prev = None

    for seq in split_brackets(pattern):
        if prev is None:
            prev = seq
            continue
        
        if seq in "*?":
            structured_pattern.append((prev, seq))

        elif prev not in "*?":
            structured_pattern.append((prev, "="))

        prev = seq

    if prev not in "*?":
        structured_pattern.append((prev, "="))

    return structured_pattern


def make_all_patterns(structured_pattern: list[tuple[str, str]]):
    if structured_pattern == []:
        yield ""
        return
    
    pattern, pattern_type = structured_pattern.pop(0)
    
    if pattern_type == "=":
        for pattern_tail in make_all_patterns(structured_pattern.copy()):
            yield pattern + pattern_tail
    
    elif pattern_type == "?":
        for pattern_tail in make_all_patterns(structured_pattern.copy()):
            yield pattern + pattern_tail
            yield pattern_tail
    
    elif pattern_type == "*":
        for pattern_tail in make_all_patterns(structured_pattern.copy()):
            for i in range(12):
                yield (pattern * i) + pattern_tail

    else:
        raise NotImplementedError


def match_password(password: str, pattern: str):
    prev = None
    
    for char, pwd in zip(pattern, password):
        if char == "x":
            prev = int(pwd)
            continue
        
        elif char == "u":
            if not (int(pwd) > prev):
                return False
            
            prev = int(pwd)
        
        elif char == "d":
            if not (int(pwd) < prev):
                return False
            
            prev = int(pwd)
    
    return True


def match_pattern(password: str, pattern: str):
    for p in make_all_patterns(structure_pattern(pattern)):
        if len(p) != len(password):
            continue

        if match_password(password, p):
            return True
    
    return False


def solution(pattern: str, p1: str, p2: str):
    match_password_1 = "No"

    if match_pattern(p1, pattern):
        match_password_1 = "Yes"

    match_password_2 = "No"

    if match_pattern(p2, pattern):
        match_password_2 = "Yes"

    return match_password_1, match_password_2


def main():
    pattern = input()
    p1 = input()
    p2 = input()
    
    for line in solution(pattern, p1, p2):
        print(line)


if __name__ == "__main__":
    main()
