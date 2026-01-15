import json
import os
from termcolor import colored

class UserInfo:
    
    def __init__(self):
        self.USER_FILE = 'user_info.json'
    
    def get_info(self):
        if os.path.exists(self.USER_FILE):
            with open(self.USER_FILE, 'r') as info:
                data = json.load(info)
            print(colored(f"Welcome existing user. Loading preset with name {data['name']}.\n", 'green'))
            return data
        print(colored("Welcome new user!", 'green'))
        data = self._format_info(self._collect_info())
        print(colored("Your preset has been saved to user_info.json. Enjoy the plotter!\n", 'green'))
        return data
    
    def _format_info(self, data):
        with open(self.USER_FILE, 'w') as outfile:
            json.dump(data, outfile)
        return data

    def _collect_info(self):
        name = input("Please enter a username: ")
        print(colored(f"Welcome, {name}. It may be helpful to Google some of the following values.", 'yellow'))
        longitude = self._force_values('longitude', 'degrees East', -180, 180)
        latitude = self._force_values('latitude', 'degrees North', -90, 90)
        altitude = self._force_values('altitude', 'meters above sea level', -430, 6000)
        offset = self._force_values('offset', 'hours difference from UTC', -12, 14)
        
        return {'name':name, 'longitude':longitude, 'latitude':latitude, 'altitude':altitude, 'offset':offset}
    
    def _force_values(self, name, unit, low, high):
        while True:
            try:
                var = float(input(f"Enter your {name} in {unit} ({low} to {high}): "))
                assert low < var < high
            except ValueError:
                print(colored("Please enter a number.", 'red'))
            except AssertionError:
                print(colored(f"Please enter a number between {low} and {high}.", 'red'))
            else:
                break
        return var