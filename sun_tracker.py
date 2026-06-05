from pysolar.solar import get_altitude,get_azimuth
class SunTracker:
    def calculate(self,lat,lon,dt):
        return get_azimuth(lat,lon,dt), get_altitude(lat,lon,dt)
