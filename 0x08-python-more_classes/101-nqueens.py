#!/usr/bin/python3
import sys
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""

def reject(board):
    """recursive backtracking function to find the solution"""
    for col_A in board:
        for col_B in board:
            if not col_A is col_B:
                if col_A[0] == col_B[0]:
                    return True
                if col_A[1] == col_B[1]:
                    return True
                if col_A[1] - col_A[0] == col_B[1] - col_B[0]:
                    return True
                if col_A[0] + col_A[1] == col_B[0] + col_B[1]:
                    return True
    return False
