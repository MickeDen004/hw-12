import random
from math import sqrt, factorial
import operator
print("The first exercise")
print("Выведите все элементы, которые меньше 5")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

print(list(filter(lambda element: element < 5, a)))

print([e for e in a if e < 5])

random_array = []
for i in range(0, 20):
    n = random.randint(1, 100)
    random_array.append(n)
f = random.randint(100, 1000)
x = random.randint(1, 1000)


print(x, f)
print(list(filter(lambda e:factorial(f) > e >= sqrt(x), random_array)))
print(sorted([e for e in random_array if e < sqrt(x)], reverse= True))

print("The second exercise")
print("Вернуть список, который состоит из элементов, общих для этих двух списков.")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(filter(lambda e:e in b, a)))
print([e for e in a if e in b])
print(set(a) & set(b))

print("exerxise 3")
print("Отсортируйте словарь по значению в порядке возрастания")


# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# result = dict(sorted(d.items(), key= operator.itemgetter(1)))
# print(result)
# result = dict(sorted(d.items(), key= operator.itemgetter(1), reverse= True))

print("Exercise 4")
print("Merge dicts")
dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}
result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)
print(result)
result_2 = {**dict_a, **dict_b, **dict_c}
print(result_2)
print("Exercise 5")
print("Triangle of pascal")
def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in
    zip(row + y, y + row)]


pascal_triangle(6)

def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome('abba'))

def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')

convert(123456)

values = input('Введите числа через запятую: ')
ints_as_strings = values.split(',')
ints = map(int, ints_as_strings)
lst = list(ints)
tup = tuple(lst)
print("List: {0}".format(lst))
print("Tuple: {0}".format(tup))


names = input('Enter string values: ')
strings = names.split(',')
striing = map(str, strings)
lst1 = list(striing)
tuple1 = tuple(lst1)
print("List: {0}".format(lst1))
print("Tuple: {0}".format(tuple1))

print(f"First element is {a[1]}\nLast element is {a[-1]}")

def get_extension(filename):
    filename_parts = filename.split('.')
    if len(filename_parts)<2:
        raise ValueError('the file has no extension')
    first, *middle, last = filename_parts
    if not last or not first and not middle:
        raise ValueError('the file has no extension')
    return filename_parts[-1]

print(get_extension('abc.py'))
print(get_extension('abc'))
print(get_extension('.abc'))
print(get_extension('.abc.def.'))

def number_operations(n: int):
    n2 = n*n
    n3 = n*n*n
    res = n + n2 + n3
    print(f"Result of n + nn +nnn is {res}")
number_operations(9)