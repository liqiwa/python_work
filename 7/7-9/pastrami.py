sandwich_orders = ['pastrami','tomato','pastrami','potato','pastrami','cheese','pastrami']
print("Pastrami is sold out")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print(sandwich_orders)