# =========================== Question 1 ===========================
    def move(self): # 根據方向移動蛇的坐標
        self.snake.reverse()                    #先把蛇相反

        front = self.snake.front
        original_x = front.x                    #原本的x座標變成蛇頭x座標
        original_y = front.y                    #原本的y座標變成蛇頭y座標
        target_x = original_x                   #下一步的x座標變成原來x座標
        target_y = original_y                   #下一步的y座標變成原來y座標
        if self.dir == 'up':                    #若方向向上
            target_y = original_y - self.g      #y軸往上一格

        elif self.dir == 'down':                #若方向向下
            target_y = original_y + self.g      #y軸往下一格

        elif self.dir == 'left':                #若方向向左
            target_x = original_x - self.g      #x軸往左一格

        elif self.dir == 'right':               #若方向向右
            target_x = original_x + self.g      #x軸往右一格

        front.x = target_x                      #蛇頭的方向是下一步的x座標
        front.y = target_y                      #蛇頭的方向是下一步的y座標



        pointer = front.next                    #設pointer是蛇頭的下一個
        while pointer != None:                  #當蛇頭後面有身體
            target_x = original_x
            target_y = original_y
            original_x = pointer.x
            original_y = pointer.y                  #蛇身就一直跟著前一個的方向走
            pointer.x = target_x
            pointer.y = target_y
            pointer = pointer.next
        self.snake.reverse()                    #把蛇相反回原本的樣子
# =========================== Question 2 ===========================
    def add_tail(self):
        self.snake.reverse()                                                #先把蛇相反
        pointer = self.snake.rear                                           #把pointer設為蛇頭
        second_pointer = pointer.pre                                        #second_pointer設為蛇尾前一個
        change_x = second_pointer.x - pointer.x                             #change_x是蛇頭前一個的x座標減蛇頭的x座標
        change_y = second_pointer.y - pointer.y                             #change_y是蛇頭前一個的y座標減蛇頭的y座標
        self.snake.enQueue(pointer.x + change_x, pointer.y + change_y)      #帶進enQueue的function
        self.snake.reverse()                                                #把蛇相反回原本的樣子
# =========================== Question 3 ===========================
    def eat_body(self): # 吃到玩家蛇的身體
        self.snake.reverse()                                    #先把蛇相反

        front = self.snake.front                                #把front設為蛇尾
        pointer = front.next                                    #把pointer設為蛇尾後一個
        is_touch = False                                        #把is_touch先設為false
        while pointer != None:                                  #當蛇尾後一個有東西
           if front.x == pointer.x and front.y == pointer.y:    #如果蛇頭的座標跟身體任一個點的座標一樣
               is_touch = True                                  #is_touch就是true
               break                                            #就跳出迴圈
           pointer = pointer.next
        self.snake.reverse()                                    #把蛇相反回原本的樣子
        pointer2 = self.snake.front                             #把pointer2設為蛇尾
        if is_touch:                                            #如果is_touch是true
            while pointer != pointer2:                          #當蛇尾後一個不等於蛇尾
                self.snake.printQueue()                         #跑printQueue()的fuction
                self.snake.deQueue()                            #跑snake.deQueue() 的fuction
                pointer2 = pointer2.next                        #蛇尾是蛇尾的下一個
                self.play_effect("eat_body")                    #撥放音效
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            self.snake.reverse()        #先把蛇相反
            front = self.snake.front        #把front設為蛇頭
            if front.x == self.itemBoxPos[0] and front.y == self.itemBoxPos[1]:     #若吃到道具
                self.play_effect("eat_item")                        #撥放音效
                self.backpack.push(random.choice(self.item_list))   #把道具存放到背包堆疊中並隨機選擇一個道具
                self.itemBoxPos = None                              #把道具方塊座標重設成None
            self.snake.reverse()            #把蛇相反回原本的樣子

# =========================== Question 5 ===========================
    def use_item(self): # 使用道具
        top_item = self.backpack.top                        #top_item是包包最新拿到的
        self.backpack.pop()
        # ["BlackHole", "Brake", "FruitBasket", "Gamble"]
        if top_item == "BlackHole":                         #如果最新拿到的道具是BlackHole
            self.item_BlackHole = True                      #BlackHole變成true讓BlackHole功能打開
        elif top_item == "Brake":                           #如果最新拿到的道具是Brake
            self.item_Brake = True                          #Brake變成true讓Brake功能打開
        elif top_item == "FruitBasket":                     #如果最新拿到的道具是FruitBasket
            self.item_FruitBasket = True                    #FruitBasket變成true讓FruitBasket功能打開
        elif top_item == "Gamble":                          #如果最新拿到的道具是Gamble
            self.item_Gamble = True                         #Gamble變成true讓Gamble功能打開