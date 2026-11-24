#Get valid activity hours from user
def get_valid_hours(activity):
    #User inputs hours based on the  activity variable that calls the function
    hours=int(input(f"Enter your weekly {activity} hours:"))
#while loop to allow user restart incase of wrong input
    while hours< 0 or hours > 168 :
        print("Invalid hours! Try again.")
        hours=int(input(f"Enter your weekly {activity} hours:"))

    return hours
    #Calculate the sum of activity hours entered by the user
def calculate_total_hours(weeklyHours):
    total = 0
    #for loop to iterate between the "weeklyHours" list
    for hour in  weeklyHours:
        total=total+hour
    
    return total
    #This function calculates the amount of free time we have left
def  calculate_free_time(totalHours):
    freeTime= 168-totalHours
    
    return freeTime
     #This function gives scheduling advice
def give_advice(freeTime):
    if freeTime <0:
       return "Your schedule is overloaded!!"
    elif freeTime<= 10:
       return "You have a very busy schedule."
    elif freeTime<= 25:
        return "You have a moderately busy schedule."
    else:
        return "You have a good amount of free time!"


freeTime= 50
advice=give_advice(freeTime)
print(advice)