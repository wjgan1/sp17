#Importing Modules
from pandas import DataFrame, Series
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = df.read_csv("../datasets/titanic/train.csv")
df #pandas Dataframe object
df.shape #dimensions
df.head() #first 5 rows
df.dtypes #types for each column
df.describe() #data frame containing stats about df
df.describe(include=['O']) #??
df.columns #pandas Index of each column name
df['Survived'] #pandas Series for that column
df['Survived'].mean()
df.groupby('Sex') #pandas GroupBy Dataframe object
df.groupby('Sex')['Survived'] #pandas GroupBy Series object
df.groupby('Sex')['Survived'].mean()
df.groupby('Sex')['Survived'].size()
#creates new column with bins created by pandas.cut
df['fare_bins'] = pd.cut(df['Fare'],bins=[0,20,50,80,1000])
df.groupby('fare_bins')['Survived'].mean()
#Even with two group by dimensions, object is still GroupByDataFrame/GroupBySeries/Series
df.groupby(['Sex','fare_bins'])['Survived'].mean()
#Aggregating several statistics together, forming a DataFrame object
df.groupby(['Sex','fare_bins'])['Survived'].agg([np.mean,np.size,np.std])
df['Age'].hist(bins=20)
plt.xlabel('Age')
plt.ylabel('Counts')
plt.title('Distribution of Age')
df.groupby('Sex')['Age'].hist(bins=20,alpha=0.5)
plt.title('Distribution of Age by Sex')
plt.legend(labels=['Female','Male'])
plt.show()
