#!/usr/bin/env python3
##  PostgreSQL Connection Test Script
##  Tests database connection and basic operations

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


def test_postgres_connection():
    """Test PostgreSQL connection and basic operations"""

    print("Testing PostgreSQL connection...")

    # Create connection URL
    url = URL.create(
        drivername="postgresql",
        username="calmclelland",
        password="password123",
        host="localhost",
        database="student",
    )

    try:
        # Create engine
        engine = create_engine(url)

        # Test basic connection
        with engine.connect() as conn:
            result = conn.execute("SELECT version();")
            version = result.fetchone()[0]
            print(f"✓ Connected to PostgreSQL: {version}")

        # Define test table
        Base = declarative_base()

        class TestStudent(Base):
            __tablename__ = "test_students"
            student_id = Column(Integer(), primary_key=True)
            first_name = Column(String(100), nullable=False)
            last_name = Column(String(100), nullable=False)
            email = Column(String(100), nullable=False)
            dob = Column(DateTime(), default=datetime.now)

        # Create tables
        Base.metadata.create_all(engine)
        print("✓ Test table created successfully")

        # Test session operations
        Session = sessionmaker(bind=engine)
        session = Session()

        # Add test record
        test_student = TestStudent(
            first_name="Test",
            last_name="Student",
            email="test@example.com",
            dob=datetime(1990, 1, 1),
        )
        session.add(test_student)
        session.commit()
        print("✓ Test record added successfully")

        # Query test record
        students = session.query(TestStudent).all()
        print(f"✓ Found {len(students)} test records")

        # Clean up test data
        session.query(TestStudent).delete()
        session.commit()

        # Drop test table
        Base.metadata.drop_all(engine)
        print("✓ Test cleanup completed")

        session.close()
        print("\n🎉 All tests passed! PostgreSQL is ready for your assignment.")
        return True

    except Exception as e:
        print(f"✗ Connection test failed: {e}")
        print("\nTroubleshooting tips:")
        print(
            "1. Make sure PostgreSQL is running: sudo systemctl status postgresql@16-main"
        )
        print("2. Check if user exists: sudo -u postgres psql -c '\\du'")
        print("3. Check if database exists: sudo -u postgres psql -c '\\l'")
        print("4. Try running the setup script again: ./setup_postgres.sh")
        return False


if __name__ == "__main__":
    test_postgres_connection()
