#!/usr/bin/env python3
"""
У нас есть данные о курсе валют по отношению к беларускому рублю на дату.
Это список из словарей, где каждая валюта представлена словарем вида:

{"Cur_ID":23,
 "Date":"2021-03-05T00:00:00",
  "Cur_Abbreviation":"CAD",
  "Cur_Scale":1,
  "Cur_Name":"Канадский доллар",
  "Cur_OfficialRate":2.0608}

Мы хотим, пользуясь этими данными. дать пользователю возможность запросить курс какой-то конкретной валюты,
по аббревиатуре, и получить в ответ сообщение вида: 

2021-03-05 1 Канадский доллар стоит 2.06 бел.руб

"""

message_from_user = "EUR"

courses = [{"Cur_ID":170,
			"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"AUD",
  			"Cur_Scale":1,
  			"Cur_Name":"Австралийский доллар",
  			"Cur_OfficialRate":2.0292},
  		   {"Cur_ID":191,
  			"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"BGN",
  			"Cur_Scale":1,
  			"Cur_Name":"Болгарский лев",
  			"Cur_OfficialRate":1.6044},
  		   {"Cur_ID":290,
  			"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"UAH",
  			"Cur_Scale":100,
  			"Cur_Name":"Гривен",
  			"Cur_OfficialRate":9.3999},
  		   {"Cur_ID":291,
  		   	"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"DKK",
  			"Cur_Scale":10,
  			"Cur_Name":"Датских крон",
  			"Cur_OfficialRate":4.2201},
  		   {"Cur_ID":145,
  		   	"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"USD",
  			"Cur_Scale":1,
  			"Cur_Name":"Доллар США",
  			"Cur_OfficialRate":2.6080},
  		   {"Cur_ID":292,
  			"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"EUR",
  			"Cur_Scale":1,
  			"Cur_Name":"Евро",
  			"Cur_OfficialRate":3.1417},
  		   {"Cur_ID":293,
  			"Date":"2021-03-05T00:00:00",
  			"Cur_Scale":10,
  			"Cur_Name":"Злотых",
  			"Cur_OfficialRate":6.8913},
  		   {"Cur_ID":355,
  			"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"JPY",
  			"Cur_Scale":100,
  			"Cur_Name":"Иен",
  			"Cur_OfficialRate":2.4295},
  		   {"Cur_ID":303,
  			"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"IRR",
  			"Cur_Scale":100000,
  			"Cur_Name":"Иранских риалов",
  			"Cur_OfficialRate":6.2095},
  		   {"Cur_ID":294,"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"ISK",
  			"Cur_Scale":100,
  			"Cur_Name":"Исландских крон",
  			"Cur_OfficialRate":2.0549},
  		   {"Cur_ID":23,
  			"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"CAD",
  			"Cur_Scale":1,
  			"Cur_Name":"Канадский доллар",
  			"Cur_OfficialRate":2.0608}]

cad_info = {"Cur_ID":23,
  			"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"CAD",
  			"Cur_Scale":1,
  			"Cur_Name":"Канадский доллар",
  			"Cur_OfficialRate":2.0608}
#2021-03-05 1 Канадский доллар стоит 2.06 бел.руб


today = cad_info["Date"]
scale = cad_info["Cur_Scale"]
money_name = cad_info["Cur_Name"]
currency = cad_info["Cur_OfficialRate"]

message = f"""{today} {scale} {money_name} стоит 
			{currency} бел.руб"""
#print(message)


today = cad_info["Date"][:-9]
scale = cad_info["Cur_Scale"]
money_name = cad_info["Cur_Name"]
currency = cad_info["Cur_OfficialRate"]

message = f"""{today} {scale} {money_name} стоит 
			{currency} бел.руб"""
#print(message)

def message_from_currency(currency):
	today = currency["Date"][:-9]
	scale = currency["Cur_Scale"]
	money_name = currency["Cur_Name"]
	currency = currency["Cur_OfficialRate"]

	message = f"{today} {scale} {money_name} стоит {currency} бел.руб"
	return message

message = message_from_currency(cad_info)
#print(message)


message = message_from_currency(courses[5])
#print(message)

#cad_info["UNEXISTED_KEY"]
#print(cad_info.get("UNEXISTED_KEY"))


def message_from_currency(currency):
	today = currency.get("Date")[:-9]
	scale = currency.get("Cur_Scale")
	money_name = currency.get("Cur_Name")
	currency = currency.get("Cur_OfficialRate")

	message = f"{today} {scale} {money_name} стоит {currency} бел.руб"
	return message

message = message_from_currency(cad_info)
#print(message)


cad_info = {"Cur_ID":23,
  			"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"CAD",
  			"Cur_Scale":1,
  			"Cur_Name":"Канадский доллар",
  			"Cur_OfficialRate":2.0608}


requested_keys = ("Date", "Cur_Scale","Cur_Name", "Cur_OfficialRate","Cur_Abbreviation")
keys = cad_info.keys()
'''
for key in requested_keys:
	if key not in keys:
		print("PROBLEM")
'''

def validate_currency(currency, requested_keys):
	keys = currency.keys()

	for key in requested_keys:
		if key not in keys:
			return False
	return True

res = validate_currency(cad_info, requested_keys)
#print(res)


ok_info = {"Cur_ID":23,
  			"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"CAD",
  			"Cur_Scale":1,
  			"Cur_Name":"Канадский доллар",
  			"Cur_OfficialRate":2.0608}

res = validate_currency(ok_info, requested_keys)
#print(res)
		
wrong_info = {"Cur_ID":23,
  			"Cur_Abbreviation":"CAD",
  			"Cur_Scale":1,
  			"Cur_Name":"Канадский доллар",
  			"Cur_OfficialRate":2.0608}

res = validate_currency(wrong_info, requested_keys)
#print(res)

normal_info = {"Date":"2021-03-05T00:00:00",
  			"Cur_Abbreviation":"CAD",
  			"Cur_Scale":1,
  			"Cur_Name":"Канадский доллар",
  			"Cur_OfficialRate":2.0608}

res = validate_currency(normal_info, requested_keys)
#print(res)


#for currency in courses:
#    print(currency)


#for currency in courses:
#	  res = validate_currency(currency, requested_keys)
#	  print(res)


#for currency in courses:
#	  res = validate_currency(currency, requested_keys)
#	  if res:
#		    print(currency["Cur_Abbreviation"])


user_message = "EUR"
"""
for currency in courses:
	  res = validate_currency(currency, requested_keys)
	  if res:
		    if currency["Cur_Abbreviation"] == user_message:
			      print(currency)
"""


for currency in courses:
    res = validate_currency(currency, requested_keys)
    if res:
        if currency["Cur_Abbreviation"] == user_message:
            message = message_from_currency(currency)
            #print(message)


user_message = "CAD"
user_message = "PLN"
user_message = "USD"
'''
for currency in courses:
    res = validate_currency(currency, requested_keys)

    if res:
        if currency["Cur_Abbreviation"] == user_message:
            message = message_from_currency(currency)
            print(message)
'''
def get_currency_by_abbr(courses, abbr):
    for currency in courses:
        res = validate_currency(currency, requested_keys)
        if res:
            if currency["Cur_Abbreviation"] == user_message:
                return currency

info = get_currency_by_abbr(courses, user_message)
#print(info)


user_message = "EUR"
user_message = "DKK"
user_message = "JPY"


def send_currency_message(courses, abbr):
	  currency = get_currency_by_abbr(courses, abbr)
	  if currency:
		    currency_message = message_from_currency(currency)
		    print(currency_message)
	  else:
		    print("Извините, данных о валюте не обнаружено")

send_currency_message(courses, user_message)



