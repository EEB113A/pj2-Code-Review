# =========================== Question 1 ===========================
    def move(self):
        #設置當按下往上鍵，並且往上走
        if self.dir == "up":
           self.snake.enQueue(self.snake.rear.x, self.snake.rear.y-self.g)
           self.snake.deQueue()

        #設置當按下往下鍵，並且往下走
        if self.dir == "down":
           self.snake.enQueue(self.snake.rear.x, self.snake.rear.y+self.g)
           self.snake.deQueue()

        #設置當按下往左鍵，並且往左走
        if self.dir == "left":
           self.snake.enQueue(self.snake.rear.x-self.g, self.snake.rear.y)
           self.snake.deQueue()

        #設置當按下往右鍵，並且往右走
        if self.dir == "right":
           self.snake.enQueue(self.snake.rear.x+self.g, self.snake.rear.y)
           self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self):
        #此if是幫助判斷是否在最後蛇尾往上要新增一個節點
        if self.snake.front.next.x == self.snake.front.x and self.snake.front.next.y-self.g == self.snake.front.y:
            new = Node(self.snake.front.x,self.snake.front.y-self.g)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new

        #此if是幫助判斷是否在最後蛇尾往下要新增一個節點
        if self.snake.front.next.x == self.snake.front.x and self.snake.front.next.y+self.g == self.snake.front.y:
            new = Node(self.snake.front.x,self.snake.front.y+self.g)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new

        #此if是幫助判斷是否在最後蛇尾往左要新增一個節點
        if self.snake.front.next.x-self.g == self.snake.front.x and self.snake.front.next.y == self.snake.front.y:
            new = Node(self.snake.front.x-self.g,self.snake.front.y)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new
        
        #此if是幫助判斷是否在最後蛇尾往右要新增一個節點
        if self.snake.front.next.x+self.g == self.snake.front.x and self.snake.front.next.y == self.snake.front.y:
            new = Node(self.snake.front.x+self.g,self.snake.front.y)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new
# =========================== Question 3 ===========================
    def eat_body(self):
        #先定義蛇頭
        cur = self.snake.front
        #這段為判斷蛇尾到蛇頭是否有一樣的點，若有就減去
        while cur != None and cur != self.snake.rear:
            if cur.x == self.snake.rear.x and cur.y == self.snake.rear.y:
                cur.next.pre = None
                self.snake.front = cur.next
                self.play_effect("eat_body")
                break
            cur = cur.next
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            #這邊if為如果蛇頭得位置剛好等於黃色方塊的話就判定為蛇吃到黃色方塊
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:
                #這邊將蛇吃完方塊，所以方塊移除
                self.itemBoxPos = None
                #當吃到方塊隨即播放eat_item音樂
                self.play_effect("eat_item")
                #並且以隨機的方式將其中一種道具放進背包
                self.backpack.push(self.item_list[random.randrange(0,3)])
# =========================== Question 5 ===========================
    def use_item(self):
        #因應題目堆疊方式，所以最後放進的道具會最先被玩家使用
        self.item = self.backpack.top.item
        if self.item == "Brake":        #如果玩家最後拿到的道具是煞車，此if要先使用此道具
            self.item_Brake = True
            self.backpack.pop()
        if self.item == "BlackHole":    #如果玩家最後拿到的道具是黑洞，此if要先使用此道具
            self.item_BlackHole = True
            self.backpack.pop()
            
        if self.item == "Gamble":       #如果玩家最後拿到的道具是賭博，此if要先使用此道具
            self.item_Gamble = True
            self.backpack.pop()
        
        if self.item == "FruitBasket":  #如果玩家最後拿到的道具是水果籃，此if要先使用此道具
            self.item_FruitBasket = True
            self.backpack.pop()