# import psycopg2

# connection = psycopg2.connect()
# host = 'localhost',
# database = 'postgres',
# user = 'postgres',
# password = '123',
# posrt = 5432

# 1. Add models for student, subject and student_subject from previous lessons in SQLAlchemy.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return f'This is {self.id} student {self.name}. Age: {self.age}'


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __str__(self):
        return f'This is {self.id} subject {self.name}'


class StudentSubject(Base):
    __tablename__ = 'student_subjects'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey ('subjects.id'))

    student = relationship('Student')
    subject = relationship ('Subject')


from sqlalchemy import create_engine

DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'

#creating connection with SQL database:
engine = create_engine(
    DATABASE_URI.format(
        host = 'localhost',
        database = 'postgres',
        user = 'postgres',
        password = 'Aliona123',
        port = 5432
    )
)


#connecting Conection with the Class
# Base.metadata.create_all(engine)

# 2. Find all students` name that visited 'English' classes.

#Openning session to SQL DB:
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

students_on_english = session.query(Student.name).\
join(StudentSubject, Student.id == StudentSubject.student_id).\
join(Subject, StudentSubject.subject_id == Subject.id).\
filter(Subject.name == 'English').all()

for student in students_on_english:
    print(student[0])