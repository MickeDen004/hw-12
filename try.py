import random


def number_operations(n: int):
    n2 = n*n
    n3 = n*n*n
    res = n + n2 + n3
    print(f"Result of n + nn + nnn is {res}")
number_operations(9)

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]
for num in numbers:
    if num % 2 == 0:
        print(num)
    elif num == 237:
        break
set_1 = set(['White', 'Black', 'Red'])
set_2 = set(['Red', 'Green'])
print(set_1 - set_2)

def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)

print(sum_digits(5245))

nums = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: not x % 15, nums))
print(result)




def curiosity(x:int, y:int, z: int):
    value = x
    nums2 = []
    for _ in range(0, y):
        n = random.randint(1, z)
        nums2.append(n)
    seq = list(filter(lambda x: x%value==5, nums))
    print(nums2)
    print(seq)

curiosity(16, 10, 890)


