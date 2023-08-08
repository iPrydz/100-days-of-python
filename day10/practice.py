def format_name(f_name, l_name):
    """Format the name and surname and capitalize every word."""
    if f_name == "" or l_name == "":
        return print("You didn't provide valid inputs.")
    firstname = f_name.title()
    lastname = l_name.title()
    return print(f"Hello {firstname} {lastname}!")

format_name(input("What's your name? "), input("What's your surname? "))