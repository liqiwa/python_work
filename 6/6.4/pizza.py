pizza = {
	'crust':'thick',
	'topping':['mushrooms','extra chess'],
}

print("You order a"+pizza['crust']+"-crust pizza"+"With the fllowing toppings:")

for topping in pizza["topping"]:
	print("\n"+topping)

