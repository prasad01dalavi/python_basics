class Person:
    my_member_variable = 5

    def setName(self, firstName, lastName):
        self.firstName = firstName  # need to creat self object within the class
        self.lastName = lastName  # and it is going to perform the operation

    def showName(self):  # self argument is always present in any member funtion arguments
        print 'In class, showName method:', self.firstName, self.lastName


name = Person()  # creating object of Person class
name.setName("Prasad", "Dalavi")  # accessing the class method using object name
name.showName()
print 'class my_member_variable =', name.my_member_variable   # 5
