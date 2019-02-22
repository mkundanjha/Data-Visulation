# Thsi program gives a bar chart of students and ther taste of food
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("taste.csv")

#importing Taste column into a list
info=data.iloc[:,-1].tolist()

#comparable list 
taste=["sweet","sour","salty","bitter","tasty","spicy"]
count=0

#New list to record the count
l=[]

# Lowers-case the elements of list info
info=[element.lower() for element in info]

for i in range(len(taste)):
    for j in range(len(info)):
        if(taste[i]==info[j]):
            count=count+1
            
    if(count>0):
        l.append(count)
        count=0
    else:
        l.append(0)

print("The graph is loading ....")

taste=[element.upper() for element in taste]

# Plotting the bar chart
index=np.arange(len(taste))
plt.bar(index,l)
plt.xlabel("Taste",fontsize=12)
plt.ylabel("Number of Students",fontsize=12)
plt.xticks(index,taste,fontsize=12)
plt.title("Student food taste response")
plt.show()


