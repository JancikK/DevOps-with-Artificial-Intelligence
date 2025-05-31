-- Create a table named 'Students'
-- ID: Unique identifier, auto-incremented
-- Name: Student's name
-- Age: Student's age
CREATE TABLE Students (
    ID INT PRIMARY KEY AUTO_INCREMENT,   -- Primary key that auto-increments
    Name VARCHAR(100),                   -- Name column with max 100 characters
    Age INT                              -- Age as an integer
);

-- Insert sample student records
INSERT INTO Students (Name, Age) VALUES ('Alice', 21);   -- Insert Alice
INSERT INTO Students (Name, Age) VALUES ('Bob', 22);     -- Insert Bob
INSERT INTO Students (Name, Age) VALUES ('Charlie', 20); -- Insert Charlie

-- Select all records from the table to verify insertion
SELECT * FROM Students;