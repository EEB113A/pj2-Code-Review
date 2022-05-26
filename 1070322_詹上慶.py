# =========================== Question 1 ===========================
    def move(self):
        if self.dir=="up":#45-47是用來決定按上並改變走向
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y-self.g)
            self.snake.deQueue()
        
        if self.dir=="down":#49-51是用來決定按下並改變走向
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y+self.g)
            self.snake.deQueue()
        
        if self.dir=="left":#53-55是用來決定按左並改變走向
            self.snake.enQueue(self.snake.rear.x-self.g, self.snake.rear.y)
            self.snake.deQueue()
            
        if self.dir=="right":#57-59是用來決定按右並改變走向
            self.snake.enQueue(self.snake.rear.x+self.g, self.snake.rear.y)
            self.snake.deQueue()


# =========================== Question 2 ===========================
    def add_tail(self):
        if self.snake.front.next.x==self.snake.front.x and self.snake.front.next.y-self.g==self.snake.front.y:#68-72判斷要在尾端往上加node
            new = Node(self.snake.front.x,self.snake.front.y-self.g)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new

        if self.snake.front.next.x==self.snake.front.x and self.snake.front.next.y+self.g==self.snake.front.y:#74-78判斷尾端往下加node
            new = Node(self.snake.front.x,self.snake.front.y+self.g)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new

        if self.snake.front.next.x-self.g==self.snake.front.x and self.snake.front.next.y==self.snake.front.y:#80-84判斷在尾端往左加node
            new = Node(self.snake.front.x-self.g,self.snake.front.y)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new
        if self.snake.front.next.x+self.g==self.snake.front.x and self.snake.front.next.y==self.snake.front.y:#85-89判斷在尾端往右加node
            new = Node(self.snake.front.x+self.g,self.snake.front.y)
            new.next = self.snake.front
            self.snake.front.pre = new
            self.snake.front = new
# =========================== Question 3 ===========================
    def eat_body(self):
        cur=self.snake.front
        while cur!=None and cur!=self.snake.rear:#從尾巴那端往頭那端尋找，假如頭的index=身體的index，從頭到尾全扣掉
            if cur.x==self.snake.rear.x and cur.y==self.snake.rear.y:
                cur.next.pre=None
                self.snake.front=cur.next
                self.play_effect("eat_body")
                break
            cur=cur.next
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 如果有顯現道具方塊的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:#頭座標=黃色方塊座標=吃到方塊
                self.itemBoxPos=None#方塊消失
                self.play_effect("eat_item")#音樂播放
                self.backpack.push(self.item_list[random.randrange(0,3)])#從list中的4個道具中隨機挑選一個放至背包

# =========================== Question 5 ===========================
    def use_item(self):
        self.item=self.backpack.top.item#找到最後要放進去使用的那個
        if self.item=="BlackHole":#如果最上面是黑洞，使之=True，執行
            self.item_BlackHole = True
            self.backpack.pop()
            

        
        if self.item=="Brake":#如果最上面是break，使之=True，執行
            self.item_Brake = True
            self.backpack.pop()
        
        if self.item=="FruitBasket":#如果最上面是FruitBasket，使之=True，執行
            self.item_FruitBasket = True
            self.backpack.pop()
        
        if self.item=="Gamble":#如果最上方是Gamble，使之=True，執行
            self.item_Gamble = True
            self.backpack.pop()