# setup 
 some setup setps for the backend for local development



## Virtual Environment setup
```bash
python3 -m venv .venv
```
## Dependencys

install all the dependencys in your virtual environment
```bash
python3 -m pip install -r requirements.txt

```


## Secrets
  
run this command to geenerate the secretkey:

```bash
openssl rand -hex 32

```
 Insert the output from the comand above in the SECRET_KEY variable
```
  // .env
  SECRET_KEY="<Secret_key>"
  ALGORITHM = "HS256"
```
