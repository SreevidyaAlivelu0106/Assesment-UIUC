# Training Data Processing Application

This is a Python-based console application that processes training completion data from a JSON file and generates outputs based on specific tasks. The data is sourced from a `trainings.txt` file, and the application produces three JSON files as output.

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks Description](#tasks-description)
- [Output Files](#output-files)
- [License](#license)

## Project Overview
This application reads training completion data from a JSON file and generates three output files with results based on the following tasks:
1. Count of how many people have completed each training.
2. List of people who completed specified trainings in a specific fiscal year.
3. List of people with expired or soon-to-expire trainings based on a given reference date.

## Prerequisites
Before running this application, ensure that you have the following installed:
- Python 3.x
- `trainings.txt` (JSON data file containing training completions)

## Installation
1. Clone this repository to your local machine:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Ensure you have Python installed on your machine. You can check this by running:
    ```bash
    python --version
    ```

3. No additional dependencies are required for this application as it uses the standard Python library.

## Usage
1. Place the `trainings.txt` file in the same directory as the Python script.
2. Run the script using Python:
    ```bash
    python training_processor.py
    ```

3. Upon successful execution, the program will generate three output JSON files:
    - `task_1_output.json`
    - `task_2_output.json`
    - `task_3_output.json`

## Tasks Description
### Task 1: Training Completion Count
For each unique training, this task counts how many people have completed it. The result is saved in `task_1_output.json`.

### Task 2: List of People Who Completed Trainings in a Fiscal Year
This task takes a set of specified trainings and a fiscal year as input and lists all people who completed those trainings within the fiscal year (defined as July 1 of the previous year to June 30 of the current year). The fiscal year and trainings used in the code are:
- Fiscal Year: 2024
- Trainings: "Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"

The result is saved in `task_2_output.json`.

### Task 3: Expired or Soon-to-Expire Trainings
Given a reference date (October 1st, 2023), this task finds all people whose trainings have either expired or will expire within one month of the reference date. It lists the training along with a status of either "expired" or "expires soon". The result is saved in `task_3_output.json`.

## Output Files
- `task_1_output.json`: Contains the count of completed trainings for all individuals.
- `task_2_output.json`: Contains a list of people who completed specified trainings during the 2024 fiscal year.
- `task_3_output.json`: Contains a list of people with expired or soon-to-expire trainings as of October 1, 2023.

## License
This project is open-source and licensed under the MIT License.
