# ==============================
# Project Step 1 : NumPy Exercise
# ==============================

import numpy as np

# ------------------------------
# Employee Details
# Columns: Employee ID, Department, Years with Company
# ------------------------------
employee_details = np.array([
    [101, 'Sales', 3],
    [102, 'HR', 5],
    [103, 'IT', 2],
    [104, 'Sales', 8],
    [105, 'IT', 6],
    [106, 'HR', 4],
    [107, 'IT', 7],
    [108, 'Sales', 1],
    [109, 'HR', 3]
], dtype=object)

# ------------------------------
# Survey Results
# Columns: Employee ID, Happiness Score (1–10)
# ------------------------------
survey_results = np.array([
    [101, 8],
    [102, 10],
    [103, 9],
    [104, 6],
    [105, 7],
    [106, 8],
    [107, 9],
    [108, 5],
    [109, 7]
])

# =====================================================
# Task 1: Merge Arrays
# =====================================================
merged_data = np.hstack((
    employee_details,
    survey_results[:, 1].reshape(-1, 1)
))

print("\nTask 1: Merged Data")
print(merged_data)

# =====================================================
# Task 2: Print Happiness Scores
# =====================================================
happiness_scores = merged_data[:, -1].astype(int)

print("\nTask 2: Happiness Scores")
print(happiness_scores)

# =====================================================
# Task 3: Sort Happiness Scores
# =====================================================
sorted_scores = np.sort(happiness_scores)

print("\nTask 3: Sorted Happiness Scores")
print(sorted_scores)

# =====================================================
# Task 4: Employee ID and Department
# =====================================================
print("\nTask 4: Employee ID and Department")
for emp in employee_details:
    print(f"Employee ID: {emp[0]}, Department: {emp[1]}")

# =====================================================
# Task 5: Happiness Score for Each Employee
# =====================================================
print("\nTask 5: Employee Happiness Scores")
for emp_id, dept, years, score in merged_data:
    print(f"Employee ID: {emp_id}, Happiness Score: {score}")

# =====================================================
# Task 6: Convert Scores to Float
# =====================================================
happiness_scores_float = happiness_scores.astype(float)

print("\nTask 6: Happiness Scores (Float)")
print(happiness_scores_float)

# =====================================================
# Task 7: Average Happiness Score
# =====================================================
average_score = np.mean(happiness_scores_float)

print("\nTask 7: Average Happiness Score")
print(average_score)

# =====================================================
# Task 8: Unique Departments
# =====================================================
departments = employee_details[:, 1]
unique_departments = np.unique(departments)

print("\nTask 8: Unique Departments")
print(unique_departments)
