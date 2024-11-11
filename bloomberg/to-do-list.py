from heapq import heappush, heappop
from collections import defaultdict

class ToDoList:
    
    def __init__(self):
        self.tasks = defaultdict(list)  # Stores each user's tasks as min-heaps
        self.task_map = {}  # Maps (userId, taskId) -> (priority, original taskId)

    def addTask(self, userId: int, taskId: int, priority: int) -> None:
        # Add task to both the heap (sorted by priority) and the task_map for easy access
        heappush(self.tasks[userId], (priority, taskId))
        self.task_map[(userId, taskId)] = (priority, taskId)

    def getAllTasks(self, userId: int) -> list[int]:
        # Filter only active tasks (not completed)
        if userId not in self.tasks:
            return []
        
        # Get all tasks, filtering out those not in the task_map (completed ones)
        return [taskId for priority, taskId in self.tasks[userId] if (userId, taskId) in self.task_map]

    def completeTask(self, userId: int, taskId: int) -> None:
        # Remove task from task_map to mark it as completed
        if (userId, taskId) in self.task_map:
            del self.task_map[(userId, taskId)]