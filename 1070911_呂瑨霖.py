# =========================== Question 1 ===========================
    def move(self):
        if self.dir=="up":#往上
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y-self.g)#上一格
            self.snake.deQueue()#去一格
        if self.dir=="down":#往下
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y+self.g)#下一格
            self.snake.deQueue()#去一格
        if self.dir=="left":#往左
            self.snake.enQueue(self.snake.rear.x-self.g,self.snake.rear.y)#左移一格
            self.snake.deQueue()#去一格
        if self.dir=="right":#往右
            self.snake.enQueue(self.snake.rear.x+self.g,self.snake.rear.y)#右移一格
            self.snake.deQueue()#去一格
# =========================== Question 2 ===========================
    def add_tail(self):
        nodex=Node(0,0)#先設一個節點
        nodex.next=self.snake.front.next#將指標next指向尾巴next
        nodex.pre=self.snake.front#將指標pre指向尾巴
        self.snake.front.next.pre=nodex#將尾巴的pre指向nodex
        self.snake.front.next=nodex#將尾巴的next指向nodex
# =========================== Question 3 ===========================
    def eat_body(self):
        tmp=self.snake.rear.pre#設tmp初始為蛇頭的後一個節點
        while tmp!=None:#當蛇頭的後一節
            if (self.snake.rear.x==tmp.x and self.snake.rear.y==tmp.y):#如果蛇頭等於tmp的座標
                self.play_effect("eat_body")#播放音效
                tmp=tmp.next#將tmp移回蛇頭
                while self.snake.front!=tmp:#如果節點不等於tmp
                    self.snake.deQueue()#尾去一格
            else:#如果蛇頭的x座標以及y座標不等於tmp的x座標以及y座標
                tmp=tmp.pre#將tmp設為再往下的一個節點
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 道具有出現
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:#如果蛇頭等於道具座標
                self.itemBoxPos = None#道具消失
                self.play_effect("eat_item")#播放音效
                self.backpack.push(self.item_list[random.randrange(0,4)])#隨機將道具列表中的其中一個push進道具背包

# =========================== Question 5 ===========================
    def use_item(self):
        self.item=self.backpack.top.item#儲存道具名稱
        if self.item=="BlackHole":#如果吃黑洞
            self.item_BlackHole=True#黑洞啟用
        if self.item=="Brake":#如果吃剎車
            self.item_Brake=True#道具啟用
        if self.item=="FruitBasket":#如果吃水果籃
            self.item_FruitBasket=True#道具啟用
        if self.item=="Gamble":#如果吃賭博
            self.item_Gamble=True#道具啟用
        self.backpack.pop()#扣除最新道具
# ==================================================================