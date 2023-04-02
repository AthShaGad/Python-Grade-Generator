# Python-Grade-Generator
This Python based application with a front-end developed using Tkinter. 
It takes a spreadsheet as an input and generated grades for students according to the grading scheme followed at PES University.

In our program, we have taken marks scored by a student in ISA-1, ISA-2, ESA and Assignments in order to calculate his grade and GPA. 
It has been assumed that ISA-1 is graded on a scale of 60, ISA-2 is graded on a scale of 45, Assignments are graded on a scale of 15 and 
ESAs are graded on a scale of 100. 

We have assumed that ISA-1 contributes to 21% of the final grade, ISA-2 contributes 14% of final grade, ESA contributes 50% of final grade 
and Assignments contribute 15% of the final grade. This brings the total to a hundred percent. 
Five subjects (Math, Computer Science, Electronics, Chemistry and Civil) have been used to compute a student's GPA.

When our program is made to run, a window appears that presents the user with two buttons:
* One is for teachers
* The other is for students

When a user clicks the teacher button, the program takes him to the teacher part of the program.
In the teacher part there are again two options:
* Import an excel sheet: Generally, most teachers have an excel sheet that stores information
regarding the marks of each of her students in various tests. On clicking the import excel sheet program, another window pops up asking her to 
locate the file on the computer. Upon doing so, the program will read the file and generate percentage, grades and GPAs for each of the
SRNs on the excel file.
* Compute individual GPA manually: In this program, the teacher has to enter the marks scored by a given student in each test to
calculate his GPA individually. The entries accept numbers only and if invalid inputs like strings or marks more than the maximum that
can be scored on a given test are entered, an invalid input message box pops up.

Student part of the program:
* He can know his SGPA by entering his SRN. This part of the program is connected to  a database containing marks of students in all tests
in all subjects and the program will calculate grades and gpa. Again, if he enters an invalid input or an invalid SRN, an invalid input
message will be given. The SRN field is case insensitive - he can type in upper case, lower case or a combination of both
and still get the required output.

* He can calculate how much he needs to score in the rest of the tests put together in order to obtain a desired GPA. If only few of 
the tests have been conducted and rest are yet to be conducted, he can calculate how much he should score in upcoming tests 
to obtain desired GPA in a subject. Again, invalid inputs will give lead to an invalid input message box popping up.
