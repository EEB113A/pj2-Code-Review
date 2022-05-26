# =========================== Question 1 ===========================
    def move(self):
        if self.dir == "right":                     #當蛇頭的方向是"右"
                             
            self.snake.enQueue(self.snake.rear.x+self.g , self.snake.rear.y)    #在蛇頭的右方加入新節點
            self.snake.deQueue()                                                #把蛇尾的節點刪掉
           
        if self.dir == "left":                      #當蛇頭的方向是"左"
                                
            self.snake.enQueue(self.snake.rear.x-self.g , self.snake.rear.y)    #在蛇頭的左方加入新節點
            self.snake.deQueue()                                                #把蛇尾的節點刪掉

        if self.dir == "up":                        #當蛇頭的方向是"上"
                       
            self.snake.enQueue(self.snake.rear.x , self.snake.rear.y-self.g)    #在蛇頭的上方加入新節點
            self.snake.deQueue()                                                #把蛇尾的節點刪掉
            
        if self.dir == "down":                      #當蛇頭的方向是"下"
        
            self.snake.enQueue(self.snake.rear.x , self.snake.rear.y+self.g)    #在蛇頭的下方加入新節點
            self.snake.deQueue()                                                #把蛇尾的節點刪掉
# =========================== Question 2 ===========================
    def add_tail(self):
        new=Node(self.snake.front.x,self.snake.front.y)       #在蛇尾後建一個新節點
        new.x*=self.g
        new.y*=self.g
        new.next = self.snake.front                           #新節點的next=蛇尾的節點
        self.snake.front.pre = new                            #蛇尾的節點的pre=新節點
        self.snake.front = new                                #把front移到新節點
# =========================== Question 3 ===========================
    def eat_body(self):
        head_x=self.snake.rear.x                #在蛇頭的x座標貼上head_x的標籤
        head_y=self.snake.rear.y                #在蛇頭的y座標貼上head_y的標籤
        tmp=self.snake.rear.pre                 #在蛇頭的前一個節點貼上tmp的標籤
        while tmp:                              
            if head_x==tmp.x and head_y==tmp.y:     #如果蛇頭和tmp所在節身體重疊
                self.play_effect("eat_body")
                self.snake.front = tmp.next         #把蛇尾的front貼到tmp的next節點
                tmp.next.pre=None                   #tmp的next的pre指向None
                break                               #跳出迴圈
            else:                               #如果重疊的不是當前tmp所在節點
                tmp=tmp.pre                     #就把tmp往蛇尾方向貼到下一個節點
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x==self.itemBoxPos[0] and self.snake.rear.y==self.itemBoxPos[1]:  #如果蛇頭碰到道具方塊
                self.itemBoxPos = None
                self.play_effect("eat_item")
                item=random.randrange(len(self.item_list))  #從(0~3)中隨機選取一個數字
                self.backpack.push(self.item_list[item])    #在self.item_list中將此數字所代表的位置的道具push進背包
# =========================== Question 5 ===========================
    def use_item(self):
        if self.backpack.top.item =="BlackHole":         #如果背包最下層的道具是"BlackHole"
            self.item="BlackHole"
            self.item_BlackHole=True                     #啟用此道具
            self.backpack.pop()                          #刪除此道具
        
        elif self.backpack.top.item =="Brake":           #如果背包最下層的道具是"Brake"
            self.item="Brake"
            self.item_Brake=True                         #啟用此道具
            self.backpack.pop()                          #刪除此道具
        
        elif self.backpack.top.item =="FruitBasket":     #如果背包最下層的道具是"FruitBasket"
            self.item="FruitBasket"
            self.item_FruitBasket=True                   #啟用此道具
            self.backpack.pop()                          #刪除此道具
       
        elif self.backpack.top.item =="Gamble":          #如果背包最下層的道具是"Gamble"
            self.item="Gamble"
            self.item_Gamble=True                        #啟用此道具
            self.backpack.pop()                          #刪除此道具