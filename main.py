# (5 points): As a developer, I want to make at least three commits with descriptive messages. 
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists. 
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!


destinations = ["Boston", "New York City", "New Haven", "Hartford", "Albany"]

restaurants_boston = ["Sorellina", "Toro", "Ostra", "Stockyard"]
restaurants_new_york = ["Del Frisco's", "Per Se", "Cote", "Gramercy Tavern"]
restaurants_new_haven = ["Zinc", "Consiglio's", "Prime 16", "Olea"]
restaurants_hartford = ["Republic at The Linden", "The Capital Grille", "Feng Chophouse", "Sorella"]
restaurants_albany = ["Barcelona", "Black & Blue Steak and Crab", "Grappa '72", "Athos"]

modes_of_transportation = ["a car", "a bus", "a train", "walking"]

entertainment_boston = [" Go to a Red Sox game", "Go to a Celtics game", "Go to a Bruins game", "Walk the Freedom trail"]
entertainment_new_york = ["tour Ellis Island", "Visit 9/11 memorial", "Go to a Yankees game", "Just walk around the city"]
entertainment_new_haven = ["Visit the Yale Center for British Art", "Go to Harkness Tower", "Go to Long Wharf Park", "Visit Vietnam Memorial Park"]
entertainment_hartford = ["See a play at the Bushnell", "Go to a baseball game", "Take a ride on the carousel", "Visit the Wadworth Atheneum Museum"]
entertainment_albany = ["Visit the Albany Institute of History", "Visit craft breweries", "See the Schuyler Mansion", "Tour the USS Slater"]

import random





def location_picker(list):

    destination = random.choice(destinations)    
    valid_response = False
    print("Welcome to the Day Trip Generator! If you aren't sure what you want to do for your vacation, you have come to the right place!")
    print(f"We have selected",  random.choice(destinations) , "for your destination! Does this sound good?")
    user_response =  input("Enter y/n: ")
           
    if user_response == "y":
        print("Awesome! Glad that is decided. Let's move on!")
        valid_response = True
               
        
    while valid_response == False:
        
        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move on!")
            valid_response = True   
                        
        elif user_response == "n":
            print(f"oh, sorry you don't like this destination. No worries, we can try something else! How about", random.choice(destinations) + "?")
            user_response = input("Enter y/n: ")    
            
        else:
            print("")

location_picker(destinations)


def transportation_picker(list):
    valid_response = False
    print(f"We have selected", random.choice(modes_of_transportation), "for your transportation option! Does this sound good?")
    user_response = input("Enter y/n: ")

    if user_response == "y":
        print("Awesome! Glad that is decided. Let's move on!")
        valid_response = True

    while valid_response == False:

        if user_response =="y":
            print("Awesome! Glad that is decided. Let's move on!")
            valid_response = True
        elif user_response == "n":
            print(f"Oh, sorry you don't like that transportation. No worries, we can try something else! How about", random.choice(modes_of_transportation) + "?")
            user_response = input("Enter y/n: ")
        else:
            print("")
        
transportation_picker(modes_of_transportation)


def entertainment_boston(list):
    valid_response = False
    print(f"We have selected", random.choice(entertainment_boston), "for your entertainment option! Does this sound good?")
    user_response = input("Enter y/n: ")

    if user_response == "y":
        print("Awesome! Glad that is decided. Let's move on!")
        valid_respone = True

    while valid_response == False:

        if user_response =="y":
            print("Awesome! Glad that is decided. Let's move on!")
            valid_response = True
        elif user_response == "n":
            print(f"Oh, sorry you don't like that entertainment. No worries, we can try something else! How about", random.choice(entertainment_boston) + "?")
            user_response = input("Enter y/n: ")
        else:
            print("")
    