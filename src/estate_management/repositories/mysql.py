from typing import List
from sqlalchemy import exc

from src.estate_management.repositories.models import EstateAgencyRow, EstateRow
from src.estate_management.entities import EstateAgency, Estate, EstateAgencyValueObject, AbstractEstateAgencyRepository, AbstractEstateRepository
from src.estate_management import exceptions


class MySQLEstateAgencyRepository(AbstractEstateAgencyRepository):

    def __init__(self, session):
        self._session = session
        self._query = self._session.query(EstateAgencyRow)

    def __create_estate_agency(self, estate_agency_row: EstateAgencyRow) -> EstateAgency:
        return EstateAgency(estate_agency_row.city, estate_agency_row.name, estate_agency_row.number, estate_agency_row.zip_code,
                            estate_agency_row.complement, estate_agency_row.address, estate_agency_row.id)

    def __update_infos(self, estate_agency: EstateAgency, estate_agency_row: EstateAgencyRow) -> None:
        estate_agency_row.city = estate_agency.city
        estate_agency_row.name = estate_agency.name
        estate_agency_row.number = estate_agency.number
        estate_agency_row.zip_code = estate_agency.zip_code
        estate_agency_row.complement = estate_agency.complement
        estate_agency_row.address = estate_agency.address

    def add(self, estate_agency: EstateAgency) -> EstateAgency:
        estate_agency_row = EstateAgencyRow()
        self.__update_infos(estate_agency, estate_agency_row)
        self._session.add(estate_agency_row)
        self._session.commit()
        estate_agency.associate_id(estate_agency_row.id)
        return estate_agency

    def get(self, estate_agency_id: int) -> EstateAgency:
        estate_agency_row = self._query.filter_by(id=estate_agency_id, deleted=False).one_or_none()

        if not estate_agency_row:
            raise exceptions.EstateAgencyNotFound

        estate_agency = self.__create_estate_agency(estate_agency_row)
        return estate_agency

    def update(self, estate_agency: EstateAgency) -> None:
        estate_agency_row = EstateAgencyRow()
        estate_agency_row.id = estate_agency.id
        self.__update_infos(estate_agency, estate_agency_row)
        self._session.merge(estate_agency_row)
        self._session.commit()

    def delete(self, estate_agency_id: int) -> None:
        estate_agency_row = self._query.filter_by(id=estate_agency_id, deleted=False).one_or_none()

        if not estate_agency_row:
            raise exceptions.EstateAgencyNotFound

        estate_agency_row.deleted = True
        self._session.commit()

    def list(self) -> List:
        return [self.__create_estate_agency(estate_agency_row) for estate_agency_row in self._query.filter()]


class MySQLEstateRepository(AbstractEstateRepository):

    def __init__(self, session):
        self._session = session
        self._query = self._session.query(EstateRow)

    def __create_estate(self, estate_row: EstateRow) -> Estate:
        estate_agency = EstateAgencyValueObject(estate_row.estate_agency.id, estate_row.estate_agency.name)
        return Estate(estate_row.status, estate_row.characteristics, estate_row.description, estate_row.estate_type,
                      estate_row.purpose, estate_row.city, estate_row.name, estate_row.address, estate_row.complement,
                      estate_row.zip_code, estate_row.number, estate_agency, estate_row.id)

    def __update_infos(self, estate: Estate, estate_row: EstateRow) -> None:
        estate_row.status = estate.status
        estate_row.characteristics = estate.characteristics
        estate_row.description = estate.description
        estate_row.city = estate.city
        estate_row.name = estate.name
        estate_row.number = estate.number
        estate_row.zip_code = estate.zip_code
        estate_row.complement = estate.complement
        estate_row.address = estate.address
        estate_row.purpose = estate.purpose
        estate_row.estate_type = estate.estate_type

    def add(self, estate: Estate) -> Estate:
        estate_row = EstateRow()
        estate_row.estate_agency_id = estate.estate_agency.id

        self.__update_infos(estate, estate_row)

        try:
            self._session.add(estate_row)
            self._session.commit()
            estate.associate_id(estate_row.id)
            return estate

        except exc.IntegrityError as ex:
            if ex.orig.args[0] == 1452:
                raise exceptions.EstateAgencyNotFound
            raise exceptions.UnexpectedDBError(ex.orig.args[1])

    def get(self, estate_id: int) -> Estate:
        estate_row = self._query.filter_by(id=estate_id).one_or_none()

        if not estate_row:
            raise exceptions.EstateNotFound

        estate = self.__create_estate(estate_row)
        return estate

    def update(self, estate: Estate) -> None:
        estate_row = EstateRow()

        if not estate_row:
            raise exceptions.EstateNotFound

        estate_row.id = estate.id
        self.__update_infos(estate, estate_row)
        self._session.merge(estate_row)
        self._session.commit()

    def delete(self, estate_id: int) -> None:
        estate_row = self._query.filter_by(id=estate_id).one_or_none()

        if not estate_row:
            raise exceptions.EstateNotFound

        estate_row.deleted = True
        self._session.commit()

    def list(self) -> List:
        return [self.__create_estate(estate_row) for estate_row in self._query.filter()]
