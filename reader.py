"""
    PartyManager:
    WebApp for ordering beverages and other stuff written in flask
    Copyright (C) 2020 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

from tkinter import *
import dboperations

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master
        self.pack(fill=BOTH, expand=1)

        self.next_order_button = Button(self, text="Next Order", command=self.refresh)
        self.next_order_button.place(x=10,y=150)

        self.number_label = Label(self, text="Click 'Mark as Done' to see the first order")
        self.number_label.place(x=10,y=20)

        self.item_label =  Label(self, text="")
        self.item_label.place(x=10,y=40)

        self.person_label =  Label(self, text="")
        self.person_label.place(x=10,y=60)

    def refresh(self):
        global order_id
        r = dboperations.get_order(order_id)
        if r:
            self.number_label.configure(text=f"Order Number: {order_id}")
            self.item_label.configure(text=f"Item: {r[0].title()}")
            self.person_label.configure(text=f"To: {r[1].title()}") 
            order_id+=1
        else:
            self.number_label.configure(text=f"No New Order")
            self.item_label.configure(text=f"Wait a moment")
            self.person_label.configure(text=f"and click 'next order'") 

if __name__ == "__main__":
    # initialize tkinter
    order_id = 1
    root = Tk()
    root.geometry("200x200")
    app = Window(root)

    # set window title
    root.wm_title("PartyManager Reader")

    # show window
    root.mainloop()