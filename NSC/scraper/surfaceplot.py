import matplotlib.pyplot as plt




x = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
y = [24.02, 16.35, 11.23, 13.14, 18.96, 23.86, 17.3, 24.29]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_xlabel('Years')
ax.set_ylabel('Surface Temp (c)')
ax.set_title('Surface Tempurature 2017 - 2024')

plt.show()