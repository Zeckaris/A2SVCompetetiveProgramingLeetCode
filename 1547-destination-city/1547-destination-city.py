class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_count = {}
        for start, dest in paths:
            city_count[start] = city_count.get(start, 0) + 1
            city_count[dest] = city_count.get(dest, 0)  
            
        for city in city_count:
            if city_count[city] == 0:
                return city
        