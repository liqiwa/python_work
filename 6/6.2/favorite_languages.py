favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',}
print("Sarah`s favorite_language is "+str(favorite_languages['sarah'].title())+'.')
#6-1
people = {'name':'mm','xing':'he','age':'30','city':'sjz'}
print(people)

words = {'liebiao':'liebiao,yuansu jihe','yuanzu':'bukebian xulie','zidian':'jianzhidui'}
for k,v in words.items():
	print(k+"\n"+v)

for name,language in favorite_languages.items():
  print(name.title()+ "'s favorite language "+language.title())

for language in set(favorite_languages.values()):
  print(language)

favorite_languages['zifuchuang'] = 'chulizifu'
favorite_languages['for xunhuan']  = 'xunhuan henduo'
print(favorite_languages)

nations = {'nile':'egypt','changjiang':'china','Amazon River':'South America'}
for river,nation in nations.items():
  print("The "+river.title()+" runs through "+nation.title())
for river in nations.keys():
	print(river)
for nation in nations.values():
	print(nation+"\n")


invite = ['jen','phil','for xunhuan']
for name,language in favorite_languages.items():
	if name in invite:
		print(name+" Thank you!")
	else:
	  print(name+" invite join survey")
print(favorite_languages)


