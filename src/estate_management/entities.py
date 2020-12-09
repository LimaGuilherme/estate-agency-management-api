from abc import ABC, abstractmethod
from typing import List

from src.estate_management import exceptions


class EstateAgencyValueObject:
    def __init__(self, id, name=None):
        self.__id = id
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name


class Estate:

    def __init__(self, status, characteristics, description, estate_type, purpose, city, name, address,
                 complement, zip_code, number, estate_agency, estate_id=None):
        self.__id = estate_id
        self.__characteristics = characteristics
        self.__description = description
        self.__city = city
        self.__name = name
        self.__address = address
        self.__complement = complement
        self.__zip_code = zip_code
        self.__number = number
        self.__estate_agency = estate_agency
        self.__status = self.__check_status_is_valid(status)
        self.__estate_type = self.__check_type_is_valid(estate_type)
        self.__purpose = self.__check_purpose_is_valid(purpose)

    def __check_status_is_valid(self, status: str) -> str:
        if status not in ['ativo', 'inativo']:
            raise exceptions.InvalidStatus(status)
        return status

    def __check_type_is_valid(self, estate_type: str) -> str:
        if estate_type not in ['apartamento', 'casa']:
            raise exceptions.InvalidEstateType(estate_type)
        return estate_type

    def __check_purpose_is_valid(self, purpose: str) -> str:
        if purpose not in ['residencial', 'escritório']:
            raise exceptions.InvalidPurpose(purpose)
        return purpose

    def associate_id(self, estate_id: int) -> None:
        self.__id = estate_id

    def update_all_infos(self, infos: dict) -> None:
        self.__city = infos['city']
        self.__name = infos['name']
        self.__address = infos['address']
        self.__complement = infos['complement']
        self.__characteristics = infos['characteristics']
        self.__zip_code = infos['zip_code']
        self.__number = infos['number']
        self.__estate_type = infos['estate_type']
        self.__purpose = infos['purpose']
        self.__description = infos['description']
        self.__status = infos['status']

    @property
    def id(self) -> int:
        return self.__id

    @property
    def characteristics(self) -> dict:
        return self.__characteristics

    @property
    def description(self) -> str:
        return self.__description

    @property
    def status(self) -> str:
        return self.__status

    @property
    def estate_type(self) -> str:
        return self.__estate_type

    @property
    def purpose(self) -> str:
        return self.__purpose

    @property
    def name(self) -> str:
        return self.__name

    @property
    def complement(self) -> str:
        return self.__complement

    @property
    def zip_code(self) -> str:
        return self.__zip_code

    @property
    def estate_agency(self) -> EstateAgencyValueObject:
        return self.__estate_agency

    @property
    def address(self) -> str:
        return self.__address

    @property
    def number(self) -> str:
        return self.__number

    @property
    def city(self) -> str:
        return self.__city


class EstateAgency:

    def __init__(self, city, name, address, complement, zip_code, number, estate_agency_id=None):
        self.__id = estate_agency_id
        self.__name = name
        self.__address = address
        self.__complement = complement
        self.__zip_code = zip_code
        self.__number = number
        self.__city = city

    def associate_id(self, estate_agency_id:  int) -> None:
        self.__id = estate_agency_id

    def update_all_infos(self, infos):
        self.__name = infos['name']
        self.__address = infos['address']
        self.__complement = infos['complement']
        self.__zip_code = infos['zip_code']
        self.__number = infos['number']
        self.__city = infos['city']

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def complement(self) -> str:
        return self.__complement

    @property
    def zip_code(self) -> str:
        return self.__zip_code

    @property
    def address(self) -> str:
        return self.__address

    @property
    def number(self) -> str:
        return self.__number

    @property
    def city(self) -> str:
        return self.__city


class AbstractEstateAgencyRepository(ABC):

    @abstractmethod
    def get(self, item_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def add(self, estate_agency: EstateAgency) -> EstateAgency:
        raise NotImplementedError

    @abstractmethod
    def update(self, estate_agency: EstateAgency) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, item_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List:
        raise NotImplementedError


class AbstractEstateRepository(ABC):

    @abstractmethod
    def get(self, item_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def add(self, estate: Estate) -> Estate:
        raise NotImplementedError

    @abstractmethod
    def update(self, estate: Estate) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, item_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List:
        raise NotImplementedError
