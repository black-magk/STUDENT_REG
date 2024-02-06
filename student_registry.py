#STEP 1: 
# Attributes: 
# # Should not be accessed: _name,_age,_grade
class Student:
    # 1.1 Define the init Dunder method
    # TODO_ITEM: N/A might equate to None instead of N/A as a string
    def __init__(self, name=None, age=13, grade="12th"):
    # 1.2 Set attributes with self
        self._name = name.lower()
        self._age = age
        self._grade = grade

    # 1.3 Define __str__ method
    def __str__(self):
         return f'Student 1: Name: {self._name.capitalize()}, Age: {self._age}, Grade: {self._grade}'
                # "Student 1: Name: Francisco, Age: 15, Grade: 12th"
    # 1.4 Return Specified String
    # Define 'study' method
    def advance(self,advanced_grade):
        return f'{self._name.capitalize()} has advanced to the {advanced_grade} grade'
    # 1.5 Define 'study' method
    # include an input variable and define it as the class subject within the f string and replace the placeholder.
    def study(self,class_being_taken):
        return f'{self._name.capitalize()} is studying {class_being_taken}'
    # ---------------------------------------------
    # GETTER FOR NAME
    # Requirement to return students name for the getter
    @property
    def get_name(self):
        return self._name.capitalize()
    # SETTER FOR NAME
    # Requirement to return students name for the getter
    @get_name.setter
    def set_name(self,new_name):
        if isinstance(new_name, str):
            # Edge Case
            if (len(new_name) >= 3) & (new_name.isalpha() == True):
                 if " " not in new_name:
                    self._name = new_name.capitalize()
                
            else:
               print("The name is not longer or equal to 3 and the name contains more than just alphabet characters") 
        else:
            print("name must be a string)")
    #----------------------------------------------
    # GETTER FOR AGE
    #/^[A-Z]+$/i
    # /^[A-Za-z]+$/
    #.isalpha : returns true if only alphabetic
    @property
    def get_age(self):
        return self._age
    # SETTER FOR AGE
    @get_age.setter
    def set_age(self,new_age):

        if isinstance(new_age,int):

            if new_age >= 11 & new_age < 18:
               self._age = new_age
        else:
            print("Age must be a Number")
    #----------------------------------------------
    # GETTER FOR GRADE
    @property
    def get_grade(self):
        return self._grade.capitalize()
    # SETTER FOR GRADE
    @get_grade.setter
    def set_grade(self,new_grade):
        if isinstance(new_grade,str):
            # Split str into num/char like list[0],list[1]
            for i in range(9,13):
                if str(i) in new_grade:
                    self._grade = new_grade
                else:
                    print('Must be between 9th-12th Grade')
        else:
            print("grade must be a string)")





student1 = Student('Landon',15,'15th')

print(student1)

# print(student1.get_name)
# student1.set_name = "dd"

  #EXAMPLE

#    @property
#     def name(self):
#         return self._first_name.capitalize()
#     @name.setter
#     def set_first_name(self, new_name):
#         if isinstance(new_name,str):
#             self._first_name = new_name.lower()
#         else: 
#             print("name must be a string)")
  


        

        
    

