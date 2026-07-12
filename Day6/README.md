# Linear Regression Model: End-to-End Implementation & Engineering Journal

Engineering journal covering data preprocessing, train-test isolation, visualization, and model evaluation for an OLS Linear Regression pipeline.


## Video Demonstration:
[Link](https://drive.google.com/file/d/1nfaDDo_isdJj8lVTzxRdhzpiGxe-qgTm/view?usp=sharing)

---
## 1. Data Preprocessing & Pipeline Architecture

### DataFrame Optimization & Index Chaining
- **Column naming:** Set column names at creation (`pd.DataFrame(prediction, columns=['ypredicted'])`) or rename after the fact (`df.rename(columns={0: 'ypredicted'})` / `df.columns = [...]`).
- **Index resets:** Splitting/filtering data fractures the index. Chain `.reset_index(drop=True)` to avoid mismatched rows and stray index columns when combining data:
  ```python
  df = pd.DataFrame(prediction, columns=['ypredicted']).reset_index(drop=True)
  ```

### Categorical Encoding & The Dummy Variable Trap
- **The trap:** One-hot encoding a binary category (e.g. Male/Female) into two columns creates perfect multicollinearity — `Is_Female = 1 - Is_Male`, so one column is fully predictable from the other.
- **Why it breaks the model:** Redundant columns prevent the model from computing independent weights, causing unstable, inflated coefficients.
- **Fix:** `drop='first'` removes the baseline column. A `0` across remaining columns implicitly signals the baseline — no information lost, collinearity resolved.

### Data Output Formatting (`sparse_output=False`)
- Default `OneHotEncoder` output is a **sparse matrix** (only stores non-zero positions, saves RAM) — but it's not human-readable or directly usable in a DataFrame.
- `sparse_output=False` returns a standard **dense NumPy array** (explicit 0s/1s), ready for Pandas.

---

## 2. Train-Test Splitting & Data Isolation

### Rule: Never Scale Before Splitting
Scaling the full dataset before `train_test_split()` causes **data leakage**:
- Scalers (`StandardScaler`, `MinMaxScaler`) compute global mean/std/min/max.
- Scaling before the split bakes test-set information into the training set's scaling metrics.
- Result: artificially inflated evaluation scores that collapse in real-world deployment.

### Correct Order
1. **Split** into `X_train` / `X_test`.
2. `scaler.fit(X_train)` — learn mean/std from training data only.
3. `scaler.transform(X_train)` — apply to training data.
4. `scaler.transform(X_test)` — apply the *same* training-derived rules. Never `.fit()` on test data.

### The Scaling Variance Myth
```python
X_train_scaled.mean()  # ≈ 0
X_train_scaled.std()   # ≈ 1
```
`X_test_scaled` will **not** be perfectly 0/1 (e.g. mean `0.02`, std `1.04`) since it's scaled using training rules on unseen data — this is expected and confirms proper isolation, not an error.

---

## 3. Programmatic Data Visualization Mechanics

- **Jagged-line bug:** Numeric columns stored as text/categorical break continuous plotting — Seaborn/Matplotlib treat points as discrete categories and connect them by index order instead of value, producing a zigzag instead of a smooth line.
- **Trend lines:** Matplotlib only draws; it doesn't compute statistics. Use NumPy for a least-squares fit:
  ```python
  slope, intercept = np.polyfit(x, y, 1)   # y = mx + c
  trendline = slope * x + intercept
  ```
- **Legends:** Map `label='...'` strings to markers/lines so charts are self-explanatory.
- **Alpha transparency:** `alpha` (0.0–1.0) controls point opacity; overlapping transparent points stack into darker regions, revealing density.
- **Axis padding:** Add manual offsets to avoid clipping markers at the chart edge:
  ```python
  plt.xlim(min_val - 2, max_val + 2)
  plt.ylim(min_val - 2, max_val + 2)
  ```

---

## 4. Structural Model Components & Evaluation Metrics

### Linear Regression Parameters

| Parameter | Meaning | Value |
|---|---|---|
| `intercept_` | Baseline prediction when all features = 0 | `79.11` |
| `coef_` | Weight per feature | `[-0.55, 9.3, -2.83, 1.91]` |

**Feature weights:**

| Feature | Coefficient | Interpretation |
|---|---|---|
| Age | `-0.55` | Average_Score drops ~0.55 points per additional year of age |
| Attendance | `9.3` | Average_Score rises ~9.3 points per unit increase in (scaled) attendance |
| Program_DS | `-2.83` | Being in DS lowers predicted score by ~2.83 points vs. baseline (AI) |
| Program_SE | `1.91` | Being in SE raises predicted score by ~1.91 points vs. baseline (AI) |

### Evaluation Metrics

| Metric | Value | Meaning |
|---|---|---|
| MAE | `3.49` | Average absolute prediction error, in Average_Score units |
| MSE | `17.90` | Average squared error — penalizes large mistakes more |
| RMSE | `4.23` | MSE rescaled back to Average_Score units (~4.23 points off, on average) |
| R² | `0.74` | Model explains 74% of variance in Average_Score |