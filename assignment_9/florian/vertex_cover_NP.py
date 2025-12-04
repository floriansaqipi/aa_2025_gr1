from itertools import combinations

def is_vertex_cover(vertices, edges, cover):
    cover_set = set(cover)
    for u, v in edges:
        if u not in cover_set and v not in cover_set:
            return False
    return True


def minimum_vertex_cover_bruteforce(vertices, edges):
    n = len(vertices)

    for k in range(n + 1):
        for subset in combinations(vertices, k):
            if is_vertex_cover(vertices, edges, subset):
                return subset

    return None


if __name__ == "__main__":
    vertices = ["Alice", "Bob", "Carol", "David", "Eve", "Frank",
                "Grace", "Heidi", "Ivan", "Judy"]

    edges = [
        ("Alice", "Bob"),
        ("Alice", "Carol"),
        ("Bob", "David"),
        ("Carol", "David"),
        ("Carol", "Eve"),
        ("David", "Frank"),
        ("Eve", "Frank"),
        ("Eve", "Grace"),
        ("Frank", "Heidi"),
        ("Grace", "Heidi"),
        ("Heidi", "Ivan"),
        ("Grace", "Ivan"),
        ("Ivan", "Judy"),
        ("Frank", "Judy"),
    ]

    best_cover = minimum_vertex_cover_bruteforce(vertices, edges)
    print("Minimum vertex cover:", best_cover, "size =", len(best_cover))

    """
        Time Complexity:
            O(2^V * E)

        Space Complexity:
            O(V + E)
    """
