from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class WorkSlot(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    shiftType = db.Column(db.String(50), nullable = False)
    date = db.Column(db.String(100), nullable = False)
    status = db.Column(db.String(100), default = 'Available',nullable = False)
    bids = db.relationship("Bids",backref="workslot",)

class UserRole(db.Model):
    role = db.Column(db.String(50), primary_key = True, unique=True)
    staffs = db.relationship("Staff", backref = "userrole")

class Staff(db.Model):
    username = db.Column(db.String(100), primary_key = True)
    password = db.Column(db.String(100), unique = True, nullable = False)
    job = db.Column(db.String(100), nullable = False)
    avail = db.Column(db.String(100), nullable = False)
    userRole = db.Column(db.String(50), db.ForeignKey(UserRole.role, ondelete="CASCADE"), nullable=False)
    bids = db.relationship("Bids", backref = "staff")
    
class Bids(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    shift_id = db.Column(db.Integer, db.ForeignKey(WorkSlot.id), nullable=False)
    shift_type = db.Column(db.String(100), nullable=False)
    shift_date = db.Column(db.String(100),  nullable=False)
    staff_user = db.Column(db.String(100), db.ForeignKey(Staff.username, ondelete = "CASCADE"), nullable=False)
    approval = db.Column(db.Boolean, nullable = True)
    
    