n = int(input("Enter the number of data: "))
count = 0
sum = 0
while count < n :
	data = int(input("Enter an integer: "))
	sum += data 
	count += 1
print ("The average of ", n , "numbers is", sum/n)