#!/bin/sh
echo "ENV: $ENV"
if [ "$ENV" = "PROD" ]; then
  [ -f /app/files/file-prod.txt ] && cp /app/files/file-prod.txt /app/file.txt
else
  [ -f /app/files/file-dev.txt ] && cp /app/files/file-dev.txt /app/file.txt
fi

echo "Starting server"
./server