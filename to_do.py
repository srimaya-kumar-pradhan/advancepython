class Task:
    def __init__(self, title, deadline, priority, category):
        self.title = title
        self.deadline = deadline
        self.priority = priority
        self.category = category


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline, priority, category):
        task = Task(title, deadline, priority, category)
        self.tasks.append(task)
        print("Task added successfully")

    def show_all_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available")
        else:
            for task in self.tasks:
                print("Task:", task.title)
                print("Deadline:", task.deadline)
                print("Priority:", task.priority)
                print("Category:", task.category)
                print("------------------")

    def filter_by_category(self, category):
        print("Tasks in category:", category)
        for task in self.tasks:
            if task.category == category:
                print(task.title, "-", task.deadline, "-", task.priority)


todo = TodoList()

todo.add_task("Complete Assignment", "10 Mar", "High", "College")
todo.add_task("Buy Groceries", "9 Mar", "Medium", "Personal")
todo.add_task("Project Meeting", "11 Mar", "High", "College")

print("\nAll Tasks:")
todo.show_all_tasks()

print("\nFiltered Tasks:")
todo.filter_by_category("College")