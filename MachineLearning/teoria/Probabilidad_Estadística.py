import statistics as stats

numbersMean = [1525, 257, 378, 9543, 7854, 152]
numbersMode = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]
numbersMedian = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]

print("Mean")
print(stats.mean(numbersMean))

print("Mode")
print(stats.mode(numbersMode))

print("Median")
print(stats.median(numbersMedian))