# Using go base image
FROM golang:1.20-alpine

#Setting working directory inside container
WORKDIR /app

#Copying all files from host golang dir to current working directory inside container
COPY golang/*.go ./
COPY golang/file.txt ./
COPY golang/file-dev.txt ./
COPY golang/file-prod.txt ./

# Initialize Go module and tidy up dependencies
RUN go mod init web.com/app && go mod tidy

#Build Go application
RUN go build -o server .

#Expose port 8080 to check server output
EXPOSE 8080

#To run the server
ENTRYPOINT ["/bin/sh", "-c", "if [ \"$ENV\" = \"PROD\" ]; then cp file-prod.txt file.txt; elif [ \"$ENV\" = \"DEV\" ]; then cp file-dev.txt file.txt; fi && ./server"]