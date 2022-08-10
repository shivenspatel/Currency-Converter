import requests
import pandas as pd

url = "https://api.apilayer.com/currency_data/live"

payload = {}
headers= {"apikey": ""} #API Key has to be obtained from https://apilayer.com/marketplace/currency_data-api

output = requests.request("GET", url, headers=headers, data = payload)
output_json = output.json()

main = pd.DataFrame(data={'Currency':list(output_json['quotes']), 'In USD':list(output_json['quotes'].values())})

for i in range(0, len(main['Currency'])):
    main.at[i, 'Currency'] = str(main.at[i, 'Currency'])[3:6]

def converter(input_currency, output_currency, input):
    if input_currency == 'USD': #Procedure if input currency is USD
        index = 0

        for i in range(0, len(main['Currency'])):
            if main.at[i, 'Currency'] == output_currency:
                index = i
                break
        return input * main.at[index, 'In USD']

    else: #Procedure if input currency is different
        index = 0

        for i in range(0, len(main['Currency'])):
            if main.at[i, 'Currency'] == input_currency:
                index = i
                break
        input_usd = input * (1/main.at[index, 'In USD'])

        if output_currency == 'USD':
            return input_usd
        else:
            indexy = 0

            for i in range(0, len(main['Currency'])):
                if main.at[i, 'Currency'] == output_currency:
                    indexy = i
                    break
            return input_usd * main.at[indexy, 'In USD']

# input_currency_input = input("What Currency Would You Like to Convert FROM? (Please Use the Abbreviation): ").upper()
# input_amount_input = float(input("How Much?: "))
# output_currency_input = input("What Currency Would You Like to Convert TO? (Please Use the Abbreviation): ").upper()

# print(str(input_amount_input) + " " + input_currency_input + " is currently worth " + str(converter(input_currency_input, output_currency_input, input_amount_input)) + " " + output_currency_input)