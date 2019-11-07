# Siigo

## Steps required to start the application

1. It is recommended to use **Python 3.4** or higher
2. Install the packages contained in **requirements.txt** using the command installation of `pip install -r requirements.txt`
3. Execute the run.py file with `python manage.py makemigrations`
3. Execute the run.py file with `python manage.py migrate`
3. Execute the run.py file with `python manage.py runserver`
4. Open the browser and go to the address http://localhost:8000/ or http://127.0.0.1:8000/


## API REST

- Fake data to models

```
curl -X POST -H "Content-Type: application/json" -d '{"number": 5}' http://127.0.0.1:8000/api/fake/
```

- Fake data to products

```
curl -X POST -H "Content-Type: application/json" -d '{"number": 5}' http://127.0.0.1:8000/api/fake-products/
```
