#BIT MANIPULATION
print(int('11111',2)) #binary to decimal
print(bin(10)) #decimal to binary
#symbols
print("OPERATORS")
print("\n")
print(23 | 13) # - or
print(23 & 13) # - and
print(23 ^ 13) # - XOR

print(22<<2) #left shift bits of number 22 two places
print(22>>2) #right shift bits of number 22 two places
print(~(3)) #flips bits

#explaination

binary=bin(22)
print(binary[2:])

#right shift

#10110 2 bits 101 ->5
#10110 2 bits left shift 1011000
print(int('1011000',2)) #i,e 88
