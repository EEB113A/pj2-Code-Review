# =========================== Question 1 ===========================
    def move(self):

        tmp = self.snake.front
        while tmp!=self.snake.rear: #蛇身的每一節換到其前一節的位置
            tmp.x,tmp.y = tmp.next.x,tmp.next.y     
            tmp = tmp.next
            
        if self.dir == "up" : #方向向上
            self.snake.rear.y -= self.g
        if self.dir == "down" : #方向向下
            self.snake.rear.y += self.g
        if self.dir == "left" : #方向向左
            self.snake.rear.x -= self.g
        if self.dir == "right" : #方向向右
            self.snake.rear.x += self.g
            
# =========================== Question 2 ===========================
    def add_tail(self):
        
        tmp = self.snake.front
        dirx = self.snake.front.next.x - self.snake.front.x #蛇尾方向的 X 座標
        diry = self.snake.front.next.y - self.snake.front.y #蛇尾方向的 Y 座標
        
        new = Node(self.snake.front.x - dirx,self.snake.front.y - diry) #增加的節點
        new.next = tmp
        tmp.pre = new
        self.snake.front = new
        
# =========================== Question 3 ===========================
    def eat_body(self):
        
        tmp_pre = self.snake.rear.pre
        tmp_x = self.snake.rear.x #蛇頭 X 座標
        tmp_y = self.snake.rear.y #蛇頭 Y 座標
        while tmp_pre:
            if tmp_pre.x == tmp_x and tmp_pre.y == tmp_y: #若蛇頭有跟蛇身重疊
                tmp_pre.next.pre = None
                self.snake.front = tmp_pre.next
                self.play_effect("eat_body")
            tmp_pre = tmp_pre.pre
            
# =========================== Question 4 ===========================
    def eat_item(self):
        
        item = self.item_list[random.randrange(0,4)]
        
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]: #若蛇頭座標跟道具方塊座標重疊
                self.backpack.push(item) #背包增加道具
                self.itemBoxPos = None
                
# =========================== Question 5 ===========================
    def use_item(self):
        
        self.item = self.backpack.top.item #背包中最新拿到的道具(self.item)
        if self.item == "FruitBasket":
            self.item_FruitBasket = True
            
        elif self.item == "BlackHole":
            self.item_BlackHole = True
            
        elif self.item == "Brake":
            self.item_Brake = True
            
        else:
            self.item_Gamble = True
            
        self.backpack.pop()