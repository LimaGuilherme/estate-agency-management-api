from app import database

db = database.AppRepository.db


class EstateAgencyRow(db.Model):
    __tablename__ = 'estate_agencies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=True)
    address = db.Column(db.String(150), nullable=True)
    complement = db.Column(db.String(50), nullable=True)
    zip_code = db.Column(db.String(8), nullable=True)
    number = db.Column(db.String(10), nullable=True)
    city = db.Column(db.String(10), nullable=True)
    deleted = db.Column(db.Boolean(), default=False, nullable=True)


class EstateRow (db.Model):
    __tablename__ = 'estates'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(7), nullable=False)
    description = db.Column(db.String(150), nullable=True)
    characteristics = db.Column(db.JSON, default=[], nullable=False)
    estate_type = db.Column(db.String(11), nullable=False)
    purpose = db.Column(db.String(11), nullable=False)
    deleted = db.Column(db.Boolean(), default=False, nullable=True)

    name = db.Column(db.String(150), nullable=True)
    address = db.Column(db.String(150), nullable=True)
    complement = db.Column(db.String(50), nullable=True)
    zip_code = db.Column(db.String(8), nullable=True)
    number = db.Column(db.String(10), nullable=True)
    city = db.Column(db.String(10), nullable=True)

    estate_agency_id = db.Column(db.Integer, db.ForeignKey('estate_agencies.id'), nullable=False)
    estate_agency = db.relationship("EstateAgencyRow")
