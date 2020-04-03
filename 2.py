binary=[]
middle=[]
def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    binary.append(num % 2)

number = int(input())

decimalToBinary(number)
last=int(len(binary)/2)

if len(binary)/2==int(len(binary)/2):
    swap_l=binary[-last:]
    swap_r=binary[0:len(binary)-last]
    # print(swap_l,swap_r)
    swapped=swap_l + swap_r
else:
    swap_l=binary[-last:]
    middle.append(binary[-last-1])
    swap_r=binary[0:len(binary)-last-1]
    # print(swap_l,middle,swap_r)
    swapped=swap_l + middle + swap_r

swapped = [str(i) for i in swapped]
s = "".join(swapped) 
print(int(s,2))
