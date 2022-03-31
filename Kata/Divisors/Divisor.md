<!-- @format -->

# Divisors and Multiples

## Description

Given an array arr of length n, for each index i from 1 to n, count the number of indices j (j != i), such that either arr[j] is a divisor of arr[i] or arr[j] is a multiple of arr[i]

Note:
-x is called a divisor of y if y is divisible by x.
-x is called a multiple of y if x is divisible by y.

## BDD

The program should:

| Input                 | Output          |
| --------------------- | --------------- |
| arr = [1, 3, 4, 2, 6] | [4, 2, 2, 3, 3] |

## Explanation

    For i = 1, Number of divisors of 1 = 0. Number of multiples of 1 = 4.
    For i = 2, Number of divisors of 3 = 1. Number of multiples of 3 = 1.
    For i = 3, Number of divisors of 4 = 2. Number of multiples of 4 = 0.
    For i = 4, Number of divisors of 2 = 1. Number of multiples of 2 = 2.
    For i = 5, Number of divisors of 6 = 3. Number of multiples of 6 = 0.
