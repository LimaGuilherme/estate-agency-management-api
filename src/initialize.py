from src import configurations, web_app as web_app_module
from src.db_connections import get_sql_alchemy_instance
from src.estate_management.repositories import MySQLEstateRepository, MySQLEstateAgencyRepository

config = configurations.get_config()
web_app = web_app_module.get_web_app()
api = web_app_module.get_api()
sql_alchemy = get_sql_alchemy_instance()

estate_repository = MySQLEstateRepository(sql_alchemy.session)
estate_agency_repository = MySQLEstateAgencyRepository(sql_alchemy.session)

estate_service = EstateService(estate_repository)
estate_agency_service = EstateAgencyService(estate_agency_repository)

estate_management_endpoints.register(
    estate_service=estate_service,
    estate_agency_service=estate_agency_service,
)
