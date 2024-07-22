import random

def random_example():
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(numbers)

if __name__ == "__main__":
    random_example()
