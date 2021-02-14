import pandas as pd
import numpy as np
class Person:
    def __init__(self, name, values, total):
        self.name = name
        self.values = [] 
        self.total = np.sum(values)

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Lucy",0,0)
p2 = Person("Jack",0,0)
p3 = Person("Thadeus",0,0)

p3.myfunc()
df = pd.read_csv('./values.csv')


print(df)
