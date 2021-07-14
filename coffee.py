import plotly.express as px
import csv
import numpy as np
def createFigure():
    file = open("coffee.csv")
    reader = csv.DictReader(file)
    figure = px.scatter(reader, x = "Coffee in ml", y = "sleep in hours")
    figure.show()
def getDataSource():
    CoffeeAmount = []
    SleepAmount = []
    file = open("coffee.csv")
    reader = csv.DictReader(file)
    for i in reader:
        CoffeeAmount.append(float(i["Coffee in ml"]))
        SleepAmount.append(float(i["sleep in hours"]))
    return {"x":CoffeeAmount, "y":SleepAmount}
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def setup():
    datasource = getDataSource()
    findCorrelation(datasource)
    createFigure()
setup()