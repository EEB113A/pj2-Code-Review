# =========================== Question 1 ===========================
    def move(self): 
        dir = {"up": 0, "right":1, "down": 2, "left": 3}
        dx = (0, 1, 0, -1)
        dy = (-1, 0, 1, 0)
        dir_ = dir[self.dir]
        head = self.snake.rear
        self.snake.enQueue(head.x + dx[dir_]*self.g, head.y + dy[dir_]*self.g)
        self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self): 
         dir = {"up": 0, "right":1, "down": 2, "left": 3}
        dx = (0, 1, 0, -1)
        dy = (-1, 0, 1, 0)
        dir_ = dir[self.dir]
        head = self.snake.rear
        self.snake.enQueue(head.x + dx[dir_]*self.g, head.y + dy[dir_]*self.g)
# =========================== Question 3 ===========================
    def eat_body(self): 
        same = lambda a, b: a.x == b.x and a.y == b.y

        head = self.snake.rear
        cnt = 0

        while True:
            p = self.snake.front
            self.snake.enQueue(p.x, p.y)
            self.snake.deQueue()
            cnt += 1
            if(same(head, p)): break
        if cnt >= self.snake.len(): return
        self.snake.reverse()
        for i in range(cnt):
            self.snake.deQueue()
        self.snake.reverse()
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            i = random.randint(0, len(self.item_list)-1)
            self.backpack.push(self.item_list[i])
            self.itemBoxPos = None

        if self.itemBoxPos != None: # 若道具方塊有顯現的話

# =========================== Question 5 ===========================
    def use_item(self): # 使用道具
        self.item = self.backpack.top.item
        self.backpack.pop()
        if(self.item == None): return
        if(self.item == "BlackHole"): self.item_BlackHole = True
        if(self.item == "Gamble"): self.item_Gamble = True
        if(self.item == "Brake"): self.item_Brake = True
        if(self.item == "FruitBasket"): self.item_FruitBasket = True