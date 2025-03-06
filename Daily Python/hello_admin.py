#Hello Admin project on page 88


username=["natalalie","levy","admin","brady", "nancy"]
for username in username:
    if username == "admin":
        print("Hello Admin, would you like to see a status report?")
    elif username in username:
        print(f"Hello {username.title()}, thank you for logging in again!")



username=[]
if username:
    for username in username:
        if username == "admin":
            print("\nHello Admin, would you like to see a status report?")
        elif username in username:
            print(f"\nHello {username.title()}, thank you for logging in again!")
else:
    print("\nWe need to get some users")


for value in range(1,10):
    if value in range (2):
        print(f"\n{value}st")
    elif value in range(3):
        print(f"{value}nd")
    elif value in range (4):
        print(f"{value}rd")
    else:
        print(f"{value}th")

    