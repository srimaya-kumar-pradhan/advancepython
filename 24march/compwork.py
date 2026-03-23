print("=" * 80)
print("COMPREHENSIVE PYTHON PROGRAM")
print("=" * 80)

# ============================================================================
#  1: Performs various operations on two integers
# ============================================================================
print("\n\n--- INTEGER OPERATIONS ---\n")

def integer_operations(num1, num2):
    
    print(f"Input Numbers: {num1} and {num2}")
    sum_result = num1 + num2
    diff_result = num1 - num2
    product_result = num1 * num2
    
    print(f"Sum: {num1} + {num2} = {sum_result}")
    print(f"Difference: {num1} - {num2} = {diff_result}")
    print(f"Product: {num1} * {num2} = {product_result}")
    if num2 != 0:
        division_result = num1 / num2
        print(f"Division: {num1} / {num2} = {division_result}")
    else:
        print("Division: Cannot divide by zero!")
    print(f"\n{num1} is {'EVEN' if num1 % 2 == 0 else 'ODD'}")
    print(f"{num2} is {'EVEN' if num2 % 2 == 0 else 'ODD'}")
    float_num1 = float(num1)
    print(f"\n{num1} converted to float: {float_num1} (type: {type(float_num1).__name__})")

# Test Task 1
integer_operations(15, 4)


# ============================================================================
#    2:                      String Processing
# ============================================================================
print("\n\n--- STRING PROCESSING ---\n")

def string_processing(sentence):
    print(f"Original Sentence: '{sentence}'")
    
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in sentence if char in vowels)
    consonant_count = sum(1 for char in sentence if char.isalpha() and char not in vowels)
    
    print(f"\nVowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    reversed_sentence = sentence[::-1]
    print(f"\nReversed: '{reversed_sentence}'")
    underscore_sentence = sentence.replace(" ", "_")
    print(f"\nWith underscores: '{underscore_sentence}'")
    capitalized_sentence = sentence.title()
    print(f"\nCapitalized: '{capitalized_sentence}'")
string_processing("hello world python programming")


# ============================================================================
#   3:                      Tuple Operations
# ============================================================================
print("\n\n--- TUPLE OPERATIONS ---\n")

def tuple_operations():
    mixed_tuple = (10, "apple", 20.5, "banana", 30, True, 15.2, "cherry")
    print(f"Mixed Tuple: {mixed_tuple}")
    
    numeric_values = tuple(item for item in mixed_tuple if isinstance(item, (int, float)) and not isinstance(item, bool))
    print(f"\nFiltered Numeric Values: {numeric_values}")

    print("\nAttempting to modify tuple:")
    try:
        mixed_tuple[0] = 100
    except TypeError as e:
        print(f"ERROR: {e}")
        print("Tuples are immutable - cannot modify in place!")

    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    concatenated_tuple = tuple1 + tuple2
    print(f"\nTuple 1: {tuple1}")
    print(f"Tuple 2: {tuple2}")
    print(f"Concatenated: {concatenated_tuple}")

tuple_operations()


# ============================================================================
#  4:          Dictionary Operations
# ============================================================================
print("\n\n--- TASK 4: DICTIONARY OPERATIONS ---\n")

def dictionary_operations():
    student_marks = {
        "Alice": 85,
        "Bob": 78,
        "Charlie": 92,
        "Diana": 88
    }
    
    print(f"Initial Dictionary: {student_marks}\n")
    
    student_marks["Eve"] = 95
    print(f"After adding Eve: {student_marks}")
    
    student_marks["Bob"] = 82
    print(f"After updating Bob's marks: {student_marks}")

    del student_marks["Charlie"]
    print(f"After deleting Charlie: {student_marks}")
    
    print(f"\nKeys: {list(student_marks.keys())}")
    
    print(f"Values: {list(student_marks.values())}")
    
    print(f"Items: {list(student_marks.items())}")
 
    print(f"\nTotal Students: {len(student_marks)}")
    print(f"Highest Marks: {max(student_marks.values())} - {[k for k, v in student_marks.items() if v == max(student_marks.values())][0]}")
    print(f"Average Marks: {sum(student_marks.values()) / len(student_marks):.2f}")

dictionary_operations()


# ============================================================================
# 5:      List Comprehension
# ============================================================================
print("\n\n--- LIST COMPREHENSION ---\n")

def list_comprehension_demo():
   
    words = ["python", "java", "c", "javascript", "ruby", "go"]
    
    sorted_by_length = sorted(words, key=len)
    print(f"Original words: {words}")
    print(f"Sorted by length: {sorted_by_length}")

    test_words = ["racecar", "hello", "level", "world", "madam", "python"]
    palindromes = [word for word in test_words if word == word[::-1]]
    print(f"\nWords to check: {test_words}")
    print(f"Palindromes: {palindromes}")
    
    sentences = [
        "hello world",
        "python programming",
        "list comprehension demo"
    ]
    hyphenated = [sentence.replace(" ", "-") for sentence in sentences]
    print(f"\nOriginal sentences: {sentences}")
    print(f"With hyphens: {hyphenated}")
list_comprehension_demo()


# ============================================================================
#  6:               Tuple to List Conversion
# ============================================================================
print("\n\n--- TUPLE TO LIST CONVERSION ---\n")

def tuple_list_conversion():
    original_tuple = (5, 15, 3, 20, 8, 25, 12, 2, 30, 7)
    print(f"Original Tuple: {original_tuple}")
    print(f"Type: {type(original_tuple).__name__}")
    
    converted_list = list(original_tuple)
    print(f"\nConverted to List: {converted_list}")
    print(f"Type: {type(converted_list).__name__}")
   
    filtered_list = [num for num in converted_list if num >= 10]
    print(f"\nAfter removing integers < 10: {filtered_list}")
   
    final_tuple = tuple(filtered_list)
    print(f"\nConverted back to Tuple: {final_tuple}")
    print(f"Type: {type(final_tuple).__name__}")

tuple_list_conversion()


# ============================================================================
# TASK 7: Student Record System
# ============================================================================
print("\n\n--- TASK 7: STUDENT RECORD SYSTEM ---\n")

class StudentRecordSystem:
    """
    A comprehensive student record system using nested dictionaries/lists
    Features:
    - Add students
    - Update marks
    - Compute averages
    - Find toppers
    """
    
    def __init__(self):
        self.students = {}
    
    def add_student(self, roll_no, name, marks):
        """
        Add a new student
        Args:
            roll_no: Student's roll number
            name: Student's name
            marks: Dictionary of subject marks
        """
        self.students[roll_no] = {
            "name": name,
            "marks": marks,
            "average": self.calculate_average(marks)
        }
        print(f"✓ Student added: {name} (Roll: {roll_no})")
    
    def calculate_average(self, marks):
        """Calculate average of marks"""
        if not marks:
            return 0
        return sum(marks.values()) / len(marks)
    
    def update_marks(self, roll_no, subject, new_mark):
        if roll_no in self.students:
            self.students[roll_no]["marks"][subject] = new_mark
            self.students[roll_no]["average"] = self.calculate_average(
                self.students[roll_no]["marks"]
            )
            print(f"✓ Updated {self.students[roll_no]['name']}'s {subject} marks to {new_mark}")
        else:
            print(f"✗ Student with roll number {roll_no} not found!")
    
    def find_toppers(self):
        if not self.students:
            print("No students in the system!")
            return
        
        max_average = max(student["average"] for student in self.students.values())
        toppers = [
            (roll_no, student["name"], student["average"])
            for roll_no, student in self.students.items()
            if student["average"] == max_average
        ]
        
        print(f"\nToppers (Average: {max_average:.2f}):")
        for roll_no, name, avg in toppers:
            print(f"  • {name} (Roll: {roll_no}) - Average: {avg:.2f}")
    
    def display_all_students(self):
        if not self.students:
            print("No students in the system!")
            return
        
        print("\n" + "=" * 70)
        print("STUDENT RECORDS")
        print("=" * 70)
        
        for roll_no, student in sorted(self.students.items()):
            print(f"\nRoll No: {roll_no}")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print(f"Average: {student['average']:.2f}")
            print("-" * 70)
    def get_statistics(self):
        if not self.students:
            print("No students in the system!")
            return
        averages = [student["average"] for student in self.students.values()]
        print("\n" + "=" * 70)
        print("STATISTICS")
        print("=" * 70)
        print(f"Total Students: {len(self.students)}")
        print(f"Highest Average: {max(averages):.2f}")
        print(f"Lowest Average: {min(averages):.2f}")
        print(f"Class Average: {sum(averages) / len(averages):.2f}")
        print("=" * 70)
print("Creating Student Record System...")
system = StudentRecordSystem()
system.add_student(101, "Aarav", {"Math": 90, "English": 85, "Science": 92})
system.add_student(102, "Priya", {"Math": 95, "English": 90, "Science": 88})
system.add_student(103, "Rohan", {"Math": 78, "English": 92, "Science": 85})
system.add_student(104, "Deepika", {"Math": 92, "English": 88, "Science": 95})
system.add_student(105, "Arjun", {"Math": 88, "English": 86, "Science": 89})
print("\nUpdating Marks...")
system.update_marks(103, "Math", 88)
system.update_marks(105, "Science", 95)
system.display_all_students()
system.find_toppers()
system.get_statistics()
print("\n\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY!")
print("=" * 80)
