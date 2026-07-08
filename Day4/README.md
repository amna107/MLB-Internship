# Day 4: Python for Data Science — NumPy & Pandas

## Video Demonstration:
[Video Recording](https://drive.google.com/file/d/1cmYkSOm9Mu8x3ISTx32GcL-ws-3p37Kp/view?usp=sharing)

## Overview
This repository contains my implementation for Day 4 of the MLB Internship. The focus of this module was mastering **NumPy** and **Pandas**, the foundational libraries for numerical computing and data manipulation in Python. I applied these concepts to perform Exploratory Data Analysis (EDA) on a dataset, focusing on vectorization, data filtering, and extracting actionable insights.

## What I Learned About NumPy
Working with NumPy shifted my approach from writing traditional Python `for` loops to using **vectorization**. Key takeaways include:
* **Memory Architecture:** NumPy is incredibly fast because it uses fixed data types (e.g., `int32`, `int16`) and stores data in **contiguous memory blocks**. This allows the CPU to utilize SIMD (Single Instruction, Multiple Data) processing and drastically improves cache efficiency compared to standard Python lists.
* **Array Initialization & Stacking:** Initializing data efficiently using `np.zeros()`, `np.full()`, and `np.random.randint()`. I also learned how to restructure data structurally using `np.vstack()` (vertical) and `np.hstack()` (horizontal).
* **Advanced Indexing:** Utilizing **Boolean Masking** (e.g., `arr[arr > 50]`) to filter arrays without loops. This core concept is the exact mechanism that powers Pandas data filtering.
* **Linear Algebra:** Moving beyond element-wise math (`a * b`) to true matrix multiplication using `np.matmul()`. 

## What I Learned About Pandas
Pandas extends NumPy's capabilities to tabular data. Key learnings include:
* **Modern Pandas (PyArrow):** Understanding the shift in modern Pandas (v2.0+) to the PyArrow backend, which provides massive performance optimizations for string operations compared to the older NumPy object backend.
* **Advanced Data Retrieval:** 
  * Mastering `.loc` for label-based indexing and `.iloc` for strict integer-position indexing.
  * Utilizing `df.query('Condition')` for a cleaner, highly readable alternative to heavy bracket syntax.
* **Data Manipulation & Aggregation:** 
  * Creating conditional columns seamlessly using `np.where()`.
  * Converting text to datetime objects using `pd.to_datetime()` to easily extract birth years or months.
  * Reshaping and summarizing data using `.groupby()`, `.pivot()`, and `pd.merge(how='left')` to join multiple datasets on a common ID.

## Key Insights from the Dataset
* **Dataset Overview:** Explored the [Insert Dataset Name] dataset, checking for structural integrity `.isna()`, `.isna.sum()`,and verifying data types using `.info()`.
* **Statistical Baselines:** Using `.describe()` revealed the median and standard deviation of the scoring columns, which helped establish a clear threshold for identifying underperformers.
* **Targeted Filtering:** Successfully isolated specific subsets of the data—specifically isolating the ID and Name records of entries that fell below the target performance metric.

## Challenges Faced During Implementation
1. **DataFrame Indexing Errors:** When trying to print only the row IDs and Names for the "low scorers," I initially passed an array of indices directly to the DataFrame (e.g., `df[low_scorers_index]`). This triggered an error because standard bracket notation on a DataFrame is designed for selecting columns or applying boolean masks, not for mapping a list of row labels to specific columns.
2. **The `.loc` Solution:** Building on the concept of NumPy boolean masking, I learned that to simultaneously filter specific rows by their index and select specific columns, the `.loc` accessor is required. Refactoring the code to `df.loc[low_scorers_index, ['ID', 'Name']]` successfully extracted the exact subset of data.
3. **Copy vs. View Confusion:** Encountered the "SettingWithCopyWarning" and learned the critical difference between a memory *view* (a slice of an array) and an independent *copy*. Using `.copy()` ensures the original dataset remains unmodified when manipulating subsets.

## Resources & References
* [FreeCodeCamp: NumPy Tutorial](https://www.youtube.com/watch?v=QUT1VHiLmmI) — Solidified my understanding of contiguous memory structures and linear algebra applications.
* [Keith Galli: Complete Python Pandas Tutorial](https://www.youtube.com/watch?v=2uvysYbKdjM) — Expanded my toolkit with `df.query()`, datetime conversions, and the modern PyArrow backend.