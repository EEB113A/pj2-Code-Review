# =========================== Question 1 ===========================
    def move(self):
        if self.dir == "right": #當鍵盤向右
            head=self.snake.rear.x #蛇頭x座標
            heady=self.snake.rear.y #蛇頭y座標
            head=head+self.g #x座標+1
            self.snake.enQueue(head,heady) #蛇頭新增一個節點
            self.snake.deQueue() #蛇尾刪除一個節點
            
        if self.dir == "left": #當鍵盤向左
            head=self.snake.rear.x
            heady=self.snake.rear.y
            head=head-self.g #x座標-1
            self.snake.enQueue(head,heady) 
            self.snake.deQueue() 
            
        if self.dir == "up": #當鍵盤向上
            head=self.snake.rear.x
            heady=self.snake.rear.y
            heady=heady-self.g #y座標-1
            self.snake.enQueue(head,heady)
            self.snake.deQueue()
            
        if self.dir == "down": #當鍵盤向下
            head=self.snake.rear.x
            heady=self.snake.rear.y
            heady=heady+self.g #y座標+1
            self.snake.enQueue(head,heady)
            self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self):
        tail=self.snake.front.x #蛇尾x座標
        taily=self.snake.front.y #蛇尾y座標
        t=Node(tail,taily) #新增一個原蛇尾座標作為蛇吃掉食物後增加的節點
        self.snake.front.pre=t 
        t.next=self.snake.front
        self.snake.front=t
# =========================== Question 3 ===========================
    def eat_body(self):
        head_x=self.snake.rear.x  #蛇頭x座標
        head_y=self.snake.rear.y  #蛇頭x座標
        tmp=self.snake.rear.pre  #蛇頭前一個身體節點
        while tmp:
            if tmp.x==head_x and tmp.y==head_y: #當蛇身體和蛇頭相碰
                tmp.pre=None #相碰之後的身體全部斷掉
                tmp.next.pre=None
                self.snake.front=tmp.next #尾巴回到相碰節點的後一個節點
                self.play_effect("eat_body") 
            tmp=tmp.pre #蛇頭前一個身體再前一個身體節點(尋找相碰身體的節點)
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.itemBoxPos[0]==self.snake.rear.x and self.itemBoxPos[1]==self.snake.rear.y: #蛇頭和道具方塊相碰
                self.play_effect("eat_item")
                chose=self.item_list[random.randrange(len(self.item_list))] #隨機選取一個道具
                self.backpack.push(chose) #將道具放入背包中
                self.itemBoxPos=None #道具方塊消失

# =========================== Question 5 ===========================
    def use_item(self):
        self.item=self.backpack.top.item #儲存最頂端的道具
        if self.item=="BlackHole": #當道具為BlackHole
            self.item_BlackHole = True #啟用道具
            self.backpack.pop() #且消除啟用之道具

        if self.item=="Brake": #當道具為Brake
            self.item_Brake = True
            self.backpack.pop()

        if self.item=="FruitBasket": #當道具為FruitBasket
            self.item_FruitBasket = True
            self.backpack.pop()

        if self.item=="Gamble": #當道具為Gamble
            self.item_Gamble = True
            self.backpack.pop()