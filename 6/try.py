#6-7
friend  = {'first_name':'li','last_name':'xiao','age':'20','city':'sjz'}
friend_0  = {'first_name':'qin','last_name':'shih','age':'40','city':'qin'}
friend_1  = {'first_name':'cao','last_name':'cao','age':'30','city':'shu'}

print(friend)
peoples = {'friend':{
'first_name':'li','last_name':'xiao','age':'20','city':'sjz'
},'friend_0':{
	'first_name':'qin','last_name':'shih','age':'40','city':'qin'
},'friend_1':{
	'first_name':'cao','last_name':'cao','age':'30','city':'shu'
}}
for people,info in peoples.items():
    print(people)
    full_name = info['first_name']+info['last_name']
    print(full_name.title()+" is "+info['age']+" in "+info['city'])
#6-8
dog = {'kind':'tugou','master':'lei'}
cat = {'kind':'jiaf','master':'qiaoz'}
turtle = {'kind':'shuigui','master':'xiaoquan'}
pets ={
	 'dog':{'kind':'tugou','master':'lei'},
	 'cat':{'kind':'jiaf','master':'qiaoz'},
	 'turtle':{'kind':'shuigui','master':'xiaoquan'}
	 }
for pet_kind,pet_info in pets.items():
	print(pet_kind)
	print(pet_info['kind'] + " is  "+ pet_info['master'])

#6-9
favorite_places = {'jobs':['america','japan','cal'],
'Musk':['mars','silicon valley'],
'he':['china','taiwan','america']}

for user,places in favorite_places.items():
    print(user.title() +" is favorite ")
    for place in places:
    	print(place.title()+"\n\t")
#6-10
favorite_number = {
	'jobs':['1','2','3'],
	'Musk':['3','4','5'],
	'he':['6','7','8']}
for name,numbers in favorite_number.items():
	print(name +"is  favorite ")
	for number in numbers:
		print(number)
#6-11
cities = {
	'beijing':{'country':'china','population':'16-million','fact':'capital'},
	'silicon valley':{'country':'America','population':'3.25-million','fact':'sitanfu'},
	'tokyo':{'country':'japan','population':'1.27-million','fact':'dongjingdaxue'}
}
for city,infos in cities.items():
	##print(city)
	if city == 'china':	
		print(city)
	else:
	  print(infos['country']+"  "+infos['population']+"  "+infos['fact'])


