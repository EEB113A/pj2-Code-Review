# =========================== Question 1 ===========================
    def move(self):
        if (self.dir == "up"):
            self.snake.rear.y -= 1*self.g
        elif(self.dir == "down"):
            self.snake.rear.y += 1*self.g
        elif(self.dir == "left"):
            self.snake.rear.x -= 1*self.g
        elif(self.dir == "right"):
            self.snake.rear.x += 1*self.g
# =========================== Question 2 ===========================
    def add_tail(self):
        if(self.snake.rear.y - self.snake.rear.pre.y > 0):
            tail_dir = "up"
        elif(self.snake.rear.y - self.snake.rear.pre.y < 0):
            tail_dir = "down"
        elif(self.snake.rear.x - self.snake.rear.pre.x < 0):
            tail_dir = "left"
        elif(self.snake.rear.x - self.snake.rear.pre.x > 0):
            tail_dir = "right"


        if(tail_dir == "up"):
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y + 1* self.g)
        elif(tail_dir == "down"):
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y - 1* self.g)
        elif(tail_dir == "left"):
            self.snake.enQueue(self.snake.rear.x - 1* self.g, self.snake.rear.y )
        elif(tail_dir == "right"):
            self.snake.enQueue(self.snake.rear.x + 1* self.g, self.snake.rear.y + 1* self.g)
# =========================== Question 3 ===========================
    def eat_body(self):
        for body in self.snake:
            count += 1
            if body.x == self.snake.rear.x and body.y == self.snake.rear.y:
                for i in range(count):
                    self.snake.deQueue()
        self.play_effect("eat_body")
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            new_item = self.item_list[random.randrange(len(self.item_list))]
            self.backpack.push(new_item)
            self.itemBoxPos
            self.play_effect("eat_item")

# =========================== Question 5 ===========================
    def use_item(self):
        use_item = self.backpack.top.item
        item_str = "item_" + use_item
        self.item_str = True
        self.backpack.pop()