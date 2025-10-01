# Lung Cancer Detection using Advanced Ensemble Models

### 1. Project Objective
The goal of this project is to develop a high-accuracy predictive model for the early detection of lung cancer. This project implements a sophisticated machine learning pipeline, leveraging advanced gradient boosting libraries (CatBoost, XGBoost) and a meta-learning algorithm (Voting Classifier) to achieve maximum diagnostic accuracy from patient data.

### 2. Dataset
The project utilizes a medical dataset containing patient attributes and lifestyle factors. The target variable, `LUNG_CANCER`, indicates a binary outcome of "YES" or "NO". A key challenge in the dataset was a significant class imbalance, which was addressed to ensure the model's reliability.

### 3. Methodology

#### a. Data Preprocessing and Feature Engineering
* **Data Cleaning:** The dataset was loaded, and categorical features like 'GENDER' were encoded into a numerical format.
* **Exploratory Data Analysis (EDA):** EDA revealed a significant class imbalance, which can heavily bias a model's performance.
* **Handling Class Imbalance with SMOTE:** To create a balanced and fair training environment for the models, the **Synthetic Minority Over-sampling Technique (SMOTE)** was applied to the training set. This synthesizes new data for the minority class, preventing the models from simply favoring the majority class.
* **Train-Test Split:** The data was split into training and testing sets *before* applying SMOTE to ensure a valid and unbiased evaluation.

#### b. Model Implementation and Evaluation
Three powerful ensemble models were trained on the balanced dataset and evaluated on the unseen test set.

1.  **CatBoost Classifier:** A state-of-the-art gradient boosting algorithm known for its exceptional performance and native handling of categorical features.
2.  **XGBoost Classifier (Extreme Gradient Boosting):** A highly optimized and popular gradient boosting framework, renowned for its speed and accuracy in data science competitions.
3.  **Voting Classifier:** A meta-classifier that combines the predictions from both CatBoost and XGBoost. It makes a final prediction based on a majority vote, leveraging the strengths of both models to create a more robust and stable final output.

### 4. Results and Conclusion

The advanced ensemble models delivered exceptional performance, showcasing their suitability for critical medical diagnostic tasks. The Voting Classifier, by combining the predictions of the two specialized models, achieved the highest accuracy.

| Model | Accuracy Score (Example) |
| :--- | :--- |
| **Voting Classifier** | **~77.85%** |
| **CatBoost Classifier** | ~76.53% |
| **XGBoost Classifier** | ~77.06% |

This project successfully demonstrates that by addressing data challenges like class imbalance and applying powerful, specialized algorithms like CatBoost and XGBoost, it is possible to build highly reliable models for lung cancer detection. The Voting Classifier further refines these predictions, providing a robust tool for supporting clinical decision-making.

### 5. How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Malaya-Kumar-Pradhan/Machine-Learning-Projects.git](https://github.com/Malaya-Kumar-Pradhan/Machine-Learning-Projects.git)
    cd Machine-Learning-Projects/Lung-Cancer-Detection
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Jupyter Notebook:**
    ```bash
    jupyter notebook "Lung_Cancer_Detection.ipynb"
    ```
