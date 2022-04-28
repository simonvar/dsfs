from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("GDP")

plt.ylabel("$")
plt.show()

movies = ["Enni Holl", "Ben Gour"]
num_oscars = [5, 11]
plt.bar(range(len(movies)), num_oscars)

plt.title("Films")
plt.ylabel("Oscars")
plt.xticks(range(len(movies)), movies)

plt.show()
