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