# Notion-API-Workshop
![alt text](https://www.daily.co/blog/authorizing-dailys-chrome-extension-beta-transcription-feature-with-notions-api/)

## Overview
This script interacts with the Notion API to manage tasks. It allows users to view tasks, add new tasks, and update the status of existing tasks in a Notion database.

## Features
- **Environment Variables**: Securely manages sensitive information like API keys and database IDs.
- **Notion API Integration**: Uses the `notion_client` library to interact with the Notion database.
- **Task Management**: Supports adding new tasks, viewing existing tasks, and updating task statuses.

## Table of Contents
- [Environment Variables](#environment-variables)
- [Initialize Notion Client](#initialize-notion-client)
- [Add a Task](#add-a-task)
- [Get All Tasks](#get-all-tasks)
- [Update a Task](#update-a-task)
- [Main Functionality](#main-functionality)
- [Program Entry Point](#program-entry-point)
- [Installation](#installation)

---

## Environment Variables
- **Purpose**: Keeps sensitive information like API keys and database IDs secure and separate from the main code.
- **`dotenv` Library**: Loads environment variables from a `.env` file.
    - `NOTION_API_KEY`: Used for authentication with the Notion API.
    - `NOTION_DATABASE_ID`: Specifies which database the program interacts with.
    - **Usage**: `os.getenv()` retrieves environment variables.

---

## Initialize Notion Client
- **Library**: `notion_client` is used to connect to the Notion API.
- **Authentication**: 
    - `Client(auth=os.getenv("NOTION_API_KEY"))`: Initializes the connection using the API key.
    - `DATABASE_ID`: Fetched from the environment variables and used throughout the program.

---

## Add a Task
The `add_task` function creates a new page in the Notion database with a task name and a default "Not started" status.
- **Basic API Usage**: Demonstrates a POST request to create a resource in the Notion database.
- **Breakdown**:
    - `notion.pages.create()`: Makes an API request to create a page.
    - `parent={"database_id": DATABASE_ID}`: Specifies where to create the task.
    - `properties`: Defines the task's properties, including a title (`task_name`) and default status.

---

## Get All Tasks
The `get_tasks` function fetches all tasks from the Notion database.
- **Basic API Usage**: Demonstrates a GET request to query data.
- **Breakdown**:
    - `notion.databases.query()`: Fetches tasks from the database.
    - Iterates over the results (`tasks`) to extract the task's name and status.
    - Prints the list of tasks.

---

## Update a Task
The `update_task` function updates the status of a specific task by its ID.
- **Basic API Usage**: Demonstrates a PATCH request to update an existing resource.
- **Breakdown**:
    - `notion.pages.update()`: Updates a specific page (task) in the database.
    - `page_id`: Specifies the task to update.
    - `properties`: Defines the updated status.

---

## Main Functionality
- **Text-Based Menu System**: Allows users to interact with the program to:
    - View tasks (`get_tasks`).
    - Add a new task (`add_task`).
    - Update an existing task's status (`update_task`).
- Demonstrates basic user input handling and a loop for continuous interaction.

---

## Program Entry Point
- The program starts execution from the `main()` function, which handles the user interface and invokes the respective functions based on user input.

---

## Installation
Before running the script, you need to install the required dependencies. In your terminal, run the following commands:

```bash
pip install notion-client
pip install python-dotenv
