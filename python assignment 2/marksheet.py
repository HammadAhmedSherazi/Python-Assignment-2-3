sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
tot=int(input("Enter total marks:"))
obt=sub1+sub2+sub3+sub4+sub5
per=(obt/tot)*100
if per>=90:
    print("Grade: A1+")
elif per>=80:
    print("Grade: A1")
elif per>=70:
    print("Grade: B")
elif per>=60:
    print("Grade: C")
elif per>=50:
    print("Grade: D")
else:
    print("Grade: F")