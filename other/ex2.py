def price_breakdown2(line_items, exchange_rates, currency_symbols):
    ans = []
    end = ""
    total = 0
    for i in line_items:
        temp = i[0] + ": "
        if i[2] != "EUR":
            temp += "("
            temp += currency_symbols[i[2]]
            temp += i[1] + ") €"
            temp += str(float(i[1]) / exchange_rates[i[2]])
            temp += " approx."
            end = " approx.\n"
            total += float(i[1]) / exchange_rates[i[2]]
        else:
            temp += "€" + i[1]
            total += float(i[1])
        ans.append(temp)
    res = ""
    for p in ans:
        res += p + "\n"
    res += "\nTOTAL: €" + str(total) + end
    return res
            
      
      



def price_breakdown(line_items, exchange_rates, currency_symbols):
    total_euros = 0
    breakdown = []

    for item in line_items:
        name = item[0]
        amount = float(item[1])
        currency = item[2]

        # Convert to Euros if currency is not EUR
        if currency != "EUR":
            exchange_rate = exchange_rates[currency]
            amount_euros = amount / exchange_rate
            breakdown.append(f"{name}: ({currency_symbols[currency]}{amount:.2f}) €{amount_euros:.2f} approx.")
            total_euros += amount_euros
        else:
            breakdown.append(f"{name}: €{amount:.2f}")
            total_euros += amount

    total_text = f"TOTAL: €{total_euros:.2f}"
    if total_euros != get_total_amount(line_items):
        total_text += " approx."
    breakdown.append(total_text)

    return "\n".join(breakdown)

def get_total_amount(line_items):
    total = 0
    for item in line_items:
        total += float(item[1])
    return total

if __name__ == "__main__":
    line_items = [
        ["Rental", "190.00", "EUR"],
        ["GPS", "15.00", "GBP"],
        ["Insurance", "30.00", "USD"]
    ]
    exchange_rates = {
        "GBP": 0.70,
        "USD": 1.20
    }
    currency_symbols = {
        "GBP": "£",
        "EUR": "€",
        "USD": "$"
    }

    print(price_breakdown2(line_items, exchange_rates, currency_symbols))
    
    
  