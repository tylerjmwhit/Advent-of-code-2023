import re

if __name__ == "__main__":
    # print("Hello world")
    sum = 0
    with open(r'Day_1\input.txt', "r") as file:
        for line in file:
            x = re.findall("[0-9]",line)
            value = (int(x[0]) * 10) + (int(x[-1]))
            sum += value
    print(sum)