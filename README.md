# Smart Decision Support System

A mini decision support platform that analyzes historical sales data, computes key performance indicators (KPIs), and provides a simple revenue forecast through an interactive dashboard.

This project demonstrates how raw business data can be transformed into actionable insights for management-level decision making.

---

## Features

- KPI calculation (total revenue, best-selling product, etc.)
- Region and product-based filtering
- Interactive Streamlit dashboard
- Baseline revenue forecasting using machine learning
- Clean and modular Python project structure

---

## Dataset

Dataset: Superstore Sales Dataset (Kaggle)  
Type: Open retail dataset  
Usage: Educational and portfolio purposes only  

The dataset is used to simulate real-world business analytics scenarios.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## Project Structure

smart-decision-support/
- app/
  - dashboard.py
- data/
  - train.csv
- src/
  - kpi.py
- README.md
- requirements.txt

---

## Installation

Clone the repository:

git clone https://github.com/the-duru/smart-decision-support.git

cd smart-decision-support

Create and activate environment (Anaconda recommended):

conda create -n decision python=3.10  
conda activate decision

Install dependencies:

pip install -r requirements.txt

---

## Run the Dashboard

streamlit run app/dashboard.py

Then open in your browser:

http://localhost:8501

---

## Example Use Case

This system can be used by:

- Business analysts
- Data teams
- Managers

to monitor sales performance, analyze product trends, and estimate future revenue.

---

## Author

Duru Macit  
Computer Engineering Student
