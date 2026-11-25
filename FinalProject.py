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
    #This function calculates the amount of free time the user has left
def  calculate_free_time(totalHours):
    freeTime= 168-totalHours
    
    return freeTime
     #This function gives scheduling advice to the user
def give_advice(freeTime):
    if freeTime <0:
       return "Your schedule is overloaded!!"
    elif freeTime<= 10:
       return "You have a very busy schedule."
    elif freeTime<= 25:
        return "You have a moderately busy schedule."
    else:
        return "You have a good amount of free time!"

print("Welcome to the Student Weekly Schedule Tracker!")
#"yes" is the what i have assigned to the while loop statemnt to make it true
again = "yes"
#This means if the statement is true then restart the program for the user
while again == "yes":
   #Collect and validate weekly hours for each activity
   workHours = get_valid_hours("work")
   classHours = get_valid_hours("class")
   studyHours = get_valid_hours("study")
   sleepHours = get_valid_hours("sleep")

   #store collected scheduled hours in a list
   weeklyHours = [workHours,classHours,studyHours,sleepHours]

   #call functions to calculate hours and give advice
   totalHours = calculate_total_hours(weeklyHours)
   freeTime = calculate_free_time(totalHours)
   advice = give_advice(freeTime)

   #Display the student's weekly schedule results
   print(f"Total scheduled hours:{totalHours}")
   print(f"Remaining free hours:{freeTime}")
   print(advice)
   #This is where the user decides if they want to restart or not
   again = input("Would you like to try again? (yes/no)")
#If the while loop condition is false then print this to the user
print("Thank you for using the Student Weekly Schedule Tracker!")