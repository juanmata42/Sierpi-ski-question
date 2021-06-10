from tkinter import *
from random import randint
from time import sleep

punto_anterior=[0,0]
punto_nuevo=[0,0]
resultado=0
veces=0
a=randint(1,600)
s=randint(1,600)
z=randint(1,600)
x=randint(1,600)
q=randint(1,600)
w=randint(1,600)


def principio():
	canvas.create_text((a,s),text = "*",fill = 'lawn green', font = ('Arial', 30))
	canvas.create_text((z,x),text = "*",fill = 'lawn green', font = ('Arial', 30))
	canvas.create_text((q,w),text = "*",fill = 'lawn green', font = ('Arial', 30))
	root.update()
	

#lo pongo como si fuera un dado normal, pero podría ser un dado de 3 caras (num aleatorio del 1 al 3)
def tirada():
    global resultado
    resultado=randint(1,6)
    return resultado

#la formula para las coordenadas del punto medio entre 2 puntos es a=(Xa,Ya)  b=(Xb,Yb) punto_medio=(Xa+Xb)/2,(Ya+Yb)/2
def calculo_coordenadas(resultado):
	global punto_anterior
	global punto_nuevo
	if resultado in [1,2]:
		punto_nuevo=[((punto_anterior[0]+a)/2),((punto_anterior[1]+s)/2)]
		canvas.create_text((punto_nuevo[0],punto_nuevo[1]),text = ".",fill = 'lawn green')
	if resultado in [3,4]:
		punto_nuevo=[((punto_anterior[0]+z)/2),((punto_anterior[1]+x)/2)]
		canvas.create_text((punto_nuevo[0],punto_nuevo[1]),text = ".",fill = 'lawn green')
	if resultado in [5,6]:
		punto_nuevo=[((punto_anterior[0]+q)/2),((punto_anterior[1]+w)/2)]
		canvas.create_text((punto_nuevo[0],punto_nuevo[1]),text = ".",fill = 'lawn green')


	punto_anterior=punto_nuevo
	return punto_anterior

def punto_inicial(event):
	
	canvas.create_text((event.x,event.y),text = ".",fill = 'lawn green')
	canvas.unbind('<Button-1>')
	punto_anterior=[event.x,event.y]
	repeticion()



def repeticion():
	global veces
	for num in range(1,9999999):
		tirada()
		calculo_coordenadas(resultado)
		contador.configure(text=f"{num}")
		sleep(0.01)
		root.update()

root = Tk()
root.title('Sierpinski triangle')
root.geometry('600x600')
canvas = Canvas(root, width=600, height=600, bg='black')
canvas.bind('<Button-1>', punto_inicial)
contador=Label(root,text = "Repeticiones",fg = 'lawn green',bg="black", font = ('Arial', 10))
contador.place(anchor=NW,y=10,x=10)
canvas.pack()
principio()

root.mainloop()