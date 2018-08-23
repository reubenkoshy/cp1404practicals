

# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()
#
# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()
#
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()
#
# n = int(input("Enter a Number: "))
#
# for i in range(1, n, 1):
#     print(end='*')

stars = int(input("Enter number of stars (*):"))
for n in range(1, stars + 1, 1):
    print("*" * n)