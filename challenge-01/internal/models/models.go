package models

// Employee struct to represent employee data
type Employee struct {
	ID           string
	FirstName    string
	LastName     string
	Department   string
	Location     string
	EmployeeType string
}

// Device struct to represent device data
type Device struct {
	ID         string
	Type       string
	Make       string
	Model      string
	RAM        string
	Disk       string
	EmployeeID string
}