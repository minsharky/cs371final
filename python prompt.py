import sys
import os
import base64
import re

from configparser import ConfigParser


############################################################
#
# classes
#
def prompt():
  """
  Prompts the user and returns the command number

  Parameters
  ----------
  None

  Returns
  -------
  Command number entered by user (0, 1, 2, ...)
  """
  print()
  print(">> Enter a command:")
  print("   0 => exit app")
  print("   1 => add location")
  print("   2 => get all locations")
  print("   3 => get unrated locations")
  print("   4 => rate location")
  print("   5 => calculate itinerary")
  print("   6 => end session")

  cmd = input()

  if cmd == "":
    cmd = -1
  elif not cmd.isnumeric():
    cmd = -1
  else:
    cmd = int(cmd)

  return cmd

############################################################
# main
#

print('** Welcome to Trip Planner App **')
print()

# eliminate traceback so we just get error message:
sys.tracebacklimit = 0

#
# what config file should we use for this session?
#
config_file = 'client-config.ini'

#
# setup base URL to web service:
#
configur = ConfigParser()
configur.read(config_file)
baseurl = configur.get('client', 'webservice')

lastchar = baseurl[len(baseurl) - 1]
if lastchar == "/":
baseurl = baseurl[:-1]

#
# main processing loop:
#

# handle user sign in or create new user
username = sign_in_or_create_user(baseurl)

cmd = prompt()

while cmd != 0:
if cmd == 1:
    # add-location
    location_name = input("Enter location name> ").strip().lower()
    cost = input("Enter cost of this activity> ")
    try:
    cost = float(cost)
    except ValueError:
    print("Invalid cost, cost can only be numeric value.")
    continue
    add_location(baseurl, location_name, cost, username)

elif cmd == 2:
    # get-locations
    get_locations(baseurl)

elif cmd == 3:
    # get-unrated-locations
    get_unrated_locations(baseurl, username)

elif cmd == 4:
    # add-rating
    location_name = input("Enter location name> ").strip().lower()
    rating = input("Enter your rating for this location/activity (0~5)> ")
    try:
    rating = float(rating)
    except ValueError:
    print("Invalid rating, rating can only be numeric value.")
    continue
    add_rating(baseurl, location_name, rating, username)

elif cmd == 5:
    # calculate itinerary
    num_locations = int(input("Enter the number of locations to visit> "))
    if num_locations <= 0:
    print(
        "Invalid number of locations, number of locations must be greater than 0. Restarting calculate itinerary..."
    )
    continue
    max_total_cost = int(
        input("Enter your maximum budget for the entire trip> "))
    if max_total_cost < 0:
    print(
        "Invalid maximum budget, maximum budget must be non-negative. Restarting calculate itinerary..."
    )
    continue
    calculate_itinerary(baseurl, num_locations, max_total_cost)

elif cmd == 6:
    reset(baseurl)
    print()
    print(
        "*** Thanks for using Trip Planner App! Hope to see you again! :) ***"
    )
    sys.exit(0)

else:
    print("** Unknown command, try again...")

cmd = prompt()

#
# done
#
print()
print('** done **')
sys.exit(0)
