### Thyroid Cancer Detection using Ensemble Methods
### 1. Project Objective
The goal of this project is to develop and evaluate a machine learning model for the accurate detection of thyroid cancer. This notebook implements a complete workflow, including data preprocessing for categorical features, model training, and a comparative analysis of three different classification algorithms: a baseline Decision Tree and two advanced ensemble methods (Random Forest and Gradient Boosting).

### 2. Dataset
The project utilizes a thyroid disease dataset which includes patient information and medical attributes. The key task is to classify a diagnosis as cancerous or non-cancerous based on these features.

### 3. Methodology
#### a. Data Cleaning and Preprocessing
* **Initial Inspection:** The dataset was loaded and inspected for null values and data types.

* **Feature Removal:** The 'other' column was identified as irrelevant or redundant and was dropped to simplify the model.

* **Categorical Data Encoding:** A crucial step in this project was handling categorical features. LabelEncoder from Scikit-learn was used to transform all object-type columns (like 'sex', 'smoking' status, etc.) into a numerical format that the machine learning models can process.

* **Feature-Target Split:** The dataset was separated into the feature matrix (X) and the target vector (y), which is the 'Recurred' column indicating the diagnosis.

* **Data Scaling:** StandardScaler was applied to the feature matrix (X) to normalize the data, ensuring that all features contribute equally to the model's performance.

* **Train-Test Split:** The scaled data was split into a training set (80%) and a testing set (20%) to evaluate the models on unseen data.

#### b. Model Implementation and Evaluation
Three different classification models were trained on the preprocessed training data and evaluated on their accuracy score using the test set.

* **Decision Tree Classifier:** A single tree model that serves as a baseline for performance.

* **Random Forest Classifier:** An ensemble of multiple decision trees, designed to improve accuracy and control for overfitting.

* **Gradient Boosting Classifier:** A powerful sequential ensemble method where each model is built to correct the errors of the previous one.

### 4. Results and Conclusion
All three models achieved very high accuracy, but the ensemble methods showed a clear advantage. The Gradient Boosting Classifier delivered the best performance.

| Model                        | Accuracy Score |
| :--------------------------- | :------------- |
| **Gradient Boosting Classifier** | **98.68%** |
| **Random Forest Classifier** | 97.26%         |
| **Decision Tree Classifier** | 97.26%         |

The results demonstrate the effectiveness of using advanced ensemble techniques like Gradient Boosting for medical diagnostic tasks. The high accuracy achieved suggests that this approach can serve as a reliable tool to support clinicians in diagnosing thyroid cancer.

### 5. How to Run This Project
1. **Clone the repository:**
```bash
git clone [https://github.com/Malaya-Kumar-Pradhan/Machine-Learning-Projects.git](https://github.com/Malaya-Kumar-Pradhan/Machine-Learning-Projects.git)
cd Machine-Learning-Projects/Thyroid-Cancer-Detection
```
2. **Install dependencies:**
```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```
3. **Run the Jupyter Notebook:**
```bash
jupyter notebook "Thyroid_Cancer_Detection.ipynb"
```
