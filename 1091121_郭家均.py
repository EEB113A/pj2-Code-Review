# =========================== Question 1 ===========================
    def move(self): # 根據方向移動蛇的坐標

        pNode = None #設為None
        if  self.snake.len() > 0 : #如果lne>0
            pNode = self.snake.front
            while pNode.next != None : #如果不為None
                pNode.x = pNode.next.x
                pNode.y = pNode.next.y
                pNode = pNode.next
            if self.dir == "up" : #如果是up
                pNode.y -= self.g #往上移動
            elif self.dir == "down" : #如果是down
                pNode.y += self.g #往下移動
            elif self.dir == "left" : #如果是left
                pNode.x -= self.g #往左移動
            elif self.dir == "right" : #如果是right
                pNode.x += self.g #往右移動

        pass
# =========================== Question 2 ===========================
    def add_tail(self): # 加一個節點到玩家蛇的尾端(此方法是在蛇吃掉食物的時候被呼叫)

        if  self.snake.len() > 0 : #如果len>0
            pNode = self.snake.front #尾巴
            nextFrone = None #設為None
            if self.dir == "up" : #如果是up
                nextFrone = Node( pNode.x , pNode.y + self.g ) #修改nextFrone
            elif self.dir == "down" : #如果是down
                nextFrone = Node( pNode.x , pNode.y - self.g ) #修改nextFrone
            elif self.dir == "left" : #如果是left
                nextFrone = Node( pNode.x + self.g , pNode.y ) #修改nextFrone
            elif self.dir == "right" : #如果是right
                nextFrone = Node( pNode.x - self.g , pNode.y ) #修改nextFrone
            pNode.pre = nextFrone ; #蛇尾的上一個
            nextFrone.next = pNode ; #新加的下一個
            nextFrone.pre = None ; #新加的上一個為None
            self.snake.front = nextFrone  #放到尾巴
# =========================== Question 3 ===========================
    def eat_body(self): # 吃到玩家蛇的身體

        if  self.snake.len() > 1 : #如果len>1
            rear = self.snake.rear
            pNode = self.snake.rear.pre
            while pNode != None : # 判斷是否有吃到自己
                if( pNode.x == rear.x ) and ( pNode.y == rear.y ) : #如果吃到了
                    while self.snake.front != pNode : #刪除節點
                        self.snake.deQueue() 
                    self.snake.deQueue()
                    self.play_effect("eat_body") #撥放音效
                    return
                pNode = pNode.pre 
        pass
# =========================== Question 4 ===========================
    def eat_item(self): # 吃到道具方塊(黃色問號)即獲得道具
        
        if self.itemBoxPos == None: #如果方塊座標為None
            return 
        item = self.itemBoxPos 
        rear = self.snake.rear
        if rear.x == item[0] and rear.y == item[1] : #如果吃到道具方塊
            self.play_effect("eat_item") #播放音效
            itemCount = len(self.item_list) 
            item =self.item_list[random.randrange( 0 , itemCount )] #隨機選出一個道具
            self.backpack.push( item ) # 加到最前面
            self.itemBoxPos = None #方塊座標重設為None
    # =========================== Question 5 ===========================
    def use_item(self): # 使用道具
        
        if self.backpack.top != None : #如果背包的頂端不是空的
            pItem = self.backpack.top 
            self.item = pItem.item 
            self.backpack.pop() #pop出來
            if self.item == "BlackHole" : #如果是黑洞
                self.item_BlackHole = True #啟動黑洞
            elif self.item == "Brake" : #如果是煞車
                self.item_Brake = True #啟動煞車
            elif self.item == "FruitBasket" : #如果是水果籃
                self.item_FruitBasket = True #啟動水果籃
            elif self.item == "Gamble" : #如果是Gamble
                self.item_Gamble = True #啟動Gamble
        pass