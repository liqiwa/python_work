#for value in range(1,21):
 #print(value)

numbers = [value for value in range(1,1000001)]
 #print(numbers)
#print("min is "+ str(min(numbers)))
##print("max is " + str(max(numbers)))
unevennumber = [value for value in range(1,20,2)]

print(unevennumber)

three = [value for value in range(3,30,3)]
print(three)
#

cube = []
for value in range(1,10):
	cube3 = value**3
	cube.append(cube3)
print(cube)
cube = [value**3 for value in range(1,10)]
print(cube)