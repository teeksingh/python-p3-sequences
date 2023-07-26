#!/usr/bin/env python3

def print_fibonacci(length):
   list = []
   first = 0
   second = 1
   temp = 0

   for i in range(length):
      if i in {0,1}:
         list.append(i)
      else:
         list.append(first +second)
         temp = second
         second = first + second
         first = temp

   print(list)
      