def total_with_tax(price, tax_rate):
    tax = price * tax_rate
    total = price + tax
    # Meant to return total
    price + tax

print(total_with_tax(100, 0.15))