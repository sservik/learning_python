import sys


def amount(digit_string):
	x = 0
	for elem in digit_string:
		x += int(elem)
	return x


if __name__ == "__main__":
    digit_string = sys.argv[1]
    print(amount(digit_string))