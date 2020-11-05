from todolist.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = list()

    def add_task(self, new_task: Task):
        if new_task in [t for t in self.tasks]:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for t in self.tasks:
            if t.name == task_name:
                t.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        res = ""
        res += f"Section {self.name}:\n"
        for t in self.tasks:
            res += f"{t.details()}\n"

        return res




