from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp_len = len(stamp)
        target_len = len(target)
        s = list(target)

        res: List[int] = []
        visited = [False] * (target_len - stamp_len + 1)
        stars = 0

        def can_stamp(pos: int) -> bool:
            made_change = False
            for j in range(stamp_len):
                if s[pos + j] == '?':
                    continue
                if s[pos + j] != stamp[j]:
                    return False
                made_change = True
            return made_change

        def do_stamp(pos: int) -> None:
            nonlocal stars
            for j in range(stamp_len):
                if s[pos + j] != '?':
                    s[pos + j] = '?'
                    stars += 1

        while stars < target_len:
            changed_in_this_round = False

            for i in range(target_len - stamp_len + 1):
                if not visited[i] and can_stamp(i):
                    do_stamp(i)
                    visited[i] = True
                    changed_in_this_round = True
                    res.append(i)
                    if stars == target_len:
                        break

            if not changed_in_this_round:
                return []

        res.reverse()

        if len(res) > 10 * target_len:
            return []

        return res


def simulate(stamp: str, target: str, moves: List[int]) -> str:
    s = list('?' * len(target))
    m = len(stamp)
    n = len(target)

    for pos in moves:
        if pos < 0 or pos + m > n:
            raise ValueError(f"Invalid move position: {pos}")
        for j in range(m):
            s[pos + j] = stamp[j]
    return ''.join(s)


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("abc", "ababc"),
        ("abca", "aabcaca"),
        ("a", "aaaa"),
        ("ab", "ababab"),
        ("xyz", "xyz"),
        ("abc", "xyz"),
    ]

    for stamp, target in tests:
        moves = sol.movesToStamp(stamp, target)
        print(f"stamp = {stamp!r}, target = {target!r}")
        print(f"  moves: {moves}")
        if moves:
            result = simulate(stamp, target, moves)
            print(f"  simulated result: {result!r}, correct: {result == target}")
        else:
            print("  No solution (empty moves list).")
        print("-" * 60)
