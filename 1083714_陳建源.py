# =========================== Question 1 ===========================
    def move(self): # 根據方向移動蛇的坐標
        #定義snake head的(x,y)座標
        headx = self.snake.rear.x 
        heady = self.snake.rear.y
        #根據移動方向queue方塊及刪減方塊
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
    def add_tail(self): # 加一個節點到玩家蛇的尾端(此方法是在蛇吃掉食物的時候被呼叫)
        tailx = self.snake.front.x
        taily = self.snake.front.y
        newtail = Node(tailx, taily)#用來增加tailx,y的值的node
        newtail.next = self.snake.front
        self.snake.front.pre = newtail#接上newtail
        self.snake.front = newtail

        
# =========================== Question 3 ===========================
    def eat_body(self): # 吃到玩家蛇的身體
        headx = self.snake.rear.x
        heady = self.snake.rear.y
        body = self.snake.rear.pre
        l = self.snake.len()
        while body:#遇到蛇身開始
            if headx == body.x and heady == body.y:#頭碰到身體
                self.play_effect("eat_body")
                for i in range (0, l):
                    self.snake.deQueue()#從尾巴刪減
                    if self.snake.front == body.next:
                        break
            body = body.pre
# =========================== Question 4 ===========================
    def eat_item(self): # 吃到道具方塊(黃色問號)即獲得道具
        if self.itemBoxPos != None: #遇到道具
            #定義頭部座標
            headx = self.snake.rear.x
            heady = self.snake.rear.y
            if headx == self.itemBoxPos[0] and heady == self.itemBoxPos[1]:
                random_item = self.item_list[random.randrange(4)]#從item_list挑選出一個道具
                self.backpack.push(random_item)#增加道具至backpack
                self.play_effect("eat_item")
                self.itemBoxPos = None #使道具圖示從地圖消失
# =========================== Question 5 ===========================
    def use_item(self): # 使用道具
        self.item = self.backpack.top.item#儲存道具名稱
        if self.item == self.item_list[0]: #黑洞
            self.item_BlackHole = True
            self.backpack.pop() #使用後移除道具
        elif self.item == self.item_list[1]: #剎車
            self.item_Brake = True
            self.backpack.pop()
        elif self.item == self.item_list[2]: #水果籃
            self.item_FruitBasket = True
            self.backpack.pop()
        elif self.item == self.item_list[3]: #隨機物品
            self.item_Gamble = True
            self.backpack.pop()