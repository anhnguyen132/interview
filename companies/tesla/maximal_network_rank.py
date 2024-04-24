# https://leetcode.com/problems/maximal-network-rank/

from typing import List


def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    """
    Calculate the # edges into each node first (i.e. rank)
    then for each pair of cities, add their ranks tgt
    then go thru the roads again to substract any double counted rank

    m = # roads
    Time O(n**2 + m) since must traverse roads twice and must go thru each pair of cities
    Space O(n ** 2) since keeping track of each pair of cities
    --> Optz: Space O(m) if use hash set to store roads
    """
    # Space optz
    ranks = [0] * n  # rank of cities
    for c1, c2 in roads:
        ranks[c1] += 1
        ranks[c2] += 1

    roads_set = set()
    for c1, c2 in roads:
        roads_set.add((c1, c2))
    curMaxNetworkRank = 0
    for c1 in range(n):
        for c2 in range(n):
            if c1 < c2:
                curNetworkRank = (
                    ranks[c1]
                    + ranks[c2]
                    - ((c1, c2) in roads_set or (c2, c1) in roads_set)
                )
                curMaxNetworkRank = max(curMaxNetworkRank, curNetworkRank)

    return curMaxNetworkRank

    # ranks = [0] * n  # rank of cities
    # for c1, c2 in roads:
    #     ranks[c1] += 1
    #     ranks[c2] += 1

    # network_ranks = {}
    # for c1 in range(n):
    #     for c2 in range(n):
    #         if c1 < c2:
    #             network_ranks[(c1, c2)] = ranks[c1] + ranks[c2]

    # for c1, c2 in roads:
    #     road = (min(c1, c2), max(c1, c2))
    #     if road in network_ranks:
    #         network_ranks[road] -= 1
    # return max(network_ranks.values())


print(maximalNetworkRank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]]) == 4)
print(
    maximalNetworkRank(n=5, roads=[[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]) == 5
)
print(
    maximalNetworkRank(n=8, roads=[[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]) == 5
)

print(maximalNetworkRank(n=2, roads=[[1, 0]]) == 1)
