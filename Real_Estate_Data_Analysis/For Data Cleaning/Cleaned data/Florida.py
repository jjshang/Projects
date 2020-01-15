import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("/Users/jennyshang/Documents/Masters/Masters/Fall 2019/DSO545/Project/For Data Cleaning/Cleaned data/Florida_all_data.csv")
data = data.dropna(subset = ["Price_per_sqft"])
data.shape
data.head(2)

data.Num_studio.mean()
data.Num_1_bed.mean()
data.Num_2_bed.mean()
data.Num_3_bed.mean()
data.Num_4_bed.mean()

data_unit_mix = data[["County","Num_units","Num_studio","Studio_avg_sqft","Studio_vacancy_%",\
                        "Num_1_bed","1_bed_avg_sqft","1_bed_vacancy_%",\
                        "Num_2_bed","2_bed_avg_sqft","2_bed_vacancy_%",\
                        "Num_3_bed","3_bed_avg_sqft","3_bed_vacancy_%",\
                        "Num_4_bed","4_bed_avg_sqft","4_bed_vacancy_%",\
                        "Price_per_sqft","Sale_price"]]

data_unit_mix.describe()

data_unit_mix.groupby("County").mean().sort_values("Price_per_sqft",ascending = False).reset_index()

plt.figure()

plt.bar("County",)

plt.show()


## Remove outliers
data_unit_mix = data_unit_mix.dropna(subset = ["Sale_price"])
data_unit_mix.shape
data_remove_outlier = data_unit_mix[data_unit_mix.Price_per_sqft < 2500]
data_remove_outlier.shape

## EDA on number of rooms for each room type in histograms
### Studio
#### Histogram
plt.figure()
plt.hist(data_unit_mix.Num_studio, bins = 20)
plt.show()

#### Scatter plt
plt.figure()
plt.scatter(data_remove_outlier.Num_studio, data_remove_outlier.Sale_price )
plt.title("Number of Studio to Sale Price")
plt.show()

#### Subplots
fig = plt.figure(figsize = (10,5))

grid = plt.GridSpec(4,3,wspace = 0.5, hspace = 1)

ax_main = fig.add_subplot(grid[0:3,0:-1]) ## use -1 in case you decide to change spec to avoid changing these codes
ax_bottom = fig.add_subplot(grid[3,0:2])

## Plot main graph (scatter plot)
ax_main.scatter('Num_studio', 'Price_per_sqft', data = data_remove_outlier)

## Plot the right boxplot
sns.boxplot(data_remove_outlier.Num_studio, ax = ax_bottom) ## orient='v': orientation is vertical
ax_bottom.set(xticks = [], yticks = [], xlabel = "") ## more than one subplot, have to set axis details in brackets

## Set title, x-label, y-label for main graph
ax_main.set(title = "Scatterplot with Boxplots \nNumber of Studio Rooms vs. Price per SQFT",
           xlabel = "Num_studio",
           ylabel = "Price_per_sqft")

plt.show()


### 1-Bedroom
#### Histogram

plt.figure()
plt.hist(data_unit_mix.Num_1_bed, bins = 20)
plt.show()

#### Scatter plots
plt.figure()
plt.scatter(data_remove_outlier.Num_1_bed, data_remove_outlier.Sale_price )
plt.title("Number of One Bedroom to Sale Price")
plt.show()

#### Subplots
fig = plt.figure(figsize = (10,5))

grid = plt.GridSpec(4,3,wspace = 0.5, hspace = 1)

ax_main = fig.add_subplot(grid[0:3,0:-1]) ## use -1 in case you decide to change spec to avoid changing these codes
ax_bottom = fig.add_subplot(grid[3,0:2])

## Plot main graph (scatter plot)
ax_main.scatter('Num_1_bed', 'Price_per_sqft', data = data_remove_outlier, color = "orange")

## Plot the right boxplot
sns.boxplot(data_remove_outlier.Num_1_bed, ax = ax_bottom,color = "orange" ) ## orient='v': orientation is vertical
ax_bottom.set(xticks = [], yticks = [], xlabel = "") ## more than one subplot, have to set axis details in brackets

## Set title, x-label, y-label for main graph
ax_main.set(title = "Scatterplot with Boxplots \nNumber of One Bedroom vs. Price per SQFT",
           xlabel = "Num_1_bed",
           ylabel = "Price_per_sqft")

plt.show()

### 2-Bedroom
#### Histogram
plt.figure()
plt.hist(data_unit_mix.Num_2_bed, bins = 20)
plt.show()

#### Scatter plot
plt.figure()
plt.scatter(data_remove_outlier.Num_2_bed, data_remove_outlier.Sale_price )
plt.title("Number of Two Bedrooms to Sale Price")
plt.show()

#### Subplots
fig = plt.figure(figsize = (10,5))

grid = plt.GridSpec(4,3,wspace = 0.5, hspace = 1)

ax_main = fig.add_subplot(grid[0:3,0:-1]) ## use -1 in case you decide to change spec to avoid changing these codes
ax_bottom = fig.add_subplot(grid[3,0:2])

## Plot main graph (scatter plot)
ax_main.scatter('Num_2_bed', 'Price_per_sqft', data = data_remove_outlier, color = "green")

## Plot the right boxplot
sns.boxplot(data_remove_outlier.Num_2_bed, ax = ax_bottom, color = "green") ## orient='v': orientation is vertical
ax_bottom.set(xticks = [], yticks = [], xlabel = "") ## more than one subplot, have to set axis details in brackets

## Set title, x-label, y-label for main graph
ax_main.set(title = "Scatterplot with Boxplots \nNumber of Two Bedrooms vs. Price per SQFT",
           xlabel = "Num_2_bed",
           ylabel = "Price_per_sqft")

plt.show()


### 3-Bedroom
#### Histogram
plt.figure()
plt.hist(data_unit_mix.Num_3_bed, bins = 20)
plt.show()

#### Scatter plot
plt.figure()
plt.scatter(data_remove_outlier.Num_3_bed, data_remove_outlier.Sale_price )
plt.title("Number of Three Bedroom to Sale Price")
plt.show()

fig = plt.figure(figsize = (10,5))

grid = plt.GridSpec(4,3,wspace = 0.5, hspace = 1)

ax_main = fig.add_subplot(grid[0:3,0:-1]) ## use -1 in case you decide to change spec to avoid changing these codes
ax_bottom = fig.add_subplot(grid[3,0:2])

## Plot main graph (scatter plot)
ax_main.scatter('Num_3_bed', 'Price_per_sqft', data = data_remove_outlier, color = "pink")

## Plot the right boxplot
sns.boxplot(data_remove_outlier.Num_3_bed, ax = ax_bottom, color = "pink") ## orient='v': orientation is vertical
ax_bottom.set(xticks = [], yticks = [], xlabel = "") ## more than one subplot, have to set axis details in brackets

## Set title, x-label, y-label for main graph
ax_main.set(title = "Scatterplot with Boxplots \nNumber of Three Bedrooms vs. Price per SQFT",
           xlabel = "Num_3_bed",
           ylabel = "Price_per_sqft")

plt.show()


### 4-Bedroom
#### Histogram
plt.figure()
plt.hist(data_unit_mix.Num_4_bed, bins = 20)
plt.show()

## Scatter plot
plt.figure()
plt.scatter(data_remove_outlier.Num_4_bed, data_remove_outlier.Sale_price )
plt.title("Number of Four Bedrooms to Sale Price")
plt.show()

fig = plt.figure(figsize = (10,5))

grid = plt.GridSpec(4,3,wspace = 0.5, hspace = 1)

ax_main = fig.add_subplot(grid[0:3,0:-1]) ## use -1 in case you decide to change spec to avoid changing these codes
ax_bottom = fig.add_subplot(grid[3,0:2])

## Plot main graph (scatter plot)
ax_main.scatter('Num_4_bed', 'Price_per_sqft', data = data_remove_outlier, color = "purple")

## Plot the right boxplot
sns.boxplot(data_remove_outlier.Num_4_bed, ax = ax_bottom, color = "purple") ## orient='v': orientation is vertical
ax_bottom.set(xticks = [], yticks = [], xlabel = "") ## more than one subplot, have to set axis details in brackets

## Set title, x-label, y-label for main graph
ax_main.set(title = "Scatterplot with Boxplots \nNumber of Four Bedrooms vs. Price per SQFT",
           xlabel = "Num_4_bed",
           ylabel = "Price_per_sqft")

plt.show()


## Plot relationships between number of units to price per Avg_unit_sqft
plt.figure()
plt.scatter(data_unit_mix.Num_units, data_unit_mix.Price_per_sqft)
plt.show()


plt.figure()
plt.scatter(data_remove_outlier.Num_units, data_remove_outlier.Price_per_sqft)
plt.show()


plt.figure()
plt.scatter(data_remove_outlier.Num_units, data_remove_outlier.Sale_price )
plt.title("Number of Units to Sale Price")
plt.show()


## Regression
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import datetime as dt

data_num_unit= data_remove_outlier[["Num_units","Price_per_sqft","Sale_price"]]
data_num_unit.shape


Y = data_num_unit["Sale_price"]/1000000
X = data_num_unit.drop(["Sale_price","Price_per_sqft"], axis = 1)

X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

model.summary()
