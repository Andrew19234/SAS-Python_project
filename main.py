import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from statsmodels.formula.api import ols

# 1. Crearea și utilizarea listelor și dicționarelor
brands = ["Toyota", "Honda", "Ford"]
models = ["Corolla", "Civic", "Focus"]
cars_dict = dict(zip(brands, models))

# 2. Utilizarea seturilor și tuplurilor
car_set = set(brands)
car_tuple = tuple(models)

# 3. Definirea și apelarea unei funcții
def calculate_tax(price):
    return price * 0.19

# 4. Utilizarea structurilor condiționale
for brand in brands:
    if brand == "Toyota":
        print("Found Toyota")

# 5. Utilizarea structurilor repetitive
for brand in brands:
    print(brand)

# 6. Importul unui fișier CSV
df = pd.DataFrame({
    'Brand': ['Toyota', 'Honda', 'Ford', 'Nissan', 'Chevrolet', 'Tesla', 'BMW', 'Mercedes', 'Audi', 'Hyundai'],
    'Model': ['Corolla', 'Civic', 'Focus', 'Altima', 'Cruze', 'Model 3', '320i', 'C-Class', 'A4', 'Elantra'],
    'Year': [2012, 2015, 2014, 2016, 2018, 2020, 2013, 2017, 2019, 2021],
    'Mileage': [120000, 95000, 110000, 60000, 50000, 30000, 85000, 45000, 40000, 15000],
    'FuelType': ['Gas', 'Gas', 'Gas', 'Gas', 'Gas', 'Electric', 'Gas', 'Diesel', 'Gas', 'Gas'],
    'Price': [8000, 10000, 7000, 12000, 14000, 35000, 15000, 27000, 22000, 17000],
    'HP': [132, 158, 160, 182, 153, 271, 180, 241, 190, 147],
    'Doors': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
})

df.to_csv('CarsDataFrame.csv', index=False)
loaded_df = pd.read_csv('CarsDataFrame.csv')
print(loaded_df)

# 7. Accesarea datelor cu loc și iloc
first_car = df.loc[0]
second_car = df.iloc[1]

# 8. Modificarea datelor
df.loc[df['Brand'] == 'Toyota', 'Price'] += 1000

# 9. Utilizarea funcțiilor de grup
numeric_cols = ['Year', 'Mileage', 'Price', 'HP']
avg_prices = df.groupby('Brand')[numeric_cols].mean()

# 10. Tratarea valorilor lipsă
df.fillna(value={'Mileage': df['Mileage'].mean()}, inplace=True)

# 11. Ștergerea de coloane și înregistrări
df.drop(columns=['Doors'], inplace=True)

# 12. Prelucrări statistice
summary_stats = df.describe()

# 13. Prelucrarea seturilor de date cu merge/join
df2 = pd.DataFrame({'Brand': ['Toyota', 'Honda'], 'Country': ['Japan', 'Japan']})
df = df.merge(df2, on='Brand', how='left')

# 14. Reprezentare grafică a datelor
plt.bar(df['Brand'], df['Price'])
plt.xlabel('Brand')
plt.ylabel('Price')
plt.title('Price by Brand')
plt.show()

# 15. Utilizarea pachetului scikit-learn
kmeans = KMeans(n_clusters=3)
df['Cluster'] = kmeans.fit_predict(df[['Price', 'HP']])

# 16. Utilizarea pachetului statsmodels
model = ols('Price ~ HP', data=df).fit()
print(model.summary())

