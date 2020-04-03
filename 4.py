def highestPowerOf2(n): 
	return (n & (~(n - 1))) 
n = int(input()) 
highest=highestPowerOf2(n)

for i in range(0,100000):
    if highest==2**i:
        highest=i
        break
print(highest)