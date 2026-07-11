# Day 5 — Student Performance: Data Cleaning & Visualization

## Overview
This project cleans and analyzes a student performance dataset covering marks in **Python, Mathematics, Statistics, and Machine Learning (ML)**. It answers a set of analysis questions (student count, subject averages, top performers, students needing improvement, and mark distribution) and visualizes the results.

**Files in this folder:**
- `Day5.mp4` — Video go through of project 
- `data_cleaning.py` — loads the raw dataset, cleans it, engineers new columns, saves the cleaned CSV
- `data_visualization.py` — general exploratory charts (per-student scores, distribution, correlation, category split, spread)
- `analysis.ipynb` — notebook answering the specific analysis questions with supporting charts
- `cleaned_student_performance.csv` — the cleaned dataset
- `Charts/` — all generated PNG visualizations
- `README.md` — this file

---

## Data Cleaning Steps Performed

1. **Checked for missing values and duplicates** using `df.isna().sum()` and `df.duplicated().sum()` — the dataset turned out to have **no missing values and no duplicate rows**, so no imputation or row-dropping was needed.
2. **Renamed columns** for consistency and brevity: `Student_ID` → `SID`, `Machine_Learning` → `ML`.
3. **Engineered a new `Average_Score` column** — calculated as the row-wise mean of the four subject columns (`Python`, `Mathematics`, `Statistics`, `ML`), with identifier/demographic columns (`SID`, `Name`, `Age`, `Program`, `Attendance`) excluded from the calculation.
4. **Engineered a `Performance` category column**, bucketing each student based on `Average_Score` into performance tiers. Implemented two ways as a comparison: a manual function applied row-by-row with `df.apply()`, and a faster vectorized version using `np.select()` — the `np.select()` version is what's kept in the final column.
5. Saved the result to `cleaned_student_performance.csv`.

> Note: since this dataset happened to be free of missing values and duplicates, the "cleaning" here was mostly about **standardizing structure and adding derived columns** rather than fixing broken data.

---

## Visualizations Created & Why

Each chart type was picked to match the kind of question being asked — comparing categories, seeing a distribution, checking a relationship, or showing parts of a whole.

| Chart | Why |
|---|---|
| **Bar chart** — avg score per student / per subject / performance counts | Best for comparing a value across separate categories — bar *length* is read more accurately than angles or scattered points. |
| **Histogram (KDE)** — distribution of Average Scores | Shows the shape of the whole class's performance (clustered, skewed, or split into groups) — something a single average can't reveal. |
| **Scatter plot** — Python vs ML marks | Only chart that shows a relationship between two numeric variables at once, to check if strong Python students also score well in ML. |
| **Pie chart** — Performance category split | Fitting since every student falls into exactly one of a few fixed categories that sum to the whole class — the one real "parts of a whole" case. |
| **Box plot** — spread across subjects | Shows consistency, median, and outliers per subject, not just the average — reveals whether a subject's average is reliable or skewed by a few scores. |
| **Side-by-side bar charts** — All students vs Top 5 | Puts the top performers in context against the full class instead of showing them in isolation. |

Bar and pie charts of the same `Performance` split were both included on purpose — the pie shows proportion, the bar shows exact counts, which is clearer when categories are close in size.

---

## Key Insights

1. **ML has the highest class average (82.6) and Python has the lowest (78.9).** The box plot also shows ML has the smallest spread of the four subjects — meaning students aren't just scoring higher on average in ML, they're also performing more consistently, while Python marks vary more widely across the class. This combination (higher average + tighter spread) makes ML the strongest-performing subject overall, not just on paper.
2. **Attendance clearly affects performance.** Average attendance by performance tier:

   | Performance | Avg. Attendance |
   |---|---|
   | Needs Improvement | 79.50 |
   | Average | 86.67 |
   | Good | 93.50 |
   | Excellent | 98.25 |

   Attendance rises steadily as performance tier improves — students in "Needs Improvement" attend nearly 19 points less on average than "Excellent" students, suggesting attendance is a genuine factor worth addressing for at-risk students, not just a side detail.

---

## Challenges Faced

- **Selecting rows by label + column together:** needed to pull a filtered list of "Needs Improvement" student names using `df.loc[df['Performance']=="Needs Improvement", 'Name']` — plain `df[...]` indexing doesn't support combining a row condition with a specific column in one step the way `.loc[]` does.
- **Labeling bars with `ax.bar_label()`:** had to learn that `sns.barplot()` returns an Axes object, but the actual bar rectangles live inside `ax.containers[0]` — passing the wrong object (or calling Axes-only methods like `.set_yticks()` directly on the bar container) caused `AttributeError`.
- **Same issue again with plain Matplotlib:** `plt.bar()` returns a `BarContainer`, not an Axes — so `.set_yticks()` failed until the Axes was retrieved separately with `plt.gca()`.
- **Boxplots have no built-in value labels:** unlike bar charts (`bar_label()`), box plots don't support automatically printing median/quartile values on the chart — this data is instead interpreted visually and described in the insights section above.

---

## How to Run

```bash
python data_cleaning.py         # produces cleaned_student_performance.csv
python data_visualization.py    # generates general exploratory charts
jupyter notebook analysis.ipynb # run the analysis + generates Charts/Project/*.png
```