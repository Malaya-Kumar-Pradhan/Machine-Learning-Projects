### Mobile Phone Price Range Prediction
### 1. Project Objective
The objective of this project is to build a classification model that can accurately predict the price range of a mobile phone based on its technical specifications. This involves a comparative study of three different machine learning algorithms to determine the most effective model for this task. The price range is categorized into four classes: 0 (low cost), 1 (medium cost), 2 (high cost), and 3 (very high cost).

### 2. Dataset
The project uses a dataset containing technical specifications for 2000 mobile phones. Key features include:

ram: RAM in Megabytes

battery_power: Total energy a battery can store in mAh

px_width, px_height: Pixel resolution width and height

int_memory: Internal Memory in Gigabytes

...and other features like blue (Bluetooth), dual_sim, four_g, wifi, etc.

The target variable is price_range, which is the focus of the prediction.

### 3. Methodology
a. Exploratory Data Analysis (EDA)
Data Inspection: The dataset was loaded and inspected for null values and data types using df.info() and df.describe(). No missing values were found.

Correlation Analysis: A heatmap was generated to visualize the correlation between different features. A strong positive correlation was observed between price_range and ram, indicating that RAM is a major factor in determining a phone's price.

Feature Distribution: Bar plots were used to visualize the relationship between individual features (like RAM and Battery Power) and the price_range, further confirming the importance of these key specifications.

b. Data Preprocessing
Feature-Target Split: The dataset was divided into the feature matrix (X) and the target vector (y), which is the price_range column.

Train-Test Split: The data was split into a training set (75%) and a testing set (25%) using Scikit-learn's train_test_split to ensure the model's performance could be evaluated on unseen data.

c. Model Implementation and Evaluation
Three different classification models were trained on the training data. Their performance was evaluated based on their accuracy score on the test set.

Logistic Regression: A linear model used as a solid baseline for classification.

Decision Tree Classifier: A non-linear model that makes predictions based on a tree-like structure.

Random Forest Classifier: An ensemble of multiple decision trees, which typically yields higher accuracy and better generalization.

### 4. Results and Conclusion
The Random Forest Classifier significantly outperformed the other models, demonstrating its strength in handling complex, non-linear relationships within the data.

| Model                        | Accuracy Score |
| :--------------------------- | :------------- |
| **Logistic Regression** | **97.60%** |
| **Random Forest Classifier** | 90.00%         |
| **Decision Tree Classifier** | 87.00%         |

The project successfully demonstrates that a mobile phone's price range can be accurately predicted from its specifications. The analysis confirms that RAM is the most critical factor influencing price, a finding that aligns with consumer and market intuition. The Random Forest model provides a reliable tool for this classification task.

### 5. How to Run This Project
Clone the repository:

|git clone [https://github.com/Malaya-Kumar-Pradhan/Machine-Learning-Projects.git](https://github.com/Malaya-Kumar-Pradhan/Machine-Learning-Projects.git)|
|----|
|cd Machine-Learning-Projects/Mobile-Price-Prediction|

Install dependencies:

|pip install pandas numpy seaborn matplotlib scikit-learn|
|---|

Run the Jupyter Notebook:

|jupyter notebook "MobilePhone_Pricing_Prediction.ipynb"|
|---|
