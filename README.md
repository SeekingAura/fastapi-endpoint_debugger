# Fast api endpoint Debugger 


# Run debugger with reverse proxy to local machine
## Fast api run locally
uvicorn fastapi-endpoint_debugger.app:app --reload --host 0.0.0.0 --port 3000

## ngrok
ngrok http 3000

## nginx
at nginx conf that are *proxy/vol-template* just copy and create *proxy/vol* this will used for docker-compose.yaml

once folder *proxy/vol* is created run service with

```
docker compose --file=./docker/nginx/docker-compose.yaml up --detach=true
```
