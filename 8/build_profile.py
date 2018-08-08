def build_profiles(first,last,**user_info):
	"""创建一个字典，其中包括我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile
##user_profile = build_profiles('he','meng',location = 'china',field ='math',age = '30')

print(build_profiles)