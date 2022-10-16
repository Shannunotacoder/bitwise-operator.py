# to find binary digits we have to divide the number with 2 and look at the remainder 
# example 19 /2 9 and remainder 1 now 9/2 remainder 1 4/2 2 and remainder 0 2/2 1 and remainder 0

#BITWISE  OPERATORS 
#they are used to comapare binary binary numbers 


# & => and if both bits are 1, it sets bit 1

# | => or  if one of te bits is 1, it sets each bit to 1

# ^ => xor if only one of the two bits is 1 , it sets each bit to 1

# - => not inverts all Bits  a=-(a+1)

#<< => zero fill left shift => binary number is appended with 0's at the end

#>> => right shift => in simple terms the right side of bits are removed

# a = 10 =1010 

# a << 2= 1010<<2 = 101000 = 40
# a >> 2= 1010>>2 = 10 =2

x = 10
y = 7 

print(x & y)
print(x | y)
print(~(x&y))