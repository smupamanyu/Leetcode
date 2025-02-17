import heapq
from collections import defaultdict

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = defaultdict(dict)
        
        # Construct adjacency list
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w
        
        # Dijkstra's algorithm: (moves left, node)
        pq = [(-maxMoves, 0)]  # Max heap (negative moves for max heap behavior)
        moves_left = {0: maxMoves}
        visited = set()
        
        while pq:
            moves, node = heapq.heappop(pq)
            moves = -moves  # Convert back to positive
            
            if node in visited:
                continue
            visited.add(node)
            
            for neighbor, weight in graph[node].items():
                new_moves = moves - weight - 1  # Moves left after reaching this neighbor
                if new_moves >= 0 and new_moves > moves_left.get(neighbor, -1):
                    moves_left[neighbor] = new_moves
                    heapq.heappush(pq, (-new_moves, neighbor))
        
        # Count the reachable original nodes
        reachable_count = len(visited)
        
        # Count the reachable subdivided nodes
        for u, v, w in edges:
            max_used = min(w, moves_left.get(u, 0) + moves_left.get(v, 0))
            reachable_count += max_used
        
        return reachable_count
