from os import environ
from json import dumps
def get_input():
    OUT_PATH = None
    TXST_CALENDAR = None

    while not TXST_CALENDAR:
        TXST_CALENDAR = input("\nEnter URL for TXST Academic Calendar \n"
                              "(press Enter to use default:"
       "https://www.registrar.txst.edu/registration/ac/academic-calendar.html)\n"
                              )
        if TXST_CALENDAR == "":
            TXST_CALENDAR = "https://www.registrar.txst.edu/registration/ac/academic-calendar.html"

    while not OUT_PATH:
        home = environ["HOMEDRIVE"]+environ['HOMEPATH']

        OUT_PATH = input("\nEnter file path where you want the output stored.\n"
                         f"(press Enter to use default:{home})")
        if OUT_PATH == "":
            OUT_PATH = home

    file = open('files/config.json', 'w')
    json = dumps({"TXST_CALENDAR": TXST_CALENDAR, "OUT_PATH":OUT_PATH})
    file.write(json)
    file.close()

if __name__ == "__main__":
    get_input()
