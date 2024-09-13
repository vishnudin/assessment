# Use the official Golang image to build Go App
FROM golang:1.23 AS builder

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy the files

COPY .  /app

# Download the dependencies

RUN go mod download 

RUN go build -o server


# Copy environment-specific files
COPY file-dev.txt .
COPY file-prod.txt .

# Command to run the executable
ENTRYPOINT ["./server"]

# Expose port (if needed)
EXPOSE 8080
