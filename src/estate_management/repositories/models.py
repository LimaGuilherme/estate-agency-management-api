from src.db_connections import get_sql_alchemy_instance

sql_alchemy = get_sql_alchemy_instance()


class EstateAgencyRow(sql_alchemy.Model):
    __tablename__ = 'estate_agencies'

    id = sql_alchemy.Column(sql_alchemy.Integer, primary_key=True)
    name = sql_alchemy.Column(sql_alchemy.String(150), nullable=True)
    address = sql_alchemy.Column(sql_alchemy.String(150), nullable=True)
    complement = sql_alchemy.Column(sql_alchemy.String(50), nullable=True)
    zip_code = sql_alchemy.Column(sql_alchemy.String(8), nullable=True)
    number = sql_alchemy.Column(sql_alchemy.String(10), nullable=True)
    city = sql_alchemy.Column(sql_alchemy.String(10), nullable=True)
    deleted = sql_alchemy.Column(sql_alchemy.Boolean(), default=False, nullable=True)


class EstateRow (sql_alchemy.Model):
    __tablename__ = 'estates'

    id = sql_alchemy.Column(sql_alchemy.Integer, primary_key=True)
    status = sql_alchemy.Column(sql_alchemy.String(7), nullable=False)
    description = sql_alchemy.Column(sql_alchemy.String(150), nullable=True)
    characteristics = sql_alchemy.Column(sql_alchemy.JSON, default=[], nullable=False)
    estate_type = sql_alchemy.Column(sql_alchemy.String(11), nullable=False)
    purpose = sql_alchemy.Column(sql_alchemy.String(11), nullable=False)
    deleted = sql_alchemy.Column(sql_alchemy.Boolean(), default=False, nullable=True)

    name = sql_alchemy.Column(sql_alchemy.String(150), nullable=True)
    address = sql_alchemy.Column(sql_alchemy.String(150), nullable=True)
    complement = sql_alchemy.Column(sql_alchemy.String(50), nullable=True)
    zip_code = sql_alchemy.Column(sql_alchemy.String(8), nullable=True)
    number = sql_alchemy.Column(sql_alchemy.String(10), nullable=True)
    city = sql_alchemy.Column(sql_alchemy.String(10), nullable=True)

    estate_agency_id = sql_alchemy.Column(sql_alchemy.Integer, sql_alchemy.ForeignKey('estate_agencies.id'), nullable=False)
    estate_agency = sql_alchemy.relationship("EstateAgencyRow")
