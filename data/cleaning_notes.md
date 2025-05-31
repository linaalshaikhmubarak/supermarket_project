# Data Cleaning Notes

## ✅ Missing Values
- Checked using `df.isnull().sum()`
- ✅ No missing values found in any column.

## ✅ Duplicate Rows
- Checked using `df.duplicated().sum()`
- ✅ No duplicate rows found.

## ✅ Date Conversion
- Converted the `Date` column from object to datetime using:
  ```python
  df['Date'] = pd.to_datetime(df['Date'])

## 🏷️ Column Name Changes
Renamed the following columns for clarity and coding convenience:

- `Invoice ID` → `InvoiceID`
- `Customer type` → `CustomerType`
- `Product line` → `ProductLine`
- `Unit price` → `UnitPrice`
- `Tax 5%` → `Tax`
- `gross margin percentage` → `GrossMarginPct`
- `gross income` → `GrossIncome`
