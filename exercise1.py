# Created by:henry david caicedo
# Group:
# Date: oct 3
# Topic, problem, theme:

#Definiing the function (is the process)
def determine_color_traffic_light(light):
    """
    Determines the what to do depending of the color of the traffic light
    
    Args:
        light (str): the color of the light
    
    Returns:
        str: The action you´re should do
    """
    if light == "green":
        return "pass, you have kinda half a minute"
    elif light == "yellow":
        return "wait, maybe it just remain 5 seconds"
    elif light == "red":
        return "stop over there, wait 40 second until it ´comes yellow"
    else:
        return "ah ah ah tf your doing"

# Main program
# The user enters the information, calls the function and display the results

print("=== Color traffic light determiner ===")
print("This program will tell you, depending of the color of the light what to do!")
print()

# Get color from user
light = str(input("Please enter color of the traffic light:"))

# Determine and display the light color
light_color = determine_color_traffic_light(light)

print(f"\nThe color is {light}, you should {light_color}")


# Add some encouraging messages
# This section is alternative but adds information to the user.
# This section is added by advanced students.

if light == "pass, you have kinda half a minute":
    print("pass, you have kinda half a minute")
elif light == "wait, maybe it just remain 5 seconds":
    print("wait, maybe it just remain 5 seconds")
elif light == "stop over there, wait 40 second until it ´comes yellow":
    print("stop over there, wait 40 second until it ´comes yellow")
else:
    print()
