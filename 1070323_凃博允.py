# =========================== Question 1 ===========================
    def move(self):
        if self.dir == "right":#input為右
            self.snake.enQueue(self.snake.rear.x+self.g, self.snake.rear.y) #在頭新增一塊
            self.snake.deQueue() #在尾巴減去一塊
        elif self.dir == "left":#input為左
            self.snake.enQueue(self.snake.rear.x-self.g, self.snake.rear.y)#在頭新增一塊
            self.snake.deQueue()#在尾巴減去一塊
        elif self.dir == "up": #input為上
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y-self.g)#在頭新增一塊
            self.snake.deQueue()#在尾巴減去一塊

        elif self.dir == "down":#input為下
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y+self.g)#在頭新增一塊
            self.snake.deQueue()#在尾巴減去一塊
# =========================== Question 2 ===========================
    def add_tail(self):
        if self.dir == "right":#input為右
            self.snake.enQueue(self.snake.rear.x+self.g, self.snake.rear.y)#若為往右，則在尾巴左邊加上
            Node(self.snake.rear.x-self.g,self.snake.rear.y)
            
        elif self.dir == "left":#input為左
            self.snake.enQueue(self.snake.rear.x-self.g, self.snake.rear.y)#若為往左，則在尾巴右邊加上
            Node(self.snake.rear.x+self.g,self.snake.rear.y)
        elif self.dir == "up":#input為上
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y-self.g)#若為往上，則在尾巴下邊加上
            Node(self.snake.rear.x,self.snake.rear.y+self.g)
            

        elif self.dir == "down":#input為下
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y+self.g)#若為往下，則在尾巴上邊加上
            Node(self.snake.rear.x,self.snake.rear.y-self.g)
# =========================== Question 3 ===========================
    def eat_body(self):
        return 0
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x==self.itemBoxPos[0] and self.snake.rear.y==self.itemBoxPos[1]:#若蛇頭有吃到方塊
                self.item=self.item_list[random.randrange(len(self.item_list))] #將list道具中隨機抽一個
                self.backpack.push(self.item)#放入stack
                self.itemBoxPos= None#被吃到的方塊消失
# =========================== Question 5 ===========================
    def use_item(self):
        
        self.backpack.pop()#將頂端pop掉
        if self.item == "BlackHole":#若頂端為黑洞
              self.item_BlackHole = True#發動效果
        elif self.item == "Brake":#發動效果
              self.item_Brake = True#若頂端為煞車
        elif self.item == "FruitBasket":#若頂端為水果籃
              self.item_FruitBasket = True #發動效果
        elif self.item == "Gamble":#若頂端為賭博
              self.item_Gamble = True#發動效果