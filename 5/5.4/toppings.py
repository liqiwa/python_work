requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print('Adding'+requested_topping +'.')
		print('\n Finished making you pizza!')
else:
	print("Are you sure you want a plain pizza?")
#####
users = ['admin','guest','xiaom','xiaoh','luren']
users = []
if users:
 for user in users:
    if user == 'admin':
    	print("Hello admin,would you like to see a status report?")
    else:
    	print("Hello thank you for logging in again")
else:
		print('We need to find some users!')
####
current_users = ['xiaoh','xiaom','jack','jobs','bill','John']
new_users = ['jack','bill','xiaoxiao','big','max','JOHN']
for new_user in new_users:
	current_users = [item.lower() for item in current_users]
	if new_user.lower() in current_users:

		print(new_user+" is usage,please entry the other one")
	else:
		print(new_user+' is new_name')
#####
ordinal = [value for value in range(1,10)]
for value in ordinal:
    if value == 1:
	    print(str(value)+'st')
    elif value == 2:
        print(str(value)+'nd')
    elif value == 3:
        print(str(value)+'rd')
    else:
        print(str(value)+'th')