#!/bin/python3

N = int(input())

def fizz_buzz(num):
    odd_cond = num % 2 == 1
    even_range1_cond = num % 2 == 0 and num in range(2,6)
    even_range2_cond = num % 2 == 0 and num in range(6,21)
    even_greater_cond = num % 2 == 0 and num > 20
    if odd_cond or even_range2_cond:
        print("Weird")
    elif even_range1_cond or even_greater_cond:
        print("Not Weird")
    

fizz_buzz(N)
