from typing import List

from src.estate_management.entities import EstateAgency, Estate, EstateAgencyValueObject
from src.estate_management.repositories import MySQLEstateRepository, MySQLEstateAgencyRepository


class EstateService(object):

    def __init__(self, estate_repository: MySQLEstateRepository) -> None:
        self.__estate_repository = estate_repository

    def create(self, estate_agency_dict: dict) -> Estate:
        estate_agency = EstateAgencyValueObject(id=estate_agency_dict.pop('estate_agency_id'))
        estate_agency_dict['estate_agency'] = estate_agency
        estate = Estate(**estate_agency_dict)
        self.__estate_repository.add(estate)
        return estate

    def update(self, estate_id: int, estate_dict: dict) -> Estate:
        estate = self.__estate_repository.get(estate_id)
        estate.update_all_infos(estate_dict)
        self.__estate_repository.update(estate)
        return estate

    def delete(self, estate_id: int) -> None:
        self.__estate_repository.delete(estate_id)

    def find(self, estate_id: int) -> Estate:
        return self.__estate_repository.get(estate_id)

    def list(self) -> List[Estate]:
        return self.__estate_repository.list()


class EstateAgencyService(object):

    def __init__(self, estate_agency_repository: MySQLEstateAgencyRepository) -> None:
        self.__estate_agency_repository = estate_agency_repository

    def create(self, estate_agency_dict: dict) -> EstateAgency:
        estate_agency = EstateAgency(**estate_agency_dict)
        self.__estate_agency_repository.add(estate_agency)
        return estate_agency

    def update(self, estate_agency_id: int, estate_agency_dict: dict) -> EstateAgency:
        estate_agency = self.__estate_agency_repository.get(estate_agency_id)
        estate_agency.update_all_infos(estate_agency_dict)
        self.__estate_agency_repository.update(estate_agency)
        return estate_agency

    def delete(self, estate_agency_id: int) -> None:
        self.__estate_agency_repository.delete(estate_agency_id)

    def find(self, estate_agency_id: int) -> EstateAgency:
        return self.__estate_agency_repository.get(estate_agency_id)

    def list(self) -> List[Estate]:
        return self.__estate_agency_repository.list()
