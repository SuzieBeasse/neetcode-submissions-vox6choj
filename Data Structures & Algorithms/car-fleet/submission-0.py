class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            pos = position[i]
            sp = speed[i]
            t = (target - pos) / sp
            cars.append((pos, sp, t))
        cars.sort()
        # print(cars)
        ans = 0
        while cars:
            pos, sp, t = cars.pop()
            ans += 1
            while cars and cars[-1][2] <= t:
                cars.pop()
        return ans