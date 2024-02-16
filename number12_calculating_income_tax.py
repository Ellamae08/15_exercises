def calculate_income_tax(taxable_income):
    tax = 0
    if taxable_income > 20000:
        tax += 10000 * 0
        tax += 10000 * 0.1
        tax += (taxable_income - 20000) * 0.2
    elif 10000 < taxable_income <= 20000:
        tax += 10000 * 0
        tax += (taxable_income - 10000) * 0.1
    else:
        tax += taxable_income * 0
    return tax

income = int(input("Enter the taxable income: "))
income_tax = calculate_income_tax(income)
print("Income tax payable:", income_tax)