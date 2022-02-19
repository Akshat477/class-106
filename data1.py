
import plotly.express as px
import csv
import numpy as np 


def get_data(datapath) : 
    icecream_sales = []
    temperature = []
    with open(datapath)as data : 
        df  = csv.DictReader(data)
        for row in df :
            icecream_sales.append(float(row["Ice-cream Sales"]))
            temperature.append(float(row["Temperature"]))
        return{"x": icecream_sales,"y":temperature}    
        #fig = px.scatter(df,x = "Temperature",y = "Ice-cream Sales")
        #fig.show()
def find_correlation(dataSource) :
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between temperature and ice-cream :",correlation[0,1]) 
def setup() :
    datapath = "data 1.csv"
    dataSource = get_data(datapath) 
    find_correlation(dataSource)
setup()     
     