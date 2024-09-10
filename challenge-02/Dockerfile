FROM golang:1.22.2-alpine as build

WORKDIR /app

COPY golang/go.* golang/*.go ./
RUN go build -v -o server .

FROM alpine:latest
RUN apk --no-cache add ca-certificates libc6-compat

WORKDIR /app/

COPY --from=build /app/server .
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

EXPOSE 8080
CMD ["/app/start.sh"]