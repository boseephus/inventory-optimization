# Project: Inventory & Job Costing Optimization Dashboard

## Objective
This project demonstrates how to transform raw, disconnected operational data into an actionable financial dashboard for a fictional construction supply company. The goal is to identify costly overstock, improve forecasting, and provide insights into job-specific material costs, directly addressing key challenges for businesses undergoing modernization.

## The Business Problem
Many established companies have valuable data spread across different systems (e.g., sales logs, inventory lists). This project solves the problem of connecting these sources to answer critical business questions:
- How much cash is tied up in inventory?
- Which items are not selling and creating a drag on our finances?
- What is the true material cost for a specific job?

## Methodology
The project uses a hybrid approach, leveraging Python for its powerful data processing capabilities and Excel for its accessible and interactive dashboarding features.

1.  **Data Ingestion:** Two raw CSV files (`inventory_data.csv`, `sales_data.csv`) represent the company's disparate data.
2.  **Automated Processing (`process_inventory.py`):** A Python script using the Pandas library automates the following:
    - Cleans and standardizes the raw data.
    - Merges inventory and sales data.
    - Calculates key metrics like total inventory value and sales velocity.
    - Enriches the data by flagging items as "Overstock Risk."
3.  **Data Output:** The clean, analyzed data is exported into a structured Excel file (`Inventory_Dashboard_Data.xlsx`).
4.  **Dashboarding:** The final Excel file contains an interactive dashboard with KPIs, charts, and slicers, allowing a manager to explore the data without needing any technical skills.

## Business Impact
This automated workflow provides:
- **Clarity:** Instantly identifies overstock, allowing the company to reduce carrying costs and free up cash.
- **Efficiency:** Replaces hours of manual data entry and analysis with a script that runs in seconds.
- **Insight:** Provides the foundation for accurate job costing and better purchasing decisions.

