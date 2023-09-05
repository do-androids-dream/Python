"""
Your task is to write a program which allows teachers to create a multiple choice test in a class called Testpaper and 
to be also able to assign a minimum pass mark. The testpaper's subject should also be included. 
The attributes are in the following order:

1. subject
2. markscheme
3. pass_mark
As well as that, we need to create student objects to take the test itself! Create another class called Student and do the following:

Create an attribute called tests_taken and set the default as  'No tests taken'.
Make a method called take_test(), which takes in the testpaper object they are completing and the student's answers. 
Compare what they wrote to the mark scheme, and append to the/create a dictionary assigned to tests_taken in the way 
as shown in the point below.
Each key in the dictionary should be the testpaper subject and each value should be a string in the format seen 
in the examples below (whether or not the student has failed, and their percentage in brackets).
Example:

paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

student1 = Student()
student2 = Student()
student1.tests_taken ➞ "No tests taken"
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
student1.tests_taken ➞ {"Maths" : "Passed! (80%)"}

student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
student2.tests_taken ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}
"""

class Testpaper:
    def __init__(self, subject, markscheme, pass_mark) -> None:
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark

class Student:
    def __init__(self) -> None:
        self.test = {}
    
    def take_test(self, paper, answer):
        correct = 0
        self.paper = paper
        self.answer = answer
        length = len(paper.markscheme)
        for i in range(length):
            if paper.markscheme[i] == answer[i]: 
                correct += 1
            score = round(correct / length * 100)
        if score >= int(paper.pass_mark[:-1]):
            result = f"Passed! ({score}%)"
        else:
            result = f"Failed! ({score}%)"
        temp = {paper.subject: result}
        self.test.update(temp)
        
    def _tests_taken(self):
        return self.test if len(self.test) else "No tests taken"
        
    tests_taken = property(_tests_taken)

paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

student1 = Student()
student2 = Student()
print(student1.tests_taken) #➞ "No tests taken"
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
print(student1.tests_taken) #➞ {"Maths" : "Passed! (80%)"}

student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
print(student2.tests_taken)