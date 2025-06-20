# 2013 BIO Question 1: Watching the Clock

# Failing one test case: solution(67, 1507) != "02:07"

def add_time(time: tuple[int, int], minutes: int):
    hours, mins = time
    tick_over_hours, new_mins = divmod(mins + minutes, 60)
    return ((hours + tick_over_hours + 1) % 24, new_mins)

def solution(clock1_offset: int, clock2_offset: int) -> str:
    # both clocks start at 00:00, 01:[OFFSET] is
    # the first hour where both clocks don't match
    clock1_time = (1, clock1_offset)
    clock2_time = (1, clock2_offset)

    while clock1_time != clock2_time:
        clock1_time = add_time(clock1_time, clock1_offset)
        clock2_time = add_time(clock2_time, clock2_offset)

    final_hours, final_minutes = clock1_time
    return f"{str(final_hours).zfill(2)}:{str(final_minutes).zfill(2)}"

def main():
    clock1_offset, clock2_offset = input().split(" ")
    print(solution(int(clock1_offset), int(clock2_offset)))

if __name__ == "__main__":
    main()
