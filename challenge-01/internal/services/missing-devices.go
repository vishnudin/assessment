package services

import (
	"challenge-01/internal/models"
	"github.com/xuri/excelize/v2"
)

// ReadEmployees extracts employee data from the Excel file
func ReadEmployees(file *excelize.File) ([]models.Employee, error) {
	rows, err := file.GetRows("Employees")
	if err != nil {
		return nil, err
	}

	var employees []models.Employee
	for _, row := range rows[1:] {
		employee := models.Employee{
			ID:           row[0],
			FirstName:    row[1],
			LastName:     row[2],
			Department:   row[3],
			Location:     row[4],
			EmployeeType: row[5],
		}
		employees = append(employees, employee)
	}

	return employees, nil
}

// ReadDevices extracts device data from the Excel file
func ReadDevices(file *excelize.File) ([]models.Device, error) {
	rows, err := file.GetRows("Devices")
	if err != nil {
		return nil, err
	}

	var devices []models.Device
	for _, row := range rows[1:] {
		device := models.Device{
			ID:         row[0],
			Type:       row[1],
			Make:       row[2],
			Model:      row[3],
			RAM:        row[4],
			Disk:       row[5],
			EmployeeID: row[6],
		}
		devices = append(devices, device)
	}

	return devices, nil
}

// FindMissingDevices returns a list of employees who don't have a device record
func FindMissingDevices(employees []models.Employee, devices []models.Device) []models.Employee {
	deviceMap := make(map[string]bool)

	// Create a map with EmployeeID as key
	for _, device := range devices {
		deviceMap[device.EmployeeID] = true
	}

	// Find employees without a device record
	var missingDevices []models.Employee
	for _, employee := range employees {
		if _, found := deviceMap[employee.ID]; !found {
			missingDevices = append(missingDevices, employee)
		}
	}

	return missingDevices
}