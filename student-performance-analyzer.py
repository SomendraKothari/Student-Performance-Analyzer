import pandas as pd
import matplotlib.pyplot as plt
# Store CSV as data_frame
data_frame = pd.read_csv("E:/coding/DATASETS/Student Performance/marksheet.csv")
# Store total marks of all students from data_frame
total_marks=data_frame.loc[:,['Science','English','Maths','History']].apply(sum,axis=1)
# Check for index having maximum marks i.e., topper's marks and store its id and name
topper = data_frame.loc[total_marks.idxmax(),['id','Name']]
print(f"Topper : {topper.id}    {topper.Name}")
# Calculate the class average
cls_avg = total_marks.sum()/len(data_frame)
print(f"Class Average : {cls_avg}")
# For students who have failed in one or more subjects
fail = data_frame.loc[(data_frame.Science<33) | (data_frame.English<33) | (data_frame.Maths<33) | (data_frame.History<33),['id']]
# Check for students having total marks more than 300 i.e., having a percentage >=75%
morethan75 = data_frame.loc[total_marks>=300,['id','Name']].reset_index(drop=True)
print(f"Students with more than 75 Percentage :\n {morethan75}")
# Create a Series having Percentage of all students i.e., Results
rs = total_marks.map(lambda x:str(round(x/4,2))+'%')
# Failing students results
rs[fail.index] = 'Fail'
# Add it in data_frame
data_frame['Result'] = rs
# Create a new DataFrame for results and upload it into a csv
results = data_frame.loc[:,['id','Name','Result']]
# For plotting graph
top25 = results.iloc[:25,2]
top25=pd.to_numeric(top25.str.replace("%","",regex=False),errors='coerce')
# graph = top25.plot(kind='bar')
# plt.xlabel('Id')
# plt.ylabel('Percentage')
# plt.title('First 25 Student Performance')
# plt.xticks(rotation=360)
# plt.show()
# results.to_csv("RESULTS",index=False)