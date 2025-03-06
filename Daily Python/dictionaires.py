# dictionaries starting on page 92


nat = {"age":"24", "height": "6'0", "qualities": "beautiful, smart, caring, cat mom, brings out the best in me"}
print(nat["qualities"])
print(nat["age"])
print(nat["height"])
nat["cat"] = "lev kink nancy booger"
print(nat)

why=nat["qualities"]
print(f"Give us the reasons you love Natalie: She is {why}!")


alien_0={"x_position": 0, "y_position": 25, "speed": "fast"}
print(f"Original POsition: {alien_0["x_position"]}")

# move alien to the right 
# ddetermine how far to move the alien based on its current speed

if alien_0["speed"]=="slow":
    x_increment=1
elif alien_0["speed"]=="medium":
    x_increment=2
else:
    x_increment=3

# the new position is the old position plus the increment

alien_0["x_position"] = alien_0["x_position"]+ x_increment
print(f"New position: {alien_0["x_position"]}")

favorite_lifts = {
    "nat": "lat pulldown",
    "brady": "clean",
    "lev": "sprints",
    "nancy": "plank",
    }
lifts=favorite_lifts["nat"].title()
print(f"Nat sure loves to do {lifts}, when she is at the Factory.")

# get() function

alien_0={"x_position": 0, "y_position": 25, "speed": "fast"}
point_value=alien_0.get("points", "No point value given.")
print(point_value)