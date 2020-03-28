from getpass import getpass
a, b, *c = (1, 2, 3, 4, 5)
condition = False
x = 1 if condition else 0
for value in c:
    print(value)
print(f'{a} is {b} and {c} {x}')


username = input("input username: ")

password = getpass("hello: ")

print(f'{username}')
