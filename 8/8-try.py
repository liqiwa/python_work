###8-3
def make_shirt(chima,word):
	print(chima+word)
make_shirt(word = " I ",chima = "l")

###8-4

def make_shirt(chima,word =" I love Python"):
	print(chima+word)

make_shirt("45")
make_shirt("33")
make_shirt("22"," I love Java")
##8-6
def city_country(city,country):
	
	print('"'+city.title()+","+country.title()+'"')
city_country("Santiago","Chile")

#8-7

def make_album(song_name,album_name,number = ""):
	if number:
		albumfullname = {'song_name':song_name,'album_name':album_name,'number':number}
	else:
		albumfullname = {'song_name':song_name,'album_name':album_name}

	return albumfullname
 
while True:
	print("Please input song_name:")
	print("\n q is  Quit!")

	song_name = input("song_name:")
	if song_name == 'q':
		break
	print("Please input album_name:")
	print("\n q is  Quit!")
	album_name = input("album_name:")
	
	if album_name == 'q':
		break
	albumfullname = make_album(song_name,album_name)
	print("\n Favorite music :"+albumfullname['song_name']+"  "+albumfullname['album_name'])





