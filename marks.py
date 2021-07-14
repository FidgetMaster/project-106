import plotly.express as px
import csv
import numpy as np
def createFigure():
    file = open("marks.csv")
    reader = csv.DictReader(file)
    figure = px.scatter(reader, x = "Marks In Percentage", y = "Days Present")
    figure.show()
def getDataSource():
    Percentage = []
    DaysPresent = []
    file = open("marks.csv")
    reader = csv.DictReader(file)
    for i in reader:
        Percentage.append(float(i["Marks In Percentage"]))
        DaysPresent.append(float(i["Days Present"]))
    return {"x":Percentage, "y":DaysPresent}
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def setup():
    datasource = getDataSource()
    findCorrelation(datasource)
    createFigure()
setup()