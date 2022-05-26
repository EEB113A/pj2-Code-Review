# =========================== Question 1 ===========================
    def move(self): 
        count = 0                               #設定一個參數來停止while迴圈
        if self.dir == "right":                 #當self.dir輸入是向右時                 
            while count < 1:
                x = self.snake.rear.x           #先讀出蛇頭的x座標
                y = self.snake.rear.y           #再讀出蛇頭的y座標 
                x_next = x + self.g             #確定蛇頭向右後的x座標
                self.snake.enQueue(x_next,y)    #將蛇佇列新增一個節點作為新蛇頭
                self.snake.deQueue()            #並把蛇尾的節點刪除 完成向右移動的畫面
                count+=1                        #count+1停止while迴圈

        if self.dir == "down":                  #當self.dir輸入是向下時   
            while count < 1:                    
                x = self.snake.rear.x           #先讀出蛇頭的x座標
                y = self.snake.rear.y           #再讀出蛇頭的y座標   
                y_next = y + self.g             #確定蛇頭向下後的y座標
                self.snake.enQueue(x,y_next)    #將蛇佇列新增一個節點作為新蛇頭
                self.snake.deQueue()            #並把蛇尾的節點刪除 完成向下移動的畫面
                count+=1                        #count+1停止while迴圈

        if self.dir == "up":                    #當self.dir輸入是向上時
            while count < 1:
                x = self.snake.rear.x           #先讀出蛇頭的x座標
                y = self.snake.rear.y           #再讀出蛇頭的y座標
                y_next = y - self.g             #確定蛇頭向上後的y座標
                self.snake.enQueue(x,y_next)    #將蛇佇列新增一個節點作為新蛇頭
                self.snake.deQueue()            #並把蛇尾的節點刪除 完成向上移動的畫面
                count+=1                        #count+1停止while迴圈

        if self.dir == "left":                  #當self.dir輸入是向左時
            while count < 1:
                x = self.snake.rear.x           #先讀出蛇頭的x座標
                y = self.snake.rear.y           #再讀出蛇頭的y座標
                x_next = x - self.g             #確定蛇頭向左後的x座標
                self.snake.enQueue(x_next,y)    #將蛇佇列新增一個節點作為新蛇頭
                self.snake.deQueue()            #並把蛇尾的節點刪除 完成向左移動的畫面
                count+=1                        #count+1停止while迴圈
# =========================== Question 2 ===========================
    def add_tail(self): 
        x = self.snake.front.x                  #先讀出蛇尾的x座標
        y = self.snake.front.y                  #再讀出蛇尾的y座標
        new_tail = Node(x,y)                    #設立一個節點作為新的尾巴
        new_tail.next = self.snake.front        #將新尾巴的指往下一個節點的指標指向原本的尾巴
        self.snake.front.pre = new_tail         #將原本的尾巴指向前一個節點的指標指向新尾巴
        self.snake.front = new_tail             #將蛇尾指標指向新尾巴
# =========================== Question 3 ===========================
    def eat_body(self):
        count2 = self.snake.len()                       #設立一個函數以便偵測蛇頭撞到身體的哪個位置
        tmp = self.snake.rear.pre                       #設立一個函數儲存蛇頭以前的節點
        while tmp != None:                              #建立while迴圈 當跑到空節點時停止
            head_x = self.snake.rear.x                  #讀出蛇頭x座標
            head_y = self.snake.rear.y                  #讀出蛇頭y座標
            body_x = tmp.x                              #讀出蛇頭前一個身體節點x座標
            body_y = tmp.y                              #讀出蛇頭前一個身體節點y座標
            if head_x != body_x or head_y != body_y:    #當蛇頭和身體節點座標不一時 不是在這個位置撞上
                tmp = tmp.pre                           #將儲存函數設為身體第一個節點的前一個節點
                count2 -= 1                             #將偵測函數-1
            if head_x == body_x and head_y == body_y:   #當蛇頭和身體節點座標一致 表示是在這個位置撞上
                if count2 > 0:                          #當偵測函數還大於1時
                    self.snake.deQueue()                #從尾巴開始刪除身體節點
                    count2-=1                           #將偵測函數-1
                if count2 == 0:                         #當偵測函數=0時 表示已經將撞上部位以後的身體節點刪除完畢
                    self.play_effect("eat_body")        #播放刪除音效
                    break                               #離開迴圈
# ==================================================================

# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None:                     #當場上有道具箱子時
            head_x = self.snake.rear.x                  #讀出蛇頭x座標
            head_y = self.snake.rear.y                  #讀出蛇頭y座標
            if self.itemBoxPos[0] ==head_x and self.itemBoxPos[1] == head_y:    #如果道具箱子的座標和蛇頭座標重疊 表示吃到了道具箱
                pick = random.randrange(0,4)            #從0~3中隨機生成變數選取道具
                item = self.item_list[pick]             #給定item作為道具函數
                self.backpack.push(item)                #將道具push進堆疊列
                self.itemBoxPos = None                  #並將道具箱從場上移除

# ==================================================================
# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top                   #給定item儲存道具欄位最上方的道具
        if self.item == "BlackHole":                    #如果此道具是BlackHole
            self.item_BlackHole = True                  #將BlackHole函數設為True
        if self.item == "Brake":                        #如果此道具是Brake
            self.item_Brake = True                      #將Brake函數設為True
        if self.item == "FruitBasket":                  #如果此道具是FruitBasket
            self.item_FruitBasket = True                #將FruitBasket函數設為True
        if self.item == "Gamble":                       #如果此道具是Gamble
            self.item_Gamble = True                     #將Gamble函數設為True
        self.backpack.pop()                             #將道具欄位最上方道具移出
# ==================================================================