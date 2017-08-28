"""
Ques: 1
To find error variance
"""

x_t = [75, 74, 79, 83, 69, 78, 71, 80, 77, 85, 81, 70]
a = 75.78
b = 0.16

assert len(x_t) == 12
# error_t = x_t - a - b*t

error_t = []
sum_x_sq = 0
print("Error: ")
for (i, x) in enumerate(x_t):
    error_t.append(x - a - (b*(i+1)))
    sum_x_sq += error_t[i] ** 2
    print(error_t[i])

mean_error = sum(error_t) / len(error_t)
print("Mean Error: %f" % mean_error)

standard_deviation = (sum_x_sq / len(error_t)) - (mean_error ** 2)
print("sigma sq : %f" % standard_deviation)
print("sigma : %f" % standard_deviation ** 0.5)
