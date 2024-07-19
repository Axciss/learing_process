def calculate(operation: str) -> float:
    return eval(operation)


def get_planet_mass(planet) -> float:
    planet = planet.lower()
    if planet == "earth":
        return 5.972e24
    if planet == "mars":
        return 6.39e23
    if planet == "jupiter":
        return 1.898e27
    if planet == "saturn":
        return 5.683e26
    if planet == "uranus":
        return 8.681e25
    if planet == "neptune":
        return 1.024e26
    if planet == "mercury":
        return 3.285e23
    if planet == "venus":
        return 4.867e24
    return None