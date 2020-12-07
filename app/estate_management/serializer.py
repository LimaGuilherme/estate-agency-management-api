from app.estate_management.domain import EstateAgency, Estate, AbstractEstateAgencySerializer


class EstateAgencyDictSerializer(AbstractEstateAgencySerializer):

    def serialize(self, estate_agency: EstateAgency) -> dict:
        return {
            'id': estate_agency.id,
            'city': estate_agency.city,
            'address': estate_agency.address,
            'complement': estate_agency.complement,
            'zip_code': estate_agency.zip_code,
            'number': estate_agency.number,
            'name': estate_agency.name,
        }


class EstateDictSerializer(AbstractEstateAgencySerializer):

    def serialize(self, estate: Estate) -> dict:
        return {
            'id': estate.id,
            'city': estate.city,
            'complement': estate.complement,
            'zip_code': estate.zip_code,
            'number': estate.number,
            'name': estate.name,
            'address': estate.address,
            'description': estate.description,
            'characteristics': estate.characteristics,
            'type': estate.estate_type,
            'purpose': estate.purpose,
            'status': estate.status
        }
