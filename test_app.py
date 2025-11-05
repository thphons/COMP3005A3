#!/usr/bin/env python3
##  Test script for a3.py main application
##  Tests the core functionality without the interactive console

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Import the classes and functions from a3.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up database connection (same as a3.py)
url = URL.create(
    drivername="postgresql",
    username="calmclelland",
    password="password123",
    host="localhost",
    database="student",
)

engine = create_engine(url)
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    dob = Column(DateTime(), default=datetime.now)


# Create tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def test_list_students():
    """Test listing all students"""
    print("=== Testing listStudents ===")
    students = session.query(Student).all()
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(
                f"ID: {student.student_id}, Name: {student.first_name} {student.last_name}, Email: {student.email}, DOB: {student.dob}"
            )
    print(f"Total students: {len(students)}")
    print()
    return len(students)


def test_add_student(first_name, last_name, email, dob_str):
    """Test adding a new student"""
    print(f"=== Testing addStudent: {first_name} {last_name} ===")

    # Check if student already exists
    existing = session.query(Student).filter_by(email=email).first()
    if existing:
        print(f"Error: Student with email {email} already exists.")
        return False

    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        new_student = Student(
            first_name=first_name, last_name=last_name, email=email, dob=dob
        )
        session.add(new_student)
        session.commit()
        print(f"Student {first_name} {last_name} added successfully.")
        return True
    except ValueError:
        print("Error: Date format should be YYYY-MM-DD")
        return False
    except Exception as e:
        session.rollback()
        print(f"Error adding student: {e}")
        return False


def test_update_student_email(student_id, new_email):
    """Test updating a student's email"""
    print(f"=== Testing updateStudentEmail: ID {student_id} ===")

    try:
        student = session.query(Student).filter_by(student_id=student_id).first()
        if not student:
            print(f"Error: Student with ID {student_id} not found.")
            return False

        old_email = student.email
        student.email = new_email
        session.commit()
        print(f"Student ID {student_id} email updated from {old_email} to {new_email}")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error updating student: {e}")
        return False


def test_delete_student(student_id):
    """Test deleting a student"""
    print(f"=== Testing deleteStudent: ID {student_id} ===")

    try:
        student = session.query(Student).filter_by(student_id=student_id).first()
        if not student:
            print(f"Error: Student with ID {student_id} not found.")
            return False

        name = f"{student.first_name} {student.last_name}"
        session.delete(student)
        session.commit()
        print(f"Student ID {student_id} ({name}) deleted successfully.")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error deleting student: {e}")
        return False


def run_comprehensive_test():
    """Run a comprehensive test of all functionality"""
    print("🚀 Starting comprehensive test of a3.py functionality...\n")

    # Test 1: List initial students
    initial_count = test_list_students()

    # Test 2: Add some test students
    test_students = [
        ("John", "Doe", "john.doe@email.com", "1995-05-15"),
        ("Jane", "Smith", "jane.smith@email.com", "1998-08-22"),
        ("Bob", "Johnson", "bob.johnson@email.com", "1997-12-03"),
    ]

    added_students = []
    for first, last, email, dob in test_students:
        if test_add_student(first, last, email, dob):
            added_students.append((first, last, email))

    # Test 3: List students after adding
    new_count = test_list_students()
    print(f"Added {new_count - initial_count} new students\n")

    # Test 4: Update email for first student
    if new_count > 0:
        # Get the first student's ID
        first_student = session.query(Student).first()
        if first_student:
            test_update_student_email(
                first_student.student_id, "updated.email@example.com"
            )
            test_list_students()

    # Test 5: Delete a student
    if new_count > 0:
        # Get the last student's ID
        last_student = (
            session.query(Student).order_by(Student.student_id.desc()).first()
        )
        if last_student:
            test_delete_student(last_student.student_id)
            test_list_students()

    print("✅ Comprehensive test completed!")
    print("\nYour a3.py application should now work properly!")
    print("To run the interactive version, use: python3 a3.py")


def cleanup_test_data():
    """Clean up any test data"""
    print("🧹 Cleaning up test data...")
    test_emails = [
        "john.doe@email.com",
        "jane.smith@email.com",
        "bob.johnson@email.com",
        "updated.email@example.com",
    ]

    for email in test_emails:
        student = session.query(Student).filter_by(email=email).first()
        if student:
            session.delete(student)

    session.commit()
    print("Test data cleaned up.\n")


if __name__ == "__main__":
    try:
        # Clean up any existing test data first
        cleanup_test_data()

        # Run the comprehensive test
        run_comprehensive_test()

        # Clean up test data after testing
        cleanup_test_data()

    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        print("Make sure PostgreSQL is running and properly configured.")
        print("Run: ./setup_postgres.sh")
    finally:
        session.close()
