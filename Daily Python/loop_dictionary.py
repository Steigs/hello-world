user_0={
    "username":"efermi",
    "first":"brady",
    "last":"steiger",
    }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


    favorite_lifts = {
    "nat": "lat pulldown",
    "brady": "cleans",
    "lev": "sprints",
    "nancy": "planks",
    }
    for name,lifts in favorite_lifts.items():
        print(f"\n{name.title()} really loves {lifts}.")

    for name in favorite_lifts.keys():
        print(name.title())

    for name in favorite_lifts.values():
        print(name.title())

    for name in favorite_lifts:
        print(name.title())


favorite_lifts = {
    "nat": "lat pulldown",
    "brady": "cleans",
    "lev": "sprints",
    "nancy": "planks",
    }

friends=["lev","nancy"]
for name in favorite_lifts.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        lift=favorite_lifts[name].title()
        print(f"\t{name.title()}, I see you love {lift}!")
    if "janine" not in favorite_lifts.keys():
        print("Janine, please take our poll!")

favorite_lifts = {
    "nat": "lat pulldown",
    "brady": "cleans",
    "lev": "sprints",
    "nancy": "planks",
    }

for name in sorted(favorite_lifts.keys()):
    print(f"{name.title()}, thank you for letting us know your favorote lift!")