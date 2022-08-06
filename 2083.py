import sys

while True:
    name, age, kg = sys.stdin.readline().split()

    if name == '#':
        break

    if int(age) > 17 or int(kg) >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')
