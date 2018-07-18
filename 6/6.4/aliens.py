alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':5}
alien_2 = {'color':'red','points':10}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
  print(alien)

aliens = []

for alien_number in range(30):
	new_alien = {'color':'yellow','points':5}
	aliens.append(new_alien)

for alien in aliens[:5]:
  print(str(alien) +" xin laide ")

