
## 📊 Advanced Analysis Questions

This section answers deeper questions based on the supermarket sales dataset.

---

### 1. 🧾 What is the average bill? (How much does a customer spend per transaction?)

```python
print(df['Sales'].mean())
```

> ✅ This shows the average amount spent in a single transaction.

---

### 2. 🌟 Do customer ratings differ between branches?

```python
print(df.groupby('Branch')['Rating'].mean())
```

> ✅ This compares the average customer satisfaction by branch.

---

### 3. 📦 What is the best-selling product category?

```python
print(df.groupby('Product line')['Sales'].sum().idxmax())
```

> ✅ This finds the product line with the highest total sales.

---

### 4. 📅 Which day of the week has the highest sales?

```python
df['Day'] = df['Date'].dt.day_name()
print(df.groupby('Day')['Sales'].sum().sort_values(ascending=False))
```

> ✅ This shows total sales by weekday, ranked from highest to lowest.

---

### 5. 🧍‍♂️ Do members spend more than normal customers?

```python
print(df.groupby('Customer type')['Sales'].mean())
```

> ✅ This compares average sales between member and normal customers.

---

### 6. 💳 What is the most commonly used payment method?

```python
print(df['Payment'].value_counts())
```

> ✅ This shows the frequency of each payment method used.

---

### 7. 🏢 Which branch performs best in terms of sales?

```python
print(df.groupby('Branch')['Sales'].sum().sort_values(ascending=False))
```

> ✅ This ranks the branches by total sales.

---
