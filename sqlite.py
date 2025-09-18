import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(25),
    class VARCHAR(25),
    section VARCHAR(25),
    marks INT,
    email VARCHAR(50),
    age INT,
    address TEXT,
    phone_number VARCHAR(15),
    date_of_birth DATE,
    admission_date DATE
)
"""

cursor.execute(table_info)

students_data = [
    ('James Anderson', 'Data Science', 'A', 90, 'james.anderson@example.com', 22, '123 Oak St, New York, NY', '555-1234', '2000-01-15', '2022-08-01'),
    ('Mary Johnson', 'Data Science', 'B', 85, 'mary.johnson@example.com', 21, '456 Maple St, Los Angeles, CA', '555-5678', '2001-04-22', '2022-09-15'),
    ('John Smith', 'Data Science', 'A', 92, 'john.smith@example.com', 23, '789 Pine St, Chicago, IL', '555-9101', '1998-06-10', '2021-10-05'),
    ('Michael Davis', 'DEVOPS', 'C', 70, 'michael.davis@example.com', 25, '101 Elm St, Houston, TX', '555-1122', '1997-12-25', '2020-07-12'),
    ('Emily Brown', 'Data Science', 'A', 95, 'emily.brown@example.com', 24, '202 Birch St, Phoenix, AZ', '555-3344', '1998-08-30', '2021-05-18'),
    ('David Taylor', 'DEVOPS', 'B', 80, 'david.taylor@example.com', 26, '303 Oak St, Austin, TX', '555-4455', '1996-03-14', '2019-09-10'),
    ('Sarah Wilson', 'Data Science', 'B', 89, 'sarah.wilson@example.com', 22, '404 Maple St, Seattle, WA', '555-5566', '2000-02-10', '2022-01-22'),
    ('Daniel Moore', 'DEVOPS', 'A', 90, 'daniel.moore@example.com', 23, '505 Pine St, San Francisco, CA', '555-6677', '1999-07-01', '2021-12-05'),
    ('Jessica Harris', 'Data Science', 'C', 65, 'jessica.harris@example.com', 21, '606 Birch St, Denver, CO', '555-7788', '2001-09-12', '2022-06-18'),
    ('Jacob Lee', 'DEVOPS', 'A', 80, 'jacob.lee@example.com', 24, '707 Cedar St, Dallas, TX', '555-8899', '1997-11-05', '2020-11-21'),
    ('Christopher Lewis', 'Data Science', 'B', 76, 'christopher.lewis@example.com', 23, '808 Pine St, Miami, FL', '555-9900', '1998-01-30', '2021-03-14'),
    ('Joshua Walker', 'DEVOPS', 'C', 72, 'joshua.walker@example.com', 25, '909 Oak St, Los Angeles, CA', '555-1235', '1997-02-22', '2019-10-09'),
    ('Matthew Young', 'Data Science', 'A', 98, 'matthew.young@example.com', 22, '101 Elm St, Boston, MA', '555-2236', '2000-05-18', '2022-07-01'),
    ('Megan Scott', 'DEVOPS', 'A', 85, 'megan.scott@example.com', 26, '202 Cedar St, Nashville, TN', '555-3345', '1996-04-08', '2020-03-12'),
    ('Ryan Adams', 'Data Science', 'B', 83, 'ryan.adams@example.com', 24, '303 Oak St, Chicago, IL', '555-4456', '1997-11-20', '2021-08-22'),
    ('Sophia Miller', 'DEVOPS', 'A', 91, 'sophia.miller@example.com', 22, '404 Maple St, Phoenix, AZ', '555-5567', '2000-03-10', '2022-02-14'),
    ('Benjamin Martinez', 'Data Science', 'C', 68, 'benjamin.martinez@example.com', 23, '505 Birch St, Atlanta, GA', '555-6678', '1998-07-15', '2021-09-03'),
    ('Victoria Taylor', 'DEVOPS', 'A', 93, 'victoria.taylor@example.com', 25, '606 Pine St, Portland, OR', '555-7789', '1997-01-10', '2020-04-05'),
    ('Oliver Robinson', 'Data Science', 'B', 79, 'oliver.robinson@example.com', 21, '707 Cedar St, Tampa, FL', '555-8890', '2001-10-25', '2022-07-21'),
    ('Liam Walker', 'DEVOPS', 'C', 71, 'liam.walker@example.com', 27, '808 Oak St, Miami, FL', '555-9901', '1996-06-12', '2019-12-10'),
    ('Amelia Green', 'Data Science', 'A', 94, 'amelia.green@example.com', 22, '909 Pine St, Seattle, WA', '555-1236', '1999-11-11', '2021-10-30'),
    ('Jack King', 'DEVOPS', 'B', 75, 'jack.king@example.com', 23, '101 Birch St, San Francisco, CA', '555-2237', '1998-12-08', '2020-08-14'),
    ('Ella Thompson', 'Data Science', 'A', 92, 'ella.thompson@example.com', 21, '202 Cedar St, Los Angeles, CA', '555-3346', '2000-05-01', '2022-09-02'),
    ('Henry Jackson', 'DEVOPS', 'A', 85, 'henry.jackson@example.com', 26, '303 Pine St, Houston, TX', '555-4457', '1997-04-10', '2021-01-15'),
    ('Chloe Harris', 'Data Science', 'C', 67, 'chloe.harris@example.com', 24, '404 Birch St, Raleigh, NC', '555-5568', '1998-02-22', '2022-05-09'),
    ('Sebastian White', 'DEVOPS', 'A', 80, 'sebastian.white@example.com', 22, '505 Cedar St, Chicago, IL', '555-6679', '2000-10-20', '2021-04-03'),
    ('Mason Lewis', 'Data Science', 'A', 96, 'mason.lewis@example.com', 25, '606 Oak St, Denver, CO', '555-7780', '1997-07-30', '2021-11-15'),
    ('Lucas Hall', 'DEVOPS', 'B', 81, 'lucas.hall@example.com', 23, '707 Pine St, Boston, MA', '555-8891', '1998-11-13', '2020-09-20'),
    ('Charlotte Clark', 'Data Science', 'A', 90, 'charlotte.clark@example.com', 22, '808 Birch St, Seattle, WA', '555-9902', '1999-03-18', '2021-02-28'),
    ('Ethan Lee', 'DEVOPS', 'C', 65, 'ethan.lee@example.com', 26, '909 Cedar St, Dallas, TX', '555-1237', '1997-01-17', '2020-07-22'),
    ('Isabella Allen', 'Data Science', 'B', 80, 'isabella.allen@example.com', 24, '101 Pine St, San Francisco, CA', '555-2238', '1997-05-05', '2021-06-19'),
    ('Alexander Harris', 'DEVOPS', 'A', 87, 'alexander.harris@example.com', 23, '202 Birch St, Houston, TX', '555-3347', '1998-08-01', '2020-10-04'),
    ('Zoe Carter', 'Data Science', 'C', 62, 'zoe.carter@example.com', 25, '303 Cedar St, Los Angeles, CA', '555-4458', '1996-12-13', '2021-05-25'),
    ('Aiden Walker', 'DEVOPS', 'B', 77, 'aiden.walker@example.com', 24, '404 Pine St, Miami, FL', '555-5569', '1997-09-21', '2020-11-08'),
    ('Lily Mitchell', 'Data Science', 'A', 92, 'lily.mitchell@example.com', 22, '505 Birch St, Chicago, IL', '555-6670', '1999-04-28', '2021-09-12'),
    ('Matthew Martin', 'DEVOPS', 'A', 93, 'matthew.martin@example.com', 23, '606 Pine St, Portland, OR', '555-7782', '1998-11-10', '2020-05-03')
]

for student in students_data:
    cursor.execute('''
    INSERT INTO STUDENT (name, class, section, marks, email, age, address, phone_number, date_of_birth, admission_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', student)

connection.commit()

print("The inserted records are:")
cursor.execute("SELECT * FROM STUDENT")
for row in cursor.fetchall():
    print(row)

# Close the connection
connection.close()