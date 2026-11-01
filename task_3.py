import heapq
import random
import time


def min_cost_list(cables):
    cables = list(cables)
    total = 0
    while len(cables) > 1:
        cables.sort()
        a = cables.pop(0)
        b = cables.pop(0)
        cost = a + b
        total += cost
        cables.append(cost)
    return total


def min_cost_heap(cables):
    heap = list(cables)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total += cost
        heapq.heappush(heap, cost)
    return total


def benchmark(n):
    data = [random.randint(1, 1000) for _ in range(n)]

    t = time.perf_counter()
    r1 = min_cost_list(data)
    t_list = time.perf_counter() - t

    t = time.perf_counter()
    r2 = min_cost_heap(data)
    t_heap = time.perf_counter() - t

    assert r1 == r2
    print(f"n={n:>6} | list: {t_list:.4f}  | heapq: {t_heap:.4f} | "
          f"time: {r1} | fast: x{t_list / t_heap:.1f}")


if __name__ == "__main__":
    print(min_cost_list([4, 3, 2, 6]), min_cost_heap([4, 3, 2, 6]))

    for n in (10_000, 50_000, 100_000, 200_000):
        benchmark(n)