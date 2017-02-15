#!/usr/bin/env python3
from sys import exit
import cgi


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero!")
        exit()


print("Content-type: text/html\n")
form = cgi.FieldStorage()
operation = form.getfirst("operation")

try:
    first_number = float(form.getfirst("first_number"))
    second_number = float(form.getfirst("second_number"))
except ValueError:
    print("Invalid input!")

calculations = {
    "+": addition(first_number, second_number),
    "-": subtraction(first_number, second_number),
    "*": multiplication(first_number, second_number),
    "/": division(first_number, second_number)
}

try:
    print("Result: {}".format(calculations[operation]))
except KeyError:
    print("Invalid input! Put only +, -, * or /")
