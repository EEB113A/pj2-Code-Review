# =========================== Question 1 ===========================
    def move(self):
        tail = self.snake.front                 #定義一個變數tail貼在蛇尾上
        if self.dir == "up":                    #如果玩家按下w或向上鍵
            for i in range(self.snake.len()-1): #此迴圈在寫把蛇尾逐漸往前，直到蛇頭和蛇尾中間沒有任何節點。
                tail.x = tail.next.x            #把蛇尾前一個的x座標更新為原本蛇尾的x座標
                tail.y = tail.next.y            #把蛇尾前一個的y座標更新為原本蛇尾的y座標
                tail = tail.next                #蛇尾再往前一個節點
                
            self.snake.rear.y -= self.g         #蛇頭的y座標減少30px的位移量

        elif self.dir == "down":                #如果玩家按下s或向下鍵
            for i in range(self.snake.len()-1): #此迴圈在寫把蛇尾逐漸往前，直到蛇頭和蛇尾中間沒有任何節點。
                tail.x = tail.next.x            #把蛇尾前一個的x座標更新為原本蛇尾的x座標
                tail.y = tail.next.y            #把蛇尾前一個的y座標更新為原本蛇尾的y座標
                tail = tail.next                #蛇尾再往前一個節點
                
            self.snake.rear.y += self.g         #蛇頭的y座標增加30px的位移量

        elif self.dir == "left":                #如果玩家按下a或向左鍵
            for i in range(self.snake.len()-1): #此迴圈在寫把蛇尾逐漸往前，直到蛇頭和蛇尾中間沒有任何節點。
                tail.x = tail.next.x            #把蛇尾前一個的x座標更新為原本蛇尾的x座標
                tail.y = tail.next.y            #把蛇尾前一個的y座標更新為原本蛇尾的y座標
                tail = tail.next                #蛇尾再往前一個節點
                
            self.snake.rear.x -= self.g         #蛇頭的x座標減少30px的位移量

        elif self.dir == "right":               #如果玩家按下d或向右鍵
            for i in range(self.snake.len()-1): #此迴圈在寫把蛇尾逐漸往前，直到蛇頭和蛇尾中間沒有任何節點。
                tail.x = tail.next.x            #把蛇尾前一個的x座標更新為原本蛇尾的x座標
                tail.y = tail.next.y            #把蛇尾前一個的y座標更新為原本蛇尾的y座標
                tail = tail.next                #蛇尾再往前一個節點
                
            self.snake.rear.x += self.g         #蛇頭的x座標增加30px的位移量
# =========================== Question 2 ===========================
    def add_tail(self):
        new = Node(self.g,self.g)               #建立一個新節點叫做new
        new.x = self.snake.front.x              #把蛇尾的x座標更新為新節點的x座標
        new.y = self.snake.front.y              #把蛇尾的y座標更新為新節點的y座標
        new.next = self.snake.front             #將new的next指標指向蛇尾
        self.snake.front.pre =  new             #將蛇尾的pre指標指向new，如此一來蛇尾和新節點就連起來。
        self.snake.front = new                  #再把蛇尾更新為new
# =========================== Question 3 ===========================
    def eat_body(self):
        tmp = self.snake.rear                                #定義一個變數tmp為蛇頭
        cur = self.snake.front                               #定義一個變數cur為蛇尾
        while cur.next != None:                              #外層迴圈當cur.next指向的節點不等於空的時候進入
            if tmp.x == cur.x and tmp.y == cur.y:            #判斷目前cur的x和y座標是否和tmp相同(代表吃到)
                self.play_effect("eat_body")                 #播放音效
                while self.snake.front != cur:               #內層迴圈當蛇尾不等於現在的cur時進入，從尾巴開始刪除節點。
                    self.snake.front = self.snake.front.next #蛇尾往前一個節點
                    self.snake.front.pre = None              #蛇尾的pre指標指向空，代表後面沒有任何節點。
                break                                        #當刪除完成後不需再進入迴圈。
            cur = cur.next                                   #cur變成下一個節點
# =========================== Question 4 ===========================
    def eat_item(self):
        head = self.snake.rear                                               #定義一個變數head為蛇頭
        if self.itemBoxPos != None:                                          # 若道具方塊有顯現的話
            if head.x == self.itemBoxPos[0] and head.y == self.itemBoxPos[1]:#如果蛇頭的x和y座標和道具箱子的x和y座標相同(代表吃到道具箱)
                r = random.randrange(4)                                      #在4種道具中隨機挑選一種
                self.backpack.push(self.item_list[r])                        #把選到的道具放入背包堆疊
                self.itemBoxPos = None                                       #把道具方塊的座標更新為空
                self.play_effect("eat_item")                                 #播放音效
# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item  #將背包堆疊頂端的道具存入self.item
        if  self.item == "FruitBasket":     #如果道具為"水果籃"
            self.item_FruitBasket = True    #將它的參數設為True
            self.backpack.pop()             #取出背包頂端之道具
        elif self.item == "BlackHole":      #如果道具為"黑洞"
            self.item_BlackHole = True      #將它的參數設為True
            self.backpack.pop()             #取出背包頂端之道具
        elif self.item == "Brake":          #如果道具為"煞車"
            self.item_FruitBasket = True    #將它的參數設為True
            self.backpack.pop()             #取出背包頂端之道具
        elif self.item == "Gamble":         #如果道具為"煞車"
            self.item_FruitBasket = True    #將它的參數設為True
            self.backpack.pop()             #取出背包頂端之道具