class Univariate():
    
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if (dataset[columnName].dtype=='object'):
               # print("qual")
                qual.append(columnName)   
            else:
                #print("quan")
                quan.append(columnName)  
        return quan,qual
def freqTable(coulmName,dataset):
    freqTable=pd.DataFrame(columns=["Unique_values","Frequency","Relative_Freqency","Cumsum"])
    freqTable["Unique_values"]= dataset[coulmName].value_counts().index
    freqTable["Frequency"]= dataset[coulmName].value_counts().values
    freqTable["Relative_Freqency"]= (freqTable["Frequency"]/103)
    freqTable["Cumsum"]= freqTable["Relative_Freqency"].cumsum()
    return freqTable
def Univariate(dataset,quan):
    descriptive=pd.DataFrame(index=["MEAN","MEDIAN","MODE","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5 rule","Lesser","Greater","Min","Max","skew","kurtosis"],columns=quan)
    for columName in quan:
        descriptive[columName]["MEAN"]=dataset[columName].mean()
        descriptive[columName]["MEDIAN"]=dataset[columName].median()
        descriptive[columName]["MODE"]=dataset[columName].mode()[0]
        descriptive[columName]["Q1:25%"]=dataset.describe()[columName]["25%"]
        descriptive[columName]["Q2:50%"]=dataset.describe()[columName]["50%"]
        descriptive[columName]["Q3:75%"]=dataset.describe()[columName]["75%"]
        descriptive[columName]["99%"]=np.percentile(dataset[columName],99)
        descriptive[columName]["Q4:100%"]=dataset.describe()[columName]["max"]
        descriptive[columName]["IQR"]=descriptive[columName]["Q3:75%"]- descriptive[columName]["Q1:25%"]
        descriptive[columName]["1.5 rule"]=1.5* descriptive[columName]["IQR"]
        descriptive[columName]["Lesser"]=descriptive[columName]["Q1:25%"]- descriptive[columName]["1.5 rule"]
        descriptive[columName]["Greater"]=descriptive[columName]["Q3:75%"]+ descriptive[columName]["1.5 rule"]
        descriptive[columName]["Min"]=dataset[columName].min()
        descriptive[columName]["Max"]=dataset[columName].max()
        descriptive[columName]["skew"]=dataset[columName].skew()
        descriptive[columName]["kurtosis"]=dataset[columName].kurtosis()
    return descriptive
    
Lesser=[]
Greater=[]
def Outliear_Columname(descriptive,quan):
    for columName in quan:
        if (descriptive[columName]["Min"]<descriptive[columName]["Lesser"]):
            Lesser.append(columName)
        if (descriptive[columName]["Max"]>descriptive[columName]["Greater"]):
            Greater.append(columName)
    return Outliear_Columname  