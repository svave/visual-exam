import requests
import time

response = requests.get(
    url='https://api.energidataservice.dk/dataset/Elspotprices?offset=0&sort=HourUTC%20DESC&timezone=dk&filter={"PriceArea":["DK1"]}')


result = response.json()

#print(result)

#for k, v in result.items():
#    print(k, v)

records = result.get('records', [])
#print(records)

#print(records[1]["SpotPriceEUR"])


current_hour = time.strftime("%Y-%m-%dT%H:00:00")



print(result)
print(current_hour)

price = 0
for x in records:
    if x['HourUTC'] == current_hour:
        price = x['SpotPriceDKK']
        print(x['SpotPriceDKK'])


kwh_per_tørk = 1.475
convert = kwh_per_tørk/1000
print(convert)
price_tørk = convert*price
print(price_tørk)



#print('records:')
#for record in records:
#    print(' ', record)


#current_hour = time.strftime("%Y-%m-%dT%H:00:00")
#print(records['SpotPriceDKK'])
