from die import Die 
import pygal

#创建2个D6骰子
die_1= Die()
die_2 = Die(10)
de = Die()
results = []
for roll_num in range(0,50000):
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

hist.title = "Results of rolling one D6 10000 times."
hist.x_labels = ['2','3','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D10',frequencies)
hist.render_to_file('die_visual.svg')
print(frequencies)

