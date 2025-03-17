import random

if __name__ == '__main__':
    max_samples = 1000000
    circle_points = 0

    for _ in range(max_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        d = x ** 2 + y ** 2

        if d <= 1:
            circle_points += 1

    pi = 4 * circle_points / max_samples

    print("Estimated pi value using the Monte Carlo method is {:.2f}".format(pi))
