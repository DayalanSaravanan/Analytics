N = int(input("Enter the number of lines to print: "))
for i in range(1,N+1): print(((N-i) * " ") + (str(i) + " ") * i)
