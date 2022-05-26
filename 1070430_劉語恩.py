# =========================== Question 1 ===========================
    def move(self):
        # 將蛇頭節點指向curNode
        curNode = self.snake.rear
        # 紀錄當前節點座標值
        curNodeOriginPos = [curNode.x, curNode.y]
        # 更新蛇頭座標
        if(self.dir=="up"):
            curNode.y -= self.g 
        elif(self.dir=="down"):
            curNode.y += self.g 
        elif(self.dir=="left"):
            curNode.x -= self.g 
        elif(self.dir=="right"):
            curNode.x += self.g 
        # 更新身體部位座標
        while curNode.pre != None:
            curNode = curNode.pre
            curNodeOriginPos[0], curNode.x =  curNode.x, curNodeOriginPos[0]
            curNodeOriginPos[1], curNode.y =  curNode.y, curNodeOriginPos[1]
# =========================== Question 2 ===========================
    def add_tail(self):
        # 新尾巴的X座標為self.snake.front.x+(self.snake.front.x-self.snake.front.next.x)
        # 新尾巴的Y座標為self.snake.front.y+(self.snake.front.y-self.snake.front.next.y)
        newTail = Node(2*self.snake.front.x-self.snake.front.next.x, 2*self.snake.front.y-self.snake.front.next.y)
        # 將新的尾巴節點添加到佇列裡
        newTail.next = self.snake.front
        self.snake.front.pre = newTail
        self.snake.front = newTail
# =========================== Question 3 ===========================
    def eat_body(self):
        # 只有蛇長度大於4時才有重疊的可能，因此加入if判斷來增加程式效能
        if self.snake.len()>4:
            # 將第3個蛇身節點指向curNode
            curNode = self.snake.rear.pre.pre.pre
            # 檢查是否有蛇身、蛇頭碰撞
            while curNode.pre != None:
                # 檢查是否有碰撞
                if curNode.pre.x == self.snake.rear.x and curNode.pre.y == self.snake.rear.y:
                    # 刪除後續蛇身
                    curNode.pre.next = None
                    curNode.pre = None
                    # 將蛇尾指向當前節點
                    self.snake.front = curNode
                    # 播放音效
                    self.play_effect("eat_body")
                    break
                # 檢查下一個身體節點
                curNode = curNode.pre
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            # 吃到道具方塊
            if self.itemBoxPos == [self.snake.rear.x, self.snake.rear.y]:
                # 將隨機道具存放到背包堆疊
                ## 用sample取物的方式，效能會比 self.item_list[random.randrange(0, len(self.item_list))] 稍好
                self.backpack.push(random.sample(self.item_list, 1)[0])
                # 道具方塊重置
                self.itemBoxPos = None
                # 播放音效
                self.play_effect("eat_item")
# =========================== Question 5 ===========================
    def use_item(self):
        # self.item 儲存堆疊頂端的道具名稱
        self.item = self.backpack.top.item
        # 啟用道具
        if self.item == "BlackHole":
            self.item_BlackHole = True
        elif self.item == "Brake":
            self.item_Brake = True
        elif self.item == "FruitBasket":
            self.item_FruitBasket = True
        elif self.item == "Gamble":
            self.item_Gamble = True
        # 刪除背包堆疊頂端的道具
        self.backpack.pop()