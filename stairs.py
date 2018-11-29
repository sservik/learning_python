import sys


def get_rung(num_steps):
	stairs = []
	for i in range (1, int(num_steps)+1):
		stairs.append(((int(num_steps) - i) * ' ') + (i * ('#')))
		rung = '\n'.join(stairs)
	return rung


if __name__ == "__main__":
    num_steps = sys.argv[1]
    print(get_rung(num_steps))