# pythonProjectManagerFastAPI

## Description

This project is a powerful project management system designed for software development teams. It provides a comprehensive set of features to help teams efficiently manage their projects, tasks, and users. The system is built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python.

## Features

- User registration and authentication using JWT tokens.
- Create, manage, and view projects stored in a database.
- Add new tasks to projects using a user-friendly form that sends data through API requests.
- Task management within projects, including status changes, assignment of assignees.
- Display a list of all tasks assigned to a user.
- Tools for managing projects, tasks, and users.

## Installation

1. Clone the repository:

git clone https://github.com/fanatik3m/pythonProjectManagerFastAPI.git

2. Install the project dependencies:

pip install -r requirements.txt


3. Configure the database settings in .env.

4. Run the database migrations:

alembic revision --autogenerate -m "First migration"
alembic upgrade head

5. Start the FastAPI server:

uvicorn main:app --reload


###Using docker:

1. Clone the repository:
  git clone https://github.com/fanatik3m/pythonProjectManagerFastAPI.git

2. install docker

3.  execute:
  + docker compose build
  + docker compose up

4. Enjoy usage of my api in localhost:9999 :)



## Usage

1. Open your web browser and go to http://localhost:8000 (if docker: http://localhost:9999).
2. Add role with id = 0, name = user in endpoint (watch in swagger docks paragraph 6) and use in it admin_password from admin_password.txt
3. Register a new user or log in with an existing account.
4. Create a new project and add tasks to it.
5. Manage tasks within the project, assign users, change statuses.
6. Use endpoints in swagger docs on http://localhost:8000/docs (if docker: http://localhost:9999/docs) to manage projects, tasks, and users.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.
