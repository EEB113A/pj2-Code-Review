# =========================== Question 1 ===========================
    def move(self):
        tmp = self.snake.front                     #將蛇尾節點複製一份
        
        if self.dir == "up":                        
            
            for i in range(self.snake.len()-1) : 
                 tmp.x = tmp.next.x                 #蛇尾當前節點的x座標只到下一個節點的x座標
                 tmp.y = tmp.next.y                 #蛇尾當前節點的y座標只到下一個節點的y座標

                 tmp = tmp.next                     #將蛇尾節點指到下個節點
            
            
            self.snake.rear.y -= self.g             #當方向為UP，蛇頭的Y座標往上移一個self.g
            
        elif self.dir == "down":
            
            for i in range(self.snake.len()-1) : 
                 tmp.x = tmp.next.x                 #蛇尾當前節點的x座標只到下一個節點的x座標
                 tmp.y = tmp.next.y                 #蛇尾當前節點的y座標只到下一個節點的y座標

                 tmp = tmp.next                     #將蛇尾節點指到下個節點
            
            self.snake.rear.y += self.g             #當方向為down，蛇頭的Y座標往下移一個self.g
        elif self.dir == "left":
            
            for i in range(self.snake.len()-1) : 
                 tmp.x = tmp.next.x                 #蛇尾當前節點的x座標只到下一個節點的x座標
                 tmp.y = tmp.next.y                 #蛇尾當前節點的y座標只到下一個節點的y座標

                 tmp = tmp.next                     #將蛇尾節點指到下個節點
            
            self.snake.rear.x -= self.g             #當方向為left，蛇頭的x座標往左移一個self.g
        elif self.dir == "right":
            
            
            for i in range(self.snake.len()-1) : 
                 tmp.x = tmp.next.x                 #蛇尾當前節點的x座標只到下一個節點的x座標
                 tmp.y = tmp.next.y                 #蛇尾當前節點的y座標只到下一個節點的y座標

                 tmp = tmp.next                     #將蛇尾節點指到下個節點
            
            self.snake.rear.x += self.g             #當方向為right，蛇頭的x座標往右移一個self.g
# =========================== Question 2 ===========================
    def add_tail(self):
        new = Node(1*self.g,1*self.g)               #產生一個新節點
        
        new.x = self.snake.front.x                  #新節點的x座標指到現在蛇尾的座標
        new.y = self.snake.front.y                  #新節點的y座標指到現在蛇尾的座標

        new.next = self.snake.front                 #新節點的下個指標指到蛇尾
        self.snake.front.pre = new                  #蛇尾的上個指標指到新產生的節點
        self.snake.front = new                      #蛇尾再改為新節點
# =========================== Question 3 ===========================
    def eat_body(self):
        tmp = self.snake.rear                       #將蛇頭節點複製一份
        cur = self.snake.front                      #將蛇尾節點複製一份
        
       
        for i in range(self.snake.len()-1):
            if tmp.x == cur.x:          
                if tmp.y == cur.y:                  #當蛇頭的X,Y座標等於蛇身體的任何一個X,Y座標時
                    self.play_effect("eat_body")
                    
                    self.snake.front = cur          #蛇尾指到現在蛇頭吃到的那段身體
                    cur.pre = None                  #將蛇尾前面的節點指到None
                    self.snake.deQueue()

                    break
                    
                    
            cur = cur.next
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.itemBoxPos[0] == self.snake.rear.x:             
                if self.itemBoxPos[1] == self.snake.rear.y:         #當蛇頭的X,Y座標等於道具方塊的X,Y座標時
                    random_item = random.randrange(0, 3, 1)         #產生一個0到3之間的隨機數
                    item = self.item_list[random_item]              #item為現今產生的道具
                    self.backpack.push(item)                        #再把item放到self.backpack裡面
                    self.itemBoxPos = None                          #把道具方塊消除

# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item              #將self.item指到現在背包頂端的道具
        
        if self.item == "BlackHole":                    #當道具為"Blackhole"
            self.item_BlackHole = True                  #執行Blackhole的程式
            self.backpack.pop()                         #刪掉背包最頂端的道具
            
                

        elif self.item == "Gamble":                     #當道具為"Gamble"
            self.item_Gamble = True                     #執行Gamble的程式
            self.backpack.pop()                         #刪掉背包最頂端的道具
           

        elif self.item == "Brake":                      #當道具為"Brake"
            self.item_Brake = True                      #執行Brake的程式
            self.backpack.pop()                         #刪掉背包最頂端的道具

            

        elif self.item == "FruitBasket":                #當道具為"FruitBasket"
            self.item_FruitBasket = True                #執行FruitBasket的程式
            self.backpack.pop()                         #刪掉背包最頂端的道具