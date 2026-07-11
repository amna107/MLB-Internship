import pandas as pd 
import numpy as np
from pathlib import Path


# get Day5 folder directory
current_dir = Path.cwd()

# steps out of day5 and goes to Day4 to get the file directory
data_path = current_dir.parent/"Day4"/"student_performance.csv"

# loading the file
df = pd.read_csv(data_path)

# # Missng values

df.isna().sum()

# # Duplicates

df.duplicated().sum()

# No nulls or duplicates found


# # Renaming Columns


# renaming Student_ID to SID and Machine_Learning to ML
df = df.rename(columns={'Student_ID': 'SID', 'Machine_Learning': 'ML'})


# # Average_Score

df.columns

marks = df.drop(columns=['SID', 'Name', 'Age', 'Program','Attendance']).copy()


df['Average_Score'] = marks.mean(axis=1)


# # Performance

# Method 1 

def performance_metric(row):
    if row['Average_Score']>=90:
        return 'Excellent'
    elif row['Average_Score']>=80:
        return 'Good'
    elif row['Average_Score']>=70:
        return 'Average'
    else:
        return 'Needs Improvement'

    
df['Performance'] = df.apply(performance_metric, axis=1)


# Or Method 2 (faster)

criteria = [
    df['Average_Score'] >= 90,
    df['Average_Score'] >= 80,
    df['Average_Score'] >= 70,
]

comment = [
    'Excellent',
    'Good',
    'Average'
]

df['Performance'] = np.select(criteria, comment, default="Needs Improvement")


df.head()


df.to_csv("cleaned_student_performance.csv")


