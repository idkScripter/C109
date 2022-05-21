import statistics
import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv") 
math_score = df["math score"].tolist()
reading_score = df["reading score"].tolist()
writing_score = df["writing score"].tolist()

math_mean = statistics.mean(math_score)
reading_mean = statistics.mean(reading_score)
writing_mean = statistics.mean(writing_score)

math_median = statistics.median(math_score)
reading_median = statistics.median(reading_score)
writing_median = statistics.median(writing_score)

math_mode = statistics.mode(math_score)
reading_mode = statistics.mode(reading_score)
writing_mode = statistics.mode(writing_score)

math_stdev = statistics.stdev(math_score)
reading_stdev = statistics.stdev(reading_score)
writing_stdev = statistics.stdev(writing_score)

print(math_mean)
print(math_median)
print(math_mode)
print(math_stdev)

print(reading_mean)
print(reading_median)
print(reading_mode)
print(reading_stdev)

print(writing_mean)
print(writing_median)
print(writing_mode)
print(writing_stdev)

math_stdev_start, math_stdev_end = math_mean - math_stdev, math_mean + math_stdev
reading_stdev_start, reading_stdev_end = reading_mean - reading_stdev, reading_mean + reading_stdev
writing_stdev_start, writing_stdev_end = writing_mean - writing_stdev, writing_mean + writing_stdev

print(math_stdev_start)
print(math_stdev_end)

print(reading_stdev_start)
print(reading_stdev_end)

print(writing_stdev_start)
print(writing_stdev_end)

fig1 = ff.create_distplot([math_score], ["math_score"], show_hist=False)
fig1.add_trace(go.Scatter(x=[math_mean, math_mean], y=[0, 1], mode = "lines", name = "Math Mean"))
fig1.show()

fig2 = ff.create_distplot([reading_score], ["reading_score"], show_hist=False)
fig2.add_trace(go.Scatter(x=[reading_mean, reading_mean], y=[0, 1], mode = "lines", name = "Reading Mean"))
fig2.show()

fig3 = ff.create_distplot([writing_score], ["writing_score"], show_hist=False)
fig3.add_trace(go.Scatter(x=[writing_mean, writing_mean], y=[0, 1], mode = "lines", name = "Writing Mean"))
fig3.show()