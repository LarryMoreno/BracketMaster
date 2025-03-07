import { render, screen, fireEvent } from "@testing-library/react";
import axios from "axios";
import RemoveBracket from "../pages/RemoveBracket";

jest.mock("axios");

describe("RemoveBracket Component", () => {
  test("updates input field when typing", () => {
    render(<RemoveBracket />);
    const input = screen.getByPlaceholderText("Bracket ID");
    
    fireEvent.change(input, { target: { value: "12345" } });
    expect(input.value).toBe("12345");
  });

  test("submits form and handles success response", async () => {
    axios.post.mockResolvedValue({ data: { message: "Bracket successfully removed!" } });
    window.alert = jest.fn();
    
    render(<RemoveBracket />);
    const input = screen.getByPlaceholderText("Bracket ID");
    const button = screen.getByText("Remove Bracket");
    
    fireEvent.change(input, { target: { value: "12345" } });
    fireEvent.click(button);
    
    expect(axios.post).toHaveBeenCalledWith("http://localhost:5000/api/remove-bracket", { bracketID: "12345" });
    await new Promise((r) => setTimeout(r, 0));
    expect(window.alert).toHaveBeenCalledWith("Bracket successfully removed!");
  });

  test("handles error response correctly", async () => {
    axios.post.mockRejectedValue(new Error("Failed to remove bracket"));
    window.alert = jest.fn();
    
    render(<RemoveBracket />);
    const input = screen.getByPlaceholderText("Bracket ID");
    const button = screen.getByText("Remove Bracket");
    
    fireEvent.change(input, { target: { value: "12345" } });
    fireEvent.click(button);
    
    await new Promise((r) => setTimeout(r, 0));
    expect(window.alert).toHaveBeenCalledWith("Failed to remove bracket.");
  });
});
