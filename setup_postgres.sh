#!/bin/bash

# PostgreSQL Setup Script for COMP3005 Assignment 3
# This script sets up PostgreSQL user and database for the assignment

echo "Setting up PostgreSQL for COMP3005 Assignment 3..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if PostgreSQL is running
if ! sudo systemctl is-active --quiet postgresql@16-main; then
    print_error "PostgreSQL is not running. Starting PostgreSQL..."
    sudo systemctl start postgresql@16-main
    if [ $? -eq 0 ]; then
        print_status "PostgreSQL started successfully"
    else
        print_error "Failed to start PostgreSQL. Please check your installation."
        exit 1
    fi
else
    print_status "PostgreSQL is already running"
fi

# Create user 'calmclelland' if it doesn't exist
print_status "Creating PostgreSQL user 'calmclelland'..."
sudo -u postgres psql -tc "SELECT 1 FROM pg_user WHERE usename = 'calmclelland'" | grep -q 1
if [ $? -eq 0 ]; then
    print_warning "User 'calmclelland' already exists"
else
    sudo -u postgres createuser calmclelland
    if [ $? -eq 0 ]; then
        print_status "User 'calmclelland' created successfully"
    else
        print_error "Failed to create user 'calmclelland'"
        exit 1
    fi
fi

# Create database 'student' if it doesn't exist
print_status "Creating database 'student'..."
sudo -u postgres psql -tc "SELECT 1 FROM pg_database WHERE datname = 'student'" | grep -q 1
if [ $? -eq 0 ]; then
    print_warning "Database 'student' already exists"
else
    sudo -u postgres createdb -O calmclelland student
    if [ $? -eq 0 ]; then
        print_status "Database 'student' created successfully"
    else
        print_error "Failed to create database 'student'"
        exit 1
    fi
fi

# Grant privileges to user
print_status "Granting privileges to user 'calmclelland'..."
sudo -u postgres psql -c "ALTER USER calmclelland CREATEDB;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE student TO calmclelland;"

# Test connection
print_status "Testing connection..."
sudo -u postgres psql -U calmclelland -d student -c "SELECT version();" > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_status "Connection test successful!"
else
    print_warning "Connection test failed, but this might be normal due to authentication"
fi

# Display connection information
print_status "PostgreSQL setup complete!"
echo ""
echo "Database connection details:"
echo "  Host: localhost"
echo "  Port: 5432"
echo "  Database: student"
echo "  User: calmclelland"
echo "  Socket: /var/run/postgresql"
echo ""
echo "For your Python code, use one of these connection strings:"
echo ""
echo "Option 1 (TCP connection):"
echo "  postgresql://calmclelland@localhost:5432/student"
echo ""
echo "Option 2 (Unix socket - more secure):"
echo "  postgresql://calmclelland@/student?host=/var/run/postgresql"
echo ""
echo "You can test the connection with:"
echo "  psql -U calmclelland -d student -h localhost"
echo "  or"
echo "  sudo -u postgres psql -U calmclelland -d student"
