import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student-mat.csv", sep=';')

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)

print(df.isnull().sum())

df = df.drop_duplicates()

print(df.shape)

average_grade = df["G3"].mean()
print("Average Final Grade (G3):", round(average_grade, 2))

above15 = df[df["G3"] > 15]
print("Students Scoring Above 15:", len(above15))

correlation = df["studytime"].corr(df["G3"])
print("Correlation Between Study Time and G3:", round(correlation, 2))

gender_avg = df.groupby("sex")["G3"].mean()
print(gender_avg)

plt.figure(figsize=(7,5))
plt.hist(df["G3"], bins=10, edgecolor="black")
plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.show()

plt.figure(figsize=(7,5))
plt.scatter(df["studytime"], df["G3"])
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade (G3)")
plt.show()

plt.figure(figsize=(5,5))
gender_avg.plot(kind="bar")
plt.title("Average Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average G3")
plt.show()

print("Average Final Grade:", round(average_grade, 2))
print("Students Scoring Above 15:", len(above15))
print("Study Time Correlation:", round(correlation, 2))
print(gender_avg)

if correlation > 0:
    print("Students who study more tend to score better.")
elif correlation < 0:
    print("Study time has a negative correlation with marks.")
else:
    print("No correlation between study time and marks.")