import time
import sys
from colorama import Fore
from random import randint

comp_lsit = ['desktop-ancholav', 'sovin-uchilk-pc']

def vzlom(arg: str):
	last_time = 50.5
	if arg.lower() in comp_lsit:
		for i in range(101):
			last_time -= 0.5
			print(f"\nПроцесс взлома {arg}, взломано {i} %")
			print(f"{Fore.BLUE}Осталось примерно {last_time} секунд{Fore.WHITE}")
			time.sleep(0.5)
			if randint(0, 99) == 99:
				print(f"\n{Fore.RED}Произошла ошибка во взломе. Повторите ещё раз.")
				input()
				sys.exit()

		print(f"\n{Fore.GREEN}Успех!")
	else:
		print(f"\n{Fore.RED}Вашего ввода нет в переменной. Попробуйте заглянуть в исходный код программы.")

def start():
	print("Heck16, VAND. Made for Ubuntu.")
	print("Внимание! Это приложение шуточное.")

	try:
		vzlom(sys.argv[1])
	except IndexError:
		print(f"{Fore.RED}\nВНИМАНИЕ!!! Произошла ошибка индекса. Возможно, аргументы программы пусты. Попробуйте ещё раз.")
	input()

start()
