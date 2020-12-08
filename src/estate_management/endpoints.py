from flask_restful import Resource

from src.estate_management import exceptions
from src.estate_management.application_service import EstateAgencyService, EstateService
from src.estate_management.serializer import EstateDictSerializer, EstateAgencyDictSerializer
from src.web_app import get_api

api = get_api()


class ResourceBase(Resource):

    @property
    def payload(self):
        payload = {}
        try:
            if request.json:
                payload.update(self.transform_key(request.json, self.camel_to_snake))
        except Exception as Ex:
            pass
        if request.form:
            payload.update(self.transform_key(request.form, self.camel_to_snake))
        if request.args:
            payload.update(self.transform_key(request.args, self.camel_to_snake))
        return payload

    def response(self, data_dict):
        return self.transform_key(data_dict, self.snake_to_camel)

    def return_ok(self, **extra):
        result = {'result': 'OK'}
        if extra is not None:
            result.update(extra)
        return result

    def return_deleted(self):
        return {'result': 'OK'}, 204

    def return_not_found(self, exception=None):
        return {'result': 'error', 'error': 'Not Found', 'exception': str(exception)}, 404

    def return_unexpected_error(self, exception=None):
        return {'result': 'error', 'error': 'General Error', 'exception': str(exception)}, 500

    def return_bad_request(self, exception=None):
        return {'result': 'error', 'error': 'Bad Request', 'exception': str(exception)}, 400

    def return_bad_parameters(self, exception=None):
        return {'result': 'error', 'error': 'Bad Parameters', 'exception': str(exception)}, 500


class EstateResource(ResourceBase):
    estate_dict_serializer = EstateDictSerializer()

    def __init__(self, estate_service):
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

    def delete(self, estate_id):
        try:
            self.estate_service.delete(estate_id)
            return self.return_deleted()
        except exceptions.EstateNotFound:
            return self.return_not_found('Estate with ID: {} was not found or already deleted'.format(estate_id))
        except exceptions.UnexpectedError as ex:
            return self.return_unexpected_error(ex)

    def post(self):
        try:
            estate = self.estate_service.create(self.payload)
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

    def put(self, estate_id):
        try:
            estate = self.estate_service.update(estate_id, self.payload)
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
        return self.response({'result': response})

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
            estate = self.estate_agency_service.create(self.payload)
            estate_json = self.estate_agency_dict_serializer.serialize(estate)
            return self.response({'result': estate_json})
        except exceptions.UnexpectedError as ex:
            return self.return_unexpected_error(ex)

    def put(self, estate_agency_id: int):
        try:
            estate_agency = self.estate_agency_service.update(estate_agency_id, self.payload)
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
