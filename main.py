#coding=utf-8
from tkinter import *
from tkinter import ttk
import os
import time


available_characters = ['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F']
available_bin_characters = ['0', '1']

class Calculator:

    def __init__(self,master):
        self.num_to_alpha = ['A', 'B', 'C', 'D', 'E', 'F']
        self.dec_num = 0
        self.master = master
        self.initWidgets()
        self.items_count = 0
        self.item1_flag = 0
        self.item2_flag = 0
        self.item3_flag = 0

    def initWidgets(self):

        self.num_in_dec = StringVar()
        self.num_in_hex = StringVar()
        self.num_in_bin = StringVar()

        main_frame = Frame(self.master)
        main_frame.pack(side=TOP,fill=BOTH,expand=YES)

        label_num_in_dec = Label(main_frame, text='dec(十进制):', width=14, height=2)
        label_num_in_hex = Label(main_frame, text='hex(十六进制):', width=14, height=2)
        label_num_in_bin = Label(main_frame, text='bin(二进制):', width=14, height=2)

        label_num_in_dec.grid(row=0, column=0)
        label_num_in_hex.grid(row=1, column=0)
        label_num_in_bin.grid(row=2, column=0)


        self.st1 = StringVar()
        self.t1 = StringVar()
        self.entry_task1 = ttk.Entry(main_frame,textvariable=self.st1,width=30,font=('Helvetica',20,'bold'),foreground='green')
        self.entry_task1.grid(row=0,column=1)


        self.st2 = StringVar()
        self.t2 = StringVar()
        self.entry_task2 = ttk.Entry(main_frame,textvariable=self.st2,width=30,font=('Helvetica',20,'bold'),foreground='green')
        self.entry_task2.grid(row=1,column=1)

        self.st3 = StringVar()
        self.t3 = StringVar()
        self.entry_task3 = ttk.Entry(main_frame,textvariable=self.st3,width=30,font=('Helvetica',20,'bold'),foreground='green')
        self.entry_task3.grid(row=2,column=1)

        button_frame = Frame(self.master)
        button_frame.pack(side=BOTTOM)
        button_quit = ttk.Button(button_frame, text='Quit(退出)', command=self.do_quit).pack(side=RIGHT, padx=5)
        button_clear = ttk.Button(button_frame, text='Clear(清空)', command=self.do_clear).pack(side=RIGHT,padx=5)
        button_cal = ttk.Button(button_frame,text='Transfer(转换)',command=self.do_calculate).pack(side=RIGHT,padx=5)

    def get_alpha(self,num):
        return self.num_to_alpha[num-10]

    def get_num_from_alpha(self,a):
        i = 0
        for b in self.num_to_alpha:
            if b == a:
                return i+10
            i += 1

    def dec_to_hex(self,n):
        count = 0
        temp = 0
        mystr = ''
        a = []
        b = []
        while n > 0:
            temp = n
            n = int(n / 16)
            a.append(int(temp % 16))
            count += 1
        for j in range(0, count):
            if a[j] in range(10, 16):
                b.append(self.get_alpha(a[j]))
            else:
                b.append(str(a[j]))
        for i in range(count-1, -1, -1):
            mystr += b[i]
        self.st2.set(mystr)

    def dec_to_bin(self,n):
        count = 0
        temp = 0
        mystr = ''
        a = []
        b = []
        while n > 0:
            temp = n
            n = int(n / 2)
            a.append(int(temp % 2))
            count += 1
        for i in range(count - 1, -1, -1):
            mystr += str(a[i])
        self.st3.set(mystr)

    def hex_to_dec(self,b):
        c = []
        count = 0
        j = 0
        for a in b:
            if a >= 'A':
                c.append(self.get_num_from_alpha(a))
            else:
                c.append(int(a))
            count += 1
        for i in range(count-1,-1,-1):
            self.dec_num += c[i] * 16 ** j
            j += 1
        self.st1.set(str(self.dec_num))

    def bin_to_dec(self,b):
        c = []
        count = 0
        j = 0
        for a in b:
            c.append(int(a))
            count += 1
        for i in range(count-1,-1,-1):
            self.dec_num += c[i] * 2 ** j
            j += 1
        self.st1.set(str(self.dec_num))

    def do_calculate(self):
        if self.st1.get() is not '':
            self.item1_flag = 1
            self.items_count += 1
        elif self.st2.get() is not '':
            self.item2_flag = 1
            self.items_count += 1
        elif self.st3.get() is not '':
            self.item3_flag = 1
            self.items_count += 1
        if self.items_count > 1:
            self.do_clear()
            self.items_count = 0
            return

        if self.item1_flag:
            dec_num = self.st1.get()
            dec_num = int(dec_num)
            if dec_num > 0:
                self.dec_to_hex(dec_num)
                self.dec_to_bin(dec_num)
            else:
                self.st1.set('不好意思，只支持正数！')
        elif self.item2_flag:
            hex_num = self.st2.get().upper()
            for i in hex_num:
                if i not in available_characters:
                    self.st2.set("输入不合法，请重新输入！")
                    return
            self.hex_to_dec(hex_num)
            self.dec_to_bin(self.dec_num)
        elif self.item3_flag:
            bin_num = self.st3.get()
            for i in bin_num:
                if i not in available_bin_characters:
                    self.st3.set("输入不合法，请重新输入！")
                    return
            self.bin_to_dec(bin_num)
            self.dec_to_hex(self.dec_num)
        else:
            print("no input")

    def do_clear(self):
        self.st1.set('')
        self.st2.set('')
        self.st3.set('')
        self.dec_num = 0
        self.items_count = 0
        self.item1_flag = 0
        self.item2_flag = 0
        self.item3_flag = 0

    def do_quit(self):
        self.do_clear()
        os._exit(0)


if __name__ == '__main__':
    root = Tk()
    root.geometry('600x120')
    root.title('System Transfer')
    mycal = Calculator(root)
    root.mainloop()






