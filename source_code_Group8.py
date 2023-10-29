# This code is a combination of data analysis + visualization.
# Comment and execute as you go. Especially for the visualization part.
# Please do not rename the data file in the folder.

import pandas as pd
import matplotlib.pyplot as plt

# data import
df=pd.read_csv('raw.csv')
df.columns = ['time','education','role','field','age','gender','use','usage','concerns','accuracy','plagiarism','plagiarism_actions','effect','future']

# data review
df['role'].value_counts()
df['field'].value_counts()
df['gender'].value_counts()
df['usage'].value_counts()
df['concerns'].value_counts()

# data cleaning
# Due to some mistake, we had some results that were typed in. We had to sort them manually.
df.drop(df[df.field.isin(['In High school '])].index,inplace=True)
df1=df.replace({'Attack Helicopter': 'Other'})
df1=df1.replace({'Second degree student ': 'Student'})
df1=df1.replace({'Law;STEM': 'Sciences and/or Engineering and/or Architectural Studies;Law'})
df1=df1.replace({'Information Technology': 'Sciences and/or Engineering and/or Architectural Studies'})
df1=df1.replace({'IT':'Sciences and/or Engineering and/or Architectural Studies'})
df1=df1.replace({'used it to create a book for an assignment': 'Project-related use (essays, presentations, assignments, etc)'})
df1=df1.replace({'not being able to actually learn. relying more on ChatGPT = not gaining knowledge for your future. point about plagiarism also counts.': 'Other'})
df1=df1.replace({'Don’t know what it is': 'Other'})
df1=df1.replace({'I don’t use Chatgpt': 'Other'})
df1=df1.replace({'Its sense of humor is not that good. ': 'Other'})
df1=df1.replace({'It could turn traditional education to redundancy': 'Other'})

# save a cleaner version of csv file
df1.to_csv('test.csv')
df2=pd.read_csv('test.csv')

# data analysis
# multi-selection questions
a = df["field"].str.contains('Sciences')
a.value_counts()
a = df["field"].str.contains('Liberal')
a.value_counts()
a = df["field"].str.contains('Law')
a.value_counts()
a = df["field"].str.contains('Creative')
a.value_counts()
df2["concerns"].str.contains('Contributes to plagiarism').value_counts()
df2["concerns"].str.contains('reliability').value_counts()
df2["concerns"].str.contains('data and privacy').value_counts()
df2["concerns"].str.contains('security').value_counts()
df2["concerns"].str.contains('Other').value_counts()
df2["concerns"].str.contains('sure').value_counts()
df2["plagiarism_actions"].str.contains('essays').value_counts()
df2["plagiarism_actions"].str.contains('homework').value_counts()
df2["plagiarism_actions"].str.contains('coursework').value_counts()
df2["plagiarism_actions"].str.contains('research').value_counts()
df2["plagiarism_actions"].str.contains('All').value_counts()
df2["plagiarism_actions"].str.contains('None').value_counts()
df2["field"].str.contains('Sciences').value_counts()
df2["field"].str.contains('Engineering').value_counts()

# STEM and non-STEM group
stem=df2.loc[df2["field"].str.contains('Science')]
non_stem=df2[~df2['field'].str.contains('Science')]
stem['use'].value_counts(normalize=True)
non_stem['use'].value_counts(normalize=True)

# students and non-students
student=df2.loc[df1["role"].str.contains('Student')]
nonstudent=df2.loc[~df1["role"].str.contains('Student')]
student['plagiarism'].value_counts(normalize=True)
nonstudent['plagiarism'].value_counts(normalize=True)

# data visualization
# comment and run as you go

# Fig1
colors = ['cornflowerblue', 'silver', 'lightpink','khaki','rosybrown']
# explode = (0.1, 0.1, 0.1,0.1,0.1)
df2['education'].value_counts().plot(kind='bar', color='lightpink')
plt.xticks(rotation=30)
# df2['role'].value_counts().plot(kind='pie', y='Education Level',fontsize=8,colors=colors, explode=explode)
plt.ylabel('')
plt.title('Fig.1: Distribution of Respondents by Education Level',y=-0.3)
plt.xticks(rotation=30)

# Fig2
python_bool = df["role"].str.contains('Student')
python_bool.value_counts(normalize=True)
rol = {'Student':144, 'TA':5, 'Professor':2,'Researcher':1}
rol_name=list(rol.keys())
rol_num=list(rol.values())
plt.bar(rol_name, rol_num, color ='cornflowerblue')
plt.title('Fig.2: Distribution of Respondents by Academic Role',y=-0.3)
colors = ['cornflowerblue', 'silver', 'lightpink','khaki','rosybrown']
explode = (0.1, 0.1, 0.1,0.1,0.1)
df2['role'].value_counts().plot(kind='bar', color='cornflowerblue')
df2['role'].value_counts().plot(kind='pie', y='Education Level',fontsize=8,colors=colors, explode=explode)

# Fig3
df2.loc[df2["field"].str.contains('Sciences')] #106
fie = {'STEM':106, 'Business':24, 'Liberal\nEducation':18,'Law':6,'Creative\nMedia':3,'Other':3}
fie_name=list(fie.keys())
fie_num=list(fie.values())
plt.bar(fie_name, fie_num, color ='steelblue')
plt.title('Fig.3: Distribution of Respondents by Field of Study',y=-0.3)
plt.xticks(rotation=30)

#Fig4
df2['age'].value_counts().plot(kind='bar', color='tomato')
plt.title('Fig.4: Distribution of Respondents by Age',y=-0.3)
plt.xticks(rotation=30)

#Fig5
df2['gender'].value_counts().plot(kind='bar', color='grey')
plt.title('Fig.5: Distribution of Respondents by Gender',y=-0.3)
plt.xticks(rotation=30)

#Fig6
colors = ['cornflowerblue', 'silver', 'lightpink','khaki']
explode = (0.1, 0.1, 0.1, 0.1)
df2=df2.replace({'No, never (0 hrs per week)': 'Never (0 hr/week)'})
df2=df2.replace({'Yes, rarely (<3 hrs per week)': '<3 hr/week'})
df2=df2.replace({'Yes, sometimes (3-10 hrs per week)': '3-10 hr/week'})
df2=df2.replace({'Yes, often (>10 hrs per week)': '>10 hr/week'})
df2['use'].value_counts().plot(kind='pie', fontsize=8,colors=colors, autopct='%1.1f%%',explode=explode)
plt.title('Fig.6: Frequency of ChatGPT Usage per Week',y=-0.3)
plt.ylabel('')

#Fig7
labels = 'Homework-related', 'Project-related', 'Creativity-related', 'Research-related','Career-related use','Other'
sizes = [39,19,15,9,7,3]
colors = ['cornflowerblue', 'silver', 'lightpink','yellow','rosybrown','khaki']
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels,colors=colors,explode=explode,autopct='%1.1f%%')
plt.title('Fig.7: Academic Usage of ChatGPT',y=-0.3)

#Fig8
labels = 'Plagiarism', 'Reliability', 'Data and Privacy', 'Security','Other','Not sure'
sizes = [85,95,37,31,4,6]
colors = ['cornflowerblue', 'silver', 'lightpink','yellow','rosybrown','khaki']
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels,colors=colors,autopct='%1.1f%%',explode=explode)
plt.title('Fig.8: Main Concerns of ChatGPT Usage in Academia',y=-0.3)

#Fig9
colors = ['cornflowerblue', 'silver', 'lightpink','khaki','rosybrown']
explode = (0.1, 0.1, 0.1, 0.1,0.1)
df2['accuracy'].value_counts().plot(kind='pie', fontsize=8,colors=colors,autopct='%1.1f%%', explode=explode)
plt.title('Fig.9: Perceived Accuracy of ChatGPT by Respondents',y=-0.3)
plt.ylabel('')


#Fig10
colors = ['cornflowerblue', 'silver', 'lightpink','khaki','rosybrown']
explode = (0.1, 0.1, 0.1, 0.1)
df2['plagiarism'].value_counts().plot(kind='pie', fontsize=8,colors=colors, autopct='%1.1f%%',explode=explode)
plt.title('Fig.10: Perceptions of ChatGPT Usage as Plagiarism by Respondents',y=-0.3)
plt.ylabel('')

#Fig11
labels = 'Writing Essays', 'Homework/Exam Answers', 'Provide Information for Coursework', 'Research-related\nPurposes','None of These'
sizes = [102,84,35,32,20]
colors = ['cornflowerblue', 'silver', 'lightpink','yellow','rosybrown','khaki']
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels,colors=colors,autopct='%1.1f%%',explode=explode)
plt.title('Fig.11: Activities with ChatGPT\nPerceived as Plagiarism by Respondents',y=-0.3)

#Fig12
colors = ['cornflowerblue', 'silver', 'lightpink','khaki','rosybrown']
explode = (0.1, 0.1, 0.1, 0.1)
df2['effect'].value_counts().plot(kind='pie', fontsize=8,colors=colors, autopct='%1.1f%%',explode=explode)
plt.title('Fig.12: Perceived Impact of ChatGPT on Education by Respondents',y=-0.3)
plt.ylabel('')

#Fig13
colors = ['cornflowerblue', 'silver', 'lightpink','khaki','rosybrown']
explode = (0.1, 0.1, 0.1, 0.1)
df2['future'].value_counts().plot(kind='pie', fontsize=8,colors=colors, autopct='%1.1f%%',explode=explode)
plt.title('Fig.13: Perceived Potential of ChatGPT to Replace Google',y=-0.3)
plt.ylabel('')


#Table1
plt.rcParams["figure.figsize"] = [7.00, 5]
plt.rcParams["figure.autolayout"] = True
fig, axs = plt.subplots(1, 1)
data = [[44.3, 37.0],
        [35.9, 52.2],
        [12.3, 10.9],
        [7.5, 0]]
columns = ('STEM (%)','non-STEM (%)')
rows = ['No, never (0 hrs per week)','Yes, rarely (<3 hrs per week)', 'Yes, sometimes (3-10 hrs per week)','Yes, often (>10 hrs per week)']
axs.axis('tight')
axs.axis('off')
the_table = axs.table(cellText=data,rowLabels=rows,colLabels=columns)
plt.title('Table 1. Frequency of ChatGPT usage \namong STEM and non-STEM respondents',x=0,y=-0.5)


plt.tight_layout()
plt.show()