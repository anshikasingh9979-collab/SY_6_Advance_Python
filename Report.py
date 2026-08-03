# Decorator
def bold(func):
    def wrapper(*args):
        return "***** " + func(*args) + " *****"
    return wrapper


# Report Class
class Report:

    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, function):
        cls.templates[name] = function

    def generate(self, name):
        return Report.templates[name](self)

    def __str__(self):
        return "Title : " + self.title + "\nContent : " + self.content


# Template 1
def simple(report):
    return str(report)


# Template 2
@bold
def fancy(report):
    return str(report)


# Main Program

Report.add_template("simple", simple)
Report.add_template("fancy", fancy)

title = input("Enter Report Title: ")
content = input("Enter Report Content: ")

r = Report(title, content)

print("\nSimple Report")
print(r.generate("simple"))

print("\nFancy Report")
print(r.generate("fancy"))