# =========================== Question 1 ===========================
    def move(self):
        s=self.snake.front
        s.x=s.next.x
        s.y=s.next.y
        for i in range(1, self.snake.len()-1):
            s=s.next
            s.x=s.next.x
            s.y=s.next.y
        if self.dir=="up":
            self.snake.rear.y-=self.g 
        elif self.dir=="down":
            self.snake.rear.y+=self.g 
        elif self.dir=="left":
            self.snake.rear.x-=self.g 
        else:
            self.snake.rear.x+=self.g 
            
# =========================== Question 2 ===========================
    def add_tail(self):
        if self.snake.front.x < self.snake.front.next.x:
            new = Node(self.snake.front.x-self.g, self.snake.front.y)
        if self.snake.front.x > self.snake.front.next.x:
            new = Node(self.snake.front.x+self.g, self.snake.front.y)
        if self.snake.front.x < self.snake.front.next.x:
            new = Node(self.snake.front.x, self.snake.front.y-self.g)
        else:
            new = Node(self.snake.front.x, self.snake.front.y+self.g)
        new.next=self.snake.front
        self.snake.front.pre=new
        self.snake.front=new
        
        
# =========================== Question 3 ===========================
    def eat_body(self):
        x=self.snake.rear.x
        y=self.snake.rear.y
        s=self.snake.rear.pre
        while s:
            if s.x==x and s.y==y:
                s.next.pre=None
                self.snake.front=s.next
                self.play_effect("eat_body")
                break
            else:
                s=s.pre
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x==self.itemBoxPos[0] and self.snake.rear.y==self.itemBoxPos[1]:
                self.backpack.push(self.item_list[random.randrange(0,4)])
                self.itemBoxPos=None
                self.play_effect("eat_item")

# =========================== Question 5 ===========================
    def use_item(self):
        self.item=self.backpack.top.item
        self.backpack.pop()
        if self.item==self.item_list[0]:
            self.item_BlackHole=True
        elif self.item==self.item_list[1]:
            self.item_Brake=True
        elif self.item==self.item_list[2]:
            self.item_FruitBasket=True
        else:
            self.item_Gamble=True