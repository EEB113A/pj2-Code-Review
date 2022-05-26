# =========================== Question 1 ===========================
    def move(self): 
        #設立頭的座標
        headx = self.snake.rear.x 
        heady = self.snake.rear.y
        #控制
        #原理:self.snake.enQueue(headx, heady)是加入新的頭節點，藉此完成移動效果
        if self.dir == "down":
            heady += self.g 
            self.snake.enQueue(headx, heady) 
            self.snake.deQueue()
        if self.dir == "up":
            heady -= self.g
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()
        if self.dir == "left":
            headx -= self.g
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()
        if self.dir == "right":
            headx += self.g
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self): 
        #尾巴座標
        tailx = self.snake.front.x
        taily = self.snake.front.y

        newtail = Node(tailx, taily) 
        newtail.next = self.snake.front #令原來的尾巴為新的尾巴的下一個節點
        self.snake.front.pre = newtail #新的尾巴為尾巴原來的上一個節點
        self.snake.front = newtail #最後令snake.front為新的尾巴
# =========================== Question 3 ===========================
    def eat_body(self): 
        #頭的座標
        headx = self.snake.rear.x
        heady = self.snake.rear.y
        body = self.snake.rear.pre #身體為頭的前面節點
        l = self.snake.len() #蛇的長度
        while body: #讀取身體座標的迴圈
            if headx == body.x and heady == body.y: #判定頭是否和身體重合
                self.play_effect("eat_body")
                for i in range (0, l): 
                    self.snake.deQueue() #去除尾巴
                    if self.snake.front == body.next:
                        break #當切除後的蛇尾和身體的下一個節點一樣時，停止迴圈
            body = body.pre #向前一個節點讀取
# =========================== Question 4 ===========================
    def eat_item(self): 
        if self.itemBoxPos != None: #若道具方塊有顯現的話
           #頭座標
           headx = self.snake.rear.x
           heady = self.snake.rear.y
           if headx == self.itemBoxPos[0] and heady == self.itemBoxPos[1]: #判定頭的位置和箱子是否一樣
               item = self.item_list[random.randrange(4)] #隨機選取物品
               self.backpack.push(item) #加入物品
               self.play_effect("eat_item")
               self.itemBoxPos = None #使物品消失

# =========================== Question 5 ===========================
    def use_item(self): # 使用道具
        self.item = self.backpack.top.item #儲存道具名稱
        if self.item == self.item_list[0]: #黑洞
            self.item_BlackHole = True
            self.backpack.pop() #移除道具
        elif self.item == self.item_list[1]: #剎車
            self.item_Brake = True
            self.backpack.pop()
        elif self.item == self.item_list[2]: #水果籃
            self.item_FruitBasket = True
            self.backpack.pop()
        elif self.item == self.item_list[3]: #隨機物品
            self.item_Gamble = True
            self.backpack.pop()