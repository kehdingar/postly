# Postly: Great Social Platform

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Technology Stack](#technologystack)
- [Usage](#usage)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to Postly, robust social platform built on Django Rest Framework! Postly is designed to provide users with a seamless and secure experience, allowing them to engage with the community through posts, votes, and likes. With token-based authentication and a comprehensive set of features.

## Features

- **User Authentication**: Secure token-based authentication ensures a safe and reliable user experience.
- **Profile Management**: Users can register, update their profiles, and change passwords with ease.
- **Post Creation and Interaction**: Create, view, and delete posts. Users can like posts and create votes to express their opinions.
- **Vote Limitations**: Prevents users from liking a post more than once.
- **Post Deletion**: Users can only delete posts they have created.
- **Comprehensive Testing**: Extensive test coverage for the accounts, posts, and votes apps to ensure robust functionality.
- **Email Notifications**: Receive confirmation and password reset emails for a seamless user experience.

## Technology Stack

- **Django REST Framework**: A powerful and flexible toolkit for building web APIs.
- **Python**: A versatile and dynamic programming language.
- **Token-Based Authentication**: A secure authentication method.
- **Comprehensive Testing**: To ensure quality and reliability.


## Installation

To get started with Postly, follow these steps:

1. Clone the repository:

    - clone this repository

2. Install dependencies:
    - pip install -r requirements.txt

3. Configure environment variables
    - follow the example in the `example-env-file.txt` and create a `.env` file in the root directory of the project

4. Apply migrations:
    - python manage.py makemigrations
    - python manage.py migrate
    
5. Run the development server:
    - python manage.py runserver

6. Since we are using a token based authentication, you can use a client like **Postman** or **curl** to test endpoints

## Usage

Postly provides a user-friendly API with clear endpoints for creating, updating, and interacting with posts and votes. Explore the API documentation for detailed information on each endpoint.

## Authentication

Token-based authentication is employed to secure user accounts and interactions. To authenticate requests, include the token in the headers:

1. Using a client like **Postman** or **curl** add [Authorization: Token your_token_here] to the header

## Endpoints

Explore the API with the following endpoints:

- /api/accounts/: User registration and profile management.
- /api/posts/: CRUD operations for posts.
- /api/votes/: Create and view votes, like posts.

## Testing

Postly comes with comprehensive test coverage to ensure the reliability of its features. 
Run the tests using:

- For each app use [python3 manage.py test -v 1 "appname".tests."Test Class"."name of test"]

- Some user might have to use "python" instead of "python3" in the above command for it to work

## Contributing

Contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE)
