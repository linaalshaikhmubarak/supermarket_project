# Data Dictionary (Cleaned Column Names)

| Column Name    | Data Type | Description                                                             
|----------------|-----------|-------------------------------------------------------------------------|
| InvoiceID      | object    | Unique identifier for each sales transaction                            |
| Branch         | object    | Store branch where the sale occurred (A, B, or C)                       |
| City           | object    | City in which the branch is located                                     |
| CustomerType   | object    | Type of customer: Member or Normal                                      |
| Gender         | object    | Gender of the customer (Male or Female)                                 |
| ProductLine    | object    | Category of the sold product (e.g., Electronics, Food, Health & Beauty) |
| UnitPrice      | float64   | Price per unit of the product (in local currency)                       |
| Quantity       | int64     | Number of units sold in the transaction                                 |
| Tax            | float64   | 5% tax added to the sales amount                                        |
| Sales          | float64   | Total amount paid including tax                                         |
| Date           | object    | Date of the transaction (later converted to datetime format)            |
| Time           | object    | Time of the transaction (hour and minute)                               |
| Payment        | object    | Payment method used (e.g., Cash, Credit card, E-wallet)                 |
| cogs           | float64   | Cost of Goods Sold, i.e., cost before taxes and profits                 |
| GrossMarginPct | float64   | Gross margin as a percentage (typically constant)                       |
| GrossIncome    | float64   | Profit earned from the transaction                                      |
| Rating         | float64   | Customer rating of the transaction (scale from 1 to 10)                 |
