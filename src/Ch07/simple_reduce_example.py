from functools import reduce

range_5 = range(5)
difference = reduce(lambda x, y: x - y, range_5)
sum = reduce(lambda x, y: x + y, range_5)
print(f"the difference of all elements in the range:\n {list(range_5)}\n is {difference}")
print(f"the sum of all elements in the range:\n {list(range_5)}\n is {sum}")

if __name__ == "__main__":
    pass