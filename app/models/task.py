from app import db
from datetime import datetime 
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable = True)
    go_id = db.Column(db.Integer, db.ForeignKey('goal.id'))
    
    goal = db.relationship("Goal", back_populates="tasks", lazy= True)


    def to_result(self):
        is_complete = True
        if not self.completed_at:
            is_complete = False
        return {
            "id":self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": is_complete,
            "go_id": self.go_id
        }
# def to_dict(self):
#         task_as_dict = {}
#         task_as_dict["id"] = self.id
#         task_as_dict["title"] = self.title
#         task_as_dict["description"] = self.description
#         task_as_dict["completed_at"] = self.completed_at

#         return task_as_dict