import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = []

for month in months:
    salesEntered = float(input(f"Enter total sales for {month}: $"))
    sales.append(salesEntered)

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o')
plt.title("Total Sales Through each Month")
plt.xlabel("Months")
plt.ylabel("Total Sales ($)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
