import numpy as np
calories_stats = np.genfromtxt('cereal.csv', delimiter = ',')

# There are 60 calories per serving of CrunchieMunchies. How much higher is the average calorie count of your competition? 
average_calories = np.mean(calories_stats)
#print(calories_stats)

#Does the average calorie count adequately reflect the distribution of the dataset?
calorie_stats_sorted = np.sort(calories_stats)
#print(calorie_stats_sorted)

# Looks like the majority of the cereals are higher than the mean. Lets see if the median is a better representative of the dataset.
median_calories = np.median(calories_stats)
#print(median_calories)

#Calculate different percentiles and print them to the terminal until you find the lowest percentile that is greater than 60 calories.
nth_percentile = np.percentile(calories_stats,12)
#print(nth_percentile)
nth_percentile = np.percentile(calories_stats,6)
#print(nth_percentile)
nth_percentile = np.percentile(calories_stats,4)
#print(nth_percentile)
nth_percentile = 4

#Lets calculate the percentage of cereals that have more than 60 calories per serving
more_calories = 100 - nth_percentile
#print(more_calories)

#Calculate the amount of variation by finding the standard deviation.
calorie_std = np.std(calories_stats)
print(calorie_std)



