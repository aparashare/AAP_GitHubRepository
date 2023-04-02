print("My First Python Program")
NoofCars=0
NoofBikes=0
NoofCars=input("Enter no. of cars parked:")
print(NoofCars)
NoofBikes=input("Enter no. of bikes parked:")
print(NoofBikes)
Revenue=0
Revenue=int(NoofCars)*40+int(NoofBikes)*20
print("NoofCars:", NoofCars)
print("NoofBikes:", NoofBikes)
print("Revenue from parking:", Revenue)
if(Revenue>=500):
    print("Profitiable Day:", Revenue)
else:
    print("Loss making day, Revenue>=500: ", Revenue)