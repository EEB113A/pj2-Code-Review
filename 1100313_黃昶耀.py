# =========================== Question 1 ===========================
    def move(self):
        tmp = self.snake.front                 #設定tmp為front
        length = self.snake.len()              #length為長度
        
        if self.dir == "up":                   #若方向是up
            for i in range(length-1) :
                tmp.x = tmp.next.x             #x變為下一個節點的x
                tmp.y = tmp.next.y             #y變為下一個節點的y
                tmp = tmp.next                 #tmp變下一個
            self.snake.rear.y -= self.g        #rear的y-self.g
            
        elif self.dir == "down":               #若方向是dowm
            for i in range(length-1) :
                tmp.x = tmp.next.x             #x變為下一個節點的x
                tmp.y = tmp.next.y             #y變為下一個節點的y
                tmp = tmp.next                 #tmp變下一個
            self.snake.rear.y += self.g        #rear的y+self.g
            
        elif self.dir == "right":             #若方向是right
            for i in range(length-1) :
                tmp.x = tmp.next.x            #x變為下一個節點的x
                tmp.y = tmp.next.y            #y變為下一個節點的y
                tmp = tmp.next                #tmp變下一個
            self.snake.rear.x += self.g       #rear的x+self.g

            
        elif self.dir == "left":              #若方向是left
            for i in range(length-1) :
                tmp.x = tmp.next.x            #x變為下一個節點的x
                tmp.y = tmp.next.y            #y變為下一個節點的y
                tmp = tmp.next                #tmp變下一個
            self.snake.rear.x -= self.g       #rear的x-self.g
# =========================== Question 2 ===========================
    def add_tail(self):
        new = Node(2*self.snake.front.x - self.snake.front.next.x,2*self.snake.front.y - self.snake.front.next.y)   #設定新節點，利用向量方法a-b=b-c，接著移向可得
        new.next = self.snake.front                                                                                 #新節點的next設為原本尾巴
        new.pre = None                                                                                              #新節點的pre為None
        self.snake.front.pre = new                                                                                  #原本尾巴的pre設為new
        self.snake.front = new                                                                                      #把new設為新尾巴
# =========================== Question 3 ===========================
    def eat_body(self):
        tmp = self.snake.front                                                   #tmp設為front
        for i in range(self.snake.len()-1):   
            if self.snake.rear.x == tmp.x and self.snake.rear.y == tmp.y :       #若頭的x等於tmp的x且頭的y等於tmp的y
                tmp.next.pre = None                                              #被碰到的那個節點設為None
                self.snake.front = tmp.next                                      #fornt指到新尾巴
                self.play_effect("eat_body")                                     #播放音效
                break
            tmp = tmp.next
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:    #若頭和道具方塊的座標一樣
                num = random.randrange(0,4)                                                            #隨機生成一個數字
                self.backpack.push(self.item_list[num])                                                #把隨機生成的數字放到list，接著把道具push進去backpack
                self.itemBoxPos = None                                                                 #道具方塊座標重設
                self.play_effect("eat_item")                                                           #播放音效
            

# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item         #儲存堆疊道具頂端的道具名稱
        
        if self.item == "BlackHole":              #若道具是BlackHole
            self.item_BlackHole = True            #發動效果
            self.backpack.pop()                   #pop
            
        elif self.item == "Brake":                #若道具是Brake
            self.item_Brake = True                #發動效果
            self.backpack.pop()                   #pop
            
        elif self.item == "FruitBasket":          #若道具是FruitBasket
            self.item_FruitBasket = True          #發動效果
            self.backpack.pop()                   #pop
            
        elif self.item == "Gamble":               #若道具是Gamble
            self.item_Gamble = True               #發動效果
            self.backpack.pop()                   #pop