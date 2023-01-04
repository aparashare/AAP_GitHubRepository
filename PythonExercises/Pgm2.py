# Basic arithematic operations
number = 1+2*3/4.0      # 1+((2*3)/4)   python follow order of operations
square = 2**2
cube = 2**3
remainder = float(11%4)
quotient = float(11/4)
lotsOfHellos = "hello" * 6
evenNumbers = [2,4,6,8,10]
oddNumbers = [1,3,5,7,9]
allNumbers = evenNumbers + oddNumbers

print("Number 1+2*3/4.0") 
print(number)
print("11%4")
print(remainder)
print(quotient)
print(square)
print(cube)
print(lotsOfHellos)
print(allNumbers)

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

    name = "Abhijit"
    age = 45
    print("%s is %s years old" % (name, age)) 