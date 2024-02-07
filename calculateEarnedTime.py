def calculateTime():
    minute = int(input("Minute :"))
    second = int(input("Second :"))
    speed = float(input("Speed :"))

    total_second = (minute * 60) + second

    final_time = total_second / speed
    new_minute = final_time // 60
    new_second = final_time % 60

    print("Current second " + str(new_second))
    print("Current minute " + str(new_minute))
    print("Earned : "+ (minute - new_minute)+" minute "+ (second-new_second)+" second" )


while True:
    calculateTime()
