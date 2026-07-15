# Student-Performance-dataset
*Description*
The Student Performance Analysis project focuses on exploring and analyzing student academic performance using Python and its data science libraries. The project uses the Student Performance Dataset, which contains information about students' demographic details, study habits, family background, and academic scores. The dataset is first loaded using the Pandas library, followed by data exploration to understand its structure, dimensions, and data types. Missing values are identified and checked to ensure data quality, while duplicate records are removed to improve accuracy.

After cleaning the data, several analyses are performed. The average final grade (G3) is calculated to measure overall academic performance. The project also counts the number of students who scored more than 15 marks, providing insight into high-performing students. To understand the relationship between study habits and academic success, the correlation between study time and final grades is computed. Additionally, the average performance of male and female students is compared using group-based analysis.

The results are presented through various visualizations, including a histogram showing the distribution of final grades, a scatter plot illustrating the relationship between study time and grades, and a bar chart comparing gender-wise average performance. This project demonstrates essential data analysis, cleaning, statistical evaluation, and visualization techniques using Pandas, NumPy, Matplotlib, and Seaborn, helping beginners gain practical experience in Python-based data science.

*OUTPUT*
   school sex  age address famsize Pstatus Medu Fedu     Mjob      Fjob reason guardian  traveltime  studytime  failures schoolsup famsup paid activities nursery higher internet romantic famrel freetime goout Dalc Walc health absences G1 G2 G3
0      GP   F   18       U     GT3       A    4    4  at_home   teacher  course   mother           2          2         0       yes     no   no         no     yes    yes       no       no      4        3     4    1    1      3        6  5  6  6
1      GP   F   17       U     GT3       T    1    1  at_home     other  course   father           1          2         0        no    yes   no         no      no    yes      yes       no      5        3     3    1    1      3        4  5  5  6
2      GP   F   15       U     LE3       T    1    1  at_home     other   other   mother           1          2         3       yes     no  yes         no     yes    yes      yes       no      4        3     2    2    3      3       10  7  8 10
3      GP   F   15       U     GT3       T    4    2   health  services    home   mother           1          3         0        no    yes  yes        yes     yes    yes      yes      yes      3        2     2    1    1      5        2 15 14 15
4      GP   F   16       U     GT3       T    3    3    other     other    home   father           1          2         0        no    yes  yes         no     yes    yes       no       no      4        3     2    1    2      5        4  6 10 10

(395, 33)

Index(['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu',
       'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime',
       'studytime', 'failures', 'schoolsup', 'famsup', 'paid',
       'activities', 'nursery', 'higher', 'internet', 'romantic',
       'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health',
       'absences', 'G1', 'G2', 'G3'],
      dtype='object')

school        object
sex           object
age            int64
address       object
famsize       object
Pstatus       object
Medu           int64
Fedu           int64
Mjob          object
Fjob          object
reason        object
guardian      object
traveltime     int64
studytime      int64
failures       int64
schoolsup     object
famsup        object
paid          object
activities    object
nursery       object
higher        object
internet      object
romantic      object
famrel         int64
freetime       int64
goout          int64
Dalc           int64
Walc           int64
health         int64
absences       int64
G1             int64
G2             int64
G3             int64
dtype: object

school        0
sex           0
age           0
address       0
famsize       0
Pstatus       0
Medu          0
Fedu          0
Mjob          0
Fjob          0
reason        0
guardian      0
traveltime    0
studytime     0
failures      0
schoolsup     0
famsup        0
paid          0
activities    0
nursery       0
higher        0
internet      0
romantic      0
famrel        0
freetime      0
goout         0
Dalc          0
Walc          0
health        0
absences      0
G1            0
G2            0
G3            0
dtype: int64

(395, 33)

Average Final Grade (G3): 10.42

Students Scoring Above 15: 40

Correlation Between Study Time and G3: 0.10

sex
F    10.24
M    10.91
Name: G3, dtype: float64

Average Final Grade: 10.42
Students Scoring Above 15: 40
Study Time Correlation: 0.10

sex
F    10.24
M    10.91
Name: G3, dtype: float64

Students who study more tend to score better.
