class LRUCache:
    def __init__(self, capacity: int):
        # Your code here
        pass
    
    def get(self, key: int) -> int:
        # Your code here
        pass
    
    def put(self, key: int, value: int) -> None:
        # Your code here
        pass

# Read and process operations
capacity = int(input())
cache = LRUCache(capacity)
n = int(input())
results = []
for _ in range(n):
    op = input().split()
    if op[0] == 'get':
        results.append(str(cache.get(int(op[1]))))
    else:
        cache.put(int(op[1]), int(op[2]))
print('\n'.join(results))