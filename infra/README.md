# infra documentation



### Getting started

prerquists 

docker installed and nodejs installed



First make a folder called vars in the project folder
```shell
 cd lreplass
 mkdir vars
```

Create a .env file in vars folder with the following contents

```
  // vars/.env
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD='postgres'
  POSTGRES_SERVER=localhost
  POSTGRES_PORT=5432
  POSTGRES_DB=lreplass
```
After you have added the .env file to the vars folder run this comand in the project root folder.

```shell
docker compose --env-file="vars/.env" up -d
```
congratiulations you have now managed to setup the project locally 