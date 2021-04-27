import math
import pytest

#Class used for Testing
class Test_Calculator():

    def test_calculator_history_file_content_storing(self):
        object_calculator_history=Calculator_History()
        assert  object_calculator_history.file_content_storing("This was a Test Run\n")==True
        del object_calculator_history

    def test_calculator_history_file_content_printing(self):
        object_calculator_history=Calculator_History()
        assert  object_calculator_history.file_content_printing()==True
        del object_calculator_history

    def test_calculator_history_file_content_deleting(self):  
        object_calculator_history=Calculator_History()
        assert  object_calculator_history.file_content_deleting()==True
        del object_calculator_history

    def test_calculator_operation_addition(self):
        object_calculator_operation=Calculator_Operation(10, 10)
        assert object_calculator_operation.addition()==20.0
        del object_calculator_operation
    
    def test_calculator_operation_subtraction(self):
        object_calculator_operation=Calculator_Operation(10, 10)
        assert object_calculator_operation.subtraction()==0.0
        del object_calculator_operation
    
    def test_calculator_operation_multiplication(self):
        object_calculator_operation=Calculator_Operation(10, 10)
        assert object_calculator_operation.multiplication()==100.0
        del object_calculator_operation
    
    def test_calculator_operation_division(self):
        object_calculator_operation=Calculator_Operation(20, 10)
        assert object_calculator_operation.division()==2.0
        del object_calculator_operation
    
    def test_calculator_operation_modulus(self):
        object_calculator_operation=Calculator_Operation(10, 8)
        assert object_calculator_operation.modulus()==2.0
        del object_calculator_operation
    
    def test_calculator_operation_power(self):
        object_calculator_operation=Calculator_Operation(2,3)
        assert object_calculator_operation.power()==8.0
        del object_calculator_operation
    
    def test_calculator_operation_power_square(self):
        object_calculator_operation=Calculator_Operation(3,0)
        assert object_calculator_operation.power_square()==9.0
        del object_calculator_operation
    
    def test_calculator_operation_power_cube(self):
        object_calculator_operation=Calculator_Operation(3,0)
        assert object_calculator_operation.power_cube()==27.0
        del object_calculator_operation

    def test_calculator_operation_factorial(self):
        object_calculator_operation=Calculator_Operation(5,0)
        assert object_calculator_operation.factorial()==120.0
        del object_calculator_operation

    def test_calculator_operation_square_root(self):
        object_calculator_operation=Calculator_Operation(25,0)
        assert object_calculator_operation.square_root()==5.0
        del object_calculator_operation
    
    def test_calculator_operation_cube_root(self):
        object_calculator_operation=Calculator_Operation(27,0)
        assert object_calculator_operation.cube_root()==3.0
        del object_calculator_operation
    
    def test_calculator_operation_sine(self):
        object_calculator_operation=Calculator_Operation(90,0)
        assert object_calculator_operation.sine()==1.0
        del object_calculator_operation

    def test_calculator_operation_cosine(self):
        object_calculator_operation=Calculator_Operation(0,0)
        assert object_calculator_operation.cosine()==1.0
        del object_calculator_operation

    def test_calculator_operation_tangent(self):
        object_calculator_operation=Calculator_Operation(45,0)
        assert object_calculator_operation.tangent()==1.6197751905438615
        del object_calculator_operation

    def test_calculator_operation_logarithm(self):
        object_calculator_operation=Calculator_Operation(1,0)
        assert object_calculator_operation.logarithm()==0.0
        del object_calculator_operation

    def test_calculator_main_menu_choice(self):
        object_calculator=Calculator()
        assert object_calculator.main_menu_choice(4)==False
        del object_calculator

    def test_calculator_sub_menu_choice(self):
        object_calculator=Calculator()
        assert object_calculator.main_menu_choice(15)==False
        del object_calculator
    

#Class use for File Handling
class Calculator_History:

    def file_content_printing(self):

        file = open("./Calculator/File/calculator_history.txt", "r")
        if(file!=None):
            print(file.read()) 
            file.close()
            return True
        else:
            file.close()
            return False

    
    def file_content_storing(self,String_to_be_stored):

        file = open("./Calculator/File/calculator_history.txt", "a")
        if(file!=None):
            file.write(String_to_be_stored)
            file.close()
            return True
        else:
            file.close()
            return False

    def file_content_deleting(self):
        file = open("./Calculator/File/calculator_history.txt", "w")
        if(file!=None):
            file.close()
            return True
        else:
            file.close()
            return False


#Class Used for All Arithmetic Operations
class Calculator_Operation:

    def __init__(self,first_number,second_number):
        self.first_number=first_number
        self.second_number=second_number
    
    def addition(self):

        return self.first_number+self.second_number

    def subtraction(self):

        return self.first_number-self.second_number
   
    def multiplication(self):

        return self.first_number*self.second_number
   

    def division(self):
        while(True):
            try:
                return self.first_number/self.second_number
                break
            except:
                object_history= Calculator_History()
                print("Please Enter Correct Value")
                object_history.file_content_storing("Please Enter Correct Value\n\n")
                self.first_number=float(input("\nEnter first value: "))
                object_history.file_content_storing("Enter first value: "+str(self.first_number)+"\n")
                self.second_number=float(input("Enter second value: "))
                object_history.file_content_storing("Enter second value: "+str(self.second_number)+"\n")
                del object_history
                continue
    
    def modulus(self):

        while(True):
            try:
                return self.first_number%self.second_number
                break
            except:
                object_history= Calculator_History()
                print("Please Enter Correct Value")
                object_history.file_content_storing("Please Enter Correct Value\n\n")
                self.first_number=float(input("\nEnter first value: "))
                object_history.file_content_storing("Enter first value: "+str(self.first_number)+"\n")
                self.second_number=float(input("Enter second value: "))
                object_history.file_content_storing("Enter second value: "+str(self.second_number)+"\n")
                del object_history
                continue
    
    def power(self):

        return self.first_number**self.second_number
    

    def power_square(self):

        return self.first_number**2
    

    def power_cube(self):

        return self.first_number**3
    
    def factorial(self):

        if(self.first_number==0):

            return 1
        else:

            result=int(1)

            while(self.first_number!=1):

                result*=(self.first_number)

                self.first_number=self.first_number-1
            return result
    

    def square_root(self):

        return self.first_number**(1/2)
    
    def cube_root(self):

        return self.first_number**(1/3)
    
    def sine(self):

        return math.sin(math.radians(self.first_number))
    
    def cosine(self):

        return math.cos(math.radians(self.first_number))
    

    def tangent(self):

        return math.tan(self.first_number)
    

    def logarithm(self):

        return math.log(self.first_number)


#Class Used for taking User Input
class Calculator_Input(Calculator_Operation):

    def __init__(self,number_of_parameter):
    
        if(number_of_parameter==1):
            while(True):
                try:
                    object_history= Calculator_History()
                    first_number_temp=float(input("\nEnter value: "))
                    object_history.file_content_storing("Enter value: "+str(first_number_temp)+"\n")
                    del object_history
                    break
                except:
                    print("Enter only float value")
                    continue
            super().__init__(first_number_temp,0) 

        elif(number_of_parameter==2):
            while(True):
                try:
                    object_history= Calculator_History()
                    first_number_temp=float(input("\nEnter first value: "))
                    object_history.file_content_storing("Enter first value: "+str(first_number_temp)+"\n")
                    second_number_temp=float(input("Enter second value: "))
                    object_history.file_content_storing("Enter second value: "+str(second_number_temp)+"\n")
                    del object_history
                    break
                except:
                    print("Enter only float value")
                    continue
            super().__init__(first_number_temp,second_number_temp)

        else:
            print("Invalid choice!!") 


#Class Used for All Menu Printing and Related Services
class Calculator():

    def main_menu(self):
        print("\n     Calculator Main Page")
        print("-------------------------------\n")
        print("0.  Exit")
        print("1.  Checking Calculator History")
        print("2.  Calculator")
        print("3.  Deleting Calculator History")
        return int(input("Enter your choice: ")) 

    def main_menu_choice(self,choice_main_menu):

        if choice_main_menu==1: 

            print("\n\tCalculator History")
            print("-------------------------------\n")
            object_history=Calculator_History()
            object_history.file_content_printing()
            del object_history
            return True
        
        elif choice_main_menu==2:

            object=Calculator()                  
            object.sub_menu_choice(object.sub_menu())
            del object
            return True

        elif choice_main_menu==3:

            print("\n\tDeleting History")
            print("-------------------------------\n")
            object_history=Calculator_History()
            object_history.file_content_deleting()
            del object_history
            print("Deletion Completed\n")
            return True

        elif choice_main_menu==0:

            print("\nExiting!\n")
            exit(0)
            return True
        
        else:

            print("Invalid choice!!") 
            return False 


    def sub_menu(self):

        print("\n\t Calculator")
        print("-------------------------------\n")
        print("0.  Main Menu")
        print("1.  Addition")
        print("2.  Subtraction")
        print("3.  Multiplication")
        print("4.  Division")
        print("5.  Modulus")
        print("6.  Power x^y")
        print("7.  Power x^2")
        print("8.  Power x^3")
        print("9.  Square Root")
        print("10. Cube Root")
        print("11. Factorial")
        print("12. Sine")
        print("13. Cosine")
        print("14. Tangent ")
        print("15. Logarithm")
        return int(input("Enter your choice: "))  

    def sub_menu_choice(self,choice):

        if choice==1:

            object_input=Calculator_Input(2)
            object_history= Calculator_History()
            print("Addition Result: ",object_input.addition()) 
            object_history.file_content_storing("Addition Result: "+str(object_input.addition())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==2:

            object_input=Calculator_Input(2)
            object_history= Calculator_History()
            print("Subtraction Result: ",object_input.subtraction())
            object_history.file_content_storing("Subtraction Result: "+str(object_input.subtraction())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==3:

            object_input=Calculator_Input(2)
            object_history= Calculator_History()
            print("Multiplication Result: ",object_input.multiplication())
            object_history.file_content_storing("Multiplication Result: "+str(object_input.multiplication())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==4:

            object_input=Calculator_Input(2)
            object_history= Calculator_History()
            print("Division Result: ",round(object_input.division()))
            object_history.file_content_storing("Division Result: "+str(object_input.division())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==5:

            object_input=Calculator_Input(2)
            object_history= Calculator_History()
            print("Modulus Result: ",object_input.modulus())
            object_history.file_content_storing("Modulus Result: "+str(object_input.modulus())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==6:

            object_input=Calculator_Input(2)
            object_history= Calculator_History()
            print("Power Result: ",object_input.power())
            object_history.file_content_storing("Power Result: "+str(object_input.power())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==7:

            object_input=Calculator_Input(1)
            object_history= Calculator_History()
            print("Power Square Result: ",object_input.power_square())
            object_history.file_content_storing("Power Square Result: "+str(object_input.power_square())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==8:

            object_input=Calculator_Input(1)
            object_history= Calculator_History()
            print("Power Cube Result: ",object_input.power_cube())
            object_history.file_content_storing("Power Cube Result: "+str(object_input.power_cube())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==9:

            object_input=Calculator_Input(1)
            object_history= Calculator_History()
            print("Square Root Result: ",object_input.square_root())
            object_history.file_content_storing("Square Root Result: "+str(object_input.square_root())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==10:

            object_input=Calculator_Input(1)
            object_history= Calculator_History()
            print("Cube Root Result: ",object_input.cube_root())
            object_history.file_content_storing("Cube Root Result: "+str(object_input.cube_root())+"\n\n")
            del object_input
            del object_history
            return True
        
        elif choice==11:

            object_input=Calculator_Input(1)
            object_history= Calculator_History()
            print("Factorial Result: ",object_input.factorial())
            object_history.file_content_storing("Factorial Result: "+str(object_input.factorial())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==12:

            object_input=Calculator_Input(1)
            object_history= Calculator_History()
            print("Sine Result: ",object_input.sine())
            object_history.file_content_storing("Sine Result: "+str(object_input.sine())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==13:

            object_input=Calculator_Input(1)
            object_history= Calculator_History()
            print("Cosine Result: ",object_input.cosine())
            object_history.file_content_storing("Cosine Result: "+str(object_input.cosine())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==14:

            object_input=Calculator_Input(1)
            object_history= Calculator_History()
            print("Tangent Result: ",object_input.tangent())
            object_history.file_content_storing("Tangent Result: "+str(object_input.tangent())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==15:

            object_input=Calculator_Input(1)
            object_history= Calculator_History()
            print("Logarithm Result: ",object_input.logarithm())
            object_history.file_content_storing("Logarithm Result: "+str(object_input.logarithm())+"\n\n")
            del object_input
            del object_history
            return True

        elif choice==0:
         
            object=Calculator()  
            object.main_menu_choice(object.main_menu())
            del object
            return True

        else:

            print("Invalid choice!!")
            return False        


#Main Function of the Program
def main():

    object=Calculator()                  

    while(True):
        object.main_menu_choice(object.main_menu())
    
    del object

if __name__ == "__main__":
    main()






