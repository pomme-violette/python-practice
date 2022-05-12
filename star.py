for _ in range(5):
    print('*', end='')

print('\n----------')

for _ in range(5):
    print('*')

print('----------')

for _ in range(5):
    print('*' * 5)

print('----------')

for i in range(1, 6):
    print("*" * i)

print('----------')


for i in range(4):
    match i:
        case 0:
            print('*')
    print(f"{' ' * i} *")


print('----------')

for i in range(5):
    print("*" * (5 - i))