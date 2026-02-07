def celestial_neighbours_age():
    earth_age = None
    
    while not isinstance(earth_age, int):
        age_input = input("How old are you in Earth years? ")
        
        if age_input.isdigit():
            earth_age = int(age_input)
        else:
            print("Please input a real number.")

    planet_orbit_periods = {
        'Mercury': 87.97,
        'Venus': 224.7,
        'Earth': 365,
        'Mars': 686.98,
        'Jupiter': 4332.82,
        'Saturn': 10755.7,
        'Uranus': 30687.15,
        'Neptune': 60190.03,
    }

    planet_adjective_names = {
    "Mercury": "Mercurian",
    "Venus": "Venusian",
    "Earth": "Terrestrial",
    "Mars": "Martian",
    "Jupiter": "Jovian",
    "Saturn": "Saturnian",
    "Uranus": "Uranian",
    "Neptune": "Neptunian"
    }

    moons_dictionary = {
    'Luna': ['The Moon'],
    'Martian': ['Phobos', 'Deimos'],
    'Galilean': ['Europa', 'Ganymede', 'Io', 'Callisto'],
    'Saturnian': ['Titan', 'Enceladus', 'Rhea', 'Mimas', 'Dione', 'Iapetus', 'Hyperion', 'Phoebe', 'Tethys'],
    'Uranian': ['Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Puck', 'Cordelia', 'Ophelia'],
    'Neptunian': ['Triton', 'Proteus', 'Nereid', 'Hippocamp', 'Galatea', 'Despina', 'Thalassa', 'Naiad'],
    'Plutonian': ['Charon', 'Nix', 'Styx', 'Kerberos', 'Hydra']
    }

    planet = input("Which planet would you like to find your age on? ").title()
    
    if planet == 'Pluto':
        print("Pluto is no longer considered a planet.")
        return

    for group, moons in moons_dictionary.items():
        if planet in moons:
            print(f"{planet} is a {group} moon.")
            return

    if planet in planet_orbit_periods:
        on_planet_age = earth_age * (planet_orbit_periods['Earth'] / planet_orbit_periods[planet])
        add_adjective = planet_adjective_names[planet]
        print(f"Your {add_adjective} age is {on_planet_age:.2f} years!")
    else:
        print(f"{planet} is not in the database")

celestial_neighbours_age()
