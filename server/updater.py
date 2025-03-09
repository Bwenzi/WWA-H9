# import schedule
import time
import get_data



def update_data():
    get_data.update()
    print('updated', time.strftime("%H:%M:%S"))

def main():
    update_data()
    #schedule.every().hour.at(":23").do(update_data)
    #print("update scheduled")
    #while True:
        #schedule.run_pending()
        #time.sleep(1)