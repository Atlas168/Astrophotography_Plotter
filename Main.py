import astropy.units as u
from astropy.coordinates import EarthLocation
from RequestManager import RequestManager
from UserInfo import UserInfo

'''
    CREATED BY: BEVERLY BIALKE
    CREATED ON: 29 JUNE 2025
                            '''

uinfo = UserInfo()

data = uinfo.get_info()

latitude = float(data['latitude'])
longitude = float(data['longitude'])
altitude = float(data['altitude'])
offset = float(data['offset'])

location = EarthLocation(lat=latitude*u.deg, lon=longitude*u.deg, height=altitude*u.m)

rm = RequestManager(offset, location)

rm.plot()
