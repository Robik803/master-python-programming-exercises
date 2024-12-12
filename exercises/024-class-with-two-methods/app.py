class InputOutString:

    def __init__(self):
        self.value = ""

    def get_string(self):
        self.value = input("Enter a string :")

    def print_string(self):
        print(self.value.upper())

string = InputOutString()
string.get_string()
string.print_string()