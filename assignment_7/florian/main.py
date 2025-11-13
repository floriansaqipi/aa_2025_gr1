from typing import List, Dict, Optional, Set

employees = [
    {"id": 1, "name": "Alice Johnson", "position": "CEO", "salary": 250000, "supervisor_id": None},
    {"id": 2, "name": "Bob Smith", "position": "CTO", "salary": 180000, "supervisor_id": 1},
    {"id": 3, "name": "Carol White", "position": "CFO", "salary": 175000, "supervisor_id": 1},
    {"id": 4, "name": "David Brown", "position": "Engineering Manager", "salary": 140000, "supervisor_id": 2},
    {"id": 5, "name": "Eve Davis", "position": "QA Manager", "salary": 130000, "supervisor_id": 2},
    {"id": 6, "name": "Frank Wilson", "position": "Senior Accountant", "salary": 95000, "supervisor_id": 3},
    {"id": 7, "name": "Grace Lee", "position": "Senior Developer", "salary": 120000, "supervisor_id": 4},
    {"id": 8, "name": "Henry Martinez", "position": "Junior Developer", "salary": 85000, "supervisor_id": 4},
    {"id": 9, "name": "Ivy Chen", "position": "QA Engineer", "salary": 90000, "supervisor_id": 5},
    {"id": 10, "name": "Jack Thompson", "position": "DevOps Engineer", "salary": 110000, "supervisor_id": 4},
    {"id": 11, "name": "Kelly Anderson", "position": "Junior Accountant", "salary": 65000, "supervisor_id": 6},
    {"id": 12, "name": "Liam Garcia", "position": "Intern Developer", "salary": 50000, "supervisor_id": 7},
]


class EmployeeDepthCalculator:
    def __init__(self, employees: List[Dict]):
        self.supervisor_by_id: Dict[int, Optional[int]] = {}
        for e in employees:
            self.supervisor_by_id[e["id"]] = e["supervisor_id"]

        self.depth_cache: Dict[int, int] = {}

    def get_employee_depth(self, employee_id: int) -> int:
        return self._get_depth_recursive(employee_id, set())

    def _get_depth_recursive(self, employee_id: int, path: Set[int]) -> int:
        if employee_id not in self.supervisor_by_id:
            return -1

        if employee_id in self.depth_cache:
            return self.depth_cache[employee_id]

        if employee_id in path:
            for eid in path:
                self.depth_cache[eid] = -1
            return -1

        path.add(employee_id)

        supervisor_id = self.supervisor_by_id[employee_id]

        if supervisor_id is None:
            depth = 0
        else:
            supervisor_depth = self._get_depth_recursive(supervisor_id, path)
            if supervisor_depth == -1:
                depth = -1
            else:
                depth = supervisor_depth + 1

        path.remove(employee_id)
        self.depth_cache[employee_id] = depth
        return depth


calculator = EmployeeDepthCalculator(employees)

print(calculator.get_employee_depth(1))   # 0  (Alice - CEO)
print(calculator.get_employee_depth(2))   # 1  (Bob - CTO)
print(calculator.get_employee_depth(7))   # 3  (Grace - Senior Developer)
print(calculator.get_employee_depth(12))  # 4  (Liam - Intern)
print(calculator.get_employee_depth(999)) # -1 (not found)
