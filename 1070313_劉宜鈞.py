# =========================== Question 1 ===========================
    def move(self):
        if self.dir=="up": #如果是按"上鍵"，就改變行進的方向
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y-self.g)
            self.snake.deQueue()
        
        if self.dir=="down": #如果是按"下鍵"，就改變行進的方向
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y+self.g)
            self.snake.deQueue()
        
        if self.dir=="left": #如果是按"左鍵"，就改變行進的方向
            self.snake.enQueue(self.snake.rear.x-self.g, self.snake.rear.y)
            self.snake.deQueue()
            
        if self.dir=="right": #如果是按"右鍵"，就改變行進的方向
            self.snake.enQueue(self.snake.rear.x+self.g, self.snake.rear.y)
            self.snake.deQueue()


# =========================== Question 2 ===========================
    def add_tail(self):
        #當要在蛇的尾端往上新增一個節點
        if self.snake.front.next.x==self.snake.front.x and self.snake.front.next.y-self.g==self.snake.front.y:
            new = Node(self.snake.front.x,self.snake.front.y-self.g)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new
        #當要在蛇的尾端往下新增一個節點
        if self.snake.front.next.x==self.snake.front.x and self.snake.front.next.y+self.g==self.snake.front.y:
            new = Node(self.snake.front.x,self.snake.front.y+self.g)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new
        #當要在蛇的尾端往左新增一個節點
        if self.snake.front.next.x-self.g==self.snake.front.x and self.snake.front.next.y==self.snake.front.y:
            new = Node(self.snake.front.x-self.g,self.snake.front.y)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new
        #當要在蛇的尾端往右新增一個節點
        if self.snake.front.next.x+self.g==self.snake.front.x and self.snake.front.next.y==self.snake.front.y:
            new = Node(self.snake.front.x+self.g,self.snake.front.y)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new
# =========================== Question 3 ===========================
    def eat_body(self):
        cur=self.snake.front #設蛇尾的節點
        # index從蛇尾往蛇頭跳，如果蛇頭之index等於蛇身之index，蛇身到蛇尾全部消失
        while cur!=None and cur!=self.snake.rear:
            if cur.x==self.snake.rear.x and cur.y==self.snake.rear.y:
                cur.next.pre=None
                self.snake.front=cur.next
                self.play_effect("eat_body")
                break
            cur=cur.next
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: #如果道具方塊有出現在地圖上
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]: #如果蛇頭之座標等於道具方塊座標=>設有吃到方塊
               self.itemBoxPos=None #道具方塊消失
               self.play_effect("eat_item") #撥放音效
               self.backpack.push(self.item_list[random.randrange(0,3)]) #從item_list中之4個道具，隨機選擇其中一個放到背包裡

# =========================== Question 5 ===========================
    def use_item(self):
        self.item=self.backpack.top.item #找出背包中最新拿到的道具=>設為要使用的那一個
        if self.item=="BlackHole": #假如最頂端的道具是BlackHole，讓它為True，並且執行
            self.item_BlackHole = True
            self.backpack.pop()
            
        if self.item=="Brake":#假如最頂端的道具是Brake，讓它為True，並且執行
            self.item_Brake = True
            self.backpack.pop()
        
        if self.item=="FruitBasket":#假如最頂端的道具是FruitBasket，讓它為True，並且執行
            self.item_FruitBasket = True
            self.backpack.pop()
        
        if self.item=="Gamble":#假如最頂端的道具是Gamble，讓它為True，並且執行
            self.item_Gamble = True
            self.backpack.pop()