from collections import defaultdict
import sys
import heapq

input = sys.stdin.readline

num_of_points, num_of_edges = map(int, input().rstrip().split())

# 우선순위 큐 초기화 (min-heap)
queue = []
heapq.heappush(queue, (0, 1))  # (거리, 노드) 형태로 삽입
dist = [float('inf') for _ in range(num_of_points + 1)]
dist[1] = 0

graph = defaultdict(list)

for _ in range(num_of_edges):
    start, end, weight = map(int, input().rstrip().split())
    graph[start].append((end, weight))


while queue:
    cur_dist, cur_point = heapq.heappop(queue)
    for point, weight in graph[cur_point]:
        distance = cur_dist + weight
        if distance < dist[point]:
            dist[point] = distance
            heapq.heappush(queue, (distance, point))

for index in range(2, num_of_points + 1):
    if dist[index] == float('inf'):
        print(-1)
    else:
        print(dist[index])