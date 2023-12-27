import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.model_selection as ms
import tkinter as tk
import matplotlib.pyplot as plt 
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
root= tk.Tk()
root.title("ML")
root.geometry("500x600")

def importdata():
    global data
    filename=filedialog.askopenfilename(initialdir="/Users/parthamradkar/Library/Mobile Documents/com~apple~CloudDocs/Code/CodeMedia/DataSets",filetypes=((("All Files", "*.*"),("Text Files", "*.txt*"))))
    print("FileName: ",filename)
    data=pd.read_csv(filename)
    messagebox.showinfo(title="Success!",message="Data Successfully Imported!")
    print(data)

importbtn=tk.Button(root,text="Import Data", command=importdata)
importbtn.place(x=0,y=0)    

def datacon():
    global array
    array=data.values
    
    messagebox.showinfo(title="Success!",message="Data Successfully Converted!")
    

dataconbtn=tk.Button(root,text="Data Conversion",command=datacon)
dataconbtn.place(x=0,y=50)

def dataprep():
    global data
    for j in range(420):
        data.loc[j,"date"] = j+1
    #print(data)
    data=data[["date","deathConfirmed","deathIncrease","deathProbable","hospitalized","hospitalizedCumulative","hospitalizedCurrently","hospitalizedIncrease","inIcuCumulative","inIcuCurrently","negative","negativeIncrease","negativeTestsAntibody","negativeTestsPeopleAntibody","negativeTestsViral","onVentilatorCumulative","onVentilatorCurrently","positive","positiveCasesViral","positiveIncrease","positiveScore","positiveTestsAntibody","positiveTestsAntigen","positiveTestsPeopleAntibody","positiveTestsPeopleAntigen","positiveTestsViral","recovered","totalTestEncountersViral","totalTestEncountersViralIncrease","totalTestResults","totalTestResultsIncrease","totalTestsAntibody","totalTestsAntigen","totalTestsPeopleAntibody","totalTestsPeopleAntigen","totalTestsPeopleViral","totalTestsPeopleViralIncrease","totalTestsViral","totalTestsViralIncrease","death"]]
    print(data)
    array=data.values
    col=0
    col=dataprepinput.get()
    a=int(col)
    global X
    global y
    X=array[:,0:a]
    y=array[:,a]
    y=y.astype(float)
    y=np.nan_to_num(y)
    X=X.astype(float)
    X=np.nan_to_num(X)
    print(X)
    print(y)
    messagebox.showinfo(title="Success!",message="Data Successfully Prepared!")



datapreplabel=tk.Label(root,text="Enter Number Of Independent Columns")
datapreplabel.place(x=0,y=100)
dataprepinput=tk.Entry(root)
dataprepinput.place(x=250,y=100)
dataprepbtn=tk.Button(root,text="Prepare Data", command=dataprep)
dataprepbtn.place(x=0,y=125)

def datasplit():
    global X_train
    global X_test
    global y_train
    global y_test
    X_train,X_test,y_train,y_test=ms.train_test_split(X,y,train_size=0.80,test_size=0.20,random_state=1)
    print(X_train)
    print(X_test)
    print(y_train)
    print(y_test)

dataprepbtn=tk.Button(root,text="Split", command=dataprep)
dataprepbtn.place(x=0,y=150)

def datatrain():
    

    model=[]
    from sklearn.svm import SVC
    model.append(SVC(gamma="auto"))

    from sklearn.linear_model import LogisticRegression
    model.append(LogisticRegression(solver="liblinear",multi_class="ovr"))

    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    model.append(LinearDiscriminantAnalysis())

    from sklearn.neighbors import KNeighborsClassifier
    model.append(KNeighborsClassifier())

    from sklearn.tree import DecisionTreeClassifier
    model.append(DecisionTreeClassifier())

    from sklearn.naive_bayes import GaussianNB
    model.append(GaussianNB())

    from sklearn.tree import DecisionTreeRegressor
    model.append(DecisionTreeRegressor(random_state=42))

    
    list_result=[]
    for i in model:
        global X_train 

        result=ms.cross_val_score(i,X_train,y_train,cv=10,scoring="accuracy")
        print(result)
        avg=(sum(result)/len(result))
        
        
        list_result.append(avg)
   
    import matplotlib.pyplot as plt
    plt.bar(["SVC","LR","LD","KN","DT","GB","DTR"],list_result,data=list_result)
    plt.show()
    best_model=max(list_result)
    print(best_model)
    d1={model[k]:list_result[k]for k in range(len(model))}
    print(d1)
    for val in d1.items():
        (model,acc)=val
        if acc==max(d1.values()):
            print((f"-------------------------------------------Premier Model:  {model}").format())
            break


    from sklearn.tree import DecisionTreeClassifier
    model5=DecisionTreeClassifier()
    result5=ms.cross_val_score(model5,X_train,y_train,cv=10,scoring="accuracy")
    print(result5)
    print(sum(result5)/len(result5))

datatrainbtn=tk.Button(root, text="Train",command=datatrain)
datatrainbtn.place(x=0,y=175)
root.mainloop()
