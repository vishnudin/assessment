# Challenge 01: Missing Devices Finder

This Go project finds employees who do not have a company-issued device recorded in the provided Excel file.

## Prerequisites

- Go 1.16 or higher
- `github.com/xuri/excelize/v2` package

## Incstructions

1. Install dependencies:

    ```bash
    go mod tidy
    ```

2. Build the program:

    ```bash
    go build cmd/main.go
    ```

2. Run the program:

    ```bash
    go run cmd/main.go
    ```

## Running Tests

1. Run the unit tests:

    ```bash
    go test ./test/...
    ```

## Project Structure

- `cmd/`: Contains the main entry point of the application.
- `internal/models/`: Defines the data models (`Employee`, `Device`).
- `internal/services/`: Contains the business logic for reading data and finding missing devices.
- `test/`: Contains unit tests for the business logic.