import functools

def reduce_example():
    data = [1, 2, 3, 4]
    result = functools.reduce(lambda x, y: x * y, data)
    print(result)

if __name__ == "__main__":
    reduce_example()
