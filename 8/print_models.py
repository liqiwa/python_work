#首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

while unprinted_designs:
	curent_design = unprinted_designs.pop()

	print("Printing model:"+curent_design)
	completed_models.append(curent_design)

print("\n The following models have been printed:")
for completed_model in completed_models:
	print(completed_model)
