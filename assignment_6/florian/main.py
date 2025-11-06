from typing import List, Dict, Any


def maximizeROI(budget: int, projects: List[Dict[str, int]]) -> Dict[str, Any]:
    n = len(projects)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = projects[i - 1]["cost"]
        roi = projects[i - 1]["roi"]

        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]

            if cost <= b:
                candidate = dp[i - 1][b - cost] + roi
                if candidate > dp[i][b]:
                    dp[i][b] = candidate

    maxROI = dp[n][budget]

    selected_projects = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            project = projects[i - 1]
            selected_projects.append(project["name"])
            b -= project["cost"]

    selected_projects.reverse()

    return {
        "maxROI": maxROI,
        "selectedProjects": selected_projects
    }

budget1 = 10000
projects1 = [
    {"name": "AI Chatbot",        "cost": 5000, "roi": 8000},
    {"name": "Mobile App",        "cost": 4000, "roi": 6000},
    {"name": "Website Redesign",  "cost": 3000, "roi": 4000},
    {"name": "Cloud Migration",   "cost": 6000, "roi": 9000},
]

print(maximizeROI(budget1, projects1))

budget2 = 15000
projects2 = [
    {"name": "CRM System",       "cost": 8000, "roi": 12000},
    {"name": "Analytics Tool",   "cost": 5000, "roi": 7000},
    {"name": "Security Upgrade", "cost": 7000, "roi": 10000},
    {"name": "API Development",  "cost": 4000, "roi": 5000},
]

print(maximizeROI(budget2, projects2))
