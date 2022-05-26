# =========================== Question 1 ===========================

#Creating moving function for a snake    
    def move(self): 
        
        #The head of the snake will have coordinates (x,y)
        headx = self.snake.rear.x
        heady = self.snake.rear.y
        
        #One unit will be equal to self.g = 30 pixel
        #If go down, coordinates will be (x,y+1)
        if self.dir == "down":
            heady += self.g
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()
            
        #If go up, coordinates will be (x,y-1)
        if self.dir == "up":
            heady -= self.g
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()
            
        #If go left, coordinates will be (x-1,y)
        if self.dir == "left":
            headx -= self.g
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()
            
        #If go right, coordinate will be (x+1,y)
        if self.dir == "right":
            headx += self.g
            self.snake.enQueue(headx, heady)
            self.snake.deQueue()
            
# =========================== Question 2 ===========================

#Function to add tail for the snake when they eat item

    def add_tail(self):
        
        #The tail of the snake will have coordinates (x,y)
        tailx = self.snake.front.x
        taily = self.snake.front.y
        
        #Create node for the new tail
        newtail = Node(tailx, taily)
        newtail.next = self.snake.front
        self.snake.front.pre = newtail
        self.snake.front = newtail
        
# =========================== Question 3 ===========================

#Function for eating its body
    def eat_body(self):
        
        #Variable head will be the node front of the snake
        head = self.snake.front
        if not head:
            return False
        body = head.next
        
        while body:            
            #Check whether the coordinates of the head are equal to the coordinates of its body or not
            if (head.x == body.x) and (head.y == body.y):
                self.play_effect("eat_body")
                return True
            body = body.next
        return False
    
# =========================== Question 4 ===========================

#Function to eat and store items in the bag

    def eat_item(self): 
        if self.itemBoxPos != None:
            #If coordinates of head are equal to the coordinates of the item -> store the iteam in list
            if self.snake.rear.x == self.itemBoxPos[0] and self.snake.rear.y == self.itemBoxPos[1]:
                self.backpack.push(self.item_list[random.randrange(0,4)])
                self.play_effect("eat_item")
                self.itemBoxPos = None      #Then return the list to None 

# =========================== Question 5 ===========================

#Function to use stored items
 
    def use_item(self): 
        if self.backpack.isEmpty() == False:
            #Use the top item in the list
            self.item = self.backpack.top.item
            if self.item == "BlackHole":
                self.item_BlackHole = True
            if self.item == "Gamble":
                self.item_Gamble = True
            if self.item == "Brake":
                self.item_Brake = True
            if self.item == "FruitBasket":
                self.item_FruitBasket = True
            self.backpack.pop()     #Can use items in the top list when press space button