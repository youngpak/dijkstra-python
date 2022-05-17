graph = {
   'A': {'B':1.3,'E':5.4},
   'B': {'A':1.3, 'C':1.3 ,'F':5.4},
   'C': {'B':1.3, 'D': 1.3,'G':5.4},
   'D': {'C':1.3, 'I':6},
   'E': {'A':5.4, 'F':1.3,'J':1.8},
   'F': {'B':5.4, 'E':1.3,'G':1.3},
   'G': {'C':5.4,'H':1.3,'F':1.3,'O':2.4},
   'H':{'G':1.3,'I':1},
   'I':{'H':1,'D':6,'S':16},
   'J':{'E':1.8,'K':2.4},
   'K':{'J':2.4,'L':4.7},
   'L':{'K':4.7,'M':4},
   'M':{'L':4,'N':3,'Q':2},
   'N':{'M':3,'O':4.2},
   'O':{'N':4.2,'G':2.4,'P':2},
   'P':{'O':2,'Q':8.6,'R':2.5},
   'Q':{'M':2,'P':8.6},
   'R':{'P':2.5,'S':5},
   'S':{'R':5,'I':16}
}


import heapq  # 우선순위 큐 구현을 위함

def dijkstra(graph, start):
  distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
  distances[start] = 0  # 시작 값은 0이어야 함
  queue = []
  heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
        distances[new_destination] = distance
        heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
  return distances


print(dijkstra(graph, 'A'))