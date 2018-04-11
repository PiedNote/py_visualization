# encoding: utf-8
import pygal
from study_pygal.die import Die
die = Die()
die2 = Die()
results = []
for roll_num in range(10000):
    result = die.roll() + die2.roll()
    results.append(result)
frequencies = []
for value in range(2, die.num_sides*2+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(results)
print(frequencies)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add('D6+D6', frequencies)
hist.render_to_file('die_visual2getouzi.svg')
