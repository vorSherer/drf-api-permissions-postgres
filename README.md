# Lab 32 - Django REST Framework, Permissions and Postgres

### *Author: Thomas Sherer*, 2020-09-17

## Description - Overview
Let’s move our site closer to production grade by adding Permissions and Postgresql Database.

## Feature Tasks and Requirements
### Features - General
- You have been supplied with two demos, each presenting a key new feature.
    - __`blogapi-permissions`__ demonstrates how to restrict access to portions of your APIs data.
    - __`blogapi-postgres`__ demonstrates switching over to using postgres vs sqlite

- Your job is to merge the functionality of both demos.
- Customize your project to use different application features/models than Blog and Post

### Features - Django REST Framework
- Make your site a DRF powered API as you did in previous lab.
- Adjust project’s permissions so that only authenticated user’s have access to API.
- Add a custom permission so that only author of blog post can update or delete it.
- Add ability to switch user’s directly from browsable API.

### Features - Docker
- __NOTE__ Refer to demo for built out __`Dockerfile`__ and __`docker-compose.yml`__ examples.
- create __`Dockerfile`__ based off __`python:3.8-slim`__
- create __`docker-compose.yml`__ to run Django app as a __`web`__ service.
- enter __`docker-compose up --build`__ to start your site.
- add __`postgres 11`__ as a service
    - __Note:__ It is not required to include a volume so that data can persist when container is shut down.

- Go to browsable api and confirm site properly restricts users based on their permissions.

## Implementation Notes
- You should __*NOT*__ be running Postgres directly on host machine.
    - This means that operations like __`createsuperuser`__ and __`migrate`__ will need to happen inside the container.
    - We’ll go over this in lecture but

### User Acceptance Tests
Adjust any tests provided in demo to work with your project.

## Configuration
Use __`poetry`__ to create __`drf-api-permissions-postgres`__ project.

    - $ poetry init -n

Use the folder created by Poetry as the root of your project’s git repository.

## Collaborations and Attributions

.gitignore content courtesy of https://www.toptal.com/developers/gitignore/api/django
