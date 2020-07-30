class Node:
	def __init__(self,data):
		self.__data=data
		self.__next=None
	
	def get_data(self):
		return self.__data
	
	def set_data(self,data):
		self.__data=data
	
	def get_next(self):
		return self.__next
	
	def set_next(self,next_node):
		self.__next=next_node

class LinkedList:
	def __init__(self):
		self.__head=None
		self.__tail=None
	
	def get_head(self):
		return self.__head
	
	def get_tail(self):
		return self.__tail
	
	def add(self,data):
		new_node=Node(data)
		if self.__head is None:
			self.__head=self.__tail=new_node
		else:
			self.__tail.set_next(new_node)
			self.__tail=new_node
	
	def display(self):
		temp=self.__head
		while temp is not None :
			print(temp.get_data())
			temp=temp.get_next()

	def find_node(self,data):
		temp = self.__head
		while(temp is not None):
			if temp.get_data() == data:
				return temp
			temp = temp.get_next()
		return None

    def insert(self,data,data_before):
        temp_node = self.find_node(data_before)
        new_node = Node(data)
        if temp_node.get_next() is None:
            temp_node.set_next(new_node)
        else:
            new_node.set_next(temp_node.get_next())
            temp_node.set_next(new_node)
	
	#You can use the below __str__() to print the elements of the DS object while debugging
	def __str__(self):
		temp=self.__head
		msg=[]
		while(temp is not None):
			msg.append(str(temp.get_data()))
			temp=temp.get_next()
		msg=" ".join(msg)
		msg="Linkedlist data(Head to Tail): "+ msg
		return msg

# Function to get the no of nodes in a Linked List
def count_nodes(list):
	count=0
	temp = list.get_head()
	 while(temp is not None):
			count += 1
			temp=temp.get_next()
	return count

list1=LinkedList()
list1.add("Sugar")
list1.add("Milk")
list1.add("Tea")
list1.add("Honey")

list1.display()

#Similarly add all the specified element(s)