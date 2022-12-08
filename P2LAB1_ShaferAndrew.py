mg = float(input())
gascost = float(input())
amount_20_miles = (20 / mg) * gascost
amount_75_miles = (75 / mg) * gascost
amount_500_miles = (500 / mg) * gascost
print('{:.2f} {:.2f} {:.2f}'.format(amount_20_miles, amount_75_miles, amount_500_miles))
