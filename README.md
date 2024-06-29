# Lead Scoring Case Study

This repository demonstrates building a machine learning model for lead scoring, which helps prioritize leads likely to convert into customers.

## Overview

The case study includes:
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Engineering
- Model Selection
- Training and Evaluation

## Contents

- **lead_scoring_ml_model.ipynb**: The complete pipeline with explanations, code, and visualizations.

## Running the Notebook

To run the notebook on Google Colab:
1. Open [Google Colab](https://colab.research.google.com/).
2. Click on **File** -> **Open notebook**.
3. Select the **GitHub** tab.
4. Paste the URL: `https://github.com/kailash105/lead-scoring-case-study`.
5. Choose `lead_scoring_ml_model.ipynb` and follow the instructions.

## Data

The dataset includes attributes of leads and their conversion status, available in `Leads.csv`.

## Machine Learning Models Used

We explore the following models for lead scoring:
- Logistic Regression
- Random Forest
- Gradient Boosting Machines (GBM)
- Support Vector Machines (SVM)
- Neural Networks
- Gradient Boosting Decision Trees (XGBoost, LightGBM, CatBoost)
- K-Nearest Neighbors (KNN)

## Results

### Test Data
- Accuracy: 92.78%
- Sensitivity: 91.98%
- Specificity: 93.26%

### Train Data
- Accuracy: 92.29%
- Sensitivity: 91.70%
- Specificity: 92.66%

## Dependencies

The notebook runs in Google Colab, which includes most dependencies. However, if you are running it locally or if additional packages are needed, you can install them using the following commands:

```bash
pip install pandas
pip install numpy
pip install scikit-learn
pip install matplotlib
pip install seaborn
pip install xgboost
```

## Contributions

Contributions are welcome! Open an issue or create a pull request for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the contributors and the open-source community.

## Contact

For inquiries or collaborations, contact:
- **GitHub Username**: [kailash105](https://github.com/kailash105)
- **Email**: [kailashkbc2@gmail.com](mailto:kailashkbc2@gmail.com)

Feel free to reach out if you have any questions or need further assistance. Happy analyzing!
