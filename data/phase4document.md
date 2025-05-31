# ✅ Sales Data Analysis – Documentation of the 10 Solved Questions (Phase 4)

## 1. How do you calculate the average total sales?
```python
print(df['Sales'].mean())
```
> ✅ Correct – because the `Sales` column represents the total invoice (including tax).

---

## 2. How do you calculate the total sales for a specific branch?
```python
print(df[df['Branch'] == 'A']['Sales'].sum())
```
> ✅ Correct – by filtering based on branch and summing the sales.

---

## 3. How do you calculate total sales by payment method?
```python
print(df.groupby('Payment')['Sales'].sum())
```
> ✅ Correct – it groups sales by each payment method (cash, credit card, etc.).

---

## 4. How do you find the highest sales value in the dataset?
```python
print(df['Sales'].max())
```
> ✅ Correct – it returns the highest recorded sales value.

---

## 5. How do you count the number of transactions per branch?
```python
print(df['Branch'].value_counts())
```
> ✅ Correct – gives the number of transactions (rows) for each branch.

---

## 6. How do you calculate the average per product line?
```python
print(df.groupby('Product line')['Sales'].mean())
```
> ✅ Correct – gives the average sales per product line.

---

## 7. How do you calculate the total tax paid?
```python
print(df['Tax 5%'].sum())
```
> ✅ Correct – sums up all values in the tax column.

---

## 8. How do you find the highest customer rating recorded?
```python
print(df['Rating'].max())
```
> ✅ Correct – returns the highest rating from customers.

---

## 9. How do you compare sales between new and returning customers?
```python
print(df.groupby('Customer Type')['Sales'].sum())
```
> ✅ Correct – shows total sales for each customer type.

---

## 10. How do you calculate total sales per month?
```python
df['Date'] = pd.to_datetime(df['Date'])
print(df.groupby(df['Date'].dt.month)['Sales'].sum())
```
> ✅ Correct – groups and sums sales by month after converting the `Date` column.
