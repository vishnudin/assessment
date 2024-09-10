package test

import (
	"challenge-01/internal/models"
	"challenge-01/internal/services"
	"testing"
)

func TestFindMissingDevices(t *testing.T) {
	employees := []models.Employee{
		{ID: "1", FirstName: "John", LastName: "Doe"},
		{ID: "2", FirstName: "Jane", LastName: "Doe"},
		{ID: "3", FirstName: "Jake", LastName: "Smith"},
	}

	devices := []models.Device{
		{EmployeeID: "1"},
		{EmployeeID: "3"},
	}

	expected := []models.Employee{
		{ID: "2", FirstName: "Jane", LastName: "Doe"},
	}

	result := services.FindMissingDevices(employees, devices)

	if len(result) != len(expected) {
		t.Errorf("expected %d employees, but got %d", len(expected), len(result))
	}

	for i := range result {
		if result[i].ID != expected[i].ID {
			t.Errorf("expected employee ID %s, but got %s", expected[i].ID, result[i].ID)
		}
	}
}