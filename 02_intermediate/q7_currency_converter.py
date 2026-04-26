# Q7: Currency Converter
# Task: Convert currency using live exchange rates from ExchangeRate-API
# API: https://www.exchangerate-api.com (1500 free requests/month)
# Sign up to get free API key

import requests

API_KEY = "your_api_key_here"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest"

def get_rates(base_currency):
    response = requests.get(f"{BASE_URL}/{base_currency}")
    if response.status_code == 200:
        return response.json()["conversion_rates"]
    else:
        print(f"Error: {response.status_code}")
        return None

def convert(amount, from_currency, to_currency):
    rates = get_rates(from_currency)
    if rates and to_currency in rates:
        result = amount * rates[to_currency]
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        return result
    else:
        print(f"Currency {to_currency} not found.")
        return None

# Test
convert(100, "USD", "INR")
convert(500, "INR", "USD")
convert(100, "USD", "EUR")