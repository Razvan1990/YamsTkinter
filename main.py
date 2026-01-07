from helper.checker import Checker
from helper.help_functions import Helper
from gui.app_gui import GuiCreator
import constans


def compute_logic():
    gui = GuiCreator()
    gui.create_main_gui()

if __name__ == "__main__":
    helper = Helper()
    checker = Checker()
    # row = 5
    # value1, value2, value3, value4, value5, value6 = 4, 6, 9, 20, 15, 24
    # print(helper.calculate_totals(row, value1, value2, value3, value4, value5, value6))
    # print("----------------------------------------")
    # dice1 = "6"
    # dice2 = "4"
    # print(helper.calculate_full(dice1, dice2))
    # print("-----------------------------------------")
    # dice1 = "8"
    # dice2= "6"
    # print(checker.check_full_calculation(dice1, dice2))
    compute_logic()