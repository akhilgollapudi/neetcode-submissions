class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet_time_stack = []

        cars = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])

        cars.sort(reverse=True)

        for i in range(len(cars)):
            distance = target - cars[i][0]
            time = distance/cars[i][1]
            if not fleet_time_stack:
                fleet_time_stack.append(time)
            elif time > fleet_time_stack[-1]:
                fleet_time_stack.append(time)
            else:
                pass
                            
        return len(fleet_time_stack)

