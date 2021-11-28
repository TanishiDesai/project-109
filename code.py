import pandas as pd
import statistics as stat
import csv 

df = pd.read_csv("data.csv")
list = df["reading score"].to_list()
mean = stat.mean(list)
median = stat.median(list)
mode = stat.mode(list)
std = stat.stdev(list)

print("Mean of data ===> ", mean)
print("median of data ===> ", median)
print("Mode of data ===> ", mode)

first_std_start, first_std_end = mean-std, mean+std
second_std_start, second_std_end = mean-(2*std), mean+(2*std)
third_std_start, third_std_end = mean-(3*std), mean+(3*std)

print("{}% of data lies within 1 standard deviation".format(len(first_std_start)*100.0/len(list)))
print("{}% of data lies within 2 standard deviations".format(len(second_std_start)*100.0/len(list)))
print("{}% of data lies within 3 standard deviations".format(len(third_std_start)*100.0/len(list)))


