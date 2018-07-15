alien_o = {'color':'green','points' :10 }

print(alien_o)

alien_o['x_position'] = 0
alien_o['y_position'] = 25

alien_o['color'] = 'yellow'
print("The alien is now"+alien_o['color'] +".")
print(alien_o)
newPoint = alien_o['points']
print("you are is get "+str(newPoint)+"points!!")