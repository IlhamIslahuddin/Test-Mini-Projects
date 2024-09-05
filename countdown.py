import time

def countdown():
    valid = False
    while valid == False:
        try:
            my_time = int(input("Enter the time for the countdown in seconds: "))
            valid = True
        except:
            print("Please input a whole number.")

    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60)
        hours = int(x / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
        print ("------------------------------")

if __name__ == "__main__":
    countdown()
