import matplotlib.pyplot as plt
from pylab import mpl
import twstock
import datetime

today = datetime.datetime.today()
month = today.month

mpl.rcParams["font.sans-serif"] = ["SimHei"]
stock2330 = twstock.Stock("2330")
print(stock2330.price)
avg5 = stock2330.moving_average(stock2330.price, 5)
avg10 = stock2330.moving_average(stock2330.price, 10)
avg20 = stock2330.moving_average(stock2330.price, 20)
i=1
day = [0] * 31
while i < 32:
    day[i-1] = i
    i = i+1



print(avg20)
plt.title(u"GG", fontsize=24)
plt.plot(day, stock2330.price, "r", day[4:], avg5, "g", day[9:], avg10, "y", day[19:], avg20, "b")

plt.show()

# plt.title(u"GG", fontsize=24)
# plt.plot(stock2330.price, "r-o")

# plt.show()

# i=0
# while i<31:
#     print("Date",stock2330.date[i])
#     print("股票收盤價",stock2330.price[i])
#     print("股票成交量",stock2330.turnover[i])
#     i=i+1
