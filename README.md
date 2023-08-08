# Movie-app


The project is about goal management. Each user has access to goals that they can create, edit, delete, and comment on. Each goal has its own status, priority, and deadline date. There is also a functionality to control certain features through a Telegram bot, for which verification is provided.

### Used

---

- Python 3.10
- Flask 2.3.2
- Flask restx 1.1.0
- SQLAlchemy 2.0.19
- Marshmallow 3.20.1
- PyJWT 2.8.0
- Pytest 7.4.0
- Docker
- Docker-compose

### Installation

---
### Linux
1. Clone Repository

    ```bash
    git clone https://github.com/Danilu2537/Movie-app.git
    ```
2. Install Docker and Docker-compose

    ```bash
    sudo apt install docker docker-compose
    ```
3. Create file .env and fill it according to the contents of .env.example


### Usage

---

1. Go to the project folder

    ```bash
    cd Movie-app
    ```

2. Create database tables

    ```bash
    python create_tables.py
    ```
3. Load fixtures

    ```bash
    python load_fixtures.py
    ```

2. Launch docker-compose

    ```bash
    sudo docker-compose up -d
    ```

3. Go to the address in the browser http://localhost
