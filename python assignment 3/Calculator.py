print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");
print("5. Power");
print("6. Exit");
choice = int(input("Enter your choice: "));
if (choice>=1 and choice<=5):
    print("Enter two numbers: ");
    num1 = int(input());
    num2 = int(input());
    if choice == 1:
    	res = num1 + num2;
    	print("Result = ", res);
    elif choice == 2:
    	res = num1 - num2;
    	print("Result = ", res);
    elif choice == 3:
    	res = num1 * num2;
    	print("Result = ", res);
    elif choice == 4:
    	res = num1 / num2;
    	print("Result = ", res);
    elif choice == 5:
    	res = num1 ** num2
    	print("Result = ", res); 
    elif choice == 6:
        exit();
else:
    print("Wrong input..!!");