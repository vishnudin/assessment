# Challenge-02: Golang Web Server Deployment

This project is a simple web server implemented in Golang. Based on the environment (DEV/PROD), it displays the content of a file as the homepage.

## Files:
- `golang/server.go`: Main Go server file.
- `golang/file-dev.txt`: Content for DEV environment.
- `golang/file-prod.txt`: Content for PROD environment.
- `Dockerfile`: Containerizes the Go app.
- `docker-compose.yml`: Orchestrates the deployment using Docker Compose.
- `start.sh`: startup script to be ran during container start.

## How to Build and Deploy

1. **Build the Docker Image:**
    ```bash
    docker-compose build
    ```

2. **Run the server**
    To run in DEV environment (default):
    ```bash
    docker-compose up
    ```

    To run in PROD environment:
    ```bash
    ENV=PROD docker-compose up
    ```

3. **Access the Server:**
    Open your browser and visit http://localhost:8080 to see the content.

## Further Improvements (Observability):

- Adding a logging framework like logrus to improve logging output.
- Adding Prometheus metrics or health checks using a package like promhttp to expose metrics.