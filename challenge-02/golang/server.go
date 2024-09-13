package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func main() {
	// Get the ENVIRONMENT variable (default is PROD if not set)
	env := os.Getenv("ENVIRONMENT")
	if env == "DEV" {
             fileName = "file-dev.txt"
        } else {
             fileName = "file-prod.txt"
        }
	
	http.HandleFunc("/", FileHandler)

	fmt.Println("Server started, running 8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func FileHandler(w http.ResponseWriter, r *http.Request) {
	data, err := os.ReadFile(fileName) // Read the content of the selected file
	if err != nil {
		panic(err)
	}

	fmt.Fprintf(w, string(data))
}