import pandas as pd
class SalesAnalyzer:
    def __init__(self,path):
        self.path=path
        self.df=pd.read_csv(self.path)
    def show_data(self):
        return self.df.head(5)
    def info_data(self):
        return f"shape: {self.df.shape} \n\ncolumns: {self.df.columns} \n\ndata-type: {self.df.dtypes}"
    def missing_value(self):
        return self.df.isnull().sum()
    def sales_city(self,city):
        self.sales=self.df[self.df["City"]==city]
        return self.sales
    def electronic_sales(self):
        return self.df[self.df["Category"]=="Electronics"]
    def high_value_orders(self,amount):
        return self.df[(self.df["Quantity"]*self.df["Price"])>amount]
    def revenue_city(self):
        self.df["Revenue"]=self.df["Quantity"]*self.df["Price"]
        return self.df.groupby("City")["Revenue"].sum()
    def merge(self,path):
        self.path=path
        self.df2=pd.read_csv(self.path)
        return self.df.merge(self.df2,on="Customer",how="inner")
    
obj=SalesAnalyzer("data.csv")
