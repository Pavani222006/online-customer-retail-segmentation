
# Online Retail Customer Segmentation

## Project Overview
Online Retail Customer Segmentation is a Machine Learning project that groups customers based on their purchasing behaviour using RFM Analysis and K-Means Clustering.

The project uses Python to analyze customer transaction data and Streamlit to display the results in an interactive dashboard.

## Objectives
- Analyze customer purchasing behaviour.
- Calculate Recency, Frequency, and Monetary values.
- Group similar customers using K-Means Clustering.
- Visualize customer segments through charts and tables.
- Download customer segmentation results as a CSV file.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- RFM Analysis
- K-Means Clustering

## RFM Analysis
- **Recency:** Number of days since the customer's last purchase.
- **Frequency:** Number of distinct invoices associated with the customer.
- **Monetary:** Total purchase value calculated using Quantity × UnitPrice.

## Project Workflow
1. Upload the online retail CSV dataset.
2. Clean and preprocess the data.
3. Calculate RFM values for each customer.
4. Scale the RFM features using StandardScaler.
5. Apply K-Means Clustering to group customers.
6. Display customer segment summaries and charts.
7. View customer details and download the results.

## Dataset Requirements
The uploaded CSV file must contain these columns:
- CustomerID
- InvoiceDate
- Quantity
- UnitPrice

The application processes the uploaded dataset and removes invalid records.

**Note:** Do not upload private or sensitive customer information to a public repository.

## Project Structure
```text
online-retail-segmentation/
├── app.py
├── online_retail_segmentation.py
├── requirements.txt
└── README.md
```

## Installation and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/online-retail-segmentation.git
cd online-retail-segmentation
```

Replace YOUR-USERNAME with your GitHub username.

### 2. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 3. Run the Application
```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal and upload your CSV dataset.

## Dashboard Features
- Total number of customers
- Number of customer segments
- Total revenue
- Customer segment summary
- Revenue comparison chart
- Customer details table
- Downloadable segmentation results

## Machine Learning Algorithm
This project uses **K-Means Clustering**, an unsupervised Machine Learning algorithm that groups customers based on similarities in their scaled RFM values.

Cluster IDs such as 0, 1, 2, and 3 are group labels. They do not automatically indicate customer quality or value.

## Future Enhancements
- Add meaningful customer segment labels.
- Improve dashboard design and visualizations.
- Evaluate different clustering configurations.
- Use larger and representative retail datasets.

## Author
Your Name

## License
This project is available for educational and learning purposes.
