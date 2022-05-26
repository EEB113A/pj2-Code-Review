# =========================== Question 1 ===========================
    def move(self):
        if(self.dir == "right"): #按下D或右
            self.snake.enQueue( self.snake.rear.x + 30, self.snake.rear.y)  # 向右移動，x座標+30
            self.snake.deQueue() #刪除front(尾巴)
        if(self.dir == 'left'):  #按下A或右
            self.snake.enQueue( self.snake.rear.x - 30, self.snake.rear.y)  # 向左移動，x座標-30
            self.snake.deQueue() #刪除front(尾巴)
        if(self.dir == 'up'):    #按下W或右
            self.snake.enQueue( self.snake.rear.x, self.snake.rear.y - 30 ) # 向上移動，y座標-30
            self.snake.deQueue() #刪除front(尾巴)
        if(self.dir == 'down'):  #按下S或右
            self.snake.enQueue( self.snake.rear.x, self.snake.rear.y + 30 ) # 向下移動，y座標+30
            self.snake.deQueue() #刪除front(尾巴)         
# =========================== Question 2 ===========================
    def add_tail(self):
        tail = Node(0,0) #設定新蛇身
        self.snake.front.pre = tail #接在蛇尾
        tail.next = self.snake.front #原蛇尾變倒數第2個
        self.snake.front = tail #指向新蛇尾                              
# =========================== Question 3 ===========================
    def eat_body(self):
        headx = self.snake.rear.x # 蛇頭的x座標
        heady = self.snake.rear.y # 蛇頭的y座標
        tmp = self.snake.rear.pre # 第一個蛇身
        while tmp:                # 當tmp有東西時
            if(tmp.x == headx and tmp.y == heady): # 如果蛇頭碰到蛇身
                itself = tmp.next  # 設被碰到的蛇身的前一個當蛇尾
                itself.pre = None  # 刪除被蛇頭碰到之後的蛇身
                tmp.next = None  # 刪除被蛇頭碰到之後的蛇身
                self.snake.front = itself # 指向新蛇尾
                self.play_effect("eat_body") # 播音樂
            tmp = tmp.pre        # 從蛇身往蛇尾一一檢查         
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            itemx = self.itemBoxPos[0] # 設itemx為道具的x座標 
            itemy = self.itemBoxPos[1] # 設itemy為道具的y座標 
            if (itemx == self.snake.rear.x and itemy == self.snake.rear.y): #如果蛇頭吃到道具時
                lengthitem=len(self.item_list) #取長度
                item = random.randrange(lengthitem) # 隨機產生道具
                self.backpack.push(self.item_list[item]) # 把道具push進包包
                self.itemBoxPos = None                   # 重設為 None
                self.play_effect("eat_item")             # 播音樂
        else:
            itemx = random.randrange(1, self.width//self.g) # 隨機產生道具的x座標
            itemy = random.randrange(1, self.width//self.g) # 隨機產生道具的y座標  
# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item # 最上面能使用的道具
        if(self.item == "BlackHole"):    # 當最上面的道具是黑洞
            self.item_BlackHole = True   # 使用此道具
            self.backpack.pop()          # pop掉此道具
        if(self.item == "Brake"):        # 當最上面的道具是 Brake
            self.item_Brake = True       # 使用此道具
            self.backpack.pop()          # pop掉此道具   
        if(self.item == "FruitBasket"):  # 當最上面的道具是 FruitBasket
            self.item_FruitBasket = True # 使用此道具
            self.backpack.pop()          # pop掉此道具
        if(self.item == "Gamble"):       # 當最上面的道具是 Gamble
            self.item_Gamble = True      # 使用此道具
            self.backpack.pop()          # pop掉此道具            