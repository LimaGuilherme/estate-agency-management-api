from importlib.resources import Resource

from src.base.serializer import CaseStyleConverter


class ResourceBase(Resource):

    def __init__(self,  *args, **kwargs):
        super(ResourceBase, self).__init__(*args, **kwargs)
        self._converter = CaseStyleConverter()

    def _serialize_in(self, data_dict):
        return self._converter.camel_to_snake(data_dict)

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

    def response(self, data_dict):
        return self._converter.camel_to_snake(data_dict)
