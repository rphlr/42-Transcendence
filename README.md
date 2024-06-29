# ft_transcendence

## Team
This project was developed by:
- Joël
- Alessandro
- Diogo
- Rita
- Raphael

## Score obtained
120/100

## Implemented Modules
- Use of a framework as backend
- Use of a database for the backend
- Standard user management
- Remote players
- Live chat
- AI Opponent
- Game stats dashboards
- Two-Factor Authentication (2FA)
- Microservices
- Expanded browser compatibility
- Multiple Language Support

## Installation and Setup

### Prerequisites
- Docker installed on your machine

### Installation Steps

1. Environment preparation:
   - Start Docker
   - Create the following folders:
     ```
     mkdir -p db_transcendence/db_transcendence db_transcendence/profile_pictures
     ```

2. Environment configuration:
   - Copy the `.env.EXAMPLE` file to `.env`
   - Fill in the missing data in the `.env` file
   
   Note: The displayed API keys are not sensitive and can be left as they are.

3. Project launch:
   Run the following command to build and start the Docker containers:
```bash
docker-compose up -d --build
```
4. Accessing the site:
- Open your browser and go to `https://localhost`
- Accept the SSL certificate warning

## Notes
We did not use a Makefile for this project, in accordance with the imposed constraints.
