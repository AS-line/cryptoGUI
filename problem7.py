from random import randint as rint
from math import fabs
from os import system




none_cash = 500
first_cash = none_cash
price_first_bitc = rint(0, 100)
price_first_ether = rint(0, 100)

price_second_bitc = price_first_bitc
price_second_ether = price_first_ether

crypt = None


while(True):

	crypt = []
	if (first_cash < 0) or (first_cash >= 1000):
		break

	print("")
	print("$"*25)
	print("Цены:\nБиткоина", price_second_bitc)
	print("Эфириума", price_second_ether)
	print("$"*25)

	print("")
	ch = input("1)bitcoin\n2)ethereum\n3)both\n4)nothing\n>>>")
	if ch == "1":
		first_cash -= price_second_bitc
		crypt.append("bitcoin")
	elif ch == "2":
		first_cash -= price_second_ether
		crypt.append("ethereum")
	elif ch == "3":
		first_cash -= price_second_bitc
		first_cash -= price_second_ether
		crypt.append("both")
	else:
		crypt = []

	# print("first_cash", first_cash)
	# print("price_second_bitc", price_second_bitc)


	price_second_bitc = rint(0, 100)
	price_second_ether = rint(0, 100)

	# print("first_cash", first_cash)
	# print("price_second_bitc", price_second_bitc)


	system("clear")
	print("#"*25)
	if price_first_bitc > price_second_bitc:
		print("Биткоин упал на", price_first_bitc - price_second_bitc, "(", "-", price_first_bitc - price_second_bitc,")")
		# print("price_second_bitc", price_second_bitc)
		if "bitcoin" in crypt:
			first_cash += price_second_bitc
			# print("111111")
	else:
		print("Биткоин вырос на", price_second_bitc - price_first_bitc, "(", "+", price_second_bitc - price_first_bitc,")")
		if "bitcoin" in crypt:
			first_cash += price_second_bitc
			# print("222222")

	if price_first_ether > price_second_ether:
		print("Эфир упал на", price_first_ether - price_second_ether, "(", "-", price_first_ether - price_second_ether,")")
		if "ethereum" in crypt:
			first_cash += price_second_ether
			# print("333333")
	else:
		print("Эфир вырос на", price_second_ether - price_first_ether, "(", "+", price_second_ether - price_first_ether,")")
		if "ethereum" in crypt:
			first_cash += price_second_ether
			# print("4444444")

	if ("both" in crypt):
		#print("bitc and ether")
		first_cash += price_second_bitc
		first_cash += price_second_ether
		# print("555555")


	print("#"*25)
	print("")
	print(">>>Cash =", str(first_cash)+"<<<")
	print("")

	price_first_bitc = price_second_bitc
	price_first_ether = price_second_ether

	print("="*25)
	if none_cash > first_cash:
		print("Сводка:\nвы в минусе("+"-"+str(fabs(first_cash-none_cash))+")")
		none_cash = first_cash
	elif none_cash < first_cash:
		print("Сводка:\nвы в плюсе("+"+"+str(fabs(none_cash-first_cash))+")")
		none_cash = first_cash
	else:
		print("Вы не произвели покупку валюты, или произошла ошибка")
	print("="*25)



if first_cash < 0:
	print("*"*25)
	print("У вас закончился капитал! Видимо криптобиржа это не ваше!")
else:
	print("*"*25)
	print("Поздравляем! Вы достигли своей цели(cash >= 1000).")
