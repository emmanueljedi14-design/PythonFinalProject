#Get valid activity hours from user
def get_valid_hours(activity):
    #User inputs hours based on the  activity variable that calls the function
    hours=int(input(f"Enter your weekly {activity} hours:"))
#while loop to allow user restart incase of wrong input
    while hours< 0 or hours > 168 :
        print("Invalid hours! Try again.")
        hours=int(input(f"Enter your weekly {activity} hours:"))

    return hours
     