import mysql.connector

class course_enrollment:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(user="root",
                                             password="root",
                                             host="localhost",
                                             database="course_enrollment")
            self.cursor=self.con.cursor()
            print("Connected Successfully")
        except Exception:
            print("Connection is not established")
    def enroll(self,student_name,course_name,duration_months,enrollment_date,fee,status):
        try:    
            query="insert into enrollments(student_name,course_name,duration_months,enrollment_date,fee,status)values(%s,%s,%s,%s,%s,%s)"
            data=[student_name,course_name,duration_months,enrollment_date,fee,status]
            self.cursor.execute(query,data)
            self.con.commit()
            print("student enrolled successfully")
        except Exception:
            print("Student is not enrolled")
    def view_enrollment(self):
        try:
            query="select* from enrollments order by fee desc"
            self.cursor.execute(query)
            record=self.cursor.fetchall()
            if record:
                for row in record:
                    print(row)
                else:
                    print("No record")
        except Exception:
            print("Cannot view the enrollment details")
    def search_enrollment(self,enrollment_id):
        try:
            query="select * from enrollments where enrollment_id=%s "
            data=[enrollment_id,]
            self.cursor.execute(query,data)
            record=self.cursor.fetchone()
            if record:
                print(record)
            else:
                print("No record")
        except Exception:
            print("cannot search the record")

    def update(self,enrollment_id,fee,status):
        try:
            query="update enrollments set fee=%s,status=%s where enrollment_id=%s"
            data=[fee,status,enrollment_id]
            self.cursor.execute(query,data)
            self.con.commit()
            if self.cursor.rowcount>0:
                print("updated Successfully")
            else:
                print("Not updated")
        except Exception:
            print("Updation is not done")

    def delete(self,enrollment_id):
        try:
            query="delete from enrollments where enrollment_id=%s"
            data=[enrollment_id,]
            self.cursor.execute(query,data)
            self.con.commit()
            if self.cursor.rowcount>0:
                print("deleted Successfully")
            else:
                print("Not deleted")
        except Exception:
            print("Deletion is not done")
    def summary(self):
        try:
           
            query="select count(enrollment_id),sum(fee),avg(fee)from enrollments"
            self.cursor.execute(query)
            record=self.cursor.fetchall()
            if record:
                for row in record:
                    print(row)

            else:
                print("No record")
            query2="select status,count(enrollment_id) from enrollments group by status"
            self.cursor.execute(query2)
            record1=self.cursor.fetchall()
            if record1:
                for row in record1:
                    print(row)
            
            else:
                print("No record")

        except Exception:
            print("Cannot fetch the financial summary")
e=course_enrollment()
while(True):
    print("1.Enroll Student")
    print("2.view all enrollments")
    print("3.Search enrollment")
    print("4.Update Enrollmet status")
    print("5.Delete enrollment")
    print("6.Enrollment summary")
    print("7.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        student_name=input("student name:")
        course_name=input("Course name:")
        duration_months=int(input("duration:"))
        enrollment_date=input("date:")
        fee=int(input("fee:"))
        status=input("Status:")
        if duration_months<0 or fee<0:
            print("duartion should be positive and fee should be non negative")
        e.enroll(student_name,course_name,duration_months,enrollment_date,fee,status)
    elif ch==2:
        e.view_enrollment()
    elif ch==3:
        enrollment_id=int(input("enrollment_id:"))
        e.search_enrollment(enrollment_id)
    elif ch==4:
        enrollment_id=int(input("enrollment_id:"))
        fee=int(input("fee:"))
        status=input("Status:")
        e.update(enrollment_id,fee,status)
    elif ch==5:
        enrollment_id=int(input("enrollment_id:"))
        e.delete(enrollment_id)
    elif ch==6:
        e.summary()
    elif ch==7:
        exit()
        
    



    




