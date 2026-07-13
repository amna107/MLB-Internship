# Iris Flower Classification — Day 7

## Video Demonstration:
[Link](https://drive.google.com/file/d/1lm0oXh9FA3Go8diP1xpNkCCvtH_Ks3H_/view?usp=sharing)

## What is Classification?

Classification is a supervised machine learning task where the goal is to predict a **discrete category/label** for a given input, rather than a continuous number. The model learns patterns from labeled training data and uses them to assign new, unseen samples to one of a fixed set of classes.

In this project, the model predicts which of **3 Iris species** (Setosa, Versicolor, Virginica) a flower belongs to, based on 4 measured features: sepal length, sepal width, petal length, and petal width.

## Difference between Regression and Classification

| | Regression | Classification |
|---|---|---|
| Output | Continuous number (e.g., price) | Discrete label/category |
| Example | Predicting house price | Predicting flower species |
| Evaluation | MAE, MSE, RMSE, R² | Accuracy, Precision, Recall, F1, Confusion Matrix |
| Algorithm used | Linear Regression | Logistic Regression, Decision Tree |

Note: despite the name, **Logistic Regression is a classification algorithm** — it uses the sigmoid function to convert a linear score into a class probability.

## Evaluation Metrics Used

- **Accuracy** = (TP + TN) / (TP + TN + FP + FN) — overall % of correct predictions. Can be misleading on imbalanced datasets (a model that always predicts the majority class can score high accuracy while being useless).
- **Precision** = TP / (TP + FP) — of everything predicted as a class, how much was actually correct. Low precision = many false alarms.
- **Recall** = TP / (TP + FN) — of everything actually belonging to a class, how much was correctly caught. Low recall = many missed cases.
- **F1-Score** = 2 × (Precision × Recall) / (Precision + Recall) — harmonic mean of Precision and Recall; used when both false positives and false negatives matter and a single balanced score is needed.
- **Confusion Matrix** — an N×N grid (rows = actual class, columns = predicted class) showing exactly which classes get confused with which. Diagonal cells = correct predictions; off-diagonal cells = misclassifications between specific classes.

Since this is a **multiclass** problem (3 species, not 2), TP/FP/TN/FN were computed per class using a one-vs-rest approach, then combined using **`average='macro'`** — a simple average across all 3 classes, treating each class equally regardless of how many samples it has. This was chosen because the Iris dataset is balanced (50 samples per class), making macro averaging a fair, representative summary.

## Model Used

**Logistic Regression** — a classification algorithm despite its name. It computes a weighted linear combination of the input features, then passes that score through the **sigmoid function** to squash it into a probability between 0 and 1:

```
z = w1×feature1 + w2×feature2 + ... + b
sigmoid(z) = 1 / (1 + e^(-z))
```

For multiclass problems like Iris, sklearn extends this internally (one-vs-rest or softmax) to output a probability for each of the 3 species, and predicts the class with the highest probability.

**Decision Tree** (bonus) — splits the data into branches using if-else conditions on feature values (e.g., "petal length ≤ 2.45?"), forming a tree where each leaf represents a predicted class. Splits are chosen to reduce **impurity** (measured via Gini or entropy) at each step. Unlike Logistic Regression, its decisions are fully interpretable — the exact reasoning path can be read directly from the tree diagram.

## Model Performance & Observations

| Metric | Logistic Regression | Decision Tree |
|---|---|---|
| Train Accuracy | 0.975 | 0.958 |
| Test Accuracy | 1.0 | 1.0 |
| Precision (macro) | 1.0 | 1.0 |
| Recall (macro) | 1.0 | 1.0 |
| F1 (macro) | 1.0 | 1.0 |

- Both models scored perfectly on the test set; Logistic Regression scored slightly higher on training data (0.975 vs 0.958).
- Test ≥ train accuracy for both, indicating neither model overfits.
- The Decision Tree splits first on petal length (isolating Setosa), then petal width (separating Versicolor/Virginica) — consistent with these being the two features most correlated with species (0.95 and 0.96 respectively, per the dataset's summary statistics).
- The tree's one impure node (4 Versicolor vs 4 Virginica) shows where its hard threshold splits struggle with overlapping classes; Logistic Regression's smoother decision boundary handles this slightly better, reflected in its higher train accuracy.
- Decision Tree is more interpretable — its exact rules are readable directly from the diagram. Logistic Regression's boundary is smoother but not directly explainable.
- With only 30 test samples, identical 1.0 scores reflect strong performance on this specific split, not proof of perfect real-world generalization.

**Conclusion:** Both models perform strongly on Iris. Decision Tree offers clearer interpretability; Logistic Regression fit the training data marginally better and may generalize more smoothly on noisier, real-world data.

## Key Takeaways

- Petal length and petal width are the most predictive features (correlation ≈ 0.95 and 0.96 with species), while sepal width is the weakest (correlation ≈ -0.42) — this was confirmed both by the dataset's summary statistics and by which features the Decision Tree chose to split on first.
- Test accuracy meeting or exceeding train accuracy for both models indicates neither is overfitting on this dataset.
- Perfect scores (1.0) should be interpreted with caution given the small test set size (30 samples) — they reflect strong performance on this split rather than guaranteed real-world generalization.