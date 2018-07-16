alien_o = {'color':'green','points' :10 }

print(alien_o)

alien_o['x_position'] = 0
alien_o['y_position'] = 25

alien_o['color'] = 'yellow'
print("The alien is now"+alien_o['color'] +".")
print(alien_o)
newPoint = alien_o['points']
print("you are is get "+str(newPoint)+" points!!")
##new alien
alien_o = {}
alien_o['color'] = 'green'
alien_o['print'] = 5
###alien 
alien_o = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-psition:"+str(alien_o['x_position']))
if alien_o['speed'] == 'medium':
   x_increment = 2
elif alien_o['speed'] =='slow':
	x_increment = 1
else:
    x_increment = 3
alien_o['x_position'] = alien_o['x_position'] + x_increment
print("New x-psition is "+str(alien_o['x_position']))

##del
alien_o = {'color':'green','x_position':'24'}
print(alien_o)
del alien_o['x_position']
print(alien_o)

