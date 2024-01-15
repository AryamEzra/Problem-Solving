class Robot:

    def __init__(self, width: int, height: int):
        self.x = 0
        self.y = 0
        self.w = width
        self.h = height
        self.dir = 0
        self.pos = [(1,0), (0,1), (-1,0), (0,-1)]
        self.compas = ["East", "North", "West", "South"]
        

    def step(self, num: int) -> None:
        
        perimeter = (self.w-1 + self.h-1) * 2
        num = num % perimeter
        if num == 0:
            num += perimeter
        
        for i in range(num):
            nx, ny = self.x + self.pos[self.dir][0], self.y + self.pos[self.dir][1] 
            while not (0 <= nx < self.w and 0 <= ny < self.h):
                self.dir = (self.dir + 1) % 4
                if self.dir % 2 == 0: # East or West
                    num = num % (self.w-1)
                else: # North or South
                    num = num % (self.h-1)
                # Find the next position of the robot
                nx, ny = self.x + self.pos[self.dir][0], self.y + self.pos[self.dir][1]
                
            self.x = nx
            self.y = ny


    def getPos(self) -> List[int]:
        return [self.x, self.y]
        
        
    def getDir(self) -> str:
        return self.compas[self.dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
