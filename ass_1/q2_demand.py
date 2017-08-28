
"""
Ques 2
a) Estimate demand for next 4 weeks using 4-week simple moving point avg as
   well as exponential smoothing method with a=0.1
"""

# Part A: Simple moving point average
print("\nPart A: By Moving Point Average Method")

demands = [108, 116, 118, 124, 96, 119, 96, 102, 112, 102, 92, 91]

print("Single moving point average:")

moving_pt_avg = []  # 4-week mva
for (i, demand) in enumerate(demands[:-3]):
    moving_pt_avg.append(sum(demands[i: i+4]) / 4.0)
    print(demands[i: i+4], sum(demands[i: i+4]) / 4.0)

print("\nDouble moving point average:")

double_mva = []
for (i, mva) in enumerate(moving_pt_avg[:-3]):
    double_mva.append(sum(moving_pt_avg[i: i+4]) / 4.0)
    print(moving_pt_avg[i: i+4], double_mva[i])

print("\nForecasts for the next 4 weeks:")

# Forecast for next 4 weeks
forecasts = []
for i in range(1, 5):
    diff_1 = (2*moving_pt_avg[-1] - double_mva[-1])
    diff_2 = i*(moving_pt_avg[-1] - (double_mva[-1]))
    forecast = (diff_1 + (2/3.0)*diff_2)
    forecasts.append(forecast)
    print(forecast)

# Part A: Simple Exponential Smoothing
print("\nPart A: By Simple Exponential Smoothing Method")

alpha = 0.1

beta = 1 - alpha
weighted_sum = 0
for (i, _) in enumerate(demands):
    weighted_sum += (beta ** (len(demands) - i - 1)) * _
a = ((1 - beta) / (1 - beta**len(demands))) * weighted_sum
print("Value of parameter a: %f" % a)


# Part B: MAD, MAPE, MSE, bias, and TS
print("\nPart B: MAD, MAPE, MSE, bias, TS")

# MAD: 4-MPA method
t_1 = sum(demands) * (
        (2*(2*len(demands) - 1)/(float(len(demands))*(len(demands) - 1))))
weighted_sum_2 = 0
for (i, _) in enumerate(demands):
    weighted_sum_2 += (i + 1)*_
t_2 = 6 * ((weighted_sum_2/float(len(demands)))/(len(demands) - 1))

a_mpa = t_1 - t_2
print("Parameter a for 4-point avg: %f" % a_mpa)

t_3 = weighted_sum_2 * (12.0 / (len(demands)*((len(demands)**2 - 1))))
t_4 = sum(demands) * (6.0 / (len(demands)*(len(demands) - 1)))

b_mpa = t_3 - t_4
print("Parameter b for 4-point avg: %f" % b_mpa)

error_t = []

print("Errors:")
for (i, _) in enumerate(demands):
    error_t.append(_ - a_mpa - (b_mpa*(i + 1)))
    print(error_t[i])

MAD_mpa = 0
for _ in error_t:
    if _ < 0:
        _ *= -1
    MAD_mpa += _

MAD_mpa /= len(demands)
print("MAD moving point avg: %f" % MAD_mpa)

error_ses = []

for _ in demands:
    error_ses.append(_ - a)
    print(_ - a)

MAD_ses = 0
for _ in error_ses:
    if _ < 0:
        _ *= -1
    MAD_ses += _
MAD_ses /= len(demands)
print("MAD simple exponential smoothing: %f" % MAD_ses)

MSE_mpa = 0
for _ in error_t:
    MSE_mpa += _**2
MSE_mpa /= len(demands)
MSE_mpa = MSE_mpa ** 0.5

print("\nMSE moving point avg: %f" % MSE_mpa)

MSE_ses = 0
for _ in error_ses:
    MSE_ses += _**2
MSE_ses /= len(demands)
MSE_ses = MSE_ses ** 0.5
print("MSE simple exponential smoothing: %f" % MSE_ses)
