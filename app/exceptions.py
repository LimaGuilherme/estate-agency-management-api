class BadParameter(Exception):
    pass


class NotAuthorized(Exception):
    pass


class UnexpectedError(Exception):
    pass


class NotFound(Exception):
    pass


class RepositoryError(Exception):
    pass


class ConfigClassNotFound(Exception):
    pass


class EstateAgencyNotFound(Exception):
    pass


class EstateNotFound(Exception):
    pass


class InvalidPurpose(Exception):

    def __init__(self, invalid_purpose):
        self.invalid_purpose = invalid_purpose


class InvalidEstateType(Exception):

    def __init__(self, invalid_estate_type):
        self.invalid_estate_type = invalid_estate_type


class InvalidStatus(Exception):

    def __init__(self, invalid_status):
        self.invalid_status = invalid_status


class UnexpectedDBError(Exception):

    def __init__(self, db_error_message):
        self.db_error_message = db_error_message
