menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

# Input data penjualan
for day in range(1, number_of_days + 1):
    daily_sales = []

    for menu in menus:
        amount = int(input(f"Day {day}, {menu}: "))
        daily_sales.append(amount)

    sales.append(daily_sales)

# Total setiap hari
print("Total per day:")

for i in range(len(sales)):
    total = 0

    for amount in sales[i]:
        total += amount

    print(f"Day {i + 1}: {total}")

# Total setiap menu
menu_totals = []

for col in range(len(menus)):
    total = 0

    for row in sales:
        total += row[col]

    menu_totals.append((menus[col], total))

print("Total per menu:", menu_totals)

# Menu terlaris
best_name, best_total = menu_totals[0]

for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print(f"Best seller: {best_name} ({best_total})")
