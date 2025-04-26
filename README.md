# Healthcare Big Data Analytics Project

## 🏥 Project Description
Healthcare insurance companies face challenges in understanding customer behavior, predicting future risks, and maximizing revenues. In this project, we leverage Big Data concepts to analyze healthcare claims, patient demographics, and disease patterns to help an insurance company improve their business strategies.

We performed full data cleaning, exploratory analysis, and designed example Spark and Hive scripts to simulate a real-world Big Data ecosystem.

## 👥 Authors
* Felix Luca Krebs (2470475)
* MD Kamruzzaman Russel (2470478)
* Justus Izuchukwu Onuh (2470477)

## ⚙️ System Requirements

| Requirement | Details |
|-------------|---------|
| Operating System | Windows 10/11 or Linux (Ubuntu 18.04+) |
| Python Version | Python 3.8 or above |
| Recommended Tools | VSCode, Jupyter Notebook |
| Big Data (Optional) | Spark 3.x, Hadoop 2.7+, Hive 2.x |

⚡ Note: For the assignment, setting up Spark and Hive is optional. We provided sample scripts under `spark_jobs/` and `hive_queries/` folders.

## 🧰 Python Libraries Used
* pandas
* matplotlib
* seaborn
* jupyter
* findspark
* pyarrow
* sqlalchemy
* pyhive

## 🚀 How to Set Up and Run the Project

1. **Clone the GitHub Repository:**
```bash
git clone https://github.com/izunwaonu/healthcare-bigdata-analytics.git
cd healthcare-bigdata-analytics
```

2. **Install All Python Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run Data Cleaning Scripts:**
```bash
python src/clean/load_and_preview.py
python src/clean/clean_data.py
```

4. **Open and Explore the Jupyter Notebook:**
```bash
jupyter notebook # Then open notebooks/exploratory_analysis.ipynb
```
You will see:
* Exploratory graphs
* Analysis of claim amounts, diseases, hospitals, and age

5. **Run Spark Script (Optional for Big Data Part):**
If Spark is installed, you can run:
```bash
spark-submit spark_jobs/customer_behavior_analysis.py
```

6. **Run Hive Query (Optional for Big Data Part):**
If Hive is installed, execute:
```bash
hive -f hive_queries/claim_summary.hql
```

## 🗂️ Project Structure
```
healthcare-bigdata-analytics/
├── data/
│   ├── raw/                # Raw datasets
│   └── processed/          # Cleaned datasets
├── database/               # Database schema
├── hive_queries/           # Sample Hive scripts
│   └── claim_summary.hql
├── notebooks/
│   └── exploratory_analysis.ipynb  # Jupyter notebook for EDA
├── reports/
│   ├── MLA_report.docx     # Full project report
│   └── MLA_presentation.pptx  # Presentation slides
├── spark_jobs/
│   └── customer_behavior_analysis.py  # PySpark job
├── src/
│   └── clean/
│       ├── load_and_preview.py  # Load data
│       └── clean_data.py        # Clean and process data
├── requirements.txt        # Python dependencies
├── README.md               # Project overview (this file)
└── .gitignore
```

## 📋 Notes
* **Dataset Source**: 
* **Reference Repository**: HELTHCARE-SYSTEM by Tejas Bansal