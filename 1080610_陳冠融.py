# =========================== Question 1 ===========================

    def move(self):
        if (self.dir == "up"):
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y - 30)
            self.snake.deQueue()
        if (self.dir == "down"):
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y + 30)
            self.snake.deQueue()
        if (self.dir == "left"):
            self.snake.enQueue(self.snake.rear.x - 30, self.snake.rear.y)
            self.snake.deQueue()
        if (self.dir == "right"):
            self.snake.enQueue(self.snake.rear.x + 30, self.snake.rear.y)
            self.snake.deQueue()

# =========================== Question 2 ===========================

    def add_tail(self):
        new_p = Node(0, 0)
        self.snake.front.pre = new_p
        new_p.next = self.snake.front
        self.snake.front = new_p

# =========================== Question 3 ===========================

    def eat_body(self):
        sn_head_x = self.snake.rear.x
        sn_head_y = self.snake.rear.y
        fir_body = self.snake.rear.pre
        while fir_body:
            if(fir_body.x == sn_head_x and fir_body.y == sn_head_y):
                body = fir_body.next
                body.pre = None
                fir_body.next = None
                self.snake.front = body
                self.play_effect("eat_body")
            fir_body = fir_body.pre

# =========================== Question 4 ===========================

    def eat_item(self):
        if self.itemBoxPos != None:  # 若道具方塊有顯現的話
            box_x = self.itemBoxPos[0]
            box_y = self.itemBoxPos[1]
            if (box_x == self.snake.rear.x and box_y == self.snake.rear.y):
                item = random.randrange(len(self.item_list))
                self.backpack.push(self.item_list[item])
                self.itemBoxPos = None
                self.play_effect("eat_item")
            elif(box_x != self.snake.rear.x or box_y != self.snake.rear.y):
                box_x = random.randrange(1, self.width//self.g)
                box_y = random.randrange(1, self.width//self.g)

# =========================== Question 5 ===========================

    def use_item(self):
        self.item = self.backpack.top.item
        if(self.item == "BlackHole"):
            self.item_BlackHole != False
            self.backpack.pop()
        if(self.item == "Brake"):
            self.item_Brake != False
            self.backpack.pop()
        if(self.item == "FruitBasket"):
            self.item_FruitBasket != False
            self.backpack.pop()
        if(self.item == "Gamble"):
            self.item_Gamble != False
            self.backpack.pop()