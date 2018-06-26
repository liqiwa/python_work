motocycles =["hoda","yamaha","sukum"]
print(motocycles)
#add
motocycles.append('jialing')
print(motocycles)
motocycles.insert(2,'yadi')
print(motocycles)
#del
del motocycles[4]
print(motocycles)
poped_motocycle = motocycles.pop()
print(motocycles)
print(poped_motocycle)
last_owned = motocycles.pop()
print("The last motocycles I owned was a "+last_owned.title()+".")
motocycles = ["hoda","yamaha","suzuki","ducati"]
print(motocycles)
too_expensive = "ducati"
motocycles.remove(too_expensive)
print(motocycles)

print("\nA "+too_expensive.title()+" is too expensive for me.")


