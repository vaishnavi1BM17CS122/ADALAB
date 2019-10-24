class BakeHouse:
    def __init__(self):
        self.occupied_table_list=[]
    def get_occupied_table_list(self):
        return self.occupied_table_list
   
    def allocate_table(self):
        self.occupied_table_list.sort()
        for i in range(1,10):
            if i not in self.occupied_table_list:
                print( i,"table allocated")
                self.occupied_table_list.append(i)
        
                break
            else:
                pass
        #self.occupied_table_list.append(i)
        return self.occupied_table_list
    def deallocate_table(self,table_number):
        #x=self.occupied_table_list.index(table_number)
        #self.occupied_table_list[self.occupied_table_list.index(table_number)]
        self.occupied_table_list.remove(table_number)
b=BakeHouse()
c=0
x=b.get_occupied_table_list()
#x[2]=1
#x[1]=3
while(1):
  y=input("enter a for allocate,d for delocate")
  if(y=='a'):
    n=int(input("enter the number of tables to be alloted"))
    for c in range(0,n):
      b.allocate_table()
  #c=c+1
#b.deallocate_table()
  if(y=='d'):
      ele=input("enter table_number")
      b.deallocate_table(ele)
