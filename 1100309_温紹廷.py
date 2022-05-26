# =========================== Question 1 ===========================
    def move(self):
        if self.dir=="up" :                                                    #往上
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y-self.g)     #蛇頭加入新節點，x不變，y減一個單位
            self.snake.deQueue()                                               #刪除蛇尾節點

        elif self.dir=="down" :                                                #往下
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y+self.g)     #蛇頭加入新節點，x不變，y加一個單位
            self.snake.deQueue()                                               #刪除蛇尾節點

        elif self.dir=="left" :                                                #往左
            self.snake.enQueue(self.snake.rear.x-self.g,self.snake.rear.y)     #蛇頭加入新節點，x減一個單位，y不變
            self.snake.deQueue()                                               #刪除蛇尾節點

        elif self.dir=="right" :                                               #往右
            self.snake.enQueue(self.snake.rear.x+self.g,self.snake.rear.y)     #蛇頭加入新節點，x加一個單位，y不變
            self.snake.deQueue()                                               #刪除蛇尾節點
# =========================== Question 2 ===========================
    def add_tail(self):
        newtail=Node(self.snake.front.x,self.snake.front.y)
        if  self.snake.len()==0:
            self.snake.rear = newtail
            self.snake.front= newtail
        else:
            newtail.next=self.snake.front                                       #新節點向後為蛇尾
            self.snake.front.pre=newtail                                        #蛇尾向前為新節點
            self.snake.front=newtail                                            #新節點為蛇尾
# =========================== Question 3 ===========================
    def eat_body(self):
        head=self.snake.rear.pre
        head_x=self.snake.rear.x
        head_y=self.snake.rear.y                                                    
        while head:                                                           #從蛇頭前指標開始
            if head_x==head.x and head_y==head.y:                             #如果重疊，將蛇尾改為下一個
                self.snake.front=head.next                                    
                head.pre=None                                                 #將重疊的前後變成none
                head.next=None
                head=None 
                self.play_effect("eat_body")
            else:
                head=head.pre
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x==self.itemBoxPos[0] and self.snake.rear.y==self.itemBoxPos[1]:       #如果碰到道具方塊時
                item = self.item_list[random.randrange(0,4,1)]                                        #隨機選一個道具
                self.backpack.push(item)                                                              #放進背包
                self.play_effect("eat_item")
                self.itemBoxPos= None                                                                 #將道具位置重設
# =========================== Question 5 ===========================
    def use_item(self):
        self.item=self.backpack.top.item                                                     #儲存堆疊道具名稱
        if self.item=="FruitBasket":                                                         #使用道具時
            self.item_FruitBasket=True                                                       #將預設道具參數的False改成True
            self.backpack.pop()                                                              #將道具從背包移除
        if self.item=="BlackHole":
            self.item_BlackHole=True
            self.backpack.pop()
        if self.item=="Brake":
            self.item_Brake=True
            self.backpack.pop()
        if self.item=="Gamble":
            self.item_Gamble=True
            self.backpack.pop()