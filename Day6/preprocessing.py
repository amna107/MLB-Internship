import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


def preprocess_data(data_path):

    df = pd.read_csv(data_path)

    # dont contribute in predicting score
    new_df = df.drop(columns=['SID', 'Name', 'Python', 'Mathematics', 'Statistics', 'ML', 'Performance'])
    # new_df.columns

    ohe = OneHotEncoder(sparse_output=False, drop='first')

    onehot_arr = ohe.fit_transform(new_df[['Program']])

    # print(onehot_arr)
    # print(ohe.get_feature_names_out())
    # print(ohe.categories_)

    encoded_df = pd.DataFrame(onehot_arr, columns=ohe.get_feature_names_out(["Program"]), index=new_df.index)

    new_df = pd.concat([new_df, encoded_df], axis=1)

    new_df = new_df.drop(columns=["Program"])
    # new_df.columns

    X = new_df[['Age', 'Attendance', 'Program_DS', 'Program_SE']]
    y = new_df['Average_Score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # print(X_train.shape, X_test.shape)

    numeric_features = ['Age', 'Attendance']
    categorical_features = ['Program_DS', 'Program_SE']

    preprocessor = ColumnTransformer(transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', 'passthrough', categorical_features)  # they are left as it is 0/1 encoded already
    ])

    X_train_scaled = preprocessor.fit_transform(X_train)
    X_test_scaled = preprocessor.transform(X_test)

    # print(X_train_scaled[:5])
    # print(X_test_scaled[:5])

    # print(X_train_scaled.mean())
    # print(X_test_scaled.mean())

    return X_train_scaled, X_test_scaled, y_train, y_test, preprocessor


if __name__ == "__main__":
    current_dir = Path(__file__).parent
    data_path = current_dir.parent / "Day5" / "cleaned_student_performance.csv"
    X_train, X_test, y_train, y_test, preprocessor = preprocess_data(data_path)
    print(X_train.shape, X_test.shape)