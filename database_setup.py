from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        Float,
                        String,
                        Date,
                        DateTime,
                        LargeBinary,
                        Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime
from datetime import datetime

Base = declarative_base()


class tblUser(Base):
    """Users: Users log time against tasks"""
    __tablename__ = 'tblUser'

    userID = Column(Integer, primary_key=True)
    userName = Column(String(100), nullable=False)
    userFName = Column(String(25))
    userLName = Column(String(25))
    userEmail = Column(String(50))
    userPhone = Column(String(25))
    userJobTitle = Column(String(50))
    dateAdd = Column(DateTime)
    dateEdit = Column(DateTime)


class tblProject(Base):
    """Projects: tasks and time billing tied to a project"""
    __tablename__ = 'tblProject'

    projectID = Column(Integer, primary_key=True)
    projectName = Column(String(100), nullable=False)
    projectDesc = Column(String(500))
    startDate = Column(Date)
    endDate = Column(Date)
    dateAdd = Column(DateTime)
    dateEdit = Column(DateTime)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'projectID': self.projectID,
            'projectName': self.projectName,
            'projectDesc': self.projectDesc,
            'startDate': self.startDate,
            'endDate': self.endDate,
            'dateAdd': self.dateAdd,
            'dateEdit': self.dateEdit,
        }


class tblTask(Base):
    """Tasks - multiple tasks can roll up into a single Project"""
    __tablename__ = 'tblTask'

    taskID = Column(Integer, primary_key=True)
    taskName = Column(String(100), nullable=False)
    taskDesc = Column(String(500))
    projectID = Column(Integer, ForeignKey('tblProject.projectID'))
    project = relationship(tblProject)
    dateAdd = Column(DateTime)
    dateEdit = Column(DateTime)


class tblOrg(Base):
    """Organizations: projects executed for / billed to organizations"""
    __tablename__ = 'tblOrg'

    orgID = Column(Integer, primary_key=True)
    orgName = Column(String(100), nullable=False)
    orgType = Column(String(25))
    orgPhone = Column(String(25))
    orgFax = Column(String(25))
    dateAdd = Column(DateTime)
    dateEdit = Column(DateTime)


class tblOrgAddress(Base):
    """Organization Addresses: multiple addresses (e.g., Billing, Mailing, Shipping) for one Organization"""
    __tablename__ = 'tblOrgAddress'

    orgAddressID = Column(Integer, primary_key=True)
    orgID = Column(Integer, ForeignKey('tblOrg.orgID'))
    org = relationship(tblOrg)
    addressType = Column(String(15))
    addressLine1 = Column(String(50))
    addressLine2 = Column(String(50))
    addressLine3 = Column(String(50))
    addressLine4 = Column(String(50))
    addressLine5 = Column(String(50))
    addressCity = Column(String(50))
    addressState = Column(String(50))
    addressZip = Column(String(50))
    addressCountry = Column(String(50))


class tblInvoice(Base):
    """Invoices: consists of billing on one or more task - single project"""
    __tablename__ = 'tblInvoice'

    invoiceID = Column(Integer, primary_key=True)
    invoiceAID = Column(String(15), nullable=False)
    invoiceSubTotal = Column(Float)
    invoiceTax = Column(Float)
    invoiceTotal = Column(Float)
    invoiceNotes = Column(String(250))
    invoiceDate = Column(Date)
    invoiceDatePaid = Column(Date)


class tblInvoiceLine(Base):
    """Invoice Line Items: multiple line items per invoice"""
    __tablename__ = 'tblInvoiceLine'

    invoiceLineID = Column(Integer, primary_key=True)
    invoiceID = Column(Integer, ForeignKey('tblInvoice.invoiceID'))
    invoice = relationship(tblInvoice)
    invoiceLineName = Column(String(50))
    invoiceLineDesc = Column(String(250))
    invoiceLineQty = Column(Float)
    invoiceLineRate = Column(Float)
    invoiceLineTotal = Column(Float)


class tblTime(Base):
    """Time Entries: Multiple Time Entries roll up into a single Task"""
    __tablename__ = 'tblTime'

    timeID = Column(Integer, primary_key=True)
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    timeDescription = Column(String(500))
    isBillable = Column(Boolean)
    taskID = Column(Integer, ForeignKey('tblTask.taskID'))
    task = relationship(tblTask)
    userID = Column(Integer, ForeignKey('tblUser.userID'))
    user = relationship(tblUser)
    invoiceID = Column(Integer, ForeignKey('tblInvoice.invoiceID'))
    invoice = relationship(tblInvoice)
    dateAdd = Column(DateTime)
    dateEdit = Column(DateTime)


class tblImage(Base):
    """Images - for Users, Organizations, etc."""
    __tablename__ = 'tblImage'

    imageID = Column(Integer, primary_key=True)
    imagePath = Column(String(300))
    joinID = Column(Integer)
    isPrimary = Column(Boolean)


engine = create_engine('sqlite:///yearn.db')
Base.metadata.create_all(engine)
