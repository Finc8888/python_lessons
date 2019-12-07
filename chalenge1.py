import math as m
file = open('input.txt', 'r')
arr = file.readlines()
# arr = [1969]
file.close()
fuel_result = 0
for item in arr:
   fuel = m.floor((int(item)/3) - 2)
   fuel_result += fuel
   while(fuel > 0):
       fuel = m.floor((int(fuel) / 3) - 2)
       if fuel > 0 :
        fuel_result += fuel
print(fuel_result)