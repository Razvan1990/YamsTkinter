import tkinter
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import constans
from helper.checker import Checker
from helper.help_functions import Helper


class GuiCreator(object):

    def __init__(self):
        self.helper = Helper()
        self.checker = Checker()
        self.ico_image = os.path.join(os.getcwd(), "images", "yams.ico")
        self.rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.index_start_x = 20
        self.index_start_y = 50
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.running_time = False
        self.dict_scores = {}
        self.list_games = ["T_NR", "F", "q", "Q", "K", "Y", "T_SB", "TOTAL_SCORES"]


    def update_clock(self, label_clock):
        if self.running_time:
            result = ""
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
                self.hours = 0
            if self.minutes == 60:
                self.seconds = 0
                self.minutes = 0
                self.hours += 1
            result = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
            label_clock["text"] = result
        # here to call it everytime, no matter the running time
        label_clock.after(1000, lambda: self.update_clock(label_clock))

    def make_calculations(self, list_entries, index_start1, index_start2):
        player1_score = 0
        player2_score = 0
        list_diff = []
        for i in range(index_start1, index_start1 + 5):
            if list_entries[i].get().isnumeric():
                player1_score += int(list_entries[i].get())
        for i in range(index_start2, index_start2 + 5):
            if list_entries[i].get().isnumeric():
                player2_score += int(list_entries[i].get())
        diff_score = abs(player2_score - player1_score)
        if player1_score > player2_score:
            list_diff.append(entry_player1.get())
            list_diff.append(diff_score)
        elif player2_score > player1_score:
            list_diff.append(entry_player2.get())
            list_diff.append(diff_score)
        else:
            list_diff.append("EQUAL")
            list_diff.append(diff_score)
        return player1_score, player2_score, list_diff

    def calculate_results(self, list_entries, list_buttons):
        '''

        :param list_entries: all the entries from the from full till yams
        :param list_buttons: buttons from the small and big totals
        :return: the self.dict_scores will be a dict like: {p1:{"totals":x, "full":y....}, p2:"{"totals":x2, "full":y2}, difference: {"totals":abs(x2-x1)...}
        '''
        list_scores_player1 =[]
        list_scores_player2 =[]
        list_scores_differences =[]
        index_starting_p1 = 60
        index_starting_p2 = 65
        # calculate totals
        total_player1, total_player2, diff_totals = self.make_calculations(list_entries, index_starting_p1,index_starting_p2)
        list_scores_player1.append(total_player1)
        list_scores_player2.append(total_player2)
        list_scores_differences.append(diff_totals)
        # calculate full
        index_starting_p1 = 70
        index_starting_p2 = 95
        full_player1, full_player2, diff_full = self.make_calculations(list_entries, index_starting_p1,index_starting_p2)
        list_scores_player1.append(full_player1)
        list_scores_player2.append(full_player2)
        list_scores_differences.append(diff_full)
        # calculate small straight
        index_starting_p1 = 75
        index_starting_p2 = 100
        straight_s_player1, straight_s_player2, diff_straight_s = self.make_calculations(list_entries, index_starting_p1,index_starting_p2)
        list_scores_player1.append(straight_s_player1)
        list_scores_player2.append(straight_s_player2)
        list_scores_differences.append(diff_straight_s)
        # calculate big straight
        index_starting_p1 = 80
        index_starting_p2 = 105
        straight_b_player1, straight_b_player2, diff_straight_b = self.make_calculations(list_entries,index_starting_p1,index_starting_p2)
        list_scores_player1.append(straight_b_player1)
        list_scores_player2.append(straight_b_player2)
        list_scores_differences.append(diff_straight_b)
        #calculate 4 of a kind
        index_starting_p1 = 85
        index_starting_p2 = 110
        careu_player1, careu_player2, diff_careu = self.make_calculations(list_entries,index_starting_p1,index_starting_p2)
        list_scores_player1.append(careu_player1)
        list_scores_player2.append(careu_player2)
        list_scores_differences.append(diff_careu)
        #calculate yams
        index_starting_p1 = 90
        index_starting_p2 = 115
        yams_player1, yams_player2, diff_yams = self.make_calculations(list_entries,index_starting_p1,index_starting_p2)
        list_scores_player1.append(yams_player1)
        list_scores_player2.append(yams_player2)
        list_scores_differences.append(diff_yams)
        '''calculate small bigs'''
        #first 5 buttons are for player1
        player1_bs= 0
        player2_bs =0
        list_diff_bs =[]
        for i in range(0, 5):
            if list_buttons[i].cget("text").isnumeric():
                player1_bs+=int(list_buttons[i].cget("text"))
        #from button index 5 is player 2
        for i in range(5, 10):
            if list_buttons[i].cget("text").isnumeric():
                player2_bs+=int(list_buttons[i].cget("text"))
        diff_bs = abs(player1_bs - player2_bs)
        if player1_bs > player2_bs:
            list_diff_bs.append(entry_player1.get())
            list_diff_bs.append(diff_bs)
        elif player2_bs > player1_bs:
            list_diff_bs.append(entry_player2.get())
            list_diff_bs.append(diff_bs)
        else:
            list_diff_bs.append("EQUAL")
            list_diff_bs.append(diff_bs)
        list_scores_player1.append(player1_bs)
        list_scores_player2.append(player2_bs)
        list_scores_differences.append(list_diff_bs)
        #TODO - POPULATE DICTIONARY
        dict_scores_player1 ={}
        dict_scores_player2 = {}
        dict_differences = {}
        total_score_player1 = sum(list_scores_player1)
        list_scores_player1.append(total_score_player1)

        total_score_player2 = sum(list_scores_player2)
        list_scores_player2.append(total_score_player2)

        list_scores_total_differences =[]
        total_difference = abs (total_score_player1 - total_score_player2)
        if total_score_player1 > total_score_player2:
            list_scores_total_differences.append(entry_player1.get())
            list_scores_total_differences.append(total_difference)
            list_scores_differences.append(list_scores_total_differences)
        elif total_score_player2 > total_score_player1:
            list_scores_total_differences.append(entry_player2.get())
            list_scores_total_differences.append(total_difference)
            list_scores_differences.append(list_scores_total_differences)
        else:
            list_scores_total_differences.append("EQUAL")
            list_scores_total_differences.append(total_difference)
            list_scores_differences.append(list_scores_total_differences)
        #list_total_scores = [total_score_player1, total_score_player2, total_difference]

        for i in range (0, len(self.list_games)):
            dict_scores_player1.update({self.list_games[i]:list_scores_player1[i]})
            dict_scores_player2.update({self.list_games[i]:list_scores_player2[i]})
            dict_differences.update({self.list_games[i]:list_scores_differences[i]})
        self.dict_scores.update({entry_player1.get():dict_scores_player1})
        self.dict_scores.update({entry_player2.get():dict_scores_player2})
        self.dict_scores.update({"DIFFERENCE":dict_differences})
        for key in self.dict_scores.keys():
            print(key, self.dict_scores[key])

        #print message to user to press calculate and enable result button
        messagebox.showinfo("PRESS CALCULATE", "Press the 'CHECK RESULTS' button on left to see the results")
        results_button["state"] = "normal"
        results_button["bg"] = "#B9F0C0"

    def insert_results(self, window):
        '''

        :param window: the frame
        :return: a treeview with the results
        '''
        columns =["Game"]
        for key in self.dict_scores:
            columns.append(key)
        col_tuple = tuple(columns)
        results_treeview = ttk.Treeview(window, show='headings', columns=col_tuple, height=9, )
        # ADD THE COLUMNS
        # define the headings
        results_treeview.heading(0, text=col_tuple[0], anchor="center")
        results_treeview.heading(1, text=col_tuple[1], anchor="center")
        results_treeview.heading(2, text=col_tuple[2], anchor="center")
        results_treeview.heading(3, text=col_tuple[3], anchor="center")
        # redefine column dimensions
        results_treeview.column(col_tuple[0], width=120, stretch=YES, anchor="center" )
        results_treeview.column(col_tuple[1], width=70, stretch=YES, anchor="center" )
        results_treeview.column(col_tuple[2], width=70, stretch=YES, anchor="center" )
        results_treeview.column(col_tuple[3], width=140, stretch=YES, anchor="center" )

        results_treeview.tag_configure("TOTAL_SCORES", background="#CDFA20", foreground="black", font=("Helvetica", 10, "bold"))
        # create a custom style
        style = ttk.Style(window)
        style.theme_use("clam") #this permits the foreground property
        style.configure("Treeview.Heading", background="#3871A8", foreground="#F0F0F0", font=("Helvetica", 10, "bold"), justify="center")
        style.configure("Treeview", background="#400F20", fieldbackground="#F2EBEB", foreground="#ffffff",
                        font=("Helvetica", 8, "bold"))
        #add values in treeview
        player1_scores = self.dict_scores[entry_player1.get()]
        player2_scores = self.dict_scores[entry_player2.get()]
        difference_scores= self.dict_scores["DIFFERENCE"]

        #just iterate over one dict -> these have the same length and get value of each game
        for game in player1_scores.keys():
            winner, score_dif = difference_scores[game]
            if winner == "EQUAL":
                diff_append = "It's equality"
            else:
                diff_append = f"{score_dif} for {winner}"
            row = (game, player1_scores[game], player2_scores[game], diff_append)
            if game == self.list_games[len(self.list_games) -1]:
                results_treeview.insert('', 'end', values=("", "", "", ""))
                results_treeview.insert('', 'end', values=row, tags="TOTAL_SCORES")
            else:
                results_treeview.insert('', 'end', values=row)
        results_treeview.place(x=10, y=70)




    def start(self):
        self.running_time = True

    def pause(self):
        self.running_time = False

    def compute_full_logic(self, dice1, dice2):
        full_chck = self.checker.check_full_calculation(dice1, dice2)
        if full_chck:
            return
        result_normal, result_10, result_served = self.helper.calculate_full(dice1, dice2)
        # start changing the labels
        label_full_result_normal["text"] = str(result_normal)
        label_full_result_plus10["text"] = str(result_10)
        label_full_result_served["text"] = str(result_served)
        # clear all other labels and entries of other games
        label_careu_result_normal["text"] = ""
        label_careu_result_plus10["text"] = ""
        label_careu_result_served["text"] = ""
        entry_dice_careu.delete(0, tkinter.END)

        label_yams_result_normal["text"] = ""
        label_yams_result_plus10["text"] = ""
        label_yams_result_served["text"] = ""
        entry_dice_yams.delete(0, tkinter.END)

    def compute_yams_careu_logic(self, dice1, option_game):
        yams_careu_chck = self.checker.yams_careu_calculation(dice1)
        if yams_careu_chck:
            return
        if option_game == 1:
            result_normal, result_10, result_served = self.helper.calculate_4_of_a_kind(dice1)
            label_careu_result_normal["text"] = str(result_normal)
            label_careu_result_plus10["text"] = str(result_10)
            label_careu_result_served["text"] = str(result_served)
            # clear all other labels of other games
            label_full_result_normal["text"] = ""
            label_full_result_plus10["text"] = ""
            label_full_result_served["text"] = ""
            entry_dice_1.delete(0, tkinter.END)
            entry_dice_2.delete(0, tkinter.END)

            label_yams_result_normal["text"] = ""
            label_yams_result_plus10["text"] = ""
            label_yams_result_served["text"] = ""
            entry_dice_yams.delete(0, tkinter.END)
        else:
            result_normal, result_10, result_served = self.helper.calculate_yams(dice1)
            label_yams_result_normal["text"] = str(result_normal)
            label_yams_result_plus10["text"] = str(result_10)
            label_yams_result_served["text"] = str(result_served)
            # clear all other labels of other games
            label_full_result_normal["text"] = ""
            label_full_result_plus10["text"] = ""
            label_full_result_served["text"] = ""
            entry_dice_1.delete(0, tkinter.END)
            entry_dice_2.delete(0, tkinter.END)

            label_careu_result_normal["text"] = ""
            label_careu_result_plus10["text"] = ""
            label_careu_result_served["text"] = ""
            entry_dice_careu.delete(0, tkinter.END)

    def check_entries(self, entries_numbers):
        '''player1'''
        if entries_numbers[0].get() != "" and entries_numbers[5].get() != "" and entries_numbers[10].get() != "" and \
                entries_numbers[15].get() != "" and entries_numbers[20].get() != "" and entries_numbers[25].get() != "":
            button_player1_down["state"] = "normal"
            button_player1_down["bg"] = "#C4F3FF"
        else:
            button_player1_down["state"] = "disabled"
            button_player1_down["bg"] = "#EDE8E8"
            # reset the total in case of mistake and put again
            entries_numbers[60].delete(0, tkinter.END)
            entries_numbers[60]["state"] = "disabled"

        if entries_numbers[1].get() != "" and entries_numbers[6].get() != "" and entries_numbers[11].get() != "" and \
                entries_numbers[16].get() != "" and entries_numbers[21].get() != "" and entries_numbers[26].get() != "":
            button_player1_up["state"] = "normal"
            button_player1_up["bg"] = "#C4F3FF"
        else:
            button_player1_up["state"] = "disabled"
            button_player1_up["bg"] = "#EDE8E8"
            entries_numbers[61].delete(0, tkinter.END)
            entries_numbers[61]["state"] = "disabled"

        if entries_numbers[2].get() != "" and entries_numbers[7].get() != "" and entries_numbers[12].get() != "" and \
                entries_numbers[17].get() != "" and entries_numbers[22].get() != "" and entries_numbers[27].get() != "":
            button_player1_up_down["state"] = "normal"
            button_player1_up_down["bg"] = "#C4F3FF"
        else:
            button_player1_up_down["state"] = "disabled"
            button_player1_up_down["bg"] = "#EDE8E8"
            entries_numbers[62].delete(0, tkinter.END)
            entries_numbers[62]["state"] = "disabled"

        if entries_numbers[3].get() != "" and entries_numbers[8].get() != "" and entries_numbers[13].get() != "" and \
                entries_numbers[18].get() != "" and entries_numbers[23].get() != "" and entries_numbers[28].get() != "":
            button_player1_free["state"] = "normal"
            button_player1_free["bg"] = "#C4F3FF"
        else:
            button_player1_free["state"] = "disabled"
            button_player1_free["bg"] = "#EDE8E8"
            entries_numbers[63].delete(0, tkinter.END)
            entries_numbers[63]["state"] = "disabled"

        if entries_numbers[4].get() != "" and entries_numbers[9].get() != "" and entries_numbers[14].get() != "" and \
                entries_numbers[19].get() != "" and entries_numbers[24].get() != "" and entries_numbers[29].get() != "":
            button_player1_served["state"] = "normal"
            button_player1_served["bg"] = "#C4F3FF"
        else:
            button_player1_served["state"] = "disabled"
            button_player1_served["bg"] = "#EDE8E8"
            entries_numbers[64].delete(0, tkinter.END)
            entries_numbers[64]["state"] = "disabled"

        '''player2'''
        if entries_numbers[30].get() != "" and entries_numbers[35].get() != "" and entries_numbers[40].get() != "" and \
                entries_numbers[45].get() != "" and entries_numbers[50].get() != "" and entries_numbers[55].get() != "":
            button_player2_down["state"] = "normal"
            button_player2_down["bg"] = "#C4F3FF"
        else:
            button_player2_down["state"] = "disabled"
            button_player2_down["bg"] = "#EDE8E8"
            entries_numbers[65].delete(0, tkinter.END)
            entries_numbers[65]["state"] = "disabled"

        if entries_numbers[31].get() != "" and entries_numbers[36].get() != "" and entries_numbers[41].get() != "" and \
                entries_numbers[46].get() != "" and entries_numbers[51].get() != "" and entries_numbers[56].get() != "":
            button_player2_up["state"] = "normal"
            button_player2_up["bg"] = "#C4F3FF"
        else:
            button_player2_up["state"] = "disabled"
            button_player2_up["bg"] = "#EDE8E8"
            entries_numbers[66].delete(0, tkinter.END)
            entries_numbers[66]["state"] = "disabled"

        if entries_numbers[32].get() != "" and entries_numbers[37].get() != "" and entries_numbers[42].get() != "" and \
                entries_numbers[47].get() != "" and entries_numbers[52].get() != "" and entries_numbers[57].get() != "":
            button_player2_up_down["state"] = "normal"
            button_player2_up_down["bg"] = "#C4F3FF"
        else:
            button_player2_up_down["state"] = "disabled"
            button_player2_up_down["bg"] = "#EDE8E8"
            entries_numbers[67].delete(0, tkinter.END)
            entries_numbers[67]["state"] = "disabled"

        if entries_numbers[33].get() != "" and entries_numbers[38].get() != "" and entries_numbers[43].get() != "" and \
                entries_numbers[48].get() != "" and entries_numbers[53].get() != "" and entries_numbers[58].get() != "":
            button_player2_free["state"] = "normal"
            button_player2_free["bg"] = "#C4F3FF"
        else:
            button_player2_free["state"] = "disabled"
            button_player2_free["bg"] = "#EDE8E8"
            entries_numbers[68].delete(0, tkinter.END)
            entries_numbers[68]["state"] = "disabled"

        if entries_numbers[34].get() != "" and entries_numbers[39].get() != "" and entries_numbers[44].get() != "" and \
                entries_numbers[49].get() != "" and entries_numbers[54].get() != "" and entries_numbers[59].get() != "":
            button_player2_served["state"] = "normal"
            button_player2_served["bg"] = "#C4F3FF"
        else:
            button_player2_served["state"] = "disabled"
            button_player2_served["bg"] = "#EDE8E8"
            entries_numbers[69].delete(0, tkinter.END)
            entries_numbers[69]["state"] = "disabled"

    def check_small_big_totals(self, entries_numbers, list_buttons):
        if entries_numbers[120].get() != "" and entries_numbers[125].get() != "":
            list_buttons[0]["state"] = "normal"
            list_buttons[0]["bg"] = "#C4F3FF"
        else:
            list_buttons[0]["text"] = ""
            list_buttons[0]["bg"] = "#f0f0f0"
            list_buttons[0]["state"] = "disabled"

        if entries_numbers[121].get() != "" and entries_numbers[126].get() != "":
            list_buttons[1]["state"] = "normal"
            list_buttons[1]["bg"] = "#C4F3FF"
        else:
            list_buttons[1]["text"] = ""
            list_buttons[1]["bg"] = "#f0f0f0"
            list_buttons[1]["state"] = "disabled"

        if entries_numbers[122].get() != "" and entries_numbers[127].get() != "":
            list_buttons[2]["state"] = "normal"
            list_buttons[2]["bg"] = "#C4F3FF"
        else:
            list_buttons[2]["text"] = ""
            list_buttons[2]["bg"] = "#f0f0f0"
            list_buttons[2]["state"] = "disabled"

        if entries_numbers[123].get() != "" and entries_numbers[128].get() != "":
            list_buttons[3]["state"] = "normal"
            list_buttons[3]["bg"] = "#C4F3FF"
        else:
            list_buttons[3]["text"] = ""
            list_buttons[3]["bg"] = "#f0f0f0"
            list_buttons[3]["state"] = "disabled"

        if entries_numbers[124].get() != "" and entries_numbers[129].get() != "":
            list_buttons[4]["state"] = "normal"
            list_buttons[4]["bg"] = "#C4F3FF"
        else:
            list_buttons[4]["text"] = ""
            list_buttons[4]["bg"] = "#f0f0f0"
            list_buttons[4]["state"] = "disabled"

        if entries_numbers[130].get() != "" and entries_numbers[135].get() != "":
            list_buttons[5]["state"] = "normal"
            list_buttons[5]["bg"] = "#C4F3FF"
        else:
            list_buttons[5]["text"] = ""
            list_buttons[5]["bg"] = "#f0f0f0"
            list_buttons[5]["state"] = "disabled"

        if entries_numbers[131].get() != "" and entries_numbers[136].get() != "":
            list_buttons[6]["state"] = "normal"
            list_buttons[6]["bg"] = "#C4F3FF"
        else:
            list_buttons[6]["text"] = ""
            list_buttons[6]["bg"] = "#f0f0f0"
            list_buttons[6]["state"] = "disabled"

        if entries_numbers[132].get() != "" and entries_numbers[137].get() != "":
            list_buttons[7]["state"] = "normal"
            list_buttons[7]["bg"] = "#C4F3FF"
        else:
            list_buttons[7]["text"] = ""
            list_buttons[7]["bg"] = "#f0f0f0"
            list_buttons[7]["state"] = "disabled"

        if entries_numbers[133].get() != "" and entries_numbers[138].get() != "":
            list_buttons[8]["state"] = "normal"
            list_buttons[8]["bg"] = "#C4F3FF"
        else:
            list_buttons[8]["text"] = ""
            list_buttons[8]["bg"] = "#f0f0f0"
            list_buttons[8]["state"] = "disabled"

        if entries_numbers[134].get() != "" and entries_numbers[139].get() != "":
            list_buttons[9]["state"] = "normal"
            list_buttons[9]["bg"] = "#C4F3FF"
        else:
            list_buttons[9]["text"] = ""
            list_buttons[9]["bg"] = "#f0f0f0"
            list_buttons[9]["state"] = "disabled"

    def totals_big_small_calculations(self, row, big_number, small_number, list_buttons):
        print("row: ", row, "big_number: ", big_number, "small_number: ", small_number, list_buttons)
        result = self.helper.calculate_totals_bs(row, int(big_number), int(small_number))
        #first disable everything in case it is again pressed by mistake
        list_buttons[row-1]["text"] = ""
        list_buttons[row - 1]["text"] = str(result)
        list_buttons[row - 1]["state"] = "disabled"

    def compute_colouring(self, list_entry, result, row_number):
        # first disable everything in case it is again pressed by mistake
        list_entry.delete(0, "end")
        list_entry["state"] = "normal"
        list_entry.insert(0, result)
        if row_number == 5 or row_number == 10:
            if result < self.helper.threshold * 2:
                list_entry["bg"] = "#A83B3C"
            elif 226 <= result <= 244:
                list_entry["bg"] = "#C1E5BE"
            elif result > 244:
                list_entry["bg"] = "#4D944B"
        else:
            if result < self.helper.threshold:
                list_entry["bg"] = "#A83B3C"
            elif 113 <= result <= 122:
                list_entry["bg"] = "#C1E5BE"
            elif result > 122:
                list_entry["bg"] = "#4D944B"

    def compute_totals(self, row_number, entries_numbers, *args):
        '''total entries start from index 60'''
        result = self.helper.calculate_totals(row_number, *args)
        # start writing
        if row_number == 1:
            self.compute_colouring(entries_numbers[60], result, row_number)
            button_player1_down["state"] = "disabled"
        if row_number == 2:
            self.compute_colouring(entries_numbers[61], result, row_number)
            button_player1_up["state"] = "disabled"
        if row_number == 3:
            self.compute_colouring(entries_numbers[62], result, row_number)
            button_player1_up_down["state"] = "disabled"
        if row_number == 4:
            self.compute_colouring(entries_numbers[63], result, row_number)
            button_player1_free["state"] = "disabled"
        if row_number == 5:
            self.compute_colouring(entries_numbers[64], result, row_number)
            button_player1_served["state"] = "disabled"
        if row_number == 6:
            self.compute_colouring(entries_numbers[65], result, row_number)
            button_player2_down["state"] = "disabled"
        if row_number == 7:
            self.compute_colouring(entries_numbers[66], result, row_number)
            button_player2_up["state"] = "disabled"
        if row_number == 8:
            self.compute_colouring(entries_numbers[67], result, row_number)
            button_player2_up_down["state"] = "disabled"
        if row_number == 9:
            self.compute_colouring(entries_numbers[68], result, row_number)
            button_player2_free["state"] = "disabled"
        if row_number == 10:
            self.compute_colouring(entries_numbers[69], result, row_number)
            button_player2_served["state"] = "disabled"

    def create_main_logic(self, window):
        # full labels and entries
        global label_full_result_normal
        global label_full_result_plus10
        global label_full_result_served
        global entry_dice_1
        global entry_dice_2
        # careu labels and entry
        global label_careu_result_normal
        global label_careu_result_plus10
        global label_careu_result_served
        global entry_dice_careu
        # yams labels and entry
        global label_yams_result_normal
        global label_yams_result_plus10
        global label_yams_result_served
        global entry_dice_yams
        # player names
        global entry_player1
        global entry_player2
        # global button players
        global button_player1_down
        global button_player1_up
        global button_player1_up_down
        global button_player1_free
        global button_player1_served
        global button_player2_down
        global button_player2_up
        global button_player2_up_down
        global button_player2_free
        global button_player2_served
        # label clock
        global label_clock
        #results button
        global results_button

        frame_game = LabelFrame(window, text="YAMS GAME", width=1500, height=850, cursor="spraycan", bg="#F2EBEB",
                                fg="#040A4A", relief="raised", font=("Georgia", 20, "bold"), labelanchor="n",
                                bd=5, borderwidth=5)
        frame_game.grid(row=0, column=0, padx=90, pady=20, sticky="nsew")
        # create frame for calculations
        frame_calculation = LabelFrame(frame_game, text="Calculations", width=400, height=700, cursor="spraycan",
                                       bg="#F2EBEB",
                                       fg="#040A4A", relief="ridge", font=("Georgia", 16, "bold"),
                                       labelanchor="n")
        frame_calculation.place(x=50, y=50)
        '''frame for full house'''
        frame_full = LabelFrame(frame_calculation, text="Full", width=350, height=150, cursor="spraycan", bg="#F2EBEB",
                                fg="#040A4A", relief="ridge", font=("Georgia", 12, "bold"), labelanchor="n")
        frame_full.place(x=20, y=20)
        label_dice1 = Label(frame_full, text="DICE1", bg="#F2EBEB", fg="#040A4A", font=("Arial", 10, "bold"),
                            justify="center", bd=2)
        label_dice1.place(x=20, y=30)
        entry_dice_1 = Entry(frame_full, fg="#912A3A", font=("Arial", 10, "bold"), bg="#BCDEE3", relief="raised",
                             justify="center", bd=1, width=6)
        entry_dice_1.place(x=80, y=30)
        label_dice2 = Label(frame_full, text="DICE2", bg="#F2EBEB", fg="#040A4A", font=("Arial", 10, "bold"),
                            justify="center", bd=2)
        label_dice2.place(x=20, y=80)
        entry_dice_2 = Entry(frame_full, fg="#912A3A", font=("Arial", 10, "bold"), bg="#BCDEE3", relief="raised",
                             justify="center", bd=1, width=6)
        entry_dice_2.place(x=80, y=80)
        button_conversion_full = Button(frame_full, text="CALCULATE", bg="#400F20", bd=5, fg="#F0F7E9", relief="raised",
                                        justify="center", font=("Arial", 8, "bold"), cursor="arrow", width="20",
                                        height="1",
                                        command=lambda: self.compute_full_logic(entry_dice_1.get(), entry_dice_2.get()))
        button_conversion_full.place(x=190, y=5)
        label_result_full = Label(frame_full, text="Normal", bg="#F2EBEB", fg="#040A4A", font=("Arial", 10, "bold"),
                                  justify="center", bd=2)
        label_result_full.place(x=200, y=40)
        label_result_full_10 = Label(frame_full, text="Normal_served", bg="#F2EBEB", fg="#040A4A",
                                     font=("Arial", 10, "bold"),
                                     justify="center", bd=2)
        label_result_full_10.place(x=200, y=70)
        label_result_full_served = Label(frame_full, text="Served", bg="#F2EBEB", fg="#040A4A",
                                         font=("Arial", 10, "bold"),
                                         justify="center", bd=2)
        label_result_full_served.place(x=200, y=100)
        label_full_result_normal = Label(frame_full, text="", bg="#F2EBEB", fg="#218A4F",
                                         font=("Arial", 10, "bold"),
                                         justify="center", bd=2)
        label_full_result_normal.place(x=310, y=40)
        label_full_result_plus10 = Label(frame_full, text="", bg="#F2EBEB", fg="#218A4F",
                                         font=("Arial", 10, "bold"),
                                         justify="center", bd=2)
        label_full_result_plus10.place(x=310, y=70)
        label_full_result_served = Label(frame_full, text="", bg="#F2EBEB", fg="#218A4F",
                                         font=("Arial", 10, "bold"),
                                         justify="center", bd=2)
        label_full_result_served.place(x=310, y=100)
        '''frame for straight'''
        frame_straight = LabelFrame(frame_calculation, text="Straight", width=350, height=150, cursor="spraycan",
                                    bg="#F2EBEB",
                                    fg="#040A4A", relief="ridge", font=("Georgia", 12, "bold"), labelanchor="n")
        frame_straight.place(x=20, y=180)
        frame_small_straight = LabelFrame(frame_straight, text="Small - 12345", width=150, height=100,
                                          cursor="spraycan", bg="#F2EBEB",
                                          fg="#040A4A", relief="ridge", font=("Georgia", 10, "bold"),
                                          labelanchor="n")
        frame_small_straight.place(x=15, y=20)
        frame_big_straight = LabelFrame(frame_straight, text="Big - 23456", width=150, height=100,
                                        cursor="spraycan", bg="#F2EBEB",
                                        fg="#040A4A", relief="ridge", font=("Georgia", 10, "bold"),
                                        labelanchor="n")
        frame_big_straight.place(x=180, y=20)
        # small straight
        label_normal_small_straight = Label(frame_small_straight, text="Normal", bg="#F2EBEB", fg="#040A4A",
                                            font=("Arial", 8, "bold"),
                                            justify="center", bd=2)
        label_normal_small_straight.place(x=10, y=10)
        label_normal_small_straight_10 = Label(frame_small_straight, text="Normal_served", bg="#F2EBEB", fg="#040A4A",
                                               font=("Arial", 8, "bold"),
                                               justify="center", bd=2)
        label_normal_small_straight_10.place(x=10, y=35)
        label_served_small_straight = Label(frame_small_straight, text="Served", bg="#F2EBEB", fg="#040A4A",
                                            font=("Arial", 8, "bold"),
                                            justify="center", bd=2)
        label_served_small_straight.place(x=10, y=60)

        label_result_straight_normal = Label(frame_small_straight, text=35, bg="#F2EBEB", fg="#218A4F",
                                             font=("Arial", 8, "bold"),
                                             justify="center", bd=2)
        label_result_straight_normal.place(x=120, y=10)
        label_result_straight_10 = Label(frame_small_straight, text="45", bg="#F2EBEB", fg="#218A4F",
                                         font=("Arial", 8, "bold"),
                                         justify="center", bd=2)
        label_result_straight_10.place(x=120, y=35)
        label_result_straight_served = Label(frame_small_straight, text="70", bg="#F2EBEB", fg="#218A4F",
                                             font=("Arial", 8, "bold"),
                                             justify="center", bd=2)
        label_result_straight_served.place(x=120, y=60)
        # big straight
        label_normal_big_straight = Label(frame_big_straight, text="Normal", bg="#F2EBEB", fg="#040A4A",
                                          font=("Arial", 8, "bold"),
                                          justify="center", bd=2)
        label_normal_big_straight.place(x=10, y=10)
        label_normal_big_straight_10 = Label(frame_big_straight, text="Normal_served", bg="#F2EBEB", fg="#040A4A",
                                             font=("Arial", 8, "bold"),
                                             justify="center", bd=2)
        label_normal_big_straight_10.place(x=10, y=35)
        label_served_big_straight = Label(frame_big_straight, text="Served", bg="#F2EBEB", fg="#040A4A",
                                          font=("Arial", 8, "bold"),
                                          justify="center", bd=2)
        label_served_big_straight.place(x=10, y=60)

        label_result_straight_big_normal = Label(frame_big_straight, text="50", bg="#F2EBEB", fg="#218A4F",
                                                 font=("Arial", 8, "bold"),
                                                 justify="center", bd=2)
        label_result_straight_big_normal.place(x=120, y=10)
        label_result_straight_big_10 = Label(frame_big_straight, text="60", bg="#F2EBEB", fg="#218A4F",
                                             font=("Arial", 8, "bold"),
                                             justify="center", bd=2)
        label_result_straight_big_10.place(x=120, y=35)
        label_result_straight_big_served = Label(frame_big_straight, text="100", bg="#F2EBEB", fg="#218A4F",
                                                 font=("Arial", 8, "bold"),
                                                 justify="center", bd=2)
        label_result_straight_big_served.place(x=120, y=60)
        '''frame for 4 of a kind'''
        frame_careu = LabelFrame(frame_calculation, text="4 Of A Kind", width=350, height=150, cursor="spraycan",
                                 bg="#F2EBEB", fg="#040A4A", relief="ridge", font=("Georgia", 12, "bold"),
                                 labelanchor="n")
        frame_careu.place(x=20, y=340)
        label_dice_careu = Label(frame_careu, text="DICE1", bg="#F2EBEB", fg="#040A4A", font=("Arial", 10, "bold"),
                                 justify="center", bd=2)
        label_dice_careu.place(x=20, y=50)
        entry_dice_careu = Entry(frame_careu, fg="#912A3A", font=("Arial", 10, "bold"), bg="#BCDEE3", relief="raised",
                                 justify="center", bd=1, width=6)
        entry_dice_careu.place(x=80, y=50)
        button_conversion_careu = Button(frame_careu, text="CALCULATE", bg="#400F20", bd=5, fg="#F0F7E9",
                                         relief="raised",
                                         justify="center", font=("Arial", 8, "bold"), cursor="arrow", width="20",
                                         height="1",
                                         command=lambda: self.compute_yams_careu_logic(entry_dice_careu.get(), 1))
        button_conversion_careu.place(x=190, y=5)
        label_careu_normal = Label(frame_careu, text="Normal", bg="#F2EBEB", fg="#040A4A", font=("Arial", 10, "bold"),
                                   justify="center", bd=2)
        label_careu_normal.place(x=200, y=40)
        label_careu_normal_10 = Label(frame_careu, text="Normal_served", bg="#F2EBEB", fg="#040A4A",
                                      font=("Arial", 10, "bold"),
                                      justify="center", bd=2)
        label_careu_normal_10.place(x=200, y=70)
        label_result_careu_served = Label(frame_careu, text="Served", bg="#F2EBEB", fg="#040A4A",
                                          font=("Arial", 10, "bold"),
                                          justify="center", bd=2)
        label_result_careu_served.place(x=200, y=100)
        label_careu_result_normal = Label(frame_careu, text="", bg="#F2EBEB", fg="#218A4F",
                                          font=("Arial", 10, "bold"),
                                          justify="center", bd=2)
        label_careu_result_normal.place(x=310, y=40)
        label_careu_result_plus10 = Label(frame_careu, text="", bg="#F2EBEB", fg="#218A4F",
                                          font=("Arial", 10, "bold"),
                                          justify="center", bd=2)
        label_careu_result_plus10.place(x=310, y=70)
        label_careu_result_served = Label(frame_careu, text="", bg="#F2EBEB", fg="#218A4F",
                                          font=("Arial", 10, "bold"),
                                          justify="center", bd=2)
        label_careu_result_served.place(x=310, y=100)
        '''frame for yams'''
        frame_yams = LabelFrame(frame_calculation, text="Yams", width=350, height=150, cursor="spraycan",
                                bg="#F2EBEB", fg="#040A4A", relief="ridge", font=("Georgia", 12, "bold"),
                                labelanchor="n")
        frame_yams.place(x=20, y=500)
        label_dice_yams = Label(frame_yams, text="DICE1", bg="#F2EBEB", fg="#040A4A", font=("Arial", 10, "bold"),
                                justify="center", bd=2)
        label_dice_yams.place(x=20, y=50)
        entry_dice_yams = Entry(frame_yams, fg="#912A3A", font=("Arial", 10, "bold"), bg="#BCDEE3", relief="raised",
                                justify="center", bd=1, width=6)
        entry_dice_yams.place(x=80, y=50)
        button_conversion_yams = Button(frame_yams, text="CALCULATE", bg="#400F20", bd=5, fg="#F0F7E9",
                                        relief="raised",
                                        justify="center", font=("Arial", 8, "bold"), cursor="arrow", width="20",
                                        height="1",
                                        command=lambda: self.compute_yams_careu_logic(entry_dice_yams.get(), 2))
        button_conversion_yams.place(x=190, y=5)
        label_yams_normal = Label(frame_yams, text="Normal", bg="#F2EBEB", fg="#040A4A", font=("Arial", 10, "bold"),
                                  justify="center", bd=2)
        label_yams_normal.place(x=200, y=40)
        label_yams_normal_10 = Label(frame_yams, text="Normal_served", bg="#F2EBEB", fg="#040A4A",
                                     font=("Arial", 10, "bold"),
                                     justify="center", bd=2)
        label_yams_normal_10.place(x=200, y=70)
        label_result_yams_served = Label(frame_yams, text="Served", bg="#F2EBEB", fg="#040A4A",
                                         font=("Arial", 10, "bold"),
                                         justify="center", bd=2)
        label_result_yams_served.place(x=200, y=100)
        label_yams_result_normal = Label(frame_yams, text="", bg="#F2EBEB", fg="#218A4F",
                                         font=("Arial", 10, "bold"),
                                         justify="center", bd=2)
        label_yams_result_normal.place(x=310, y=40)
        label_yams_result_plus10 = Label(frame_yams, text="", bg="#F2EBEB", fg="#218A4F",
                                         font=("Arial", 10, "bold"),
                                         justify="center", bd=2)
        label_yams_result_plus10.place(x=310, y=70)
        label_yams_result_served = Label(frame_yams, text="", bg="#F2EBEB", fg="#218A4F",
                                         font=("Arial", 10, "bold"),
                                         justify="center", bd=2)
        label_yams_result_served.place(x=310, y=100)
        '''
        Create the yams table
        '''
        frame_table = LabelFrame(frame_game, text="PLAY", width=560, height=700, cursor="spraycan",
                                 bg="#F2EBEB",
                                 fg="#040A4A", relief="ridge", font=("Georgia", 16, "bold"),
                                 labelanchor="n")
        frame_table.place(x=475, y=50)
        # put the entries
        entry_player1 = Entry(frame_table, fg="#8C1235", font=("Arial", 10, "bold"), bg="#BCDEE3", relief="raised",
                              justify="center", bd=1, width=35)
        entry_player1.insert(0, "P1")
        entry_player1.place(x=41, y=30)
        entry_player2 = Entry(frame_table, fg="#8C1235", font=("Arial", 10, "bold"), bg="#BCDEE3", relief="raised",
                              justify="center", bd=1, width=35)
        entry_player2.insert(0, "P2")
        entry_player2.place(x=290, y=30)
        # create clock
        label_time = Label(frame_table, fg="#000000", bg="#CCC8C8", font=("Arial", 12, "bold"), relief="groove",
                           justify="center", text="Time", width=4)
        label_time.place(x=10, y=5)
        label_clock = Label(frame_table, fg="#000000", bg="#CCC8C8", font=("Arial", 12, "bold"), relief="groove",
                            justify="center", text="00:00:00", width=8)
        label_clock.place(x=60, y=5)
        self.update_clock(label_clock)
        # create buttons start and stop
        button_start = Button(frame_table, fg="#000000", bg="#CCC8C8", font=("Arial", 8, "bold"), relief="groove",
                              justify="center", text="START", width=4,
                              command=self.start)
        button_start.place(x=210, y=5)
        button_pause = Button(frame_table, fg="#000000", bg="#CCC8C8", font=("Arial", 8, "bold"), relief="groove",
                              justify="center", text="STOP", width=4,
                              command=self.pause)
        button_pause.place(x=250, y=5)

        '''create first row with buttons'''
        button_start_yams = Button(frame_table, text="Yams", bg="#CFDBE3", bd=2, fg="#000000", border=2,
                                   justify="center", font=("Arial", 8, "bold"), cursor="arrow", width="5", height="1",
                                   relief="solid", state="disabled", )
        button_start_yams.place(x=0, y=50)
        button_player1_down = Button(frame_table, text=constans.ROW_NAMES[0], bg="#EDE8E8", bd=2, fg="#000000",
                                     border=2,
                                     justify="center", font=("Arial", 8, "bold"), cursor="arrow", width=6, height="1",
                                     relief="solid", state="disabled", anchor="n",
                                     command=lambda: self.compute_totals(
                                         1, entries_numbers, int(entries_numbers[0].get()),
                                         int(entries_numbers[5].get()),
                                         int(entries_numbers[10].get()), int(entries_numbers[15].get()),
                                         int(entries_numbers[20].get()),
                                         int(entries_numbers[25].get())))
        button_player1_down.place(x=43, y=50)
        button_player1_up = Button(frame_table, text=constans.ROW_NAMES[1], bg="#EDE8E8", bd=2, fg="#000000",
                                   border=2,
                                   justify="center", font=("Arial", 8, "bold"), cursor="arrow", width=6, height="1",
                                   relief="solid", state="disabled", anchor="center",
                                   command=lambda: self.compute_totals
                                   (2, entries_numbers, int(entries_numbers[1].get()), int(entries_numbers[6].get()),
                                    int(entries_numbers[11].get()), int(entries_numbers[16].get()),
                                    int(entries_numbers[21].get()),
                                    int(entries_numbers[26].get())))
        button_player1_up.place(x=90, y=50)
        button_player1_up_down = Button(frame_table, text=constans.ROW_NAMES[2], bg="#EDE8E8", bd=2, fg="#000000",
                                        border=2,
                                        justify="center", font=("Arial", 8, "bold"), cursor="arrow", width=6,
                                        height="1",
                                        relief="solid", state="disabled", anchor="center",
                                        command=lambda: self.compute_totals
                                        (3, entries_numbers, int(entries_numbers[2].get()),
                                         int(entries_numbers[7].get()),
                                         int(entries_numbers[12].get()), int(entries_numbers[17].get()),
                                         int(entries_numbers[22].get()),
                                         int(entries_numbers[27].get())))
        button_player1_up_down.place(x=140, y=50)
        button_player1_free = Button(frame_table, text=constans.ROW_NAMES[3], bg="#EDE8E8", bd=2, fg="#000000",
                                     border=2,
                                     justify="center", font=("Arial", 8, "bold"), cursor="arrow", width=6,
                                     height="1",
                                     relief="solid", state="disabled", anchor="center",
                                     command=lambda: self.compute_totals
                                     (4, entries_numbers, int(entries_numbers[3].get()), int(entries_numbers[8].get()),
                                      int(entries_numbers[13].get()), int(entries_numbers[18].get()),
                                      int(entries_numbers[23].get()),
                                      int(entries_numbers[28].get())))
        button_player1_free.place(x=190, y=50)
        button_player1_served = Button(frame_table, text=constans.ROW_NAMES[4], bg="#EDE8E8", bd=2, fg="#000000",
                                       border=2,
                                       justify="center", font=("Arial", 8, "bold"), cursor="arrow", width=6,
                                       height="1",
                                       relief="solid", state="disabled", anchor="center",
                                       command=lambda: self.compute_totals
                                       (5, entries_numbers, int(entries_numbers[4].get()),
                                        int(entries_numbers[9].get()),
                                        int(entries_numbers[14].get()), int(entries_numbers[19].get()),
                                        int(entries_numbers[24].get()),
                                        int(entries_numbers[29].get())))
        button_player1_served.place(x=238, y=50)
        # player2
        x_continuation = 289
        button_player2_down = Button(frame_table, text=constans.ROW_NAMES[0], bg="#EDE8E8", bd=2, fg="#000000",
                                     border=2,
                                     justify="center", font=("Arial", 8, "bold"), cursor="arrow", width=6, height="1",
                                     relief="solid", state="disabled", anchor="n",
                                     command=lambda: self.compute_totals
                                     (6, entries_numbers, int(entries_numbers[30].get()),
                                      int(entries_numbers[35].get()),
                                      int(entries_numbers[40].get()), int(entries_numbers[45].get()),
                                      int(entries_numbers[50].get()),
                                      int(entries_numbers[55].get())))
        button_player2_down.place(x=x_continuation, y=50)
        button_player2_up = Button(frame_table, text=constans.ROW_NAMES[1], bg="#EDE8E8", bd=2, fg="#000000",
                                   border=2,
                                   justify="center", font=("Arial", 8, "bold"), cursor="arrow", width=6, height="1",
                                   relief="solid", state="disabled", anchor="center",
                                   command=lambda: self.compute_totals
                                   (7, entries_numbers, int(entries_numbers[31].get()), int(entries_numbers[36].get()),
                                    int(entries_numbers[41].get()), int(entries_numbers[46].get()),
                                    int(entries_numbers[51].get()),
                                    int(entries_numbers[56].get())))
        button_player2_up.place(x=x_continuation + 50, y=50)
        button_player2_up_down = Button(frame_table, text=constans.ROW_NAMES[2], bg="#EDE8E8", bd=2, fg="#000000",
                                        border=2,
                                        justify="center", font=("Arial", 8, "bold"), cursor="arrow", width=6,
                                        height="1",
                                        relief="solid", state="disabled", anchor="center",
                                        command=lambda: self.compute_totals
                                        (8, entries_numbers, int(entries_numbers[32].get()),
                                         int(entries_numbers[37].get()),
                                         int(entries_numbers[42].get()), int(entries_numbers[47].get()),
                                         int(entries_numbers[52].get()),
                                         int(entries_numbers[57].get())))
        button_player2_up_down.place(x=x_continuation + 100, y=50)
        button_player2_free = Button(frame_table, text=constans.ROW_NAMES[3], bg="#EDE8E8", bd=2, fg="#000000",
                                     border=2,
                                     justify="center", font=("Arial", 8, "bold"), cursor="arrow", width=6,
                                     height="1",
                                     relief="solid", state="disabled", anchor="center",
                                     command=lambda: self.compute_totals
                                     (9, entries_numbers, int(entries_numbers[33].get()),
                                      int(entries_numbers[38].get()),
                                      int(entries_numbers[43].get()), int(entries_numbers[48].get()),
                                      int(entries_numbers[53].get()),
                                      int(entries_numbers[58].get())))
        button_player2_free.place(x=x_continuation + 150, y=50)
        button_player2_served = Button(frame_table, text=constans.ROW_NAMES[4], bg="#EDE8E8", bd=2, fg="#000000",
                                       border=2,
                                       justify="center", font=("Arial", 8, "bold"), cursor="arrow", width=6,
                                       height="1",
                                       relief="solid", state="disabled", anchor="center",
                                       command=lambda: self.compute_totals
                                       (10, entries_numbers, int(entries_numbers[34].get()),
                                        int(entries_numbers[39].get()),
                                        int(entries_numbers[44].get()), int(entries_numbers[49].get()),
                                        int(entries_numbers[54].get()),
                                        int(entries_numbers[59].get())))
        button_player2_served.place(x=x_continuation + 198, y=50)
        '''
        Creating column rows
        '''
        for i in range(0, len(constans.C0LUMN_NAMES)):
            if constans.C0LUMN_NAMES[i] == "T":
                button_column = Button(frame_table, text=constans.C0LUMN_NAMES[i], bg="#EDE8E8", bd=2, fg="#000000",
                                       border=2,
                                       justify="center", font=("Arial", 8, "bold"), cursor="arrow", width="5",
                                       height="2",
                                       relief="solid", state="disabled", anchor="center", )
                self.index_start_y += 38
                button_column.place(x=0, y=self.index_start_y)
            elif constans.C0LUMN_NAMES[i] == "Y":
                button_column = Button(frame_table, text=constans.C0LUMN_NAMES[i], bg="#EDE8E8", bd=2, fg="#000000",
                                       border=2,
                                       justify="center", font=("Arial", 8, "bold"), cursor="arrow", width="5",
                                       height="2",
                                       relief="solid", state="disabled", anchor="center", )
                self.index_start_y += 38
                button_column.place(x=0, y=self.index_start_y)
            else:
                if i == 0:
                    button_column = Button(frame_table, text=constans.C0LUMN_NAMES[i], bg="#EDE8E8", bd=2, fg="#000000",
                                           border=2,
                                           justify="center", font=("Arial", 8, "bold"), cursor="arrow", width="5",
                                           height="2",
                                           relief="solid", state="disabled", anchor="center", )
                    self.index_start_y += 25
                    button_column.place(x=0, y=self.index_start_y)
                else:
                    button_column = Button(frame_table, text=constans.C0LUMN_NAMES[i], bg="#EDE8E8", bd=2, fg="#000000",
                                           border=2,
                                           justify="center", font=("Arial", 8, "bold"), cursor="arrow", width="5",
                                           height="2",
                                           relief="solid", state="disabled", anchor="center", )
                    self.index_start_y += 38
                    button_column.place(x=0, y=self.index_start_y)
        '''create first entries'''
        entries_numbers = []
        # we have 5 rows and 6 columns -> i till 30

        x0 = 45
        y0 = 76  # self.index_start_y+38
        dx = 49
        dy = 38

        for i in range(30):
            row = i // 5
            col = i % 5

            globals()[f"entry_{i}"] = Entry(
                frame_table,
                bg="#ffffff",
                bd=2,
                fg="#000000",
                border=2,
                justify="center",
                font=("Arial", 8, "bold"),
                cursor="arrow",
                width=7,
                relief="raised",
            )
            # globals()[f"entry_{i}"].insert(0, str(i))
            x = x0 + col * dx
            y = y0 + row * dy
            entries_numbers.append(globals()[f"entry_{i}"])
            globals()[f"entry_{i}"].place(x=x, y=y, height=38)
            globals()[f"entry_{i}"].bind("<KeyRelease>", lambda event: self.check_entries(entries_numbers))

        '''player2'''
        # we have 5 rows and 6 columns -> i till 30

        x0 = 293.5
        y0 = 76  # self.index_start_y+38
        dx = 49
        dy = 38

        for i in range(0, 30):
            row = i // 5
            col = i % 5

            globals()[f"entry_{i + 30}"] = Entry(
                frame_table,
                bg="#ffffff",
                bd=2,
                fg="#000000",
                border=2,
                justify="center",
                font=("Arial", 8, "bold"),
                cursor="arrow",
                width=7,
                relief="raised",
            )
            x = x0 + col * dx
            y = y0 + row * dy
            entries_numbers.append(globals()[f"entry_{i + 30}"])
            globals()[f"entry_{i + 30}"].place(x=x, y=y, height=38)
            globals()[f"entry_{i + 30}"].bind("<KeyRelease>", lambda event: self.check_entries(entries_numbers))
        '''entries for totals'''
        x_start = 45
        y_start = 305
        # next entry is 63
        for i in range(0, 10):
            globals()[f"entry_{i + 63}"] = Entry(frame_table, bg="#EDE8E8", bd=2, fg="#000000", border=2,
                                                 justify="center", font=("Arial", 8, "bold"), cursor="arrow", width=7,
                                                 relief="solid", state="normal",
                                                 )
            globals()[f"entry_{i + 63}"].insert(0, str(i+63))
            globals()[f"entry_{i + 63}"].place(x=x_start, y=y_start, height=38)
            entries_numbers.append(globals()[f"entry_{i + 63}"])
            if i == 4:
                x_start += 53
            else:
                x_start += 49

        '''create lower games'''
        '''5 * 5 = 25'''
        # player1
        # index is at 70
        x0 = 45
        y0 = 343
        dx = 49
        dy = 38

        for i in range(25):
            row = i // 5
            col = i % 5
            if i >= 20:
                globals()[f"entry_{i + 70}"] = Entry(
                    frame_table,
                    bg="#F0F0F0",
                    bd=2,
                    fg="#000000",
                    border=2,
                    justify="center",
                    font=("Arial", 8, "bold"),
                    cursor="arrow",
                    width=7,
                    relief="solid",
                )
                x = x0 + col * dx
                y = y0 + row * dy
                globals()[f"entry_{i+70}"].insert(0, str(i+70))
                entries_numbers.append(globals()[f"entry_{i + 70}"])
                globals()[f"entry_{i + 70}"].place(x=x, y=y, height=38)
            else:
                globals()[f"entry_{i + 70}"] = Entry(
                    frame_table,
                    bg="#ffffff",
                    bd=2,
                    fg="#000000",
                    border=2,
                    justify="center",
                    font=("Arial", 8, "bold"),
                    cursor="arrow",
                    width=7,
                    relief="raised",
                )
                x = x0 + col * dx
                y = y0 + row * dy
                globals()[f"entry_{i + 70}"].insert(0, str(i + 70))
                entries_numbers.append(globals()[f"entry_{i + 70}"])
                globals()[f"entry_{i + 70}"].place(x=x, y=y, height=38)
        # player2
        # index is at 95
        x0 = 293.5
        y0 = 343
        dx = 49
        dy = 38
        for i in range(25):
            row = i // 5
            col = i % 5
            if i >= 20:
                globals()[f"entry_{i + 95}"] = Entry(
                    frame_table,
                    bg="#F0F0F0",
                    bd=2,
                    fg="#000000",
                    border=2,
                    justify="center",
                    font=("Arial", 8, "bold"),
                    cursor="arrow",
                    width=7,
                    relief="solid",
                )
                x = x0 + col * dx
                y = y0 + row * dy
                globals()[f"entry_{i+95}"].insert(0, str(i+95))
                entries_numbers.append(globals()[f"entry_{i + 95}"])
                globals()[f"entry_{i + 95}"].place(x=x, y=y, height=38)
            else:
                globals()[f"entry_{i + 95}"] = Entry(
                    frame_table,
                    bg="#ffffff",
                    bd=2,
                    fg="#000000",
                    border=2,
                    justify="center",
                    font=("Arial", 8, "bold"),
                    cursor="arrow",
                    width=7,
                    relief="raised",
                )
                x = x0 + col * dx
                y = y0 + row * dy
                globals()[f"entry_{i + 95}"].insert(0, str(i + 95))
                entries_numbers.append(globals()[f"entry_{i + 95}"])
                globals()[f"entry_{i + 95}"].place(x=x, y=y, height=38)
        '''small and bigs'''
        # player1
        # index is at 120
        # 5 *2=10
        x0 = 45
        y0 = 533
        dx = 49
        dy = 38

        for i in range(10):
            row = i // 5
            col = i % 5
            globals()[f"entry_{i + 120}"] = Entry(
                frame_table,
                bg="#ffffff",
                bd=2,
                fg="#000000",
                border=2,
                justify="center",
                font=("Arial", 8, "bold"),
                cursor="arrow",
                width=7,
                relief="raised",
            )
            x = x0 + col * dx
            y = y0 + row * dy
            globals()[f"entry_{i + 120}"].insert(0, str(i+120))
            entries_numbers.append(globals()[f"entry_{i + 120}"])
            globals()[f"entry_{i + 120}"].place(x=x, y=y, height=38)
            globals()[f"entry_{i + 120}"].bind("<KeyRelease>",
                                               lambda event: self.check_small_big_totals(entries_numbers,
                                                                                         list_buttons_totals))
        # player2
        # index is at 130
        # 5 *2=10
        x0 = 293.5
        y0 = 533
        dx = 49
        dy = 38

        for i in range(10):
            row = i // 5
            col = i % 5
            globals()[f"entry_{i + 130}"] = Entry(
                frame_table,
                bg="#ffffff",
                bd=2,
                fg="#000000",
                border=2,
                justify="center",
                font=("Arial", 8, "bold"),
                cursor="arrow",
                width=7,
                relief="raised",
            )
            x = x0 + col * dx
            y = y0 + row * dy
            globals()[f"entry_{i + 130}"].insert(0, str(i+130))
            entries_numbers.append(globals()[f"entry_{i + 130}"])
            globals()[f"entry_{i + 130}"].place(x=x, y=y, height=38)
            globals()[f"entry_{i + 130}"].bind("<KeyRelease>",
                                               lambda event: self.check_small_big_totals(entries_numbers,
                                                                                         list_buttons_totals))
        '''totals for big and small'''
        x_start = 42
        y_start = 607
        list_buttons_totals = list()

        # Button 0
        button_0 = Button(
            frame_table,
            bg="#F0F0F0", bd=2, fg="#000000", border=2,
            justify="center", font=("Arial", 8, "bold"),
            cursor="arrow", width=6, relief="solid",
            state="disabled", height=2, anchor="center",
            command=lambda: self.totals_big_small_calculations(1, entries_numbers[125].get(),
                                                               entries_numbers[120].get(), list_buttons_totals))
        button_0.place(x=x_start, y=y_start)
        list_buttons_totals.append(button_0)
        x_start += 49

        # Button 1
        button_1 = Button(
            frame_table,
            bg="#F0F0F0", bd=2, fg="#000000", border=2,
            justify="center", font=("Arial", 8, "bold"),
            cursor="arrow", width=6, relief="solid",
            state="disabled", height=2, anchor="center",
            command=lambda: self.totals_big_small_calculations(2, entries_numbers[126].get(),
                                                               entries_numbers[121].get(),
                                                               list_buttons_totals))
        button_1.place(x=x_start, y=y_start)
        list_buttons_totals.append(button_1)
        x_start += 49

        # Button 2

        button_2 = Button(
            frame_table,
            bg="#F0F0F0", bd=2, fg="#000000", border=2,
            justify="center", font=("Arial", 8, "bold"),
            cursor="arrow", width=6, relief="solid",
            state="disabled", height=2, anchor="center",
            command=lambda: self.totals_big_small_calculations(3, entries_numbers[127].get(),
                                                               entries_numbers[122].get(),
                                                               list_buttons_totals))
        button_2.place(x=x_start, y=y_start)
        list_buttons_totals.append(button_2)
        x_start += 49

        # Button 3
        button_3 = Button(
            frame_table,
            bg="#F0F0F0", bd=2, fg="#000000", border=2,
            justify="center", font=("Arial", 8, "bold"),
            cursor="arrow", width=6, relief="solid",
            state="disabled", height=2, anchor="center",
            command=lambda: self.totals_big_small_calculations(4, entries_numbers[128].get(),
                                                               entries_numbers[123].get(),
                                                               list_buttons_totals))
        button_3.place(x=x_start, y=y_start)
        list_buttons_totals.append(button_3)
        x_start += 49

        # Button 4
        button_4 = Button(
            frame_table,
            bg="#F0F0F0", bd=2, fg="#000000", border=2,
            justify="center", font=("Arial", 8, "bold"),
            cursor="arrow", width=6, relief="solid",
            state="disabled", height=2, anchor="center",
            command=lambda: self.totals_big_small_calculations(5, entries_numbers[129].get(),
                                                               entries_numbers[124].get(),
                                                               list_buttons_totals))
        button_4.place(x=x_start, y=y_start)
        list_buttons_totals.append(button_4)
        x_start += 53  # special case

        # Button 5
        button_5 = Button(
            frame_table,
            bg="#F0F0F0", bd=2, fg="#000000", border=2,
            justify="center", font=("Arial", 8, "bold"),
            cursor="arrow", width=6, relief="solid",
            state="disabled", height=2, anchor="center",
            command=lambda: self.totals_big_small_calculations(6, entries_numbers[135].get(),
                                                               entries_numbers[130].get(),
                                                               list_buttons_totals))
        button_5.place(x=x_start, y=y_start)
        list_buttons_totals.append(button_5)
        x_start += 49

        # Button 6
        button_6 = Button(
            frame_table,
            bg="#F0F0F0", bd=2, fg="#000000", border=2,
            justify="center", font=("Arial", 8, "bold"),
            cursor="arrow", width=6, relief="solid",
            state="disabled", height=2, anchor="center",
            command=lambda: self.totals_big_small_calculations(7, entries_numbers[136].get(),
                                                               entries_numbers[131].get(),
                                                               list_buttons_totals))
        button_6.place(x=x_start, y=y_start)
        list_buttons_totals.append(button_6)
        x_start += 49

        # Button 7
        button_7 = Button(
            frame_table,
            bg="#F0F0F0", bd=2, fg="#000000", border=2,
            justify="center", font=("Arial", 8, "bold"),
            cursor="arrow", width=6, relief="solid",
            state="disabled", height=2, anchor="center",
            command=lambda: self.totals_big_small_calculations(8, entries_numbers[137].get(),
                                                               entries_numbers[132].get(),
                                                               list_buttons_totals))
        button_7.place(x=x_start, y=y_start)
        list_buttons_totals.append(button_7)
        x_start += 49

        # Button 8
        button_8 = Button(
            frame_table,
            bg="#F0F0F0", bd=2, fg="#000000", border=2,
            justify="center", font=("Arial", 8, "bold"),
            cursor="arrow", width=6, relief="solid",
            state="disabled", height=2, anchor="center",
            command=lambda: self.totals_big_small_calculations(9, entries_numbers[138].get(),
                                                               entries_numbers[133].get(),
                                                               list_buttons_totals))
        button_8.place(x=x_start, y=y_start)
        list_buttons_totals.append(button_8)

        x_start += 49

        # Button 9
        button_9 = Button(
            frame_table,
            bg="#F0F0F0", bd=2, fg="#000000", border=2,
            justify="center", font=("Arial", 8, "bold"),
            cursor="arrow", width=6, relief="solid",
            state="disabled", height=2, anchor="center",
            command=lambda: self.totals_big_small_calculations(10, entries_numbers[139].get(),
                                                               entries_numbers[134].get(),
                                                               list_buttons_totals))

        button_9.place(x=x_start, y=y_start)
        list_buttons_totals.append(button_9)
        x_start += 49
        '''create button to finish game'''
        button_finish = Button(frame_table, text="FINISH GAME", bg="#B9F0C0", bd=2, fg="#000000",
                               relief="raised",
                               justify="center", font=("Arial", 10, "bold"), cursor="arrow", width="10",
                               height="1",
                               command=lambda: self.calculate_results(entries_numbers, list_buttons_totals))
        button_finish.place(x=245, y=645)

        '''create the frame for the results'''
        frame_calculation = LabelFrame(frame_game, text="Results", width=420, height=700, cursor="spraycan",
                                      bg="#F2EBEB",
                                      fg="#040A4A", relief="ridge", font=("Georgia", 16, "bold"),
                                      labelanchor="n")
        frame_calculation.place(x=1060, y=50)
        #add button results
        results_button = Button(frame_calculation, text="CHECK RESULTS",  fg="#000000", bg="#CCC8C8", bd=2,
                               relief="raised",
                               justify="center", font=("Arial", 10, "bold"), cursor="arrow", width="15",
                               height="2",state="disabled",command=lambda: self.insert_results(frame_calculation))
        results_button.place(x=frame_calculation["width"]/3-5, y=20) #~118



    def create_main_gui(self):
        root = Tk()
        root.title("Yams Game")
        root.geometry("1700x900")
        root.iconbitmap(self.ico_image)
        root["bg"] = "#F2EBEB"
        self.create_main_logic(root)
        root.resizable(False, False)
        root.mainloop()
