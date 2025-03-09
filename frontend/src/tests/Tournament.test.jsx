import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import '@testing-library/jest-dom'
import axios from "axios";
import Tournament from "../pages/Tournament";

jest.mock("axios");

beforeAll(() => {
  window.alert = jest.fn();
});

describe("Tournament Component", () => {
  test("renders correctly", () => {
    render(
      <MemoryRouter>
        <Tournament />
      </MemoryRouter>
    );

    expect(screen.getByRole("heading", { name: /find tournament/i })).toBeInTheDocument();
    expect(screen.getByPlaceholderText("Bracket ID")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /find tournament/i })).toBeInTheDocument();
  });

  test("allows user to type a Bracket ID", () => {
    render(
      <MemoryRouter>
        <Tournament />
      </MemoryRouter>
    );

    const input = screen.getByPlaceholderText("Bracket ID");
    fireEvent.change(input, { target: { value: "12345" } });

    expect(input.value).toBe("12345");
  });

  test("submits the form successfully", async () => {
    axios.post.mockResolvedValue({ data: {} });

    render(
      <MemoryRouter>
        <Tournament />
      </MemoryRouter>
    );

    const input = screen.getByPlaceholderText("Bracket ID");
    const button = screen.getByRole("button", { name: /find tournament/i });

    fireEvent.change(input, { target: { value: "12345" } });
    fireEvent.click(button);

    await waitFor(() => {
      expect(axios.post).toHaveBeenCalledWith("http://localhost:5000/tournament", {
        bracketID: "12345",
      });
      expect(window.alert).toHaveBeenCalledWith("Tournament Found");
    });
  });

  test("handles API error correctly", async () => {
    axios.post.mockRejectedValue(new Error("Failed to find Tournament"));

    render(
      <MemoryRouter>
        <Tournament />
      </MemoryRouter>
    );

    const input = screen.getByPlaceholderText("Bracket ID");
    const button = screen.getByRole("button", { name: /find tournament/i });

    fireEvent.change(input, { target: { value: "54321" } });
    fireEvent.click(button);

    await waitFor(() => {
      expect(window.alert).toHaveBeenCalledWith("Failed to find Tournament.");
    });
  });
});