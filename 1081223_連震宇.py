# =========================== Question 1 ===========================
    def move(self):
        if(self.dir == "right"): #當按下D或右
            self.snake.enQueue( self.snake.rear.x + 30, self.snake.rear.y)  # 一格寬度是30，要向右移動，x座標+30
            self.snake.deQueue() #刪除front
        if(self.dir == 'left'):  #當按下A或右
            self.snake.enQueue( self.snake.rear.x - 30, self.snake.rear.y)  # 一格寬度是30，要向左移動，x座標-30
            self.snake.deQueue() #刪除front
        if(self.dir == 'up'):    #當按下W或右
            self.snake.enQueue( self.snake.rear.x, self.snake.rear.y - 30 ) # 一格寬度是30，要向上移動，y座標-30
            self.snake.deQueue() #刪除front    
        if(self.dir == 'down'):  #當按下S或右
            self.snake.enQueue( self.snake.rear.x, self.snake.rear.y + 30 ) # 一格寬度是30，要向下移動，y座標+30
            self.snake.deQueue() #刪除front         
# =========================== Question 2 ===========================
    def add_tail(self):
        x = Node(0,0)             # 設定新的蛇身
        self.snake.front.pre = x  # 接在蛇尾後
        x.next = self.snake.front # 原本的蛇尾變成倒數第2個
        self.snake.front = x      # 指向新的蛇尾           
# =========================== Question 3 ===========================
    def eat_body(self):
        head_x = self.snake.rear.x # 蛇頭 x 座標
        head_y = self.snake.rear.y # 蛇頭 y 座標
        tmp = self.snake.rear.pre  # 第一個蛇身
        while tmp:            # 當 tmp 不為 None 時
            if(tmp.x == head_x and tmp.y == head_y): # 如果蛇頭碰到蛇身
                body = tmp.next  # 指定被碰到的蛇身的前一個為蛇尾
                body.pre = None  # 刪除被蛇頭咬到之後的蛇身
                tmp.next = None  # 刪除被蛇頭咬到之後的蛇身
                self.snake.front = body # 指向新的蛇尾
                self.play_effect("eat_body") # 播放音效
            tmp = tmp.pre        # 蛇身往蛇尾檢查         
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            item_x = self.itemBoxPos[0] # itemBoxPos 的 x 座標 
            item_y = self.itemBoxPos[1] # itemBoxPos 的 y 座標 
            if (item_x == self.snake.rear.x and item_y == self.snake.rear.y): # 如果蛇頭碰到道具方塊
                item = random.randrange(len(self.item_list)) # 隨機產生道具
                self.backpack.push(self.item_list[item]) # 將道具推入背包
                self.itemBoxPos = None                   # 重設為 None
                self.play_effect("eat_item")             # 播放音效
        else:
            item_x = random.randrange(1, self.width//self.g) # 隨機產生 x 座標
            item_y = random.randrange(1, self.width//self.g) # 隨機產生 y 座標   
# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item # 背包最上面的道具
        if(self.item == "BlackHole"):    # 當背包最上面的道具是 BlackHole
            self.item_BlackHole = True   # 使用道具
            self.backpack.pop()          # 刪除道具
        if(self.item == "Brake"):        # 當背包最上面的道具是 Brake
            self.item_Brake = True       # 使用道具
            self.backpack.pop()          # 刪除道具   
        if(self.item == "FruitBasket"):  # 當背包最上面的道具是 FruitBasket
            self.item_FruitBasket = True # 使用道具
            self.backpack.pop()          # 刪除道具
        if(self.item == "Gamble"):       # 當背包最上面的道具是 Gamble
            self.item_Gamble = True      # 使用道具
            self.backpack.pop()          # 刪除道具            