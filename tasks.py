from storage import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, description):
        task = {"id": len(self.tasks)+1, "desc": description, "done": False}
        self.tasks.append(task)
        save_tasks(self.tasks)
        print("✅ Task added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            status = "✅" if task["done"] else "❌"
            print(f"{task['id']}. {task['desc']} - {status}")

    def mark_done(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                save_tasks(self.tasks)
                print("✔️ Task marked as done.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        # Reassign IDs
        for idx, task in enumerate(self.tasks):
            task["id"] = idx + 1
        save_tasks(self.tasks)
        print("🗑️ Task deleted.")
