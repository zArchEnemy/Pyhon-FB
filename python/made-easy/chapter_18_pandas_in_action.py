"""Module on pandas."""

import pandas as pd

# Pandas (panel data (панельные данные))— это библиотека с открытым исходным кодом, построенная на основе библиотеки NumPy. Pandas позволя­
# ет упростить импорт данных. В ней есть функции для поиска, очистки, преобразо­
# вания, визуализации и анализа данных. Pandas работает быстро, что обеспечивает
# высокую производительность конечного приложения.
# Pandas является надстройкой над библиотекой NumPy, т. е. в Pandas используется
# или повторяется большая часть NumPy. Данные в Pandas часто используются для
# статистического анализа в SciPy, построения графиков функций в Matplotlib и
# алгоритмов машинного обучения в Scikit-learn'.

# +
# conda install pandas
# pip install pandas
# # !pip install pandas
# -

# В Pandas есть новый тип данных.Этот тип называется
# DataFrame (датафрейм).  DataFrame состоит из Series (серий). Каждый столбец в DataFrame представляет собой объект Series.

# ![image.png](attachment:image.png)

data = {"apples": [4, 5, 6], "bananas": [4, 2, 1]}
df = pd.DataFrame(data)
df

# Обратите внимание на индексы от О
# до 4 слева от первого столбца. Индексы автоматически создаются в Pandas, если мы
# не передаем значения для них сами. Индекс можно изменить в любой момент.

pur = pd.DataFrame(data, index=["Peter", "Nick", "Ron"])
pur

# два варианта обратиться к столбцу
print(df["apples"])  # print(df.apples)

# # + oranges
df["oranges"] = pd.Series([8, 10, 7])
df

# # + total
df["total"] = df.apples + df.bananas + df["oranges"]
df

# del столбец
del df["oranges"]
df

# изменить value  в столбце
df["total"] = df.apples + df.bananas
df

# ## строки

df_2 = pd.DataFrame(data, index=["Peter", "Nick", "Ron"])
df_2

# loc for locate
df_2.loc["Peter"]

# iloc for locate by index
df_2.iloc[0]

# slice of rows
df_2[1:3]

# # Operations with DataFrame

# * .max()- макс показание по столбцу
# * .describe()- стат методы
# * .info()# краткий обзор данных DataFrame.
# * .head()
# * .tails()
# * .dtypes # attribute not a method
# * .shape # размер фрэйма
# * df.ilос[8:19, 4:7] # выбор нескольих строк и столбцов
# * df.rename(columns={'present column namer':'new name'})
# * df = df.rename(columns = str.upper)
# * df['col_name'].mean() -  среднееи значение по колонке
# * df[['col_name_1', 'col_name_2']].median() - медиана
# * df.agg({'col_1':['max', 'min'], 'col_2':['skew','mean']})
# * df.groupby('col_name').count() # подсчет к-ва категорий в колонке
# * df[['col_1', 'col_2']].groupby('col_1').count() # Обращаеися к 2 столбцам датафрема. Группируемся по 1 столбцу и подсчитываем к-во едениц 'col_2'
# * df[["col_1", "col_2"]].groupby("cyl").mean()
#

# ![image.png](attachment:image.png)

# Поскольку нас интересует средний пробег для каждого типа двигателя, выбранного
# по количеству цилиндров, сначала мы делаем выборку из трех столбцов: mpg[["cty",
# "hwy", "cyl"]]. Затем к столбцу cyl применяется метод groupbyO, чтобы сгруппиро­
# вать значения по категориям. Наконец, вычисляется и возвращается средний пробег
# для каждой категории.

# Если нас интересует только средний пробег для каждого цилиндра, то для сгруппи­
# рованных данных также поддерживается выбор столбцов (квадратные скобки [ ],
# как обычно)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # Работа с файлами

# * df = pd.read_csv('mpg.csv', index_col=0) # Чтение из файла
# * df.to_excel('df.xlsx', sheet_name='cars', index='False')
# * df.to_* # во все форматы

# # Фильтрация

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # Сортировка строк

# Мы можем отсортировать данные в порядке возрастания или убывания любого
# столбца или даже нескольких столбцов.

# отсортируем данные по объему
# двигателя в возрастающем порядке.

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # Объединение данных из нескольких таблиц

# объединить данные из двух
# pd.concat ().

# * df = pd.concat([df_1, df_2, df_3], axis=0) - конкатенация по строкам. К-во столбцов одинаково! Строки + в конец

# ![image.png](attachment:image.png)

# **Объединение с использованием общего идентификатора**

# +
path_0 = "/home/tatiana/Documents/github/"
path_1 = "Data-Science-For-Beginners/Datasets/titanic.csv"
path = path_0 + path_1
titanic = pd.read_csv(
    path,
    index_col=0,
)

titanic.head()
# -

titanic["Fare_Pound"] = titanic["Fare"] * 0.80
titanic.head()

col = {"Ticket": "Ticket Number", "Fare": "Fare_Dollar"}
titanic_1 = titanic.rename(columns=col)
titanic_1.head()

titanic_1 = titanic_1.rename(columns=str.upper)
titanic_1.head()

titanic[["Name", "Sex"]].groupby("Sex").count()

titanic[["Sex", "Age"]].groupby("Sex").mean()

titanic.groupby("Sex")["Age"].mean()

titanic.groupby(["Sex", "Pclass"])["Fare"].mean()

titanic.sort_values(by="Age").head()

titanic.sort_values(by=["Pclass", "Age"], ascending=False).head()

# +
titanic_male = titanic[titanic["Sex"] == "male"]

titanic_female = titanic[titanic["Sex"] == "female"]
# -

titanic_male.head()

titanic_female.head(3)

# +
print(titanic_female.shape)

print(titanic_male.shape)
# -

titanic_all = pd.concat([titanic_female, titanic_male], axis=0)
titanic_all

# +
dataset1 = titanic[["Name", "Sex", "Age"]]

dataset1
# -

dataset2 = titanic[["Name", "Pclass", "Cabin"]]
dataset2

# Теперь у нас есть два DataFrame, в каждом из которых есть по 891 строке и по столб­
# цу с общим идентификатором Name. При выполнении объединения Pandas будет ис­
# кать общий идентификатор в обоих DataFrame и соответствующим образом соеди­
# нять строки. Для ЭТОЙ операции МЫ используем функцию pd.merge ().

# +
merged_dataset = pd.merge(dataset1, dataset2, how="left", on="Name")

merged_dataset
# -

# Вы видите, что набор merged dataset тоже содержит 891 строку, но уже 5 столбцов
# (34-3 — 1, общий столбец).
# У обеих таблиц общий столбец Name, который используется в качестве ключа для
# объединения информации. При выборе левого соединения в результирующую таб­
# лицу попадают только имена, доступные в таблице dataseti (слева). В конце кон­
# цов, в обоих наборах данных будут присутствовать одни и те же имена, но эта
# функция будет полезна, если вы будете выполнять соединение некоторых реальных
# данных и вам нужно будет решить, какая таблица будет первой с точки зрения
# выбора общего идентификатора
