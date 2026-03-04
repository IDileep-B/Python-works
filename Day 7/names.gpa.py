def calculate_average_cgpa(students_data):
    if not students_data:
        return 0
    total_points = sum(students_data.values())
    average_cgpa = total_points / len(students_data)
    return round(average_cgpa, 2)


students_cgpa = {
    "Alice": 8.5,
    "Bob": 7.2,
    "Charlie": 9.1,
    "David": 6.8
}

print("--- Student CGPA Data ---")

for name, cgpa in students_cgpa.items():
    print(f"* {name}: {cgpa} CGPA")


avg_cgpa = calculate_average_cgpa(students_cgpa)
print(f"\nOverall Average CGPA: {avg_cgpa}")
