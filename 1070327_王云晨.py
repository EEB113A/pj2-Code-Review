# =========================== Question 1 ===========================
    def move(self):
        if self.dir == "up":                                                  #上
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y-self.g)    #蛇頭加一格
        elif self.dir == "down":                                              #下
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y+self.g)    #蛇頭加一格
        elif self.dir == "left":                                              #左
            self.snake.enQueue(self.snake.rear.x-self.g,self.snake.rear.y)    #蛇頭加一格
        elif self.dir == "right":                                             #右
            self.snake.enQueue(self.snake.rear.x+self.g,self.snake.rear.y)    #蛇頭加一格
        self.snake.deQueue()                                                  #蛇尾減一格
# =========================== Question 2 ===========================
    def add_tail(self):
        if self.dir == "up":                                                 #若往上
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y-self.g)  #尾巴下面加上Node
            Node(self.snake.rear.x,self.snake.rear.y-self.g)                 
        elif self.dir == "down":                                             #若往下
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y+self.g)  #尾巴上面加上Node
            Node(self.snake.rear.x,self.snake.rear.y+self.g)                 
        elif self.dir == "left":                                             #若往左
            self.snake.enQueue(self.snake.rear.x-self.g, self.snake.rear.y)  #尾巴右邊加上Node
            Node(self.snake.rear.x-self.g,self.snake.rear.y)                 
        elif self.dir == "right":                                            #若往右
            self.snake.enQueue(self.snake.rear.x+self.g, self.snake.rear.y)  #尾巴左邊加上Node
            Node(self.snake.rear.x+self.g,self.snake.rear.y)                 
# =========================== Question 3 ===========================
    def eat_body(self):
        bd = self.snake.front                                                # 蛇尾
        while bd != self.snake.rear.pre:                                     # 執行蛇尾到蛇頭前一格之迴圈
            if self.snake.rear.x == bd.x and self.snake.rear.y == bd.y:      # 判定蛇頭吃到身體                                 
                self.snake.front = bd.next                                   # 將蛇尾指派為身體碰處點的下一格
                self.snake.front.pre = None                                  # 碰處點之後面身體消失
                self.play_effect("eat_body")                                      
                break                                                        
            else:
                body = body.next                                             # 往蛇頭前進一格
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if  self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]: #若蛇頭吃到道具方塊
                 self.item = self.item_list[random.randrange(len(self.item_list))]                   #從item_list中隨機選一個道具
                 self.backpack.push(self.item)                                                       #將道具push到背包(Stack)中
                 self.itemBoxPos = None                                                              #道具方塊被吃到後消失
                 self.play_effect("eat_item")
# =========================== Question 5 ===========================
    def use_item(self):
        self.backpack.pop()                      #將背包之top pop掉
        if self.item == "BlackHole":             #若top為黑洞
              self.item_BlackHole = True         #發動效果
        elif self.item == "Brake":               #若top為煞車
              self.item_Brake = True             #發動效果
        elif self.item == "FruitBasket":         #若top為水果籃
              self.item_FruitBasket = True       #發動效果
        elif self.item == "Gamble":              #若top為賭博
              self.item_Gamble = True            #發動效果