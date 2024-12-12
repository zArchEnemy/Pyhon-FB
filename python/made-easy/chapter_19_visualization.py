"""Module on visualization."""

# +
import folium
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %matplotlib inline
# -

# # Visualization in Python

# +
PATH_0 = "/home/tatiana/Documents/github/Data-Science-For-Beginners/"
PATH_1 = "Datasets/air_quality_no2.csv"
PATH = PATH_0 + PATH_1

air_quality = pd.read_csv(
    PATH,
    index_col=0,
    parse_dates=True,
)
# -

air_quality.head()

# # %matplotlib— это волшебная команда, которая указывает Jupyter Notebook отображать
# графики и изображения в самом документе.

# ![image.png](attachment:image.png)

# Метод plot () создает Графики ИЗ DataFrame (рис. 19.1), а также ИЗ объектов
# Графики также сами по себе являются объектами1.

air_quality.plot()
fig = plt.gcf()
fig.savefig("plot1.png", dpi=300)

# Сейчас мы никак не настраивали оси, метки или какие-либо цвета. В результате
# получился простейший график, который дает нам представление об уровнях NO2 по
# каждому городу по датам (рис. 19.2).
# С помощью DataFrame по умолчанию создается линейный график для каждого
# столбца с числовыми данными

# в Pandas нетрудно выделить столбец как объект Series.
# Давайте сделаем это, и, как я уже сказал, у Series и DataFrame есть метод plot о.
# Итак, давайте посмотрим, как график строится для одного столбца

air_quality["station_london"].plot()
fig = plt.gcf()
fig.savefig("plot2.png", dpi=300)

# # Базовая диаграмма рассеяния

# Давайте построим
# диаграмму рассеяния по Лондону и Парижу

air_quality.plot.scatter(x="station_london", y="station_paris")
fig = plt.gcf()
fig.savefig("plot3.png", dpi=300)

# Точки диаграммы рассеяния можно сде­
# лать более прозрачными, и таким образом будет легко определить, какие области
# диаграммы более густо заполнены.Значение прозрачности alpha может варьироваться от 0 до 1.

air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
fig = plt.gcf()
fig.savefig("plot4.png", dpi=300)

# "alpha" varies between 0 to 1. Change the values of "alpha" in the above code and see how the chart differs for different values.

dir(air_quality.plot)

# Давайте удалим из созданного функцией dir () списка все элементы, которые начи­
# наются с символа подчеркивания _. В результате мы получим список всех методов,
# с помощью которых можно строить графики. Для этого я использую списковое
# включение.

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# **Диаграмма размаха**

air_quality.plot.box()
fig = plt.gcf()
fig.savefig("plot5.png", dpi=300)

# **Несколько графиков**

# Давайте разделим линей­
# ные графики, которые мы видели выше , на несколько — по одному
# столбцу на каждый график

# Если вам не нужен служебный текст, который выводится над графиками, самый простой способ убрать его— присвоить график
# другому объекту.

air_quality.plot(figsize=(12, 4), subplots=True)
fig = plt.gcf()
fig.savefig("plot6.png", dpi=300)

subplots = air_quality.plot(figsize=(12, 4), subplots=True)
fig = plt.gcf()
fig.savefig("plot7.png", dpi=300)

# Create an empty matplotlib Figure and Axes
fig, axs = plt.subplots(figsize=(12, 4))
# put the area plot on the prepared Figure/Axes
air_quality.plot.area(ax=axs)
# Do any matplotlib customization you like
axs.set_ylabel("NO$_2$ concentration")
# Save the Figure/Axes
fig.savefig("no2_concentrations.pdf")
fig = plt.gcf()
fig.savefig("plot8.png", dpi=300)

# В примере загружен набор данных tips — внутренний набор данных
# Seaborn.

sns.set()
tips = sns.load_dataset("tips")
sns.relplot(
    x="total_bill",
    y="tip",
    col="time",
    hue="smoker",
    style="smoker",
    size="size",
    data=tips,
)
fig = plt.gcf()
fig.savefig("plot9.png", dpi=300)

# Библиотека Folium упрощает визуализацию данных Python на интерактивной карте.
# Она позволяет привязать данные к карте и выполнять визуализацию хороплетных
# карт. Хороплетная карта (картограмма) — это тип тематической карты, на кото­
# рой области затенены или раскрашены пропорционально статистической перемен­
# ной, которая представляет собой совокупную сводку географических характери­
# стик в каждой области, например плотность населения или доход на душу населе­
# ния. Кроме того, можно добавлять векторные/растровые/НТМЕ-изображения в качестве маркеров на карте.

map_ = folium.Map(location=[45.5236, -122.6750])
fig = plt.gcf()
fig.savefig("plot9.png", dpi=300)

map_

# Gleam
# Библиотека Gleam позволяет создавать интерактивные веб-визуализации данных
# с помощью Python, при этом знание HTML или JavaScript не требуется!

# # **Matplotlib**

# Matplotlib отображает графики с помощью объектов Figure (например, в окнах,
# виджетах Jupyter и т. д.), каждый из которых может содержать один или несколько
# объектов Axes (т. е. линии с координатами х и у, а также это может быть угол-радиус
# в полярном графике или х, у и z в трехмерном графике). Самый простой способ соз­
# дать график с осями (рис. 20.3)— использовать метод pypiot.subplots(). Затем мы
# можем вызвать метод Axes.plot () для отображения данных по осям.

# создает два объекта и назначает их переменным fig
fig, ax = plt.subplots()
# добавление данных на оси
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

# для каждого метода построения гра­
# фика Axes существует соответствующая функция в модуле matplotlib.pyplot, которая
# строит график на «текущих» осях, создавая сами оси по умолчанию

# **Иерархия объектов Matplotlib**

# ![image.png](attachment:image.png)
