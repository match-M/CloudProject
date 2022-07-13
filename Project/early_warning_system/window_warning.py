from tkinter import *
root = Tk()
canvas = Canvas(root)
canvas.pack()
time = 60
def Warning():
	def tick():
		
		canvas.delete(ALL)
		
		global time
		time -= 1
		
		canvas.create_text(50, 50, text=time)
		if time == 0:
			do_something()
		else:
			canvas.after(1000, tick)
	canvas.after(1, tick)
	root.mainloop()
