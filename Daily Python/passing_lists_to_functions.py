# project on page 146

def messages(unread_messages , show_messages):
    '''display unread messages into show messages'''

    while unread_messages:
        current_messages=unread_messages.pop()
        print(f"\nThe following messages have not been shown: {current_messages} ")
        show_messages.append(current_messages)

def now_show (show_messages):
    '''Show all messages'''
    print("\nThe following messages have been shown:")
    for show_message in show_messages:
        print(show_message)

unread_messages = ["Yo", "Sup", "LOL"]
show_messages = []

messages(unread_messages[:], show_messages)
now_show(show_messages)

print(unread_messages)
print(show_messages)