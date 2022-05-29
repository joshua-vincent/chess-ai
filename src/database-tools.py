# -*- coding: utf-8 -*-
"""
A set of tools for managing chess game data.
    Created on Sun May 29 16:26:29 2022

@author: Joshua Vincent
"""

def 


# def generateEmails(file):
#     """ 
#     Takes the location of a text file contianing a list of usernames.
#     Generates a new text file with Bently email addresses for the specified names.
#     The file names are in alphabetical order on separate lines.
    
#     file : str, path location to text file containing list of usernames
#     """
    
#     username_file = open(file)
#     usernames = username_file.read()
#     username_list = usernames.replace('\n', ' ').split()
#     username_list.sort()
    
#     email_file = open('emails.txt', 'w')
    
#     for user in username_list:
#         email_file.write(user + '@bentley.edu\n')