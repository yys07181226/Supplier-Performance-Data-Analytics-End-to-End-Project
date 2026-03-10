:link: [Live Dashboard (Power BI)]([https://app.powerbi.com/view?r=UE_18UkvfA?ctid=54c31b7a-3fa1-44f5-afef-a69a6c51529a&pbi_source=linkShare]
## 📌 Overview

This project provides a complete analysis of supplier performance, inventory status, and profitability across 12,261 different brands and 131 suppliers. Using a strong data pipeline and careful statistical checks, it finds important market opportunities, shows ways to save costs through bulk buying, and gives practical suggestions to improve supply chain operations.

---

## ❓ Business Problem

Effective inventory and sales management are critical for optimizing profitability in the retail and wholesale industry. Companies must ensure they are not incurring losses due to inefficient pricing, poor inventory turnover, or vendor dependency.

The goals of this analysis are to:

* 🔎 Identify underperforming brands that require promotional or pricing adjustments.
* 🏆 Determine top vendors contributing to sales and gross profit.
* 📦 Analyze the impact of bulk purchasing on unit costs.
* 📊 Assess inventory turnover to reduce holding costs and improve efficiency.
* 💡 Investigate profitability variance between high-performing and low-performing vendors.

---

## 🔄 Workflow

1. **Define Business Problem**

   * Identify objectives and key vendor performance questions.
   * Understand business needs and expected outcomes.
     
2. **Save original data to database**
   
   * Save raw data into the local Mysql database inventory.db.
   
4. **Data Exploration & Cleaning (SQL)**

   * Explore database tables.
   * Merge relevant tables.
   * Perform data cleaning & transformation.
   * Create an **aggregated table**.

5. **Save & Load Data**

   * Save aggregated data into the local Mysql database.
   * Load the aggregated table into **Jupyter Notebook**.

6. **Data Analysis with Python**

   * Perform **Exploratory Data Analysis (EDA)**.
   * Data cleaning & preprocessing.
   * Solve business/research questions.
   * Analyze & interpret results.

7. **Data Visualization & Dashboard (Power BI)**

   * Build interactive dashboards.
   * Highlight KPIs and vendor performance metrics.
   * Provide actionable insights for stakeholders.

8. **Report Writing**

   * Document findings and insights.
   * Share business recommendations.

---

## 🛠️ Tools & Technologies

* **SQL** → Data exploration, cleaning, and aggregation
* **Python (Jupyter Notebook)** → EDA, data cleaning, solving research questions
* **Power BI** → Dashboard creation, visualization

---

## 📊 Deliverables

* ✅ Cleaned & aggregated dataset
* ✅ Jupyter Notebook with analysis & insights
* ✅ Interactive Power BI dashboard
* ✅ Final project report

---

## 🚀 Use Cases

* Evaluate vendor efficiency & reliability
* Identify top and low-performing vendors
* Support procurement & vendor management decisions
* Improve supply chain strategies

---

## Files

The following original data CSV files are required to run the analysis:

- `begin_inventory.csv` - Beginning inventory data
- `end_inventory.csv` - Ending inventory data
- `purchase_prices.csv` - Purchase price information
- `purchases.csv` - Purchase transaction data (~345 MB)
- `sales.csv` - Sales transaction data (~1.5 GB)
- `vendor_invoice.csv` - Vendor invoice information

## Note

These data files are not included in the Git repository due to their large size (total ~2 GB). They are excluded via `.gitignore` to keep the repository lightweight and follow best practices for version control.

---
