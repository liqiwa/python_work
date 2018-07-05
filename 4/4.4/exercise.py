players = ["charles","martina","michal","florence","eli"]
print('The first three items in the list are:')
print(players[:3])
print('Three items from the middle of the list are:')
print(players[1:-1])
print('The last three items in the list are:')
print(players[-3:])
#4-11
pizzas = ["fruit","beef","shrimp"]
friend_pizzas = pizzas[:]
pizzas.append('vegetables')
friend_pizzas.append('onion')
print('My favorite pizzas are:')
for value in pizzas:
	print(value)
print("My frined's favorite pizzas are: ")
for  value in friend_pizzas:
	print(value)
#4-12
my_foods = ["pizza","orange","falafel","carrot cake"]
friends_foods = my_foods[:]
friends_foods.append('pepery')
print("My favorite foods are:")
for  value in my_foods:
	print(value)
print("My friend's favorite foods are:")
for value in friends_foods:
	print(value)
