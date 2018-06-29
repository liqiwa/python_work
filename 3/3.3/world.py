worldplace = ["shenzhen","beijing","amarican","riben","xiaweiyi"]
print(worldplace)
print("Here is sorted list")
print(sorted(worldplace))
print("Here is original list")
print(worldplace)

print(sorted(worldplace,reverse= True))
print(worldplace)
#fanzhuan
print("Here is reverse method")
worldplace.reverse()
print(worldplace)
print("Here is reverse again")
worldplace.reverse()
print(worldplace)
print("Here is use sort")
worldplace.sort()
print(worldplace)
print("Here is use sort reverse word ")
worldplace.sort(reverse = True)
print(worldplace)
####all function and method 
worldcup = ["Germany","Brazil","Italy","Japan","Argentina","Holland","Portugal"]
# yongjiuxing method
worldcup.sort()
print(worldcup)
worldcup.sort(reverse = True)
print(worldcup)
worldcup.append("China")
print(worldcup)
worldcup.insert(0,"korea")
print(worldcup)
del worldcup[0]
print(worldcup)
print(worldcup.pop()+" out")
print(worldcup)
print(worldcup.pop(4)+" out ")
print(worldcup)
#int cast str 
print("remain "+ str(len(worldcup))+ " Team")
weedout = "Japan"
print(worldcup.remove(weedout))
print(weedout+"is  weedout")
print(worldcup)
print(sorted(worldcup))
