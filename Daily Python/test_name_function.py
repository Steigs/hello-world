# page 213

from ch11_name_function import get_formatted_name

def test_first_last_name():
    '''Do names like 'Janis Joplin' work?'''
    formatted_name = get_formatted_name ('janis', 'joplin')
    assert formatted_name =="Janis Joplin"

def test_first_last_middle_names():
    '''Do names like Brady Michael Steiger work?'''
    formatted_name = get_formatted_name('brady', 'steiger' ,'michael')
    assert formatted_name == "Brady Michael Steiger"