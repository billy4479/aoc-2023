def part_1(input: str):
    lines = input.splitlines()
    nums = []

    for line in lines:
        first_num = None
        last_num = None
        for char in line:
            if char.isdigit():
                if first_num is None:
                    first_num = char
                last_num = char

        nums.append(int(first_num + last_num))

    sum = 0
    for num in nums:
        sum += num

    return sum


def part_2(input: str):
    lines = input.splitlines()
    nums = []

    digits_str = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for i in range(len(lines)):
        line = lines[i]
        first_num = None
        last_num = None

        for j in range(len(line)):
            char = line[j]

            if char.isdigit():
                if first_num is None:
                    first_num = char
                last_num = char
                continue

            a = line[j : j + 5]  # 5 is the maximum length of digits's names
            if len(a) < 3:  # 3 is the minimum instead
                continue

            for digit_num in range(len(digits_str)):
                digit = digits_str[digit_num]
                if a.startswith(digit):
                    if first_num is None:
                        first_num = str(digit_num + 1)
                    last_num = str(digit_num + 1)
                    break

        num = int(first_num + last_num)
        nums.append(num)

    sum = 0
    for num in nums:
        sum += num

    return sum
