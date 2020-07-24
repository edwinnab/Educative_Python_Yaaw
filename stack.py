class Family:
    def __init__(self):
        self.names = []
#adds a name to the top of the stack
    def push(self, name):
        self.names.append(name)
#checks if a stack is empty
    def is_empty(self):
        return self.names == []
#peeks and returns the last element of the stack

    def peek(self):
        if not self.is_empty():
            return self.names[-1]
    def pop(self):
        return self.names.pop()

    def get_Names(self):
        return self.names
members = Family()
members.push("Edwinna Bikeri")
members.push("Stacy Kimberly")
members.push("money money")
print(members.get_Names())
members.push("Anita Joy")
print(members.pop())
print(members.peek())
