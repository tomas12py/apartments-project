# Apartments project

This project aims to manage real estate by providing the necessary resources to sell and rent apartments. It uses Django Rest Framework as the API backend, MySQL for the database, and Redis for caching.
<br>
<br>
## Project structures

- REST API
- JWT authentication
- Rate limiting
- DRY 
- Polymorphism
- Class inheritance
- Multiple class inheritance
- Swagger
- Dockerized application
- Caching
<br>

## How to initiliaze the project 

You need to activate your virtual enviroment using this command or do this the way you feel comfortable:

`env/Scripts/activate`

Run the project using this command:

`python manage.py runserver`

If you wanna use docker, run the docker-compose using this command:

`docker-compose up --build`

## Application functionalities

### Login

All the endpoint routes are protected so you need to do the normal flow of JWT but you can change it from settings.

<img width="1622" height="527" alt="Captura de pantalla 2026-01-16 015347" src="https://github.com/user-attachments/assets/a5abf69c-2cca-496b-90bd-7138fd894dfa" />
<br>
<br>
<img width="1624" height="475" alt="Captura de pantalla 2026-01-16 022356" src="https://github.com/user-attachments/assets/71dfd96a-21de-432a-a9c2-bdae21258010" />

<br>
<br>

### Get all apartments
This endpoint gets all apartments.

<img width="1630" height="744" alt="Captura de pantalla 2026-01-16 015944" src="https://github.com/user-attachments/assets/06e49f37-cfe4-4ff8-a892-c63e77286fef" />
<br>
<br>

### Create an apartment

This endpoint creates an apartment and if there's something wrong the errors are captured.

<img width="1616" height="738" alt="Captura de pantalla 2026-01-16 020838" src="https://github.com/user-attachments/assets/fcd9b784-bfcc-4704-98d2-2734c89b6c80" />
<br>
<br>
<img width="1632" height="733" alt="Captura de pantalla 2026-01-16 020913" src="https://github.com/user-attachments/assets/a0ddc52a-fff6-4190-b001-c7e02188fb17" />

<br>
<br>

### Update an apartment

This endpoint updates an apartment and verifys is the parameter has a valid type, I made this customized validation.

<img width="1373" height="460" alt="Captura de pantalla 2026-01-16 021312" src="https://github.com/user-attachments/assets/7d5c94d0-cf01-40e6-a21f-e89bc5ce8965" />
<br>
<br>
<img width="1543" height="424" alt="Captura de pantalla 2026-01-16 021715" src="https://github.com/user-attachments/assets/e75921ff-6829-492e-89f6-fc3c8fc77969" />

<br>
<br>

### Delete an apartment

This endpoint deletes an apartment and has its own validations.

<img width="1277" height="451" alt="Captura de pantalla 2026-01-16 022106" src="https://github.com/user-attachments/assets/c1bdc988-6936-4323-8aeb-022332687cf2" />
<br>
<br>
<img width="1608" height="474" alt="Captura de pantalla 2026-01-16 022615" src="https://github.com/user-attachments/assets/d288c06f-95d6-405c-9003-2355ead2d44e" />

<br>
<br>


### Filter an apartment using nested parameters

You can filter in these ways:
- Range filtering 
- Exact value matching 
- Case-insensitive searches


<img width="1585" height="694" alt="Captura de pantalla 2026-01-16 023013" src="https://github.com/user-attachments/assets/b9eb0b4f-1106-4ec1-a87e-4d7999d47ca2" />
<br>
<br>
<img width="1615" height="706" alt="Captura de pantalla 2026-01-16 023628" src="https://github.com/user-attachments/assets/66ddf2ac-2d4c-4c43-a1ec-63495c6118b7" />

### Pagination for apartments

You can get the page size and page number using query parameters.

<img width="1632" height="541" alt="Captura de pantalla 2026-01-16 025843" src="https://github.com/user-attachments/assets/1095585d-2144-418d-b41a-611b89abecd7" />

### Rate limiting
All endpoints use rate limiting for prevent external attacks and save requests, you can choose how many requests a user would do for a specific endpoint.

<img width="1442" height="504" alt="Captura de pantalla 2026-01-16 030111" src="https://github.com/user-attachments/assets/173cc740-f857-4cfd-9b8f-35d44d5f4704" />

<br>
<br>

### Caching
You can caching a view for improve its performance using this decorator.

<img width="900" height="450" alt="caching" src="https://github.com/user-attachments/assets/e51bf0c7-295c-4f3a-8851-dcc72ab59bc2" />
<br>
<br>
<img width="1588" height="520" alt="Captura de pantalla 2026-01-16 031230" src="https://github.com/user-attachments/assets/9c90131e-d1fd-48d3-8d2b-888ffd724148" />

<br>
<br>

### Swagger
You can create customized documentation using swagger in this way.

<img width="600" height="1300" alt="Swagger documentation" src="https://github.com/user-attachments/assets/53f80584-f3b0-4216-99bd-84dcd915005a" />
<br>
<br>
<img width="1250" height="500" alt="Captura de pantalla 2026-01-16 032443" src="https://github.com/user-attachments/assets/400cee26-4b00-466a-afe7-146d056bd18a" />

<br>
<br>

### Health check
Using this endpoint you can know what's the application status, it verifys the databases making writting and reading operations. By default it returs a html response but using the query parameter format you can change it.


<img width="1503" height="451" alt="Captura de pantalla 2026-01-16 033057" src="https://github.com/user-attachments/assets/107f52cf-4f25-416a-91de-0d728c65a6db" />

### Testing
You can testing data structures and http codes in this way.



<img width="500" height="700" alt="Captura de pantalla 2026-01-16 034218" src="https://github.com/user-attachments/assets/6adf0616-d65f-4937-a928-fc083f68813f" />

