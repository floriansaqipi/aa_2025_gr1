#!/bin/usr/env python3

from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0

        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(i)

        if source not in stop_to_buses or target not in stop_to_buses:
            return -1

        queue = deque()
        visited_buses = set()
        target_buses = set(stop_to_buses[target])

        for start_bus in stop_to_buses[source]:
            queue.append((start_bus, 1))
            visited_buses.add(start_bus)

        while queue:
            current_bus, cost = queue.popleft()

            if current_bus in target_buses:
                return cost

            for stop in routes[current_bus]:
                for next_bus in stop_to_buses[stop]:
                    if next_bus not in visited_buses:
                        visited_buses.add(next_bus)
                        queue.append((next_bus, cost + 1))
        
        return -1
