# =========================== Question 1 ===========================
    def move(self): # 根據方向移動蛇的坐標
        cur=self.snake.rear.pre#令cur指到蛇身的第一個節點
        next_x=self.snake.rear.x#next_x儲存蛇身節點需更新的x座標
        next_y=self.snake.rear.y#next_y儲存蛇身節點需更新的y座標
        while True:
            if cur==None:
                break
            now_x=cur.x#now_x紀錄當前節點的x座標
            now_y=cur.y#now_y紀錄當前節點的y座標
            cur.x=next_x#34,35改變節點的座標值
            cur.y=next_y
            next_x=now_x#36,37將當前座標位置改為下一個節點需抵達的座標
            next_y=now_y
            cur=cur.pre#指到下一個節點
        if self.dir=="up": #39-46依照方向的輸入決定蛇頭的座標需如何改變
            self.snake.rear.y-=self.g
        if self.dir=="down": 
            self.snake.rear.y+=self.g
        if self.dir=="left": 
            self.snake.rear.x-=self.g
        if self.dir=="right": 
            self.snake.rear.x+=self.g
# =========================== Question 2 ===========================
    def add_tail(self): # 加一個節點到玩家蛇的尾端(此方法是在蛇吃掉食物的時候被呼叫)
        tail=self.snake.front
        x=tail.x+(tail.x-tail.next.x)#54,55通過比較蛇尾與前一個節點的x,y座標來找出需延伸蛇尾的方向
        y=tail.y+(tail.y-tail.next.y)
        new=Node(x,y)#56-59用來在front處增加一個新節點
        new.next=tail
        self.snake.front.pre=new
        self.snake.front=new
# =========================== Question 3 ===========================
    def eat_body(self):
        cur=self.snake.front.next
        while True:
            x=self.snake.rear.x#x=目前蛇頭的x
            y=self.snake.rear.y#y=目前蛇頭的y
            if cur.next==self.snake.rear:#比對到蛇頭前的節點就停止迴圈
                break
            if cur.x==x and cur.y==y:
                self.snake.front=cur#將front改成cur節點
                self.snake.front.pre=None#將pre指到None以斷開蛇尾後的節點
                self.play_effect("eat_body")
                break
            cur=cur.next
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            x=self.snake.rear.x#x=目前蛇頭的x
            y=self.snake.rear.y#y=目前蛇頭的y
            if self.itemBoxPos==[x,y]:#碰到道具方塊就隨機PUSH一個道具進入backpack
                self.backpack.push(self.item_list[random.randrange(0,4)])
                self.play_effect("eat_item")
                self.itemBoxPos=None#重製道具方塊的座標
# =========================== Question 5 ===========================
    def use_item(self):
        self.item=self.backpack.top.item#將self.item用來儲存位於top的道具名稱
        if self.item=="BlackHole":
            self.item_BlackHole=True
        if self.item=="Brake=":#115-122依照對應的道具名稱將道具的參數改為True
            self.item_Brake=True
        if self.item=="FruitBasket":
            self.item_FruitBasket=True
        if self.item=="Gamble":
            self.item_Gamble=True
        self.backpack.pop()#移除使用過的道具
# ==================================================================