# Show Catalog

Make migrations 
```
python3 manage.py makemigrations
```

Migrate change to the database
```
python3 manage.py migrate
```

Start the docker containers with this command
```
./docker-start.sh
```
OR
```
docker compose --env-file ./logger/.env --env-file ./app/.env up -d
```

Connect to PSQL as root
```
sudo psql -U root -h 127.0.0.1 -d postgres
```

Connect to MongoDB via MongoDB Compass
```
mongodb://${MONGODB_USERNAME}:${MONGODB_PASSWORD}@localhost:27017/
```

## App APIs
[App APIs](./docs/app_api.md)

