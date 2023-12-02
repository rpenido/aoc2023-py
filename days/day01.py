from .utils import utils

numbers = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def get_calibration_values_a(input):
    first_digit = None
    last_digit = None
    calibration_sum = 0
    for line in input:
        for c in line:
            if c.isnumeric():
                first_digit = c
                break

        for c in line[::-1]:
            if c.isnumeric():
                last_digit = c
                break
        assert first_digit is not None
        assert last_digit is not None
        calibration_value = int(f'{first_digit}{last_digit}')
        calibration_sum += calibration_value

    return calibration_sum

def get_calibration_values_b(input):
    calibration_sum = 0
    for line in input:
        first_digit = None
        last_digit = None
        for i, c in enumerate(line):
            if c.isnumeric():
                first_digit = c
                break

            for word in numbers:
                if line[i:].startswith(word):
                    first_digit = numbers[word]
                    break

            if first_digit is not None:
                break

        for i, c in enumerate(line[::-1]):
            if c.isnumeric():
                last_digit = c
                break
            for word in numbers:
                if i == 0:
                    if line.endswith(word):
                        last_digit = numbers[word]
                        break

                if line[:-i].endswith(word):
                    last_digit = numbers[word]
                    break

            if last_digit is not None:
                break

        assert first_digit is not None
        assert last_digit is not None
        calibration_value = int(f'{first_digit}{last_digit}')
        calibration_sum += calibration_value

    return calibration_sum

def test_a():
    file = utils.get_input("./day01_input_test_a.txt")
    return get_calibration_values_a(file)

def test_b():
    file = utils.get_input("./day01_input_test_b.txt")
    return get_calibration_values_b(file)

def part_a():
    file = utils.get_input("./day01_input.txt")
    return get_calibration_values_a(file)

def part_b():
    file = utils.get_input("./day01_input.txt")
    return get_calibration_values_b(file)

print(part_b())
