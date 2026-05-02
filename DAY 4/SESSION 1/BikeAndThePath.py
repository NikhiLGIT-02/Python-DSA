class BikeAndThePath:
    N=4

    def findPath(self,maze,row,col,path):
        if row<0 or col<0 or row>=self.N or col>=self.N:
            return False
        if maze[row][col]==0:
            return False
        
        if row==self.N-1 and col==self.N-1:
            print(path)
            return True
       
        maze[row][col]=0

        #DOWN
        if self.findPath(maze,row+1,col,path+"D"):
            return True
        
        #Right
        if self.findPath(maze,row,col+1,path+"R"):
            return True
        
        maze[row][col]=1
        return False




#Main
maze=[[1,0,0,0],
      [1,1,0,1],
      [0,1,0,0],
      [1,1,1,1]]
#for i in range(4):
#    row=list(map(int,input().split()))
#    maze.append(row)

obj=BikeAndThePath()
if not obj.findPath(maze,0,0,""):
    print("No path found")