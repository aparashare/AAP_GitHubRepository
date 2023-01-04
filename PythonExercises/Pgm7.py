#!/usr/bin/env python3

# working with disctionaries --> Key value pair

phonebook = {   "Abhijit"   : 8007285798,
                "krupa"     : 9881014908,
                "Vaidehi"   : 1010120131
}

phonebook.pop("Abhijit")                    # Deletes
phonebook["Aakash"] = 2012022034            # add
del phonebook["Vaidehi"]                    # add

print(phonebook)