import time
import sys
from colorama import Fore

comp_lsit = ['desktop-ancholav', 'sovin-uchilk-pc']

def vzlom(arg: str):
	if arg.lower() in comp_lsit:
		for i in range(101):
			print(f"\nПроцесс взлома {arg}, взломано {i} %")
			print(f"{Fore.BLUE}Осталось примерно {100-i} секунд{Fore.WHITE}")
			time.sleep(1)
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
