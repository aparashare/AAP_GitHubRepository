#!/usr/bin/env python3 

class myClass:
    variable = "abhijit"

    def function(self):
        print("This is message inside the myClass")

object1 = myClass()                     # each object contains independent copies of the variable defined in a class
object2 = myClass()

object1.variable = "parashare"
print(object1.variable)
print(object2.variable)
object1.function()