# 2017 BIO Question 1: Coloured Triangles


def solution(colors: list[str]):
    while len(colors) > 1:
        new_colors = []

        for i in range(len(colors) - 1):
            left = colors[i]
            right = colors[i + 1]

            if left == right:
                new_colors.append(left)

            else:
                # returns a set with one element hence the comma after `remaining`
                remaining, = {"R", "G", "B"} - {left, right}
                new_colors.append(remaining)

        colors = new_colors
    return colors[0]


def main():
    colors = list(input())
    print(solution(colors))
