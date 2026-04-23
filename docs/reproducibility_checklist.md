# 🔁 Reproducibility Checklist

---

## 📥 Input Files Required

* Raw dataset file(s) (e.g., CSV format) located in the `data/` folder
* Any additional configuration or parameter files (if applicable)

---

## ⚙️ Scripts to be Executed

* `scripts/data_cleaning.py` → Handles missing values and preprocessing
* `scripts/visualization.py` → Generates plots and visual outputs

---

## 🔄 Execution Order

1. Load raw dataset from `data/`
2. Run data cleaning script

   ```bash
   python scripts/data_cleaning.py
   ```
3. Run visualization script

   ```bash
   python scripts/visualization.py
   ```

---

## 📊 Expected Output Files

* Cleaned dataset saved in `data/processed/`
* Visualization files (graphs/plots) saved in `visuals/`
* Optional logs or intermediate files

---

## 🧩 Software Dependencies

* Python (version 3.x)
* Required libraries (listed in `requirements.txt`), such as:

  * pandas
  * matplotlib
  * numpy (if used)

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🧠 Assumptions

* Dataset is correctly formatted and accessible
* Missing values are present and handled using mean/median strategies
* Scripts are executed in the correct order
* Required libraries are installed

---

## ⚠️ Limitations

* Results depend on data quality and size
* Imputation techniques may introduce bias
* No advanced validation or testing included
* Visualizations are static and may not capture all patterns

---

## ✅ Notes

Following the above steps should allow any user to reproduce the results and outputs of this project successfully.
