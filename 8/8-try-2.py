#8-9

magic_name = ['zhoujielun','hemm','fangshiyu']

def show_magicians(name):
	print(name)

new_magic_name = []
def make_great(name,names):
	for old_name in name:
		new_name = "the Great " + old_name
		new_magic_name.append(new_name)
		
	show_magicians(new_magic_name)
	show_magicians(names)
make_great(magic_name[:],magic_name)