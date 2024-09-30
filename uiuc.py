import json
from datetime import datetime, timedelta

# Load data from JSON file
def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Task 1: List each completed training with a count of how many people completed it
def task_1(data):
    training_count = {}
    for person in data:
        for completion in person['completions']:
            training_name = completion['name']
            if training_name in training_count:
                training_count[training_name] += 1
            else:
                training_count[training_name] = 1
    return training_count

# Task 2: List all people that completed specified trainings within the fiscal year
def task_2(data, trainings, fiscal_year):
    results = {}
    start_date = datetime(fiscal_year - 1, 7, 1)
    end_date = datetime(fiscal_year, 6, 30)
    
    for training in trainings:
        results[training] = []
        for person in data:
            for completion in person['completions']:
                if completion['name'] == training:
                    completion_date = datetime.strptime(completion['timestamp'], "%m/%d/%Y")
                    if start_date <= completion_date <= end_date:
                        results[training].append(person['name'])
    return results

# Task 3: Find all people with expired or soon-to-expire training
def task_3(data, reference_date):
    reference_date = datetime.strptime(reference_date, "%m/%d/%Y")
    soon_threshold = reference_date + timedelta(days=30)
    expiring_soon = {}
    
    for person in data:
        expiring_soon[person['name']] = []
        for completion in person['completions']:
            if completion.get('expires'):
                expires_date = datetime.strptime(completion['expires'], "%m/%d/%Y")
                if expires_date < reference_date:
                    expiring_soon[person['name']].append({"training": completion['name'], "status": "expired"})
                elif reference_date <= expires_date <= soon_threshold:
                    expiring_soon[person['name']].append({"training": completion['name'], "status": "expires soon"})
        if not expiring_soon[person['name']]:
            del expiring_soon[person['name']]  # Remove people without any soon-to-expire or expired trainings
    return expiring_soon

def main():
    data = load_data("./trainings.txt")
    
    # Task 1
    task1_output = task_1(data)
    with open("task_1_output.json", "w") as file:
        json.dump(task1_output, file, indent=4)
    
    # Task 2
    task2_trainings = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]
    task2_fiscal_year = 2024
    task2_output = task_2(data, task2_trainings, task2_fiscal_year)
    with open("task_2_output.json", "w") as file:
        json.dump(task2_output, file, indent=4)
    
    # Task 3
    task3_date = "10/1/2023"
    task3_output = task_3(data, task3_date)
    with open("task_3_output.json", "w") as file:
        json.dump(task3_output, file, indent=4)

if __name__ == "__main__":
    main()
