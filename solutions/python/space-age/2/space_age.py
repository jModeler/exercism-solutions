class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.orbital_periods = {
            "mercury": 0.2408467,                     
            "venus": 0.61519726,                    
            "earth": 1.0,                     
            "mars": 1.8808158,                     
            "jupiter": 11.862615,                     
            "saturn": 29.447498,                     
            "uranus": 84.016846,                     
            "neptune": 164.79132  
        }
        self.earth_days = 365.25
        self.earth_day_seconds = 86400

    def earth_age(self):
        "To provide pre rounded earth age"
        age = self.seconds/(self.earth_days * self.earth_day_seconds)
        return age
    
    def __getattr__(self, name):
        if name.startswith("on_"):
            planet = name[3:]
            if planet in self.orbital_periods:
                return lambda: round(self.earth_age()/self.orbital_periods[planet], 2)
        raise AttributeError(f"{name} is not a valid method")