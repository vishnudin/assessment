FROM golang:1.20 as builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o server server.go
# using a new stage from a minimal image
FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/server .
COPY file-dev.txt .
COPY file-prod.txt .
RUN chmod +x /app/server
EXPOSE 8080
CMD ["/app/server"]
