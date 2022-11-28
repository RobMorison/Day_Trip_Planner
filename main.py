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

entertainment_boston = ["going to a Red Sox game", "going to a Celtics game", "going to a Bruins game", "walking the Freedom trail"]
entertainment_new_york = ["touring Ellis Island", "visiting 9/11 memorial", "going to a Yankees game", "just walking around the city"]
entertainment_new_haven = ["visiting the Yale Center for British Art", "going to Harkness Tower", "going to Long Wharf Park", "visiting Vietnam Memorial Park"]
entertainment_hartford = ["seeing a play at the Bushnell", "going to a baseball game", "taking a ride on the carousel", "visiting the Wadworth Atheneum Museum"]
entertainment_albany = ["visiting the Albany Institute of History", "visiting craft breweries", "seeing the Schuyler Mansion", "touring the USS Slater"]

import random





def location_picker(list):
    location = random.choice(destinations) 
    valid_response = False
    print("Welcome to the Day Trip Generator! If you aren't sure what you want to do for your vacation, you have come to the right place!")
    print(f"We have selected",  location , "for your destination! Does this sound good?")(input("Enter y/n:"))
    user_response =  input("Enter y/n: ")
           

    if user_response == "y":
        print("Awesome! Glad that is decided. Let's move on!")
        valid_response = True
        return location
               
        
    while valid_response == False:
        
        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move on!")
            valid_response = True  
            return location 
                        
        elif user_response == "n":
            location = random.choice(destinations)
            print(f"oh, sorry you don't like this destination. No worries, we can try something else! How about", location + "?")
            user_response = input("Enter y/n: ")  
              
         
        else:
            location = random.choice(destinations)
            print(f"oh, sorry you don't like this destination. No worries, we can try something else! How about", location + "?")
            user_response = input("Enter y/n: ") 

destination = location_picker(destinations)


def transportation_picker(list):
    select_transportation = random.choice(modes_of_transportation)
    valid_response = False
    print(f"We have selected", select_transportation , "for your transportation option! Does this sound good?")
    user_response = input("Enter y/n: ")

    if user_response == "y":
        print("Awesome! Glad that is decided. Let's move on!")
        valid_response = True
        return select_transportation

    while valid_response == False:

        if user_response =="y":
            print("Awesome! Glad that is decided. Let's move on!")
            valid_response = True
            return select_transportation
        elif user_response == "n":
            select_transportation = random.choice(modes_of_transportation)
            print(f"Oh, sorry you don't like that transportation. No worries, we can try something else! How about", select_transportation + "?")
            user_response = input("Enter y/n: ")

        else:
            select_transportation = random.choice(modes_of_transportation)
            print(f"Oh, sorry you don't like that transportation. No worries, we can try something else! How about", select_transportation + "?")
            user_response = input("Enter y/n: ")

        
transportation = transportation_picker(modes_of_transportation)

def entertainment_picker (list, list_one, list_two, list_three, list_four):

    while destination == "Boston":
        boston_entertainment = random.choice(entertainment_boston)
        valid_response = False
        print("We have selected", boston_entertainment, " for your entertainment option! Does this sounds good?")
        user_response = input("Enter y/n: ")

        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move one!")
            valid_response = True
            return boston_entertainment

        while valid_response == False:
            if user_response == "y":
                print("Awesome! Glad that is decided. Let's move one!")
                valid_response = True
                return boston_entertainment
            elif user_response == "n":
                boston_entertainment = random.choice(entertainment_boston)
                print(f"Oh, sorry you don't like that entertainment. No worries, we can try something else! How about", boston_entertainment + "?")
                user_response = input("Enter y/n: ")
            else:
                boston_entertainment = random.choice(entertainment_boston)
                print(f"Oh, sorry you don't like that entertainment. No worries, we can try something else! How about", boston_entertainment + "?")
                user_response = input("Enter y/n: ")
    
    while destination == "New York City":
        new_york_entertainment = random.choice(entertainment_new_york)
        valid_response = False
        print("We have selected", new_york_entertainment, " for your entertainment option! Does this sounds good?")
        user_response = input("Enter y/n: ")

        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move one!")
            valid_response = True
            return new_york_entertainment

        while valid_response == False:
            if user_response == "y":
                print("Awesome! Glad that is decided. Let's move one!")
                valid_response = True
                return new_york_entertainment
            elif user_response == "n":
                new_york_entertainment = random.choice(entertainment_new_york)
                print(f"Oh, sorry you don't like that entertainment. No worries, we can try something else! How about", new_york_entertainment + "?")
                user_response = input("Enter y/n: ")
            else:
                new_york_entertainment = random.choice(entertainment_new_york)
                print(f"Oh, sorry you don't like that entertainment. No worries, we can try something else! How about", new_york_entertainment + "?")
                user_response = input("Enter y/n: ")
    
    while destination == "New Haven":
        new_haven_entertainment = random.choice(entertainment_new_haven)
        valid_response = False
        print("We have selected", new_haven_entertainment, " for your entertainment option! Does this sounds good?")
        user_response = input("Enter y/n: ")

        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move one!")
            valid_response = True
            return new_haven_entertainment

        while valid_response == False:
            if user_response == "y":
                print("Awesome! Glad that is decided. Let's move one!")
                valid_response = True
                return new_haven_entertainment
            elif user_response == "n":
                new_haven_entertainment = random.choice(entertainment_new_haven)
                print(f"Oh, sorry you don't like that entertainment. No worries, we can try something else! How about", new_haven_entertainment + "?")
                user_response = input("Enter y/n: ")
            else:
                new_haven_entertainment = random.choice(entertainment_new_haven)
                print(f"Oh, sorry you don't like that entertainment. No worries, we can try something else! How about", new_haven_entertainment + "?")
                user_response = input("Enter y/n: ")

    while destination == "Hartford":
        hartford_entertainment = random.choice(entertainment_hartford)
        valid_response = False
        print("We have selected", hartford_entertainment, " for your entertainment option! Does this sounds good?")
        user_response = input("Enter y/n: ")

        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move one!")
            valid_response = True
            return hartford_entertainment

        while valid_response == False:
            if user_response == "y":
                print("Awesome! Glad that is decided. Let's move one!")
                valid_response = True
                return hartford_entertainment
            elif user_response == "n":
                hartford_entertainment = random.choice(entertainment_hartford)
                print(f"Oh, sorry you don't like that entertainment. No worries, we can try something else! How about", hartford_entertainment + "?")
                user_response = input("Enter y/n: ")
            else:
                hartford_entertainment = random.choice(entertainment_hartford)
                print(f"Oh, sorry you don't like that entertainment. No worries, we can try something else! How about", hartford_entertainment + "?")
                user_response = input("Enter y/n: ")
    
    while destination == "Albany":
        albany_entertainment = random.choice(entertainment_albany)
        valid_response = False
        print("We have selected", albany_entertainment, " for your entertainment option! Does this sounds good?")
        user_response = input("Enter y/n: ")

        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move one!")
            valid_response = True
            return albany_entertainment

        while valid_response == False:
            if user_response == "y":
                print("Awesome! Glad that is decided. Let's move one!")
                valid_response = True
                return albany_entertainment
            elif user_response == "n":
                albany_entertainment = random.choice(entertainment_albany)
                print(f"Oh, sorry you don't like that entertainment. No worries, we can try something else! How about", albany_entertainment + "?")
                user_response = input("Enter y/n: ")
            else:
                albany_entertainment = random.choice(entertainment_albany)
                print(f"Oh, sorry you don't like that entertainment. No worries, we can try something else! How about", albany_entertainment + "?")
                user_response = input("Enter y/n: ")

entertainment = entertainment_picker(entertainment_new_haven, entertainment_albany, entertainment_boston, entertainment_hartford, entertainment_new_york)

def restaurant_picker (list, list_one, list_two, list_three, list_four):

    while destination == "Boston":
        boston_restaurant = random.choice(restaurants_boston)
        valid_response = False
        print("We have selected", boston_restaurant , " for your dining option! Does this sounds good?")
        user_response = input("Enter y/n: ")

        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move one!")
            valid_response = True
            return boston_restaurant

        while valid_response == False:
            if user_response == "y":
                print("Awesome! Glad that is decided. Let's move one!")
                valid_response = True
                return boston_restaurant
            elif user_response == "n":
                boston_restaurant = random.choice(restaurants_boston)
                print(f"Oh, sorry you don't like that restaurant. No worries, we can try something else! How about", boston_restaurant + "?")
                user_response = input("Enter y/n: ")
            else:
                boston_restaurant = random.choice(restaurants_boston)
                print(f"Oh, sorry you don't like that restaurant. No worries, we can try something else! How about", boston_restaurant + "?")
                user_response = input("Enter y/n: ")
    
    while destination == "New York City":
        new_york_restaurant = random.choice(restaurants_new_york)
        valid_response = False
        print("We have selected", new_york_restaurant, " for your dining option! Does this sounds good?")
        user_response = input("Enter y/n: ")

        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move one!")
            valid_response = True
            return new_york_restaurant

        while valid_response == False:
            if user_response == "y":
                print("Awesome! Glad that is decided. Let's move one!")
                valid_response = True
                return new_york_restaurant
            elif user_response == "n":
                new_york_restaurant = random.choice(restaurants_new_york)
                print(f"Oh, sorry you don't like that restaurant. No worries, we can try something else! How about", new_york_restaurant + "?")
                user_response = input("Enter y/n: ")
            else:
                new_york_restaurant = random.choice(restaurants_new_york)
                print(f"Oh, sorry you don't like that restaurant. No worries, we can try something else! How about", new_york_restaurant + "?")
                user_response = input("Enter y/n: ")
    
    while destination == "New Haven":
        new_haven_restaurant = random.choice(restaurants_new_haven)
        valid_response = False
        print("We have selected", new_haven_restaurant, " for your dining option! Does this sounds good?")
        user_response = input("Enter y/n: ")

        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move one!")
            valid_response = True
            return new_haven_restaurant

        while valid_response == False:
            if user_response == "y":
                print("Awesome! Glad that is decided. Let's move one!")
                valid_response = True
                return new_haven_restaurant
            elif user_response == "n":
                new_haven_restaurant = random.choice(restaurants_new_haven)
                print(f"Oh, sorry you don't like that restaurant. No worries, we can try something else! How about", new_haven_restaurant + "?")
                user_response = input("Enter y/n: ")
            else:
                new_haven_restaurant = random.choice(restaurants_new_haven)
                print(f"Oh, sorry you don't like that restaurant. No worries, we can try something else! How about", new_haven_restaurant + "?")
                user_response = input("Enter y/n: ")

    while destination == "Hartford":
        hartford_restaurant = random.choice(restaurants_hartford)
        valid_response = False
        print("We have selected", hartford_restaurant, " for your dining option! Does this sounds good?")
        user_response = input("Enter y/n: ")

        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move one!")
            valid_response = True
            return hartford_restaurant

        while valid_response == False:
            if user_response == "y":
                print("Awesome! Glad that is decided. Let's move one!")
                valid_response = True
                return hartford_restaurant
            elif user_response == "n":
                hartford_restaurant = random.choice(restaurants_hartford)
                print(f"Oh, sorry you don't like that restaurant. No worries, we can try something else! How about", hartford_restaurant + "?")
                user_response = input("Enter y/n: ")
            else:
                hartford_restaurant = random.choice(restaurants_hartford)
                print(f"Oh, sorry you don't like that restaurant. No worries, we can try something else! How about", hartford_restaurant + "?")
                user_response = input("Enter y/n: ")
    
    while destination == "Albany":
        albany_restaurant = random.choice(restaurants_albany)
        valid_response = False
        print("We have selected", albany_restaurant, " for your dining option! Does this sounds good?")
        user_response = input("Enter y/n: ")

        if user_response == "y":
            print("Awesome! Glad that is decided. Let's move one!")
            valid_response = True
            return albany_restaurant

        while valid_response == False:
            if user_response == "y":
                print("Awesome! Glad that is decided. Let's move one!")
                valid_response = True
                return albany_restaurant
            elif user_response == "n":
                albany_restaurant = random.choice(restaurants_albany)
                print(f"Oh, sorry you don't like that restaurant. No worries, we can try something else! How about", albany_restaurant + "?")
                user_response = input("Enter y/n: ")
            else:
                albany_restaurant = random.choice(restaurants_albany)
                print(f"Oh, sorry you don't like that restaurant. No worries, we can try something else! How about", albany_restaurant + "?")
                user_response = input("Enter y/n: ")

restaurants = restaurant_picker(restaurants_new_haven, restaurants_albany, restaurants_boston, restaurants_hartford, restaurants_new_york)

print("The trip we have generated for you is:")
print(f"Destination: " , destination)
print(f"Transportaion: ", transportation)
print(f"Entertainment: ", entertainment)
print(f"Restaurant: ", restaurants)
print("Would you like to finalize this trip?")
input("Enter y/n: ")
print(f"Prepare for your dream vacation to come alive! You will be arriving in", destination +" by", transportation + ", where you will spend the day", entertainment + ". You will end the evening dining in style at", restaurants)

