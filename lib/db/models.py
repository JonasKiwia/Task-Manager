from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # Ensures name is required
    projects = relationship("Project", backref="category")  # One-to-many with Project

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))  # Foreign key to Category
    tasks = relationship("Task", backref="project")  # One-to-many with Task

    def __repr__(self):
        return f"<Project(id={self.id}, name='{self.name}', category_id={self.category_id})>"

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default="Pending")  # Default status
    project_id = Column(Integer, ForeignKey('projects.id'))  # Foreign key to Project

    def __repr__(self):
        return f"<Task(id={self.id}, name='{self.name}', status='{self.status}')>"