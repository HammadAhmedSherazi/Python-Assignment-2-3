list = []
num = int(input('How many numbers: '))
for i in range(num):
    numbers = int(input('Enter number '))
    list.append(numbers)
print("Maximum element in the list is :", max(list)) 