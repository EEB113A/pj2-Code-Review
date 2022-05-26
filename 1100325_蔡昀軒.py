# =========================== Question 1 ===========================
    def move(self):
        self.lastnode = Node(self.snake.front.x,self.snake.front.y)  #記錄之後dequeue掉的蛇尾座標
        self.snake.deQueue()        #把拿出來的元素放成一個佇列
        if(self.dir == "right"):    #往右
            self.snake.enQueue(self.snake.rear.x+self.g , self.snake.rear.y)   #蛇頭x座標往右30(self.g),y座標不變
        elif(self.dir == "left"):   #往左
            self.snake.enQueue(self.snake.rear.x-self.g , self.snake.rear.y)   #蛇頭x座標往左30(self.g),y座標不變
        elif(self.dir == "down"):   #往下
            self.snake.enQueue(self.snake.rear.x , self.snake.rear.y+self.g)   #蛇頭x座標不變,y座標增加30(self.g)
        elif(self.dir == "up"):     #往上
            self.snake.enQueue(self.snake.rear.x , self.snake.rear.y-self.g)   #蛇頭x座標不變,y座標減少30(self.g)
            

        
# =========================== Question 2 ===========================
    def add_tail(self):
        self.snake.front.pre = self.lastnode    #吃到食物後從蛇尾新增一塊(往pre)也就是從lastnode恢復一塊(lastnode為紀錄被dequeue掉蛇尾的部分)
        self.lastnode.next = self.snake.front   #lastnode的下一個節點,也就是設為原本蛇尾front的位置
        self.snake.front = self.lastnode        #接著把蛇尾設置成新的節點lastnode

            
# =========================== Question 3 ===========================
    def eat_body(self):
        ptr1 = self.snake.front     #先設定一個ptr1暫存蛇尾的座標位置
        while ptr1.next != None:    #在ptr1下一個節點不為空值的情況下
            if(ptr1.x == self.snake.rear.x and ptr1.y == self.snake.rear.y):  #如果ptr1的x y座標分別等於蛇頭的x y座標(兩者重疊)
                self.play_effect("eat_body")   #音效
                ptr2 = self.snake.front        #再設一個ptr2代表新暫存的蛇尾
                while ptr1 != ptr2:            #原暫存和新暫存的座標不同時
                    ptr2 = ptr2.next           #更新為下一個節點
                    self.snake.deQueue()       #把拿出來的蛇尾加入佇列
                self.snake.deQueue()           #同上
                break
            ptr1 = ptr1.next                   #蛇尾座標更新(下一個節點)

# =========================== Question 4 ===========================
    def eat_item(self):
        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            if(self.itemBoxPos[0] == self.snake.rear.x and self.itemBoxPos[1] == self.snake.rear.y):  #若道具方塊座標的x座標[0]和蛇頭x座標相同且道具方塊座標的y座標[1]和蛇頭y座標相同
                self.play_effect("eat_item")   #音效
            self.backpack.push(self.item_list[random.randrange(4)])   #背包內加入隨機的一個道具
            self.itemBoxPos = None   #再把道具方塊座標(self.itemBoxPos)重設成None

# =========================== Question 5 ===========================
    def use_item(self):
        self.item = self.backpack.top.item    #用self.item儲存堆疊頂端的道具名稱
        if self.item == "BlackHole":          #若道具名稱(字串)為BlackHole
            self.item_BlackHole = True        #啟用該道具(True)
        elif self.item == "Brake":            #若道具名稱(字串)為Brake
            self.item_Brake = True            #啟用該道具(True)
        elif self.item =="FruitBasket":       #若道具名稱(字串)為FruitBasket
            self.item_FruitBasket = True      #啟用該道具(True)
        elif self.item =="Gamble":            #若道具名稱(字串)為Gamble
            self.item_Gamble = True           #啟用該道具(True)
        self.backpack.top.pop()               #刪除背包堆疊頂端的道具