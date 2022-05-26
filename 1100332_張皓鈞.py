# =========================== Question 1 ===========================
    def move(self): # 根據方向移動蛇的坐標
        #往上
        if self.dir == "up":                               
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y - self.g)
            self.snake.deQueue()
        
        #往下
        if self.dir == "down":
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y + self.g)
            self.snake.deQueue()

        #往右
        if self.dir == "right":
            self.snake.enQueue(self.snake.rear.x + self.g, self.snake.rear.y )
            self.snake.deQueue()

        #往左
        if self.dir == "left":
            self.snake.enQueue(self.snake.rear.x - self.g, self.snake.rear.y )
            self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self): # 加一個節點到玩家蛇的尾端(此方法是在蛇吃掉食物的時候被呼叫)
        
        nt = Node(self.snake.front.x, self.snake.front.y)
        if self.snake.len() == 0:
            self.snake.rear = nt
            self.snake.front = nt
        else:
            nt.next = self.snake.front
            self.snake.front.pre = nt
            self.snake.front = nt
# =========================== Question 3 ===========================
    def eat_body(self): # 吃到玩家蛇的身體
        head = self.snake.rear.pre
        headx = self.snake.rear.x
        heady = self.snake.rear.y
        while head:
            if headx == head.x and heady == head.y:
                self.snake.front = head.next
                head = None
                head.next = None
                head.pre = None
                self.play_effect("eat_body")
            else:
                head = head.pre
# =========================== Question 4 ===========================
    def eat_item(self):

        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if (self.snake.rear.x == self.itemBoxPos[0]) and (self.snake.rear.y == self.itemBoxPos[1]):#吃到道具
                item = self.item_list[random.randrange(0, 4, 1)]
                self.backpack.push(item)

                #重置
                self.itemBoxPos = None                        

# =========================== Question 5 ===========================
    def use_item(self):
        
        self.item = self.backpack.top.item
        if self.item == "FruitBasket":
            self.item_FruitBasket = True    #使用道具
            self.backpack.pop()     #用掉(消耗)
        if self.item == "BlackHole":
            self.item_BlackHole = True
            self.backpack.pop()
        if self.item == "Brake":
            self.item_Brake = True
            self.backpack.pop()
        if self.item == "Gamble":
            self.item_Gamble = True
            self.backpack.pop()