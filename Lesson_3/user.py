class User:
    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name

    def p_firstName(self):
        print(self.firstName)

    def p_lastName(self):
        print(self.lastName)

    def p_fullName(self):
        print(f"{self.firstName} {self.lastName}")