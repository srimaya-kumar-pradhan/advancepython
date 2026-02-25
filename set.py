from datetime import datetime

names = set()
set1 = set()
set2 = set()

n = int(input("Enter total number of members:\n"))

for i in range(n):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = input(f"Enter your Name [{current_time}]: ")

    if name.lower() in names:
        set2.add((name, current_time))
        print(name, "is duplicate, name already exists...")
    else:
        names.add(name.lower())
        set1.add((name, current_time))
        print(name, "is an original name...")

print("\nOriginal Names:")
print([x[0] for x in set1])

print("\nDuplicate Names:")
print([x[0] for x in set2])




















