from math import ceil
distance=float(input('Enter Distance in KM: '))
mileage = float(input('Enter Mileage: '))
fuel = float(input('Enter Fuel Price per ltr: '))
toll = float(input('Enter Toll: '))
daily_wage = float(input('Enter Daily Wage: '))
budget = float(input('Enter Budget: '))

days=ceil(distance/500)



Fuel_Cost =  ceil(distance/mileage)*fuel
Driver_cost = daily_wage*days
Total_trip_cost = Fuel_Cost + toll + Driver_cost

print("Total Cost: ",Total_trip_cost)

d1=budget-Total_trip_cost
d2=Total_trip_cost-budget

if Total_trip_cost>budget:
    print("OVER BUDGET BY: ",d1)
else:
    print("WITHIN BUDGET SAVINGS:",d2)