#!/usr/bin/python3

#This is simple calculator by which you can calculate your CGPA.

import sys

def grade(CGPA):

	if CGPA>=4.00:
		print("Grade : A+")
	elif CGPA >=3.75:
		print("Grade : A")
	elif CGPA>=3.50:
		print("Grade : A-")
	elif CGPA>=3.25:
		print("Grade : B+")
	elif CGPA>=3.00:
		print("Grade : B")
	elif CGPA>=2.75:
		print("Grade : B-")
	elif CGPA>=2.50:
		print("Grade : C+")
	elif CGPA>=2.25:
		print("Grade : C")
	elif CGPA>=2.00:
		print("Grade : C-")
	else: 
		print("Grade : F")


def calculate_CGPA():

	number_of_course=input("Enter The Number of Total Course : ")
	loop_counter=0

	while number_of_course=='':
		print("Wrong Input!!!! Try Again!!!")
		number_of_course=input("Enter The Number of Total Course : ")
		loop_counter+=1
		if loop_counter==5:
			sys.exit()


	number_of_course=int(number_of_course)
	total_credit=0
	total_CGPA=0

	print("-------------------------------------------")

	for i in range(1,number_of_course+1):

		course_CGPA=float(input("Course {}:".format(i)))
		course_credit=float(input("Credit : "))

		total_CGPA+=course_CGPA*course_credit
		total_credit+=course_credit

	print()
	print("---------------Result----------------------")
	print()
	
	final_CGPA=total_CGPA/total_credit
	print("CGPA  : %.2f " %final_CGPA)
	_grade=grade(final_CGPA)

	print("-------------------------------------------")


if __name__ == "__main__":

	calculate_CGPA()



