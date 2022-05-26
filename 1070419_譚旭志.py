# =========================== Question 1 ===========================
    def move(self):
        if self.dir == "up":
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y - self.g)    # 收到為up在蛇頭上方增加一格
        elif self.dir == "down":
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y + self.g)    # 收到為down在蛇頭下方增加一格
        elif self.dir == "left":
            self.snake.enQueue(self.snake.rear.x - self.g, self.snake.rear.y)    # 收到為left在蛇頭左方增加一格
        elif self.dir == "right":
            self.snake.enQueue(self.snake.rear.x + self.g, self.snake.rear.y)    # 收到為right在蛇頭右方增加一格
        self.snake.deQueue()    # 將蛇尾減少一格

# =========================== Question 2 ===========================
    def add_tail(self):
        if self.snake.front.next.x == self.snake.front.x:
            if self.snake.front.next.y == self.snake.front.y - self.g:
                new = Node(self.snake.front.x, self.snake.front.y + self.g)    # 檢測蛇尾的前一格在上方，Node設在在蛇尾下方一格
            elif self.snake.front.next.y == self.snake.front.y + self.g:
                new = Node(self.snake.front.x, self.snake.front.y - self.g)    # 檢測蛇尾的前一格在下方，Node設在在蛇尾上方一格
        elif self.snake.front.next.y == self.snake.front.y:
            if self.snake.front.next.x == self.snake.front.x - self.g:
                new = Node(self.snake.front.x + self.g, self.snake.front.y)    # 檢測蛇尾的前一格在左方，Node設在在蛇尾右方一格
            elif self.snake.front.next.x == self.snake.front.x + self.g:
                new = Node(self.snake.front.x - self.g, self.snake.front.y)    # 檢測蛇尾的前一格在右方，Node設在在蛇尾左方一格
        
        # 將新的Node加在蛇尾
        new.next = self.snake.front
        self.snake.front.pre = new
        self.snake.front = new

# =========================== Question 3 ===========================
    def eat_body(self):
        body = self.snake.front                                                # 紀錄蛇尾資訊
        while body != self.snake.rear.pre:                                     # 執行迴圈直到蛇頭後一格
            if body.x == self.snake.rear.x and body.y == self.snake.rear.y:    # 判定蛇頭經過身體
                self.play_effect("eat_body")                                   # 撥放音樂
                self.snake.front = body.next                                   # 將蛇尾變為碰處點的下一格
                self.snake.front.pre = None                                    # 蛇尾前一格設為None
                break                                                          # 中斷迴圈
            else:
                body = body.next                                               # 再繼續往蛇頭進一格

# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.itemBoxPos[0] == self.snake.rear.x and self.itemBoxPos[1] == self.snake.rear.y:    # 判定蛇頭經過道具位置
                self.backpack.push(self.item_list[random.randrange(1, 4)])                             # 將四種道具隨機選一樣到背包
                self.play_effect("eat_item")                                                           # 撥放音樂
                self.itemBoxPos = None                                                                 # 道具方塊座標重設成None

# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item    # 把self.item設為背包裡最後得到的物品
        if self.item == "BlackHole":
            self.item_BlackHole = True        # 如果是黑洞就將其設為True
        elif self.item == "Gamble":
            self.item_Gamble = True           # 如果是賭博就將其設為True
        elif self.item == "Brake":
            self.item_Brake = True            # 如果是剎車就將其設為True
        elif self.item == "FruitBasket":
            self.item_FruitBasket = True      # 如果是水果籃就將其設為True
        self.backpack.pop()                   # 將背包裡最後得到的物品移除