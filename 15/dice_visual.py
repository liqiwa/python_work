from die import Die 
import pygal
import matplotlib.pyplot as plt  
#创建2个D6骰子
die_1= Die()
die_2 = Die()
de = Die()
results = []
for roll_num in range(0,100):
	result = die_1.roll() +die_2.roll()
	results.append(result)
#分析结果
frequencies = []
max_result = die_1.num_sides +die_2.num_sides
for value in range(2,max_result+1):
	frquency = results.count(value)
	frequencies.append(frquency)

#对结果进行可视化
hist = pygal.Bar()
labels = []
hist.title = "Results of rolling one D6 10000 times."
for xlabel in range(2,max_result+1):
	labels.append(str(xlabel))

hist.x_labels = labels[:]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')
print(frequencies)

