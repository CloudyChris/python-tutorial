# In programming, we need to make decisions based on both input data and other stuff that's going on
# This is also called flow control
# In python, decision making is based around the keyword "if" (most of the time)
# Other special keywords exist for other types of decision making (like "assert" for when stuff really needs to be a certain value or state)

# For example, if you want to take a list of employee salaries and raise only the ones below a certain threshold you'd need to check whether
# the salary of the employee you're looking at is smaller than said threshold.
# To do that we'll use a class (because python doesn't have normal structs like C) to group together employee data,
# a vector or list to put all of the data inside of, a threshold to check for, and the raise value

class Employee:
    def __init__(self, i_name, i_salary):
        # self is the keyword for the scope of the current class and can only be accessed and used by the methods within that class
        # we're basically definind the member values of the class and assigning them the values from the constructor
        self.name = i_name
        self.salary = i_salary

# bad global vars, but this is just an example
threshold = 2500
salary_raise = 200

print("Raise threshold is", threshold)
print("Salaries will be raised by", salary_raise)

# list/array with all the employees
employees = [
    Employee("Joe", 2800),
    Employee("Paul", 2500),
    Employee("Dan", 2600),
    Employee("Maria", 2496)
]

# looping with "for <element> in <list>" for convenience
old_salary = ""
for employee in employees:
    old_salary = ""
    # Checking the salary with the "lesser" operator
    if employee.salary < threshold:
        # scoped variable within the if within the for (nested like a birb)
        old_salary = employee.salary
        # modifying the salary member value of the employee the <element> is currently pointing at
        employee.salary = employee.salary + salary_raise
        print(employee.name, "got a raise from", old_salary, "to", employee.salary)
    # You can define multiple checks and if they are dependent on one another (as in, the second one should be checked only if the first one is false)
    # we use elif for that (which is an abbreviation of else if)
    elif employee.salary == threshold:
        old_salary = employee.salary
        employee.salary = employee.salary + int(salary_raise/2)
        print(employee.name, "got a raise from", old_salary, "to", employee.salary)
    else:
        # else branch is accessed if the condition in the "if" is false
        print(employee.name, "didn't get a raise. They already have", employee.salary)

# neither the elif or the else are mandatory
# sometimes you only want to do something if a condition is true and do nothing otherwise
# say, if an employee has over 2600 salary you wanna call them a jerk

for employee in employees:
    if employee.salary > 2600:
        print(employee.name, "is a rich jerk")

# it is not good code to include an empty else with say, a pass directive, when you don't actually have a use for it. If can and should be used alone when appropriate.

# LETTUCE DISCUSS the match statement which is python's "switch" cause it wanted to feel special
# match takes a variable and matches it against a list of cases

match (salary_raise):
    case 100 | 200: print("Greedy managers don't want me to eat")
    case 300: print("They don't love us enough")
    case 400: print("Azi mancam cu carne")
    case _: print("Unexpected")

# _ (underscore) is the default case, aka, the else in a match .. case thing
# cases technically use patterns, but you can have ifs in them, the value checked can be a set or list
# and there are, as shown in the fist case, ways to comine checks (the vertical bar stand for logical "or")
