list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20] 
repeat=[]
for i in range (len(list1)):
	k=i+1
	for j in range(k, len(list1)):
		if list1[i]==list1[j] and list1[i] not in repeat:
			repeat.append(list1[i])
			
			print(repeat)
		