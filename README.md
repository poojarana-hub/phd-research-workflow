# 📊 Project Title

**Data Cleaning and Visualization Workflow for Research Analysis**

---

## 📁 Project Structure

```
project-root/
│── data/                  # Raw and processed datasets  
│── notebooks/             # Analysis / experimentation files  
│── scripts/               # Data cleaning and processing scripts  
│── visuals/               # Generated plots and charts  
│── README.md              # Project documentation  
│── .gitignore             # Ignored files  
```

---

## 📂 Files and Folders Used

* **data/** → Contains dataset used for analysis
* **scripts/** → Includes preprocessing logic (handling missing values, transformations)
* **visuals/** → Stores output graphs and plots
* **README.md** → Documentation of the workflow
* **.gitignore** → Excludes IDE files like `.idea/`

---

## ▶️ How to Run the Project

1. Clone the repository

   ```bash
   git clone https://github.com/poojarana-hub/phd-research-workflow.git
   ```

2. Navigate to the project folder

   ```bash
   cd phd-research-workflow
   ```

3. Run preprocessing scripts

   ```bash
   python scripts/data_cleaning.py
   ```

4. Generate visualizations

   ```bash
   python scripts/visualization.py
   ```

---

## 📈 Expected Outputs

* Cleaned dataset with handled missing values
* Visualizations such as:

  * Distribution plots
  * Comparative charts (mean vs median strategies)
* Insights into data preprocessing choices

---

## 🧠 Assumptions Made in Data Cleaning and Visualization

* Missing values handled using:

  * **Mean imputation** for normally distributed data
  * **Median imputation** for skewed data
* Duplicate entries removed
* Outliers handled based on domain understanding
* Visualization chosen to clearly represent distribution and trends

---

## 🔮 Future Scope

* Apply advanced imputation techniques (KNN, ML-based imputation)
* Integrate machine learning models for prediction
* Automate the pipeline using workflows
* Expand dataset for better generalization
* Use advanced visualization tools (interactive dashboards)

---

## 👩‍💻 Author

**Pooja Rana**
M.Sc. Computer Science | UGC NET Qualified
Interested in Machine Learning, Research, and Data Analysis

---

## ⭐ Notes

This project demonstrates:

* Practical use of data preprocessing techniques
* Handling real-world conflicts in version control
* Structured workflow for research-oriented projects
