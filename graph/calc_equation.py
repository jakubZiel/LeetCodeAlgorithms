from typing import List, Dict, Optional, Tuple

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    if len(equations) <= 0:
        return []

    if len(queries) <= 0:
        return []

    EDGES = len(equations)
    QUERIES = len(queries)

    graph: Dict[str, Dict[str, float]] = {}
    
    for edge_index in range(0, EDGES):
        src = equations[edge_index][0]
        dst = equations[edge_index][1]
        rate = values[edge_index]

        if src in graph:
            graph[src][dst] = rate
        else:
            graph[src] = {dst: rate}

    def get_ratio(top: str, bottom:str) -> Optional[float]:
        try:
            ratio = graph[top][bottom]

        except:
            if ratio is None:
                ratio = graph[bottom][top]
                ratio = 1 / ratio if ratio is not None else None

        return ratio
    
    results: List[Tuple[str, str, str, str, float]] = []

    for query in queries:
        results.append((query[0], query[1], None, None, 1.0))

    queue: List[Tuple[str, str]] = [(equations[0][0], equations[0][1])]

    visited = set()

    while queue:
        top, bottom = queue.pop()

        if bottom in visited:
            continue

        for result_index in range(0, QUERIES):
            beg_top, beg_bottom, curr_top, curr_bottom, value = results[result_index]

            if beg_top == curr_top and beg_bottom == curr_bottom:
                continue    
        
        if curr_top is None or curr_bottom is None:
            pass
        else:
            pass
            
        visited.add(bottom)

    return results


equations = [["a","b"],["b","c"]]
values = [2.0,3.0] 
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

# equations = [["a","b"],["b","c"],["bc","cd"]] 
# values = [1.5,2.5,5.0] 
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

print(calcEquation(equations, values, queries))