import os
from queue import LifoQueue

stack = LifoQueue(maxsize=3)

def menu () :
    print("Aplikasi Gudang")
    print("1.Liat stack")
    print("2.Nambah stack")
    print("3.Keluar stack")
    print("4.Konfigurasi stack")
    print("5.Exit")
    pilihan = input("pilihan :")
    pilihanmenu(pilihan)

def pilihanmenu(pilihan):
    if pilihan == '1' :
        liatstack()
    elif pilihan == '2' :
        addstack()
    elif pilihan == '3' :
        popstack()
    elif pilihan == '4' :
        konfigstack()
    elif pilihan == '5' :
        exit()
    else :
        menu()

def liatstack() :
    global stack
    print(stack.queue)
    menu()

def addstack() :
    global stack
    stack.put(input())
    menu()

def popstack() :
    global stack
    print(stack.get())
    menu()

def konfigstack():
    global stack
    stack = LifoQueue(maxsize=input())

def exit():
    print('bye')

menu()
print("Ukuran: ", stack.qsize())