CREATE TABLE IF NOT EXISTS ClassRoom(
    ClassRoom_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Class_Room_Name VARCHAR(10),
    Location VARCHAR(20)
);
CREATE TABLE IF NOT EXISTS Teacher(
    Teacher_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    F_name CHAR(50),
    L_name CHAR(50),
    Assigned_class VARCHAR(10),
    Age int
);

CREATE TABLE IF NOT EXISTS subject(
    subject_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(10),
    ClassRoom_ID int,
    Teacher_ID int,
    FOREIGN KEY (ClassRoom_ID) REFERENCES ClassRoom(ClassRoom_ID),    
    FOREIGN KEY (Teacher_ID) REFERENCES Teacher(Teacher_ID)
);

CREATE TABLE IF NOT EXISTS student(
    student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    F_name CHAR(50),
    L_name CHAR(50),
    Class VARCHAR(10),
    Age INTEGER,
    subject_ID INTEGER,
    FOREIGN KEY (subject_ID) REFERENCES subject(subject_ID)
);
-- INSERT INTO ClassRoom (Class_Room_Name, Location) VALUES
-- ('A101', 'Building A'),
-- ('B202', 'Building B'),
-- ('C303', 'Building C');
-- INSERT INTO Teacher (F_name, L_name, Assigned_class, Age) VALUES
-- ('Alice', 'Smith', 'Grade 1', 30),
-- ('Bob', 'Johnson', 'Grade 2', 45),
-- ('Charlie', 'Williams', 'Grade 3', 39);
-- INSERT INTO subject (Subject_Name, ClassRoom_ID, Teacher_ID) VALUES
-- ('Math', 1, 1),
-- ('Science', 2, 2),
-- ('History', 3, 3);
-- INSERT INTO Student (F_name, L_name, Class, Age, Subject_ID) VALUES
-- ('Emma', 'Brown', 'Grade 1', 6, 1),
-- ('Liam', 'Davis', 'Grade 2', 7, 2),
-- ('Olivia', 'Miller', 'Grade 3', 8, 3),
-- ('Noah', 'Wilson', 'Grade 1', 6, 1),
-- ('Sophia', 'Moore', 'Grade 2', 7, 2);



