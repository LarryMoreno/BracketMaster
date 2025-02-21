import React from 'react';
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import RegisterForm from "../pages/RegisterForm.jsx";

// Mock global alert and fetch
global.alert = jest.fn();
global.fetch = jest.fn();

describe("RegisterForm", () => {
  beforeEach(() => {
    // Clear previous calls to alert and fetch before each test
    global.alert.mockClear();
    global.fetch.mockClear();
  });

  test("should render the form correctly", () => {
    render(<RegisterForm />);

    // Check if the form elements are rendered
    expect(screen.getByPlaceholderText("Username")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("Password")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("Email")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Register" })).toBeInTheDocument();
  });

  test("should show an alert when fields are missing", async () => {
    render(<RegisterForm />);

    // Submit the form without filling any fields
    fireEvent.click(screen.getByRole("button", { name: "Register" }));

    // Expect alert to be called
    expect(global.alert).toHaveBeenCalledWith("Please fill in all the fields.");
  });

  test("should submit the form successfully with valid data", async () => {
    // Mock the fetch response
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ message: "User registered successfully!" }),
    });

    render(<RegisterForm />);

    // Fill in the form fields
    fireEvent.change(screen.getByPlaceholderText("Username"), {
      target: { value: "testuser" },
    });
    fireEvent.change(screen.getByPlaceholderText("Password"), {
      target: { value: "password123" },
    });
    fireEvent.change(screen.getByPlaceholderText("Email"), {
      target: { value: "testuser@example.com" },
    });

    // Submit the form
    fireEvent.click(screen.getByRole("button", { name: "Register" }));

    // Wait for the fetch to complete and expect the alert to be called with the success message
    await waitFor(() => expect(global.alert).toHaveBeenCalledWith("User registered successfully!"));

    // Check that the form fields have been cleared after successful submission
    expect(screen.getByPlaceholderText("Username").value).toBe("");
    expect(screen.getByPlaceholderText("Password").value).toBe("");
    expect(screen.getByPlaceholderText("Email").value).toBe("");
  });

  test("should show an error message if registration fails", async () => {
    // Mock the fetch response with an error
    global.fetch.mockResolvedValueOnce({
      ok: false,
      json: async () => ({ error: "Username already exists" }),
    });

    render(<RegisterForm />);

    // Fill in the form fields
    fireEvent.change(screen.getByPlaceholderText("Username"), {
      target: { value: "testuser" },
    });
    fireEvent.change(screen.getByPlaceholderText("Password"), {
      target: { value: "password123" },
    });
    fireEvent.change(screen.getByPlaceholderText("Email"), {
      target: { value: "testuser@example.com" },
    });

    // Submit the form
    fireEvent.click(screen.getByRole("button", { name: "Register" }));

    // Wait for the fetch to complete and expect the alert to show the error message
    await waitFor(() => expect(global.alert).toHaveBeenCalledWith("Error: Username already exists"));
  });

  test("should catch errors during fetch", async () => {
    // Mock the fetch to throw an error
    global.fetch.mockRejectedValueOnce(new Error("Network error"));

    render(<RegisterForm />);

    // Fill in the form fields
    fireEvent.change(screen.getByPlaceholderText("Username"), {
      target: { value: "testuser" },
    });
    fireEvent.change(screen.getByPlaceholderText("Password"), {
      target: { value: "password123" },
    });
    fireEvent.change(screen.getByPlaceholderText("Email"), {
      target: { value: "testuser@example.com" },
    });

    // Submit the form
    fireEvent.click(screen.getByRole("button", { name: "Register" }));

    // Wait for the fetch to complete and expect the alert to show the error message
    await waitFor(() => expect(global.alert).toHaveBeenCalledWith("There was an error with the registration. Please try again."));
  });
});
