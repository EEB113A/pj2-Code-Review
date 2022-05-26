# =========================== Question 1 ===========================
    def move(self): 
        if self.dir =="right":
            cur = self.snake.front
            while cur.next:
                cur.x = cur.next.x
                cur.y = cur.next.y
                cur = cur.next
            cur.x += self.g
        if self.dir =="up":
            cur = self.snake.front
            while cur.next:
                cur.x = cur.next.x
                cur.y = cur.next.y
                cur = cur.next
            cur.y -= self.g
        if self.dir =="left":
            cur = self.snake.front
            while cur.next:
                cur.x = cur.next.x
                cur.y = cur.next.y
                cur = cur.next
            cur.x -= self.g
        if self.dir =="down":
            cur = self.snake.front
            while cur.next:
                cur.x = cur.next.x
                cur.y = cur.next.y
                cur = cur.next
            cur.y += self.g
# =========================== Question 2 ===========================
    def add_tail(self): 
        cur = self.snake.front
        if cur.y == cur.next.y:
            if cur.x<cur.next.x:
                x = Node(cur.x-self.g,cur.y)
                x.next = self.snake.front
                cur.pre = x
                self.snake.front = x
            if cur.x>cur.next.x:
                x = Node(cur.x+self.g,cur.y)
                x.next = self.snake.front
                cur.pre = x
                self.snake.front = x
        if cur.x == cur.next.x:
            if cur.y<cur.next.y:
                x = Node(cur.x,cur.y-self.g)
                x.next = self.snake.front
                cur.pre = x
                self.snake.front = x
            if cur.x>cur.next.x:
                x = Node(cur.x,cur.y+self.g)
                x.next = self.snake.front
                cur.pre = x
                self.snake.front = x
# =========================== Question 3 ===========================
    def eat_body(self): 
        cur = self.snake.front
        while cur.next!=self.snake.rear:
            if self.snake.rear.x == cur.x and self.snake.rear.y == cur.y:
                self.play_effect("eat_body")
                self.snake.front = cur
                cur.pre = None
                
            cur = cur.next
# =========================== Question 4 ===========================
    def eat_item(self): 
        if self.itemBoxPos != None:
            if self.snake.rear.x== self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:
                self.itemBoxPos = None
                if Stack.isFull:
                    self.play_effect("eat_item")
                    x = random.randrange(0,4)
                    self.backpack.push(self.item_list[x])
             # 若道具方塊有顯現的話

# =========================== Question 5 ===========================
    def use_item(self): 
        if Stack.isEmpty:
            
            self.item = self.backpack.top.item
            self.backpack.pop()
            if self.item == "FruitBasket":
                self.item_FruitBasket = True
            if self.item == "BlackHole":
                self.item_BlackHole = True
            if self.item == "Brake":
                self.item_Brake = True
            if self.item == "Gamble":
                self.item_Gamble = True