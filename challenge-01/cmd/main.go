package main

import (
	"fmt"
	"log"

	"challenge-01/internal/services"
	"github.com/xuri/excelize/v2"
)

func main() {
	// Open the Excel file
	file, err := excelize.OpenFile("table_data.xlsx")
	if err != nil {
		log.Fatalf("Failed to open Excel file: %v", err)
	}

	// Read employee and device data
	employees, err := services.ReadEmployees(file)
	if err != nil {
		log.Fatalf("Failed to read employees: %v", err)
	}

	// Read device data
	devices, err := services.ReadDevices(file)
	if err != nil {
		log.Fatalf("Failed to read devices: %v", err)
	}

	// Find employees without devices
	employeesWithoutDevices := services.FindMissingDevices(employees, devices)

	// Print employees without a device
	fmt.Println("Employees without a device record:")
	for _, employee := range employeesWithoutDevices {
		fmt.Printf("%s %s\n", employee.FirstName, employee.LastName)
	}
}