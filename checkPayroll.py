import pandas as pd
import numpy as np



class Person:
    def __init__(self, name, values):
        self.name = name
        self.values = [] 
    

    def myfunc(self):
        print("totals for " + self.name)
    def setValues(self):
        number = np.sum(self.values)
        return number  * 1
    def sumValues(self):
        print(np.sum(self.values))


        
        

p1 = Person("Lucy",0)
p2 = Person("Jack",0)
p3 = Person("Thadeus",0)

data = pd.read_csv('./QB2.csv')
df = pd.DataFrame(data, columns = ['Date', 'Description', 'Amount'])
################Grab and print person 1
Lucy = df[df['Description'].str.contains('cy')].Amount
p1.values=Lucy
p1.myfunc()
p1.sumValues()
##########Grab and print person 2
Jack = df[df['Description'].str.contains('J',regex=True)].Amount
p2.values = Jack 
p2.myfunc()
##print(df[df['Description'].str.contains('J',regex=True)])
p2.sumValues()
###############Grab and print person 3
Thadeus = df[df['Description'].str.contains('Thad')].Amount
p3.values = Thadeus
p3.myfunc()
##print( df[df['Description'].str.contains('Thad')])
p3.sumValues()

print(p1.setValues()+ p2.setValues()+p3.setValues())