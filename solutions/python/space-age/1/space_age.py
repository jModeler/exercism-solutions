class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.orbital_periods = {
            "Mercury": 0.2408467,                     
            "Venus": 0.61519726,                    
            "Earth": 1.0,                     
            "Mars": 1.8808158,                     
            "Jupiter": 11.862615,                     
            "Saturn": 29.447498,                     
            "Uranus": 84.016846,                     
            "Neptune": 164.79132  
        }
        self.earth_days = 365.25
        self.earth_day_seconds = 86400

    def earth_age(self):
        "To provide pre rounded earth age"
        age = self.seconds/(self.earth_days * self.earth_day_seconds)
        return age

    def on_earth(self):
        age = self.earth_age()
        age = round(age, 2)
        return age 
    
    def on_mercury(self):
        age = self.earth_age()
        age = round(age/self.orbital_periods["Mercury"], 2)
        return age

    def on_venus(self):
        age = self.earth_age()
        age = round(age/self.orbital_periods["Venus"], 2)
        return age

    def on_mars(self):
        age = self.earth_age()
        age = round(age/self.orbital_periods["Mars"], 2)
        return age

    def on_jupiter(self):
        age = self.earth_age()
        age = round(age/self.orbital_periods["Jupiter"], 2)
        return age

    def on_saturn(self):
        age = self.earth_age()
        age = round(age/self.orbital_periods["Saturn"], 2)
        return age

    def on_uranus(self):
        age = self.earth_age()
        age = round(age/self.orbital_periods["Uranus"], 2)
        return age

    def on_neptune(self):
        age = self.earth_age()
        age = round(age/self.orbital_periods["Neptune"], 2)
        return age