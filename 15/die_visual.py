from die import Die 
import pygal
de = Die()
results = []
for roll_num in range(0,100):
	result = de.roll()
	results.append(result)
#分析结果
frequencies = []
for value in range(1,de.num_sides+1):
	frquency = results.count(value)
	frequencies.append(frquency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 10000 times."
hist.x_labels = ['1','2','3','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
print(frequencies)

