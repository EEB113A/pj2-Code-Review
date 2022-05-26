# =========================== Question 1 ===========================
    def move(self):
        if self.dir=="up":#如果方向往上
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y-self.g)#蛇頭y上移一格
            self.snake.deQueue()#尾巴去掉一格
        if self.dir=="down":#如果方向往下
            self.snake.enQueue(self.snake.rear.x,self.snake.rear.y+self.g)#蛇頭y下移一格
            self.snake.deQueue()#尾巴去掉一格
        if self.dir=="left":#如果方向往左
            self.snake.enQueue(self.snake.rear.x-self.g,self.snake.rear.y)#蛇頭x左移一格
            self.snake.deQueue()#尾巴去掉一格
        if self.dir=="right":#如果方向往右
            self.snake.enQueue(self.snake.rear.x+self.g,self.snake.rear.y)#蛇頭x右移一格
            self.snake.deQueue()#尾巴去掉一格
# =========================== Question 2 ===========================
    def add_tail(self):
        nodex=Node(0,0)#先設一個節點之後要加到尾巴
        nodex.next=self.snake.front.next#將nodex指標next指向尾巴的指標next
        nodex.pre=self.snake.front#將nodex指標pre指向尾巴
        self.snake.front.next.pre=nodex#將尾巴的pre指向nodex
        self.snake.front.next=nodex#將尾巴的next指向nodex
# =========================== Question 3 ===========================
    def eat_body(self):
        tmp=self.snake.rear.pre#設tmp初始為蛇頭的後一個節點(之後會再往下一個節點找)
        while tmp!=None:#當蛇頭的後一節存在
            if (self.snake.rear.x==tmp.x and self.snake.rear.y==tmp.y):#如果蛇頭的x座標以及y座標等於tmp的x座標以及y座標
                self.play_effect("eat_body")#此時吃到身體播放音效
                tmp=tmp.next#將tmp移回蛇頭的位置
                while self.snake.front!=tmp:#從尾巴的節點開始看回來，如果節點不等於tmp的節點
                    self.snake.deQueue()#尾巴去掉一格
            else:#如果蛇頭的x座標以及y座標不等於tmp的x座標以及y座標
                tmp=tmp.pre#將tmp設為再往下的一個節點
# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:#如果蛇頭的x座標以及y座標等於道具方塊的x座標以及y座標
                self.itemBoxPos = None#道具消失
                self.play_effect("eat_item")#播放音效
                self.backpack.push(self.item_list[random.randrange(0,4)])#隨機將道具列表中的其中一個push進道具背包

# =========================== Question 5 ===========================
    def use_item(self):
        self.item=self.backpack.top.item#用self.item儲存堆疊頂端的道具名稱
        if self.item=="BlackHole":#如果self.item==黑洞
            self.item_BlackHole=True#黑洞道具啟用(無敵)
        if self.item=="Brake":#如果self.item==剎車
            self.item_Brake=True#剎車道具啟用(減速)
        if self.item=="FruitBasket":#如果self.item==水果籃
            self.item_FruitBasket=True#水果籃道具啟用(地圖噴出水果)
        if self.item=="Gamble":#如果self.item==賭博
            self.item_Gamble=True#賭博道具啟用(加分或死亡)
        self.backpack.pop()#道具背包扣除最新拿到的道具