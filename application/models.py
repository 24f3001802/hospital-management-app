from .database import db
from datetime import datetime, date, time
import enum


class AppointmentDetail(enum.Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    BOOKED = "Booked"

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    doctor_id=db.Column(db.Integer,db.ForeignKey('doctor.id'),nullable=False)
    details=db.Column(db.Enum(AppointmentDetail),nullable=False)
    treatment=db.relationship('Treatment', backref='appointment')
    __table_args__ = (db.UniqueConstraint('doctor_id', 'appointment_date', 'appointment_time'),)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False)   
    email = db.Column(db.String(100), unique=True, nullable=True)
    dob= db.Column(db.Date, nullable=False)
    appointments = db.relationship('Appointment', backref='patient')
    password = db.Column(db.String(100), nullable=False)

class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diagnosis=db.Column(db.String(100), nullable=False)
    prescription=db.Column(db.String(150), nullable=False)
    treatment_date = db.Column(db.DateTime)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), nullable=False, unique=True)



class Doctor(db.Model):  
     id=db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(100), nullable=False)
     phone_no=db.Column(db.String(20), unique=True, nullable=False)
     department_id = db.Column(db.Integer, db.ForeignKey('dept.id'), nullable=False)
     available = db.Column(db.String(50), nullable=True)
     appointments = db.relationship('Appointment', backref='doctor')

class Dept(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(100), unique=True, nullable=False)  
      doctor = db.relationship('Doctor', backref='dept')
      overview_dept=db.Column(db.String(500), nullable=True)
