# Decorator for formatting report text
def bold_text(func):
    def wrapper(*args, **kwargs):
        return "***************\n" + func(*args, **kwargs) + "\n***************"
    return wrapper


# Report Class
class Report:
    # Class variable to store templates
    templates = {}

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class method to add templates
    @classmethod
    def add_template(cls, name, template_function):
        cls.templates[name] = template_function

    # Class method to get template
    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    # Magic Method (__call__)
    def __call__(self, template_name):
        template = self.get_template(template_name)
        if template:
            return template(self)
        else:
            return "Template not found."

    # Magic Method (__str__)
    def __str__(self):
        return f"Report Title : {self.title}\nReport Content : {self.content}"


# Simple Template
def simple_template(report):
    return f"""
----- SIMPLE REPORT -----
Title   : {report.title}
Content : {report.content}
-------------------------
"""


# Fancy Template with Decorator
@bold_text
def fancy_template(report):
    return f"""
***** FANCY REPORT *****
Title   : {report.title}
Content : {report.content}
************************
"""


# Main Function
def main():
    # Add Templates
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    # Create Report
    report = Report(
        "Student Report",
        "This report demonstrates decorators, class methods, and magic methods."
    )

    # Display Default Report
    print("\nDefault Report")
    print(report)

    # Generate Simple Report
    print("\nSimple Template")
    print(report("simple"))

    # Generate Fancy Report
    print("\nFancy Template")
    print(report("fancy"))


# Driver Code
if __name__ == "__main__":
    main()
    