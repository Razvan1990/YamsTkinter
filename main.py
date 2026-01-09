from gui.app_gui import GuiCreator


def compute_logic():
    gui = GuiCreator()
    gui.create_main_gui()

if __name__ == "__main__":
    compute_logic()