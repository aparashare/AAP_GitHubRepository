# Add variables, strings and print
numbers = []
strings = []
names = ["Abhijit", "Vaidehi", "Krupa", "Aakash"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("Pune")
strings.append("Ahmedabad")
strings.append("Mumbai")

first_names = names[0]
second_names = names[1]
third_names = names[2]
forth_names = names[3]

print(numbers)

for x in numbers:               
    print(x)
# we have not defined x then how does it work? Does python automitcally takes variable definition??

print("The second name of the names list is %s" %second_names)
print("Names %s:" %names)
print("Cities %s: " %strings)

#   note
#   %s - String (or any object with a string representation, like numbers)
#   %d - Integers
#   %f - Floating point numbers
#   %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#   %x/%X - Integers in hex representation (lowercase/uppercase)  

data = ("Abhijit","Parashare", 100.25)
format_string = "Hello %s %s, your account balance is: %s"
print(format_string %data)