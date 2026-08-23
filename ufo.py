import pandas as pd
import matplotlib.pyplot as plt

ufo = pd.read_csv('ufo_sightings_scrubbed.csv')

print(ufo.head())  # To see the first few rows of the dataset

#print(ufo.to_string())

print(ufo.info())

print("##### Summary for numeric columns in the dataset #####")
print(ufo.describe())  # Gives summary statistics for the numeric columns in your dataset.


print("##### Columns in the dataset #####")
print(ufo.columns)  # To know exactly what columns are in the dataset


ufo['datetime'] = pd.to_datetime(ufo['datetime'], errors='coerce') # Convert 'datetime' column to datetime format, coercing errors to NaT
ufo['date posted'] = pd.to_datetime(ufo['date posted'], errors='coerce') # Convert 'date posted' column to datetime format, coercing errors to NaT

ufo["year"] = ufo["datetime"].dt.year

print(ufo.head())


print("##### NULL values in the dataset #####")
print(ufo.isnull().sum())  # To investigate missing values in the dataset


print("##### How many times a shape was reported #####")
print(ufo["shape"].value_counts())



print("##### UFO sightings by year #####")
year_counts = ufo["year"].value_counts().sort_index()
print(year_counts.to_string())




#how many UFO sightings by year (matplotlib)
year_counts.plot(kind="line")
plt.title("UFO Sightings by Year")
plt.xlabel("Year")
plt.ylabel("Number of Sightings")
plt.xticks(rotation=45)
plt.show()



#how many times a shape was reported (matplotlib)
shape = ufo["shape"].value_counts().head(10)
shape.plot(kind="bar")
plt.title("Top 10 Most Common UFO Shapes")
plt.xlabel("Shape")
plt.ylabel("Number of Sightings")
plt.xticks(rotation=45)
plt.show()



#how many times a country was reported (matplotlib)
ufo['country'] = ufo['country'].replace({'us': 'United States', 'gb': 'United Kingdom', 'ca': 'Canada', 'de': 'Germany', 'fr': 'France', 'au': 'Australia', 'it': 'Italy', 'es': 'Spain', 'ru': 'Russia'})
ufo["country"].value_counts().plot(kind="line")

plt.title("Countries with UFO Sightings")
plt.xlabel("Country")
plt.ylabel("Number of Sightings")
plt.xticks(rotation=45)
plt.show()

#average duration of UFO sightings by shape 
ufo["duration (seconds)"] = pd.to_numeric(ufo["duration (seconds)"], errors="coerce")

print("##### Average duration of UFO sightings by shape #####")
print(ufo.groupby('shape')['duration (seconds)'].mean().sort_values(ascending=False).head(10))


#top 10 UFO shapes in Canada
canada_ufo = ufo[ufo['country'] == 'Canada']
print("##### Top 10 UFO shapes in Canada #####")
print(canada_ufo['shape'].value_counts().head(10))