class UserDetails:
    """This is the class's DOCSTRING"""
    def __init__(self, name, id, age):
        self.name = name
        self.docstring = UserDetails.__doc__
        self.id = id
        self.age = age

    def printDetails(self):
        print(f"The name of the user is {self.name}.\nThe age of the user is {self.age} and id is {self.id}.\nDocstring: {self.docstring}")

    def __repr__(self) -> str:
        return f"UserDetails('{self.name}', {self.age}, '{self.id}')"

    def __str__(self) -> str:
        details = f"""
        UserDetails:
            name: {self.name}
            id: {self.id}
            age: {self.age}
        """
        return details

# UserDetails("Biraj Tiwari", "AA230448S", 18).printDetails()
cust = UserDetails("Biraj Tiwari", "AA230448S", 18)
print(cust.__repr__) # will implicitly call __repr__
print(cust)
