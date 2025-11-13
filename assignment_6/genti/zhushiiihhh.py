#!/usr/bin/env python3

from sys import argv
import heapq
from project import Project 

def maximize_roi(budget: float, projects: list[Project]):
    net_profits = -(n.roi - n,cost) for n in projects
    heapq.heapify(net_profits)
    
    while budget > 0 or net_profits:
        best_roi = heapq.heapify(heap)



    return max_roi, selected_projects

if __name__ == "__main__":
    try:
        arg = int(argv[1]) if len(argv) > 1 else 1
    except:
        print("hej... kush t'ka msu kshtu more pis?! veç numra! [t'plotë, bile bile; veç 1!]")
    
    budget1 = 10000
    projects1 = [
                Project('AI Chatbot', 5000, 8000),
                Project('Mobile App', 4000, 6000),
                Project('Website Redesign', 3000, 4000),
                Project('Cloud Migration', 6000, 9000),
            ]

    bugdet = budget1
    projects = projects1

    max_roi, selected_projects = maximize_roi(budget, projects)
