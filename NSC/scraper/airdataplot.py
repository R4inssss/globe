import matplotlib.pyplot as plt




x = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
y = [4.14, 6.61, 7.74, 7.79, 11.92, 11.25, 8.53, 1.82, 11.26, 8.18]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_xlabel('Years')
ax.set_ylabel('Air Temp (c)')
ax.set_title('Air Tempurature 2015 - 2024')

plt.show()