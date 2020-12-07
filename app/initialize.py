from app import configurations, web_app as web_app_module, connections

config = configurations.get_config()
web_app = web_app_module.get_web_app()
api = web_app_module.get_api()

connections.register(web_app)

estate_repository = MySQLEstateRepository(db_connection.session)
estate_agency_repository = MySQLEstateAgencyRepository(db_connection.session)

estate_service = EstateService(estate_repository)
estate_agency_service = EstateAgencyService(estate_agency_repository)

estate_management_endpoints.register(
    estate_service=estate_service,
    estate_agency_service=estate_agency_service,
)