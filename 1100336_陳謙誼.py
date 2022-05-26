# =========================== Question 1 ===========================
    def move(self):
        
        Snake_tail=self.snake.front
        Snake_tail.x=Snake_tail.next.x
        Snake_tail.y=Snake_tail.next.y
        
        SnakeLen=self.snake.len()        
        for i in range(1,SnakeLen-1):
            Snake_tail=Snake_tail.next
            Snake_tail.x=Snake_tail.next.x
            Snake_tail.y=Snake_tail.next.y

        if self.dir=="right":
            self.snake.rear.x=self.snake.rear.x+1*self.g
            
        elif self.dir=="light":
            self.snake.rear.x=self.snake.rear.x-1*self.g
            
        elif self.dir=="up":
            self.snake.rear.y=self.snake.rear.y-1*self.g
            
        elif self.dir=="down":
            self.snake.rear.y=self.snake.rear.y+1*self.g
# =========================== Question 2 ===========================
    def add_tail(self):

        if self.snake.front.x<self.snake.front.next.x:
            new=Node(self.snake.front.x-self.g,self.snake.front.y)
            new=Node(self.snake.front.x,self.snake.front.y-self.g)
        if self.snake.front.x>self.snake.front.next.x:
            new=Node(self.snake.front.x+self.g,self.snake.front.y)
            new=Node(self.snake.front.x,self.snake.front.y+self.g)
            
        new.next=self.snake.front
        self.snake.front.pre=new
        self.snake.front=new
        
# =========================== Question 3 ===========================
    def eat_body(self):
        #鏈結串列走訪
        head_x=self.snake.rear.x
        head_y=self.snake.rear.y
        tmp=self.snake.rear.pre
        while tmp:  
            if tmp.x==head_x and tmp.y==head_y:  #如果頭的座標和tmp的座標一樣
                self.play_effect("eat_body")   #撥放音效
                tmp.pre.next=None  #把該節點的pre和next指向None
                tmp.pre=None
                #tmp.next=None
                #tmp.next.pre=None
                
            else:    #如果頭的座標和tmp的座標不一樣
                tmp=tmp.pre #tmp指向下一個
                
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x==self.itemBoxPos[0] and self.snake.rear.y==self.itemBoxPos[1]:#如果道具和頭的座標一樣
                self.play_effect("eat_item")
                tool=self.item_list[random.range(0,4)]#從道具列表(self.item_list)內隨機選擇一個道具
                self.backpack.push(tool)#該到具備push進backpack
                self.itemBoxPos=None#將self.itemBoxPos座標設成None
                
# =========================== Question 5 ===========================
    def use_item(self):
        self.backpack.data[0]
        self.backpack.pop()#把backpack的pop出去