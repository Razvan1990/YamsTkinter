from tkinter import messagebox
class Checker(object):

    def check_full_calculation(self, dice1, dice2) -> bool:
        #1. check to see if it is completed
        if dice1 == "" or dice2 == "":
            messagebox.showerror("Error", "Please enter the 2 dices")
            return True
        #2. check if dice is numeric
        if not dice1.isnumeric() or not dice2.isnumeric():
            messagebox.showerror("Error", "Please enter numeric digits")
            return True
        #3. check if dices are between 1 and 6
        if not 1<=int(dice1)<=6 or not 1<=int(dice2)<=6:
            messagebox.showerror("Error", "Please enter a digit between 1 and 6")
            return True
        #4. check if dices are not equal
        if int(dice1) == int(dice2):
            messagebox.showerror("Error", "Cannot have 2 dices the same for full")
            return True
        return False

    def yams_careu_calculation(self, dice1) -> bool:
        # 1. check to see if it is completed
        if dice1 == "":
            messagebox.showerror("Error", "Please enter the dice")
            return True
        # 2. check if dice is numeric
        if not dice1.isnumeric():
            messagebox.showerror("Error", "Please enter numeric digits")
            return True
        # 3. check if dices are between 1 and 6
        if not 1 <= int(dice1) <= 6:
            messagebox.showerror("Error", "Please enter a digit between 1 and 6")
            return True
        return False

