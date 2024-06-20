#Nuseyba Mohammed
#501282985
"""
Problem Description:
This project involves creating a to-do list application using Python. The application allows users to add, remove,
mark as complete, and list tasks. The task data is stored in a text file and includes the status of each task (Done/Not Done).
The application should demonstrate the use of Python constructs such as conditions, sequences, iteration, namespaces, 
functions, and file I/O.
"""

import os  # Importing os module for file operations

# File to store the to-do list
TODO_FILE = 'todo_list.txt'

def read_todo_list():
    """
    Read the to-do list from the file and return it as a list of dictionaries.
    Each task is represented as a dictionary with 'title' and 'completed' keys.
    This function handles file I/O for reading tasks.
    """
    if not os.path.exists(TODO_FILE):
        return []  # Return an empty list if the file does not exist

    with open(TODO_FILE, 'r') as file:
        lines = file.readlines()  # Read all lines from the file

    todo_list = []
    for line in lines:
        parts = line.strip().split('|')  # Split each line into task title and status
        if len(parts) == 2:  # Check if the line has exactly two parts
            task = {'title': parts[0], 'completed': parts[1] == 'Done'}  # Convert 'Done'/'Not Done' to boolean
            todo_list.append(task)  # Add task dictionary to the list
    
    return todo_list

def write_todo_list(todo_list):
    """
    Write the to-do list to the file.
    Each task is written as 'title|status' where status is 'Done' or 'Not Done'.
    This function handles file I/O for writing tasks.
    """
    with open(TODO_FILE, 'w') as file:
        for task in todo_list:
            status = 'Done' if task['completed'] else 'Not Done'  # Convert boolean to 'Done'/'Not Done'
            file.write(f"{task['title']}|{status}\n")  # Write task to file

def add_task(todo_list, title):
    """
    Add a new task to the to-do list.
    The task is initially marked as not completed.
    """
    todo_list.append({'title': title, 'completed': False})  # Append new task dictionary to the list

def remove_task(todo_list, title):
    """
    Remove a task from the to-do list based on the task title.
    This function uses list comprehension to filter out the task to be removed.
    """
    todo_list[:] = [task for task in todo_list if task['title'] != title]  # List comprehension to filter tasks

def mark_task_completed(todo_list, title):
    """
    Mark a task as completed based on the task title.
    This function iterates through the list and updates the task status.
    """
    for task in todo_list:
        if task['title'] == title:
            task['completed'] = True  # Set task status to completed
            break  # Exit loop once the task is found and marked as completed

def list_tasks(todo_list):
    """
    List all tasks in the to-do list with their status.
    This function prints each task and its status to the console.
    """
    if not todo_list:
        print("No tasks in the to-do list.")
        return

    for task in todo_list:
        status = "Done" if task['completed'] else "Not Done"  # Determine task status
        print(f"Task: {task['title']}, Status: {status}")  # Print task and status

def main():
    """
    Main function to run the to-do list application.
    Provides a menu for the user to interact with the application.
    This function handles user input and calls the appropriate functions based on user choices.
    """
    todo_list = read_todo_list()  # Read the existing to-do list from file

    while True:
        # Display the menu options
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()  # Get user input

        if choice == '1':
            title = input("Enter the task title: ").strip()  # Get task title from user
            add_task(todo_list, title)  # Add new task
            write_todo_list(todo_list)  # Write updated list to file
            print("Task added.")
        elif choice == '2':
            title = input("Enter the task title to remove: ").strip()  # Get task title from user
            remove_task(todo_list, title)  # Remove task
            write_todo_list(todo_list)  # Write updated list to file
            print("Task removed.")
        elif choice == '3':
            title = input("Enter the task title to mark as completed: ").strip()  # Get task title from user
            mark_task_completed(todo_list, title)  # Mark task as completed
            write_todo_list(todo_list)  # Write updated list to file
            print("Task marked as completed.")
        elif choice == '4':
            list_tasks(todo_list)  # List all tasks
        elif choice == '5':
            print("Exiting the application.")
            break  # Exit the loop to end the program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

if __name__ == '__main__':
    main()  # Run the main function if this script is executed directly

