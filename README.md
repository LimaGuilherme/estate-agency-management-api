# Setting using Docker

    $ cp .env.sample .env #change your variables
    $ cp .env.test.sample .env.test #change your variables
    $ docker-compose up --build -d

# Running

    $ docker-compose up


Some JSON samples

Estate Agency

    {
        "name": "My Hunter Imobiliária",
        "address": "Avenida 13",
        "complement": "Executive Tower - 16° Andar",
        "zip_code": "74180-040",
        "number": 960,
        "city": "Goiânia"
    }
    
Estates

    {
        "estate_agency_id": 1,
        "city": "Goiânia"
        "complement": "Esq c/rua C16",
        "zip_code": "74170-090",
        "number": "55",
        "name": "Casa 200m² proximo ao centro",
        "address": "Rua C88",
        "description": "Casa reformada e nenhum inquilino anterior",
        "characteristics": {quartos: 2, banheiros: 2, suites: 1},
        "type": "casa",
        "purpose": "residencial",
        "status": "ativo"
    }
   