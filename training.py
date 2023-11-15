import pandas as pd
import joblib

from sklearn.cluster import KMeans

### Lendo o CSV
data = pd.read_csv('Src/FivePersonality.csv', sep='\t')

### Formatando a saída dos valores
pd.options.display.float_format = "{:.2f}".format

### Tirando as colunas desnecessárias para o sistema
# print(data.describe())
data.drop(data.columns[50:], axis=1, inplace=True)

### Retirando todos os registros com valores 0 como resposta
#print(data[(data == 0.00).all(axis=1)].describe())
data = data[(data > 0.00).all(axis=1)]

### Treinamento do sistema para 5 clusters
kmeans = KMeans(n_clusters=5)
model = kmeans.fit(data)

### Geração do modelo
joblib.dump(model, 'Models/model.joblib')