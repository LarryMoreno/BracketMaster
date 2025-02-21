import React from "react";
import "@testing-library/jest-dom";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import RegisterForm from "../pages/RegisterForm.jsx";

global.alert = jest.fn();
global.fetch = jest.fn();

describe("RegisterForm", () => {
  beforeEach(() => {
    global.alert.mockClear();
    global.fetch.mockClear();
    global.alert = jest.fn();
  });

  test("should render the form correctly", () => {
    render(<RegisterForm />);

    expect(screen.getByPlaceholderText("Username")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("Password")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("Email")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Register" })).toBeInTheDocument();
  });

  test("should submit the form successfully with valid data", async () => {
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ message: "User registered successfully!" }),
    });

    render(<RegisterForm />);

    fireEvent.change(screen.getByPlaceholderText("Username"), {
      target: { value: "testuser" },
    });
    fireEvent.change(screen.getByPlaceholderText("Password"), {
      target: { value: "password123" },
    });
    fireEvent.change(screen.getByPlaceholderText("Email"), {
      target: { value: "testuser@example.com" },
    });

    fireEvent.click(screen.getByRole("button", { name: "Register" }));

    await waitFor(() => expect(global.alert).toHaveBeenCalledWith("User registered successfully!"));

    expect(screen.getByPlaceholderText("Username").value).toBe("");
    expect(screen.getByPlaceholderText("Password").value).toBe("");
    expect(screen.getByPlaceholderText("Email").value).toBe("");
  });

  test("should show an error message if registration fails", async () => {
    global.fetch.mockResolvedValueOnce({
      ok: false,
      json: async () => ({ error: "Username already exists" }),
    });

    render(<RegisterForm />);

    fireEvent.change(screen.getByPlaceholderText("Username"), {
      target: { value: "testuser" },
    });
    fireEvent.change(screen.getByPlaceholderText("Password"), {
      target: { value: "password123" },
    });
    fireEvent.change(screen.getByPlaceholderText("Email"), {
      target: { value: "testuser@example.com" },
    });

    fireEvent.click(screen.getByRole("button", { name: "Register" }));

    await waitFor(() => expect(global.alert).toHaveBeenCalledWith("Error: Username already exists"));
  });

  test("should catch errors during fetch", async () => {
    global.fetch.mockRejectedValueOnce(new Error("Network error"));

    render(<RegisterForm />);

    fireEvent.change(screen.getByPlaceholderText("Username"), {
      target: { value: "testuser" },
    });
    fireEvent.change(screen.getByPlaceholderText("Password"), {
      target: { value: "password123" },
    });
    fireEvent.change(screen.getByPlaceholderText("Email"), {
      target: { value: "testuser@example.com" },
    });

    fireEvent.click(screen.getByRole("button", { name: "Register" }));

    await waitFor(() => expect(global.alert).toHaveBeenCalledWith("There was an error with the registration. Please try again."));
  });
});
