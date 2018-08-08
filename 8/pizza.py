def make_pizza(*toppings):
	print(toppings)

make_pizza('xxxx''www')


make_pizza("xigua","xihongshi","huanggua")

##8-12
def sanwich(*material):
	print(material)

sanwich('xihongshi')

sanwich("tomato",'potato')

sanwich('Bacon','lettuce','cuke')


#8-13
def build_profile(first,last,**user_info):
	"""创建一个字典，其中包括我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('he','meng',location = 'china',field ='math',age = '30')

print(user_profile)

