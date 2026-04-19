class TaskManager:
	def __init__(self):
		self.tasks = []

	def add_task(self, description):
		task = Task(description)
		self.tasks.append(task)
		return task

	def list_tasks(self):
		return [task.to_dict() for task in self.tasks]

	def mark_task_done(self, index):
		if index < 0 or index >= len(self.tasks):
			raise IndexError("Task index out of range")

		self.tasks[index].mark_done()

class Task:
	def __init__(self, description):
		self.description = description.strip()
		if not self.description:
			raise ValueError("Task description cannot be empty")
		self.done = False

	def mark_done(self):
		self.done = True

	def to_dict(self):
		return {"description": self.description, "done": self.done}

	def __str__(self):
		return f"{'[x]' if self.done else '[ ]'} {self.description}"


if __name__ == "__main__":
	manager = TaskManager()
	manager.add_task("Buy groceries")
	manager.add_task("Read 20 pages")
	manager.mark_task_done(0)

	print("Tasks as dictionaries:")
	print(manager.list_tasks())

	print("\nTasks as strings:")
	for task in manager.tasks:
		print(task)

