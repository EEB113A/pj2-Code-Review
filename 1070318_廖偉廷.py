# =========================== Question 1 ===========================
    def move(self):
        
        # 方向往上
        if self.dir == "up":
            # 蛇頭上移
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y - self.g)
            # 蛇尾刪掉一格
            self.snake.deQueue()
        # 方向往下
        if self.dir == "down":
            # 蛇頭下移
            self.snake.enQueue(self.snake.rear.x, self.snake.rear.y + self.g)
            # 蛇尾刪掉一格
            self.snake.deQueue()
        # 方向往左
        if self.dir == "left":
            # 蛇頭左移
            self.snake.enQueue(self.snake.rear.x - self.g, self.snake.rear.y)
            # 蛇尾刪掉一格
            self.snake.deQueue()
        # 方向往右
        if self.dir == "right":
            # 蛇頭右移
            self.snake.enQueue(self.snake.rear.x + self.g, self.snake.rear.y)
            # 蛇尾刪掉一格
            self.snake.deQueue()
# =========================== Question 2 ===========================
    def add_tail(self): 

        # 新增一個要加到蛇尾的節點
        new_node = Node(self.snake.front.x, self.snake.front.y)
        # 新節點指標next指向蛇尾的指標next
        new_node.next = self.snake.front.next
        # 新節點指標pre指向蛇尾
        new_node.pre = self.snake.front
        # 蛇尾的指標next的指標pre指向新節點
        self.snake.front.next.pre=new_node
        # 蛇尾的指標next指向新節點
        self.snake.front.next=new_node
# =========================== Question 3 ===========================
    def eat_body(self):
        
        # 蛇頭的座標
        head_x = self.snake.rear.x
        head_y = self.snake.rear.y
        # 蛇頭的下一個節點
        tmp = self.snake.rear.pre
        while tmp != None:
            # tmp的座標是否等於蛇頭座標
            if tmp.x == head_x and tmp.y == head_y:
                self.play_effect("eat_body")
                # tmp回到蛇頭節點
                tmp = tmp.next
                # 蛇尾節點不等於tmp節點
                while self.snake.front != tmp:
                    # 刪除節點
                    self.snake.deQueue()
            else:
                # 再往下一個節點 
                tmp = tmp.pre
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            # 蛇頭座標
            head_x = self.snake.rear.x
            head_y = self.snake.rear.y
            # 蛇頭座標是否等於道具方塊座標
            if head_x == self.itemBoxPos[0] and head_y == self.itemBoxPos[1]:
                # 道具消失
                self.itemBoxPos = None
                self.play_effect("eat_item")
                # 隨機選擇一個道具
                item_choice = self.item_list[random.randrange(0,4)]
                # 道具放到背包堆疊
                self.backpack.push(item_choice)

# =========================== Question 5 ===========================
    def use_item(self):
        
        # 儲存堆疊頂端的道具名稱
        self.item = self.backpack.top.item
        # 啟用道具
        if self.item == "BlackHole":
            self.item_BlackHole = True
        if self.item == "Brake":
            self.item_Brake = True 
        if self.item == "FruitBasket":
            self.item_FruitBasket = True
        if self.item == "Gamble":
            self.item_Gamble = True
        self.backpack.pop()