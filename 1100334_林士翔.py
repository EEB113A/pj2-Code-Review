# =========================== Question 1 ===========================
    def move(self):

        cur=self.snake.front  # 先將變數 cur 貼到 front     
        for i in range(self.snake.len()-1): # 將蛇身到蛇尾都往前移一個位子
            cur.y,cur.x=cur.next.y, cur.next.x                  
            cur=cur.next            
            
        if self.dir== "right": # 最後將蛇頭移到以鍵盤輸入方向為基準，往前挪一格位子。        
            self.snake.rear.x+=self.g         
                    
        elif self.dir== "left":
            self.snake.rear.x-=self.g
            
                
        elif self.dir== "up":
            self.snake.rear.y-=self.g
             

        elif self.dir== "down":
            self.snake.rear.y+=self.g
# =========================== Question 2 ===========================
    def add_tail(self):

        front=self.snake.front 
        i=2*front.y-front.next.y # 利用向量的概念求出新節點的座標(新節點的座標-蛇尾的座標=蛇尾的座標-蛇尾下個節點的座標)
        j=2*front.x-front.next.x 
        new=Node(j,i) # 將new標籤貼給新節點
        new.next,front.pre,self.snake.front=front,new,new # 將new的next指向蛇尾，蛇尾的pre指向new，蛇尾的標籤重新貼到新節點
        
# =========================== Question 3 ===========================
    def eat_body(self):
        
        cur=self.snake.front        
        for i in range(self.snake.len()-3): # 從蛇尾開始檢查，找出被吃掉的節點。            
            if cur.x==self.snake.rear.x and cur.y==self.snake.rear.y:
                cur.next.pre,self.snake.front=None,cur.next # 被吃掉的節點的下個節點為cur.next
                # 將cur.next 的 pre 指向 None，再把蛇尾的標籤貼給cur.next
                self.play_effect("eat_body")                
                break                              
            cur=cur.next
        
        

# =========================== Question 4 ===========================
    def eat_item(self):

        if self.itemBoxPos != None: # 若道具方塊有顯現的話
            rear=self.snake.rear 
            i=random.randrange(0,4) # 產生0~3其中一個數字           
            if self .itemBoxPos[0]==rear.x and self .itemBoxPos[1]==rear.y:
                self.backpack.push(self.item_list[i]) # 將選到的一個道具放到背包堆疊中
                self.play_effect("eat_item")
                self.itemBoxPos=None
            

# =========================== Question 5 ===========================
    def use_item(self):
# ==================================================================
        self.item=self.backpack.top.item # 儲存堆疊頂端的道具名稱
        if self.item =="BlackHole":   # 判斷堆疊頂端的道具屬於哪個，再將道具的參數調成True 
            self.item_BlackHole = True

        elif self.item =="Gamble":            
            self.item_Gamble = True

        elif self.item =="Brake":            
            self.item_Brake = True

        elif self.item =="FruitBasket":            
            self.item_FruitBasket = True
        
        self.backpack.pop()  # 刪除背包堆疊頂端的道具