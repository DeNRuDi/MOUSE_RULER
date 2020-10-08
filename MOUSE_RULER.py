from pynput import mouse
from pynput import keyboard
print("MOUSE_RULER v1.0\nCopyright © 2020 DeNRuDi (Denis Rudnitskiy)")
print('Вышла v2.0 программы, ознакомиться - https://github.com/DeNRuDi/MOUSE_RULERv2')
i = 1
def main():
	def on_press(key):
		if key == keyboard.Key.esc:
			return False	

	def on_scroll(x, y, dx, dy):
		global i
		print(i, end='\r')
		i+=1
		
	with mouse.Listener(on_scroll=on_scroll), keyboard.Listener(on_press=on_press) as listener:
		listener.join()
	print()
	x = float(i - 1) / 3.4
	print("Твой результат: " + str(round((x),2)) + " Cм\n")
	
while True:
	answer = input("[1]Измерить предмет колёсиком мыши\n[2]Выход\n\nВведите ответ>")
	if answer == str(1):
		i = 1
		print("После измерения, нажмите - 'ESC'")
		main()
	elif answer == str(2):
		break
	else:
		print("\nВведен неверный ответ!\n")
