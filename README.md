# Dungeons and Dragons

|               |                     |
| ------------- | ------------------  |
|**Name**       | Dungeons and Dragons|
|**Contributer**| Musa Kazem          |
|**Version**    | 2.0.0               |

## Contents

1. Project Overview
1. How to install
    - Overview
    - Packages
    - Installing Postgresql
    - Database configuration

---

## Project Overview

A dungeons and dragons terminal game.

## How to install

### Overview

To play the game you would need to install packages and  a database on your system. It is also important configure the database for the last step.

Will be using `Postgresql` for this project.
The following packages need to be installed `psycopg2`, `SQLAlchemy`, `SQLAlchemy-Utils`.

### Packages

To install `psycopg2`:

```bash
pip install psycopg2
```

To install `SQLAlchemy`:

```bash
pip install SQLAlchemy
```

To install `SQLAlchemy-Utils`:

```bash
pip install SQLAlchemy-Utils
```

### Postgresql

As an open source object-relational database management system, PostgreSQL available for MacOS, Linux, and Windows.

#### MacOS

Let's walk through installing PostgreSQL with the postgresapp on Mac.

1) Visit `http://postgresapp.com/`
2) Download the most recent version --> Click "Download"
3) Open the application, and click "initialize" to create a new PostgreSQL server
4) Ensure that the Postgres.app bin folder has been added to your $PATH;
  4.1) In the command line, enter: `echo "$PATH"`
  4.2) Search through the output and make sure Postgres.app/Contents/Version/latest/bin is there
       in order to ensure that this directory's executables are callable from any directory in bash.
5) In the command line, enter: `lsof -i tcp:5432`, and ensure that the postgres `COMMAND` appears.
   This checks if the Postgres server is now running on port 5432 under the name `localhost:postgresql`

#### Linux

1) Acquire the source code: `wget ftp://ftp.postgresql.org/pub/source/v9.3.2/postgresql-9.3.2.tar.bz2`
2) Install the packages needed for building Postgres:
   `sudo apt-get install build-essential libreadline-dev zlib1g-dev flex bison libxml2-dev libxslt-dev libssl-dev`

#### Windows

1) Download the installer specified by EnterpriseDB for all supported PostgreSQL versions. The installer is available here:
  `https://www.postgresql.org/download/windows/`

## Database Configuration

Set variables accordingly in this file `./db/config.py`:

```python
DB_NAME = #dnd_v2
PASSWORD = #database password
HOST = #host
PORT = #port
```
