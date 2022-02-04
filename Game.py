import random
from math import floor,log10

# Constants 
new_values=[2,4]
winning_value=2048
MAX_DIGITS=floor(log10(winning_value)+1) 

# Globals
location=None # Position of the newly added value. Used for coloring.

class Game:
    def __init__(self,n):           
        self.n=n                                # Board size - n
        self.board=[[-1]*n for i in range(n)]   # Board intialized with -1 for all cells
        self.empty=[]                           # List which will contain the location of empty cells


    def start(self):            
        seen=[]
        for i in range(2):
            x,y=self.get_random_position()
            while (x,y) in seen:        # While loop to make sure that the two cells are not the same
                x,y=self.get_random_position()
            val=random.choice(new_values)   # Choose a random value between 2 or 4
            self.board[x][y]=val 
            seen.append((x,y))
        self.refresh_empty()


    # Method to get a random cell location 
    def get_random_position(self):              
        x=random.randint(0,self.n-1)
        y=random.randint(0,self.n-1)
        return (x,y)


    # Method to re-calculate the empty cells
    def refresh_empty(self): 
        self.empty.clear()         
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j]==-1:
                    self.empty.append((i,j))


    # Driver method - Returns 1 if the game is won and -1 if lost
    def move(self,direction):  

       # variable to keep track of which direction the merging of cells should happen
        right_to_left=False                 
        if direction==2 or direction==4:
            right_to_left=True 
    
        idx=0
        while(idx<self.n):
            elements=self.get_elements(direction,idx)       # Get the elements of a row or column
            new_elements=self.merge(elements,right_to_left)    # Add and merge compatible elements
            if new_elements==[]:
                return  1
            self.replace(new_elements,idx,direction,right_to_left)      # Replace the row or column with the merged values
            idx+=1
        
        if len(self.empty)==0:    # If no cells are empty game is lost
            return -1

        self.set_new_value()      # else, set a value in one of the empty cells

    
    # Method which adds and merges the elements
    def merge(self,elements,rev):
        new_elements=[]
        stack=[]

        # if direction is right or down, then reverse the elements
        # makes it easier to work with further down the line
        if rev==True:
            elements.reverse()

        for i in elements:
            if len(stack)==0:
                stack.append(i)
            else:
                # Double the value if the top of stack matches with the current element
                if stack[-1]==i:    
                    v=2*stack[-1]

                    # if 2048 is reached then return [] denoting victory
                    if v==winning_value: 
                        return []

                    # Empty the stack into result array
                    for i in range(len(stack)-1):
                        new_elements.append(stack[i])
                    new_elements.append(v)

                    stack.clear()
                else:
                    stack.append(i)

        # Checking for leftover elements
        while len(stack)>0:
            new_elements.append(stack[0])
            stack.pop(0)

        # Padding the array till it reaches size N to make it easier to work with
        while len(new_elements)<self.n:
            new_elements.append(-1)

        return new_elements


    # Method to replace a row or column of the current board with updated values
    def replace(self,elements,idx,direction,rev):
        if rev==True:
            if direction==2:
                for col in range(self.n-1,-1,-1):
                    self.board[idx][col]=elements[self.n-col-1]
            elif direction==4:
                for col in range(self.n-1,-1,-1):
                    self.board[col][idx]=elements[self.n-col-1]
        else:
            if direction==1:
                for col in range(self.n):
                    self.board[idx][col]=elements[col]
            elif direction==3:
                for col in range(self.n):
                    self.board[col][idx]=elements[col]

    
    # Method to get the elements of a row or column
    def get_elements(self,direction,idx):
        elements=[]
        if direction==1 or direction==2:
            for i in self.board[idx]:
                if i!=-1:
                    elements.append(i)
        else:
            for i in range(self.n):
                if self.board[i][idx]!=-1:
                    elements.append(self.board[i][idx])
        return elements

    
    # Method for putting an new value in an empty cell
    def set_new_value(self):        
        global location
        self.refresh_empty()
        x,y=random.choice(self.empty)       # Select a random empty cell
        location=(x,y)
        value=random.choice(new_values)
        self.empty.remove((x,y))
        self.board[x][y]=value


    # Method for printing the 2048 board
    def print_board(self):      
        print(f"\n{'-'*29}")       
        for i in range(self.n):
            print("|",end="")
            
            for j in range(self.n):
                val=self.board[i][j]
                
                # Check if cell is empty. ie., -1 
                if val==-1:                
                    print("     ",end=" ")

                else:   
                    # Print spaces
                    digit=floor(log10(val)+1) 
                    for k in range((MAX_DIGITS-digit)):
                        print(" ",end="")
                    print(" ",end="")  

                    # Print newly added value in red
                    if (i,j)==location:
                        print(f"\033[91m{val}\033[00m",end=" ")
                    else:
                        print(val,end=" ")

                print("|",end="")

            print()
            print(f"{'-'*29}")       