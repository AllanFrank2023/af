import tkinter as tk
import math  # Importer math-modulet for de matematiske funktioner

import math

class Calculator:
    @staticmethod
    def calculate(expression):
        try:
            result = eval(expression)
            return result
        except:
            return "Error"

    @staticmethod
    def square_root(a):
        return math.sqrt(a)

    @staticmethod
    def sine(angle):
        return math.sin(math.radians(angle))

    @staticmethod
    def cosine(angle):
        return math.cos(math.radians(angle))

    @staticmethod
    def tangent(angle):
        return math.tan(math.radians(angle))

#class Calculator:
#    @staticmethod
#    def add(a, b):
#        return a + b

 #   @staticmethod
  #  def subtract(a, b):
 #       return a - b

  #  @staticmethod
  #  def multiply(a, b):
  #      return a * b

  #  @staticmethod
  #  def divide(a, b):
   #     if b != 0:
   #         return a / b
    #    else:
     #       return "Undefined"

   # @staticmethod
    #def square_root(a):
   #     return a ** 0.5

   # @staticmethod
  #  def sine(angle):
  #      return math.sin(angle)

   # @staticmethod
  #  def cosine(angle):
  #      return math.cos(angle)

   # @staticmethod
  #  def tangent(angle):
   #     return math.tan(angle)

