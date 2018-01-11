# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:43:16 2018

@author: yxh
"""
# assign function to a variable


def greet(name):
    return 'hello' + name


greet_someone = greet
print greet_someone('Jhon')
print type(greet_someone('Jhon'))

# define functions inside other functions


def greet(name):
    def get_message():
        return 'Hello'
    result = get_message() + name
    return result


print greet('Jhon')

# Functions can be passed as parameters to other functions


def greet(name):
    return 'Hello' + name


def call_func(func):
    other_name = 'Jhon'
    return func(other_name)


print call_func(greet)

#Functions can return other functions, In other words,
#functions generating other functions


def compose_greet_func():
    def get_message():
        return 'Hello there!'
    return get_message


greet = compose_greet_func()
print greet()
