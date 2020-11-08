#!/usr/bin/env python3

# COP2002.0M1 Programming Logic
# Module 11 Project 11-1 Arrival Time Estimator Program
# Submitted by Richard Ruth

# Program obtains date of departure, time of departure, miles to be travelled, and miles per hour data from user
#  and calculates and displays duration of travel, as well as estimated date of arrival and time of arrival

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    # Main module calls functions for obtaining user input, travel calculations, and displays output

    print("\nArrival Time Estimator\n")
    choice = "y"
    while choice.lower() == "y":
        departure_date = get_departure_date()
        departure_time = get_departure_time()
        miles = get_miles()
        mph = get_mph()

        # combine departure date and time for time span purposes

        departure_combined = departure_date + " " + departure_time
        departure_combined = datetime.strptime(departure_combined, "%Y-%m-%d %H:%M")
        travelTimeMinutes = calculate_travel_time(miles, mph)
        outputHours = int(travelTimeMinutes / 60)
        outputMinutes = int(travelTimeMinutes % 60)

        # calculate arrival date and time

        arrival_date = departure_combined + timedelta(minutes=travelTimeMinutes)

        # display output

        outputArrivalDate = arrival_date.strftime("%Y-%m-%d")
        outputArrivalTime = arrival_date.strftime("%I:%M %p")
        print("\nEstimated Travel Time")
        print("Hours: ", outputHours)
        print("Minutes: ", outputMinutes)
        print("Estimated date of arrival: ", str(outputArrivalDate))
        print("Estimated time of arrival: ", str(outputArrivalTime))
        print()
        choice = input("Continue? (y/n): ")
        print()


# Function get_departure_date obtains departure date input from user

def get_departure_date():
    date_str = input("Enter estimated date of departure (YYYY-MM-DD): ")
    departure_date = datetime.strptime(date_str, "%Y-%m-%d")
    departure_date = datetime.strftime(departure_date, "%Y-%m-%d")
    return departure_date


# Function get_departure_time obtains departure time input from user and converts to 24 hour format for time span calculation purposes

def get_departure_time():
    time_str = input("Enter estimated time of departure (HH:MM AM/PM): ")
    departure_time = datetime.strptime(time_str, "%I:%M %p")
    departure_time = datetime.strftime(departure_time, "%H:%M")
    return departure_time


# Function get_miles gets miles input from user

def get_miles():
    miles = int(input("Enter miles: "))
    return miles


# Function get_mph gets miles per hour input from user

def get_mph():
    mph = int(input("Enter miles per hour: "))
    return mph


# Function calculate_travel_time calculates travel time in minutes using miles and mph data

def calculate_travel_time(miles, mph):
    travelTimeMinutes = float((miles / mph * 60))
    return travelTimeMinutes


# If this module is the main module, call the main() function

if __name__ == "__main__":
    main()

