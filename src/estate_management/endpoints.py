from flask import request

from src.base.endpoints import ResourceBase
from src.estate_management import exceptions
from src.estate_management.application_service import EstateAgencyService, EstateService
from src.estate_management.serializer import EstateDictSerializer, EstateAgencyDictSerializer
from src.web_app import get_api

api = get_api()


class EstateResource(ResourceBase):
    estate_dict_serializer = EstateDictSerializer()

    def __init__(self, estate_service):
        super(EstateResource, self).__init__()
        self.estate_service = estate_service

    def get(self, estate_id: int = None):
        if estate_id:
            try:
                estate = self.estate_service.find(estate_id)
                estate_json = self.estate_dict_serializer.serialize(estate)
                return self.response({'result': estate_json})
            except exceptions.EstateNotFound:
                return self.return_not_found('Estate with ID: {} was not found.'.format(estate_id))
            except exceptions.UnexpectedError as ex:
                return self.return_unexpected_error(ex)

        estates = self.estate_service.list()
        response = [self.estate_dict_serializer.serialize(estate) for estate in estates]
        return self.response({'result': response})

    def delete(self, estate_id: int):
        try:
            self.estate_service.delete(estate_id)
            return self.return_deleted()
        except exceptions.EstateNotFound:
            return self.return_not_found('Estate with ID: {} was not found or already deleted'.format(estate_id))
        except exceptions.UnexpectedError as ex:
            return self.return_unexpected_error(ex)

    def post(self):
        try:
            data_to_create_estate = self._serialize_in(request.json)
            estate = self.estate_service.create(data_to_create_estate)
            estate_json = self.estate_dict_serializer.serialize(estate)
            return self.response({'result': estate_json})
        except exceptions.EstateAgencyNotFound:
            return self.return_not_found('Estate Agency with ID: {} was not found'.format(self.payload['estate_agency_id']))
        except exceptions.InvalidPurpose as ex:
            return self.response({'result': 'Wrong Type of Purpose: {}, try resiencial or comerciall'.format(ex.invalid_purpose)})
        except exceptions.InvalidEstateType as ex:
            return self.response({'result': 'Wrong Type of Purpose: {}, try casa or apartamento'.format(ex.invalid_estate_type)})
        except exceptions.InvalidStatus as ex:
            return self.response({'result': 'Wrong Type of Status: {}, try ativo or invativo'.format(ex.invalid_status)})
        except exceptions.UnexpectedError as ex:
            return self.return_unexpected_error(ex)

    def put(self, estate_id: int):
        try:
            data_to_update_estate = self._serialize_in(request.json)
            estate = self.estate_service.update(estate_id, data_to_update_estate)
            estate_json = self.estate_dict_serializer.serialize(estate)
            return self.response({'result': estate_json})
        except exceptions.EstateNotFound:
            return self.return_not_found('Estate with ID: {} was not found or already deleted'.format(estate_id))
        except exceptions.EstateAgencyNotFound:
            return self.return_not_found('Estate Agency with ID: {} was not found or already deleted'.format(self.payload['estate_agency_id']))
        except exceptions.UnexpectedError as ex:
            return self.return_unexpected_error(ex)


class EstateAgencyResource(ResourceBase):
    estate_agency_dict_serializer = EstateAgencyDictSerializer()

    def __init__(self, estate_agency_service):
        super(EstateAgencyResource, self).__init__()
        self.estate_agency_service = estate_agency_service

    def get(self, estate_agency_id=None):
        if estate_agency_id:
            try:
                estate_agency = self.estate_agency_service.find(estate_agency_id)
                estate_json = self.estate_agency_dict_serializer.serialize(estate_agency)
                return estate_json
            except exceptions.EstateAgencyNotFound:
                return self.return_not_found('Estate Agency with ID: {} was not found.'.format(estate_agency_id))
            except exceptions.UnexpectedError as ex:
                return self.return_unexpected_error(ex)

        estate_agencies = self.estate_agency_service.list()
        response = [self.estate_agency_dict_serializer.serialize(estate_agency) for estate_agency in estate_agencies]
        return self._serialize_out(response), 200

    def delete(self, estate_agency_id: int):
        try:
            self.estate_agency_service.delete(estate_agency_id)
            return self.return_deleted()
        except exceptions.EstateAgencyNotFound:
            return self.return_not_found('Estate Agency with ID: {} was not found or already deleted'.format(estate_agency_id))
        except exceptions.UnexpectedError as ex:
            return self.return_unexpected_error(ex)

    def post(self):
        try:
            data_to_create_estate_agency = self._serialize_in(request.json)
            estate = self.estate_agency_service.create(data_to_create_estate_agency)
            estate_dict = self.estate_agency_dict_serializer.serialize(estate)
            return self.response({'result': estate_dict})
        except exceptions.UnexpectedError as ex:
            return self.return_unexpected_error(ex)

    def put(self, estate_agency_id: int):
        try:
            data_to_update_estate_agency = self._serialize_in(request.json)
            estate_agency = self.estate_agency_service.update(estate_agency_id, data_to_update_estate_agency)
            estate_json = self.estate_agency_dict_serializer.serialize(estate_agency)
            return self.response({'result': estate_json})
        except exceptions.EstateAgencyNotFound:
            return self.return_not_found('Estate Agency with ID: {} was not found.'.format(estate_agency_id))
        except exceptions.UnexpectedError as ex:
            return self.return_unexpected_error(ex)


def register(estate_service: EstateService, estate_agency_service: EstateAgencyService) -> None:
    api.add_resource(EstateResource, '/api/estates', '/api/estates/<int:estate_id>',
                     resource_class_kwargs={'estate_service': estate_service})

    api.add_resource(EstateAgencyResource, '/api/estate_agencies', '/api/estate_agencies/<int:estate_agency_id>',
                     resource_class_kwargs={'estate_agency_service': estate_agency_service})
