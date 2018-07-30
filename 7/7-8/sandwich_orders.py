sandwich_orders = ['pastrami','tomato','pastrami','potato','pastrami','cheese','pastrami']

finished_sandwich = []

while  sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your "+current_sandwich.title()+"sand_which")
    finished_sandwich.append(current_sandwich)
for sand_which in finished_sandwich:
  print("Finsihed swich:"+sand_which)


