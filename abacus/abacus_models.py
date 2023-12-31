#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BiQuinaryRod:
    def __init__(self):
        self.quinary = [0] * 5  # Five spots for beads, representing 1-4
        self.binary = [0] * 2  # Two spots for beads, representing 0 or 5

    # New method to get the total value of the rod
    def value(self):
        return sum(self.quinary) + (5 if self.binary[1] else 0)

    # New method to set the value of the rod
    def set_value(self, value):
        self.binary[1] = 1 if value >= 5 else 0
        self.quinary = [1 if i < value % 5 else 0 for i in range(5)]

    def display(self):
        return self.binary + self.quinary


def modify_displayed_list(lst_original):
    lst = lst_original.copy()

    # Rule: if second element is 0 first should be 1
    if lst[1] == 0:
        lst[0] = 1

    # Rule: if last 4 are 0 they should be changed to 1
    if all(x == 0 for x in lst[-5:]):
        for i in range(4):
            lst[-(i + 1)] = 1

    # Additional rules based on the state of the 3rd, 4th, 5th, and 6th elements
    if lst[2] == 1 and lst[3] == 0 and lst[4] == 0 and lst[5] == 0 and lst[6] == 0:
        lst[4:6] = [1, 1, 1]
    if lst[2] == 1 and lst[3] == 1 and lst[4] == 0 and lst[5] == 0 and lst[6] == 0:
        lst[5:6] = [1, 1]
    if lst[2] == 1 and lst[3] == 1 and lst[4] == 1 and lst[5] == 0 and lst[6] == 0:
        lst[6] = [1]

    return lst


class Abacus:
    def __init__(self, rods=10):
        self.rods = [BiQuinaryRod() for _ in range(rods)]
        self.max_value = int('9' * rods)

    def current_value(self):
        total = 0
        for i, rod in enumerate(self.rods):
            total += rod.value() * (10 ** i)
        return total

    def add(self, number):

        if number > self.max_value or self.current_value() + number > self.max_value:
            raise ValueError("Adding error: Number too large to be represented")

        carry = 0

        for i in range(len(self.rods)):
            digit = (number % 10) + carry
            number //= 10

            # Update current rod and calculate carry
            new_value = self.rods[i].value() + digit
            carry = new_value // 10
            self.rods[i].set_value(new_value % 10)

            # If there's no more number and no carry, break the loop
            if number == 0 and carry == 0:
                break

    def subtract(self, number):

        if number > self.current_value():
            raise ValueError("Subtraction error: Number too large to subtract")

        borrow = 0
        for i in range(len(self.rods)):
            # Adjust digit with current borrow
            digit = (number % 10) + borrow
            number //= 10

            # Calculate the new value considering borrow
            new_value = self.rods[i].value() - digit

            # If new value is negative, set borrow for the next rod
            if new_value < 0 and i < len(self.rods) - 1:
                borrow = 1
                new_value += 10  # Adjust new value after borrowing
            else:
                borrow = 0

            self.rods[i].set_value(new_value)

            # Break if no more number to subtract and no borrow
            if number == 0 and borrow == 0:
                break

    def display(self):
        display_rows = [''] * 7
        for rod in reversed(self.rods):
            rod_display = modify_displayed_list(rod.display())
            for i in range(7):
                display_rows[i] += ' * ' if rod_display[i] else ' | '
                display_rows[i] += ' '
        display_rows.insert(2, ' -- ' * len(self.rods))  # Separator line after binary part
        return '\n'.join(display_rows)

    def reset(self):
        for rod in self.rods:
            rod.quinary = [0] * 5
            rod.binary = [0] * 2
