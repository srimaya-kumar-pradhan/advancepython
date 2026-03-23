def sort_numbers_ascending():
    """Sort numbers from small to large"""
    print("\n--- SORT NUMBERS (ASCENDING) ---")
    numbers = [5, 2, 8, 1, 9, 3, 7]
    print(f"Original: {numbers}")
    sorted_asc = sorted(numbers)
    print(f"Sorted: {sorted_asc}")
 
def sort_numbers_descending():
    print("\n--- SORT NUMBERS (DESCENDING) ---")
    numbers = [5, 2, 8, 1, 9, 3, 7]
    print(f"Original: {numbers}")
    sorted_desc = sorted(numbers, reverse=True)
    print(f"Sorted: {sorted_desc}")

 
def sort_names():
    """Sort names in alphabetical order"""
    print("\n--- SORT NAMES (A-Z) ---")
    names = ["Zara", "Arjun", "Priya", "Mukesh", "Deepika"]
    print(f"Original: {names}")
    sorted_names = sorted(names)
    print(f"Sorted: {sorted_names}")

def sort_by_length():
    """Sort words by length (shortest to longest)"""
    print("\n--- SORT BY LENGTH ---")
    words = ["python", "java", "c", "javascript", "ruby"]
    print(f"Original: {words}")
    sorted_words = sorted(words, key=len)
    print(f"Sorted: {sorted_words}")

 
def sort_students_by_marks():
    """Sort students by marks (highest to lowest)"""
    print("\n--- SORT STUDENTS BY MARKS ---")
    
    students = [
        {"name": "Arjun", "marks": 85},
        {"name": "Priya", "marks": 92},
        {"name": "Rohan", "marks": 78},
        {"name": "Deepika", "marks": 88}
    ]
    
    print("Original:")
    for student in students:
        print(f"  {student['name']}: {student['marks']}")
    
    sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)
    
    print("Sorted (Highest to Lowest):")
    for student in sorted_students:
        print(f"  {student['name']}: {student['marks']}")

 
def sort_tuples():
    """Sort list of tuples"""
    print("\n--- SORT TUPLES ---")
    
    data = [("Apple", 50), ("Banana", 30), ("Cherry", 40)]
    print(f"Original: {data}")
    sorted_data = sorted(data, key=lambda x: x[1])
    print(f"Sorted by quantity: {sorted_data}")


 
def custom_sort():
    """User enters numbers and sorts them"""
    print("\n--- CUSTOM SORT ---")
    
    while True:
        try:
            numbers_input = input("Enter numbers (comma-separated): ")
            numbers = [int(x.strip()) for x in numbers_input.split(",")]
            
            print(f"\nOriginal: {numbers}")
            print(f"Ascending: {sorted(numbers)}")
            print(f"Descending: {sorted(numbers, reverse=True)}")
            break
        except:
            print("  Invalid input! Enter numbers like: 5, 2, 8, 1")


 
def sort_with_ranking():
    """Sort with ranking numbers"""
    print("\n--- SORT WITH RANKING ---")
    
    scores = [85, 92, 78, 88, 95, 80]
    print(f"Original scores: {scores}")
    
    sorted_scores = sorted(scores, reverse=True)
    
    print("\nRanking:")
    for rank, score in enumerate(sorted_scores, 1):
        print(f"  Rank {rank}: {score} marks")
 
def sort_employees():
    """Sort employees by salary"""
    print("\n--- SORT EMPLOYEES BY SALARY ---")
    
    employees = [
        {"name": "John", "salary": 50000},
        {"name": "Alice", "salary": 60000},
        {"name": "Bob", "salary": 45000},
        {"name": "Diana", "salary": 65000}
    ]
    
    sorted_emp = sorted(employees, key=lambda x: x["salary"], reverse=True)
    
    for emp in sorted_emp:
        print(f"  {emp['name']}: ${emp['salary']}")

 
def main():
    """Main menu"""
    
    while True:
        print("\n" + "=" * 50)
        print("SORTING PROGRAM - BEGINNER LEVEL")
        print("=" * 50)
        print("\n1. Sort Numbers (Ascending)")
        print("2. Sort Numbers (Descending)")
        print("3. Sort Names (A-Z)")
        print("4. Sort by Length")
        print("5. Sort Students by Marks")
        print("6. Sort Tuples")
        print("7. Custom Sort (Enter your numbers)")
        print("8. Sort with Ranking")
        print("9. Sort Employees by Salary")
        print("10. Exit")
        
        choice = input("\nEnter choice (1-10): ").strip()
        
        if choice == "1":
            sort_numbers_ascending()
        elif choice == "2":
            sort_numbers_descending()
        elif choice == "3":
            sort_names()
        elif choice == "4":
            sort_by_length()
        elif choice == "5":
            sort_students_by_marks()
        elif choice == "6":
            sort_tuples()
        elif choice == "7":
            custom_sort()
        elif choice == "8":
            sort_with_ranking()
        elif choice == "9":
            sort_employees()
        elif choice == "10":
            print("\nThank you! Goodbye! \n")
            break
        else:
            print("\nInvalid choice! Please enter 1-10")
if __name__ == "__main__":
    main()