from random import randint
import main


def test(n):
    for i in range(n):
        test_mas = [[randint(0, 100) for i in range(5)] for j in range(5)]
        print(f"Test {i}"
              f"\n{test_mas[0]}"
              f"\n{test_mas[1]}"
              f"\n{test_mas[2]}"
              f"\n{test_mas[3]}"
              f"\n{test_mas[4]}")
        print(main.ssd(test_mas))


test(10)