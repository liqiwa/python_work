my_foods = ["pizza","orange","falafel","carrot cake"]
friend_foods = my_foods[:]
print(friend_foods)

my_foods.append("my_foods + 1")
friend_foods.append("friedd_foods + 2")

print(my_foods)
print(friend_foods)

my_foods = friend_foods
my_foods.append('cannoli')
print(my_foods)
print(friend_foods)