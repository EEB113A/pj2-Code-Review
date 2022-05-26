# =========================== Question 1 ===========================
    def move(self):
        if self.dir=="up":                      # 上
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y-self.g)
            self.snake.deQueue()
        if self.dir=="down":                    # 下
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y+self.g)
            self.snake.deQueue()
        if self.dir=="left":                    # 左
            self.snake.enQueue(self.snake.rear.x-self.g,self.snake.rear.y)
            self.snake.deQueue()
        if self.dir=="right":                   # 右
            self.snake.enQueue(self.snake.rear.x+self.g,self.snake.rear.y)
            self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self):
        nodex = Node(0,0)
        nodex.next = self.snake.front.next
        nodex.pre = self.snake.front
        self.snake.front.next.pre = nodex
        self.snake.front.next = nodex
# =========================== Question 3 ===========================
    def eat_body(self):
        cur = self.snake.front
        while cur != None and cur != self.snake.rear:                       # 從尾端往頭部找
            if cur.x == self.snake.rear.x and cur.y == self.snake.rear.y:   # 如果頭的index等於身體的index
                cur.next.pre = None                                         # 則身體到尾巴都消除
                self.snake.front = cur.next
                self.play_effect("eat_body")
                break
            cur = cur.next
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]: # 頭部座標等於黃色問號
                self.itemBoxPos = None                                                              # 方塊消失
                self.play_effect("eat_item")                                                        # 放音樂
                self.backpack.push(self.item_list[random.randrange(0,3)])                           # 從item_list(4個)中隨機得到一個道具放入背包

# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item              # 找到最新拿到的item
        if self.item == "BlackHole":                    # 如果最上面的是BlachHole
            self.item_BlackHole = True                  # 讓它=True，使用(執行)
            self.backpack.pop() 
        if self.item == "Brake":                        # 如果最上面的是Brake
            self.item_Brake = True                      # 讓它=True，使用(執行)
            self.backpack.pop()
        if self.item == "FruitBasket":                  # 如果最上面的是FruitBasket
            self.item_FruitBasket = True                # 讓它=True，使用(執行)
            self.backpack.pop()
        if self.item == "Gamble":                       # 如果最上面的是Gamble
            self.item_Gamble = True                     # 讓它=True，使用(執行)
            self.backpack.pop()