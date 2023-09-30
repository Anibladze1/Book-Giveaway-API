# Book GiveAway

## Api To Get or Giveaway Books For Free

The Book Giveaway Service is a platform where users can generously offer books they no longer need and 
pick up books shared by others, all for free. While anyone can browse the collection of available books, 
only registered members can participate in the giving and taking. 
The platform also provides detailed information about each book, including its author, genre, condition, and more. 
Everyone who uses the API can filter books by its genre, author, title and etc.

**Note:** Only SuperUser Can Create Conditions. Create it When Starting the Project (e.g., New, Used).

### Once you've started the server, you can access the Book GiveAway API through your web browser or API client to This Url:
- 0.0.0.0:8000

## Run Locally Without Docker
To run locally, you need to create a virtual environment and install all the requirements.
Also you'll need to have PG admin installed, or Instead of PostgresSQL use sql lite. 

### Steps
1. **Clone The Repo From GitHub**
```sh
git clone https://github.com/Anibladze1/Book-Giveaway-API
```

2. **Create Virtual Environment and Activate it**
```sh
python3 -m bin venv venv
```
```sh
source venv/bin/activate
```

3. **Requirements**
Install all required packages with pip
```sh
pip install -r requirements.txt
```

4.  **Run Migrations**
#### If you have PG Admin running Locally then: 

- Create .env file in root repository (or rename sample.env to .env and add values to it), copy sample.env
and Fill with values to connect database locally
```sh
python manage.py makemigrations
python manage.py migrate
```

#### Else
- Open library Directory -> settings.py -> Scroll Down to Database and See The instructions there, Then:

### Start Server
```sh
python manage.py runserver
```

### Run Unit Tests
```sh
python manage.py test users.tests
```


## Run Locally With Docker
To run locally with docker, you need to clone the repo, build and start container. 
It will automatically run migrations when you build the container.

### Steps
- Clone The Repo From GitHub
```sh
git clone https://github.com/Anibladze1/Book-Giveaway-API
```

- Create .env file in root repository (or rename sample.env to .env and add values to it), copy sample.env
and Fill with values to connect database locally

- Run and Build Docker Container
```sh
docker compose up --build
```

### Run Unit Tests (Before this Enter in Docker Container with: docker exec -it container-name bash(or shell or zsh))
```sh
python manage.py test users.tests
```
