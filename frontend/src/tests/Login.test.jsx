import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import axios from "axios";
import Login from "../pages/Login"
import '@testing-library/jest-dom'

// mock axios for api requests
jest.mock("axios");

describe("Login Component", () => {
  test("renders form correctly", () => {
    render(<Login />);

    expect(screen.getByPlaceholderText("Email")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("Password")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /login/i })).toBeInTheDocument();
  });

  test("updates input fields correctly", () => {
    render(<Login />);

    const emailInput = screen.getByPlaceholderText("Email");
    const passwordInput = screen.getByPlaceholderText("Password");

    fireEvent.change(emailInput, { target: { value: "test@example.com" } });
    fireEvent.change(passwordInput, { target: { value: "password123" } });

    expect(emailInput.value).toBe("test@example.com");
    expect(passwordInput.value).toBe("password123");
  });

  // ensure login is successful by rendering the component
  test("submits form and handles successful login", async () => {
    axios.post.mockResolvedValue({ data: { token: "mockToken123" } });
    Storage.prototype.setItem = jest.fn();

    render(<Login />);

    fireEvent.change(screen.getByPlaceholderText("Email"), { target: { value: "test@example.com" } });
    fireEvent.change(screen.getByPlaceholderText("Password"), { target: { value: "password123" } });

    fireEvent.click(screen.getByRole("button", { name: /login/i }));

    await waitFor(() => expect(screen.getByText("Login successful!")).toBeInTheDocument());
    expect(localStorage.setItem).toHaveBeenCalledWith("token", "mockToken123");
  });

  test("handles invalid login attempts", async () => {
    axios.post.mockRejectedValue(new Error("Invalid credentials"));

    render(<Login />);

    fireEvent.change(screen.getByPlaceholderText("Email"), { target: { value: "wrong@example.com" } });
    fireEvent.change(screen.getByPlaceholderText("Password"), { target: { value: "wrongpassword" } });

    fireEvent.click(screen.getByRole("button", { name: /login/i }));

    await waitFor(() => expect(screen.getByText("Invalid credentials.")).toBeInTheDocument());
  });
});
