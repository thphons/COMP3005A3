##  Cal McLelland
#   Assignment 3
##  COMP 3005 Fall 2025

# a3.py
import code
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# engine for Postgres
url = URL.create(
    drivername="postgresql",
    username="calmclelland",
    host="/tmp/postgresql/socket",
    database="student"
)

engine = create_engine(url)

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer(), primary_key=True)
    first_name: Column(String(100), nullable=False)
    last_name: Column(String(100), nullable=False)
    email: Column(String(100), nullable=False)
    dob: Column(DateTime(), default=datetime.now)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

## define banner and exit messages
bannerMsg = "COMP3005 A3!"
exitMsg = "bye!"
helpMsg =   "\nValid commands are:\n" \
            "   help                                                    " \
            "list all commands\n" \
            "   listStudents                                            " \
            "list all student records\n" \
            "   addStudents <first_name> <last_name> <email> <dob>      " \
            "add a new student record with the specified values\n" \
            "   deleteStudent <student_id>                              " \
            "delete the student record with the specified id\n" \
            "   exit                                                    " \
            "exit the program\n"

def listStudents():
    print("listing all students...")
    #reteive and list all student records

def addStudent(args):
    print("adding new student...")
    #check for valid arguments
    #check if student already exists

def updateStudentEmail(args):
    print("updating student email...")
    #check for valid arguments
    #check if student exists
    #update the students email

def deleteStudent(args):
    print("updating student email")
    #check for valid arguments
    #check if student exists
    #delete student


# create a read-eval-print loop
class Repl(code.InteractiveConsole):
    def runsource(self, source, filename="<input>", symbol="single"):
        tokens = source.split()
        command = tokens[0]
        args = tokens.pop(0)
        match command:
            case "help":
                print(helpMsg)
            case "listStudents":
                listStudents()
            case "addStudent":
                addStudent(args)
            case "updateStudentEmail":
                updateStudentEmail(args)
            case "deleteStudent":
                deleteStudent(args)
            case "exit" | "quit":
                exit(0)
            case _:
                print("command not recognized:", source)


## create an interactive console
repl = Repl()
repl.interact(banner=bannerMsg, exitmsg=exitMsg)
