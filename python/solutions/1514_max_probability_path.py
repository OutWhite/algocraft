import heapq
from collections import defaultdict
from typing import List


class Solution:
      def maxProbability(
          self,
          n: int,
          edges: List[List[int]],
          succProb: List[float],
          start_node: int,
          end_node: int,
      ) -> float:
          graph = defaultdict(list)

          for (a, b), p in zip(edges, succProb):
              graph[a].append((b, p))
              graph[b].append((a, p))

          best = [0.0] * n
          best[start_node] = 1.0

          heap = [(-1.0, start_node)]

          while heap:
              neg_prob, node = heapq.heappop(heap)
              prob = -neg_prob

              if node == end_node:
                  return prob

              if prob < best[node]:
                  continue

              for nei, edge_prob in graph[node]:
                  next_prob = prob * edge_prob

                  if next_prob > best[nei]:
                      best[nei] = next_prob
                      heapq.heappush(heap,(-next_prob, nei))

          return 0.0