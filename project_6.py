from math import *


def solution(a, b, c):
    """Function to solve quadratic equation."""

    dis = (b ** 2) - 4 * a * c

    while dis < 0:
        print("There isn't any solution. Enter other coefficients.")
        a, b, c = int(input('a = ')), int(input('b = ')), int(input('c = '))
        dis = (b ** 2) - 4 * a * c

    if dis > 0:
        first_x = (-b + sqrt(dis)) / (a * 2)
        second_x = (-b - sqrt(dis)) / (a * 2)
        print('The discriminant is equal to: ', dis)
        print('First solution: ', round(first_x, 1))
        print('Second solution: ', round(second_x, 1))

    elif dis == 0:
        x = (-b) / (a * 2)
        print('The discriminant is equal to: ', dis)
        print('Single solution: ', round(x, 1))


def main():
    print('Enter the coefficients a, b, c:')
    solution(int(input('a = ')), int(input('b = ')), int(input('c = ')))


if __name__ == '__main__':
    main()
