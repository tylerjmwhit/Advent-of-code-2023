import re

if __name__ == "__main__":
    # print("Hello world")
    sum = 0
    word2num = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
    }
    with open(r'Day_1\input.txt', "r") as file:
        for line in file:
            line = line.lower()
            regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
            x = re.findall(pattern = regex,string = line, flags = re.IGNORECASE)
            x = [word2num.get(match,match)for match in x]
            value = int(x[0] + x[-1])
            sum += value
    print(sum)