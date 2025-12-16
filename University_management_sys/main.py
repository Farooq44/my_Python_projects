class Person:
    def __init__(self, id:int, name:str, age:int):
        self.id = id
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, id:int, name:str, age:int, dept:str):
        super().__init__(id, name , age)
        self.dept = dept

    def student_details(self):
        return f"My name is {self.name} and i am belongs to {self.dept}"
    

class Employee(Person):
    def __init__(self, id:int, name:str, age:int, dept:str,salary:int, subjects:list[str]): 
        super().__init__(id, name, age)
        self.dept = dept
        self.subjects = subjects
        self.salary = salary 
        
    def employee_details(self):
        return f"My name is {self.name} and i am belongs to {self.dept} \
            i can teach {",".join(self.subjects)}"
        

class University:
    std_table = {}
    emp_table = {}
    def __init__(self, name:str, course_list:list[str]):
        self.name = name
        self.course_list = course_list
    
    def admision(self, std_obj:Student):
        if std_obj.id not in self.std_table:
            self.std_table[std_obj.id] = [std_obj.name, std_obj.age, std_obj.dept]
            return "Student added successfully"
        
    def employee_admision(self, emp_obj:Employee):
        if emp_obj.id not in self.emp_table:
            self.emp_table[emp_obj.id] = [emp_obj.name, emp_obj.age, \
                        emp_obj.dept, emp_obj.salary, emp_obj.subjects]
            return "Employee added successfully"
        
    def student_details(self,std_id:int=None,  dept:str=None):
        # returning the student details if student is present
        if std_id:
            return self.std_table[std_id]
        elif dept:
            students = []
            for item in self.std_table.items():
                if item[1][2] == dept:
                    students.append(item)
            return students
        elif not std_id and not dept:
            return self.std_table.items()
        else:
            return "Student id or department not found"
        
        
    def employee_details(self, emp_id:int=None, dept:str=None):
        if emp_id:
            return self.emp_table[emp_id]
        elif dept:
            employees = []
            for item in self.emp_table.items():
                if item[1][2] == dept:
                    employees.append(item)
            return employees
        elif not emp_id and not dept:
            return self.emp_table.items()
        else:
            return "Employee id or department not found"
        
    def total_student_count(self):
        return f"Total students in university is {len(self.std_table)}"
    def total_employee_count(self):
        return f"Total Employees in university is {len(self.emp_table)}"
    def remove_student(self, std_id:int):
        if std_id in self.std_table:
            self.std_table.pop(std_id)
            return "Successfully student removed from university"
        else:
            return "Student id not found"
        
    def remove_employee(self, emp_id:int):
        if emp_id in self.emp_table:
            self.emp_table.pop(emp_id)
            return "Successfully employee removed from university"
        else:
            return "employee id not found" 
    

# main
if __name__ == "__main__":
    s1 = Student(101,"Ravi", 18,'ECE')
    s2 = Student(102,"Srinu", 19,'CSE')
    s3 = Student(103,"Siva",17,'ECE')
    s4 = Student(104,"Sai", 20,'IT')
    s5 = Student(105,"Vivek", 18,'CSE')
    # creating object for university class
    uni = University(name="Codegnan", course_list=["ECE","CSE","IT"])
    # adding studens to university
    print(uni.admision(std_obj=s1))
    print(uni.admision(std_obj=s2))
    print(uni.admision(std_obj=s3))
    print(uni.admision(std_obj=s4))
    print(uni.admision(std_obj=s5))
    # employee objects
    e1 = Employee(1001,"Surya",25,"ECE",45000,["Java", "VLSI","STLD"])
    e2 = Employee(1002,"Akshay",25,"CSE",45000,["Java", "Python","c"])
    e3 = Employee(1003,"Farooq",25,"IT",45000,["Java", "DSA","python"])
    #adding employees
    print(uni.employee_admision(emp_obj=e1))
    print(uni.employee_admision(emp_obj=e2))
    print(uni.employee_admision(emp_obj=e3))
    # calling all methods
    print(uni.total_employee_count())
    print(uni.total_student_count())
    print(uni.student_details(std_id=102))
    print(uni.student_details(dept = "ECE"))
    print(uni.student_details())
    print(uni.employee_details(emp_id=1002))
    print(uni.employee_details())
    print(uni.employee_details(dept="IT"))
    print(uni.remove_student(std_id=105))