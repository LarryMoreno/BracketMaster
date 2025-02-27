import { render, screen, fireEvent } from "@testing-library/react";
import '@testing-library/jest-dom'
import CreateBracket from "../pages/CreateBracket";

// mock axios for requests
jest.mock("axios");
global.alert = jest.fn();

describe("CreateBracket Component", () => {

  // check if the html elements are rendering properly on the page
  test("renders form correctly", () => {
    render(<CreateBracket />);

    expect(screen.getByPlaceholderText("Bracket Name")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("Event Type")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("Bracket Type")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("User ID")).toBeInTheDocument();
    expect(
      screen.getByRole("button", { name: /create bracket/i })
    ).toBeInTheDocument();
  });  
  
  // tests input field functionality w/ test data
  test("updates input fields correctly", () => {
    render(<CreateBracket />);

    const bracketNameInput = screen.getByPlaceholderText("Bracket Name");
    const eventTypeInput = screen.getByPlaceholderText("Event Type");
    const bracketTypeInput = screen.getByPlaceholderText("Bracket Type");
    const userIDInput = screen.getByPlaceholderText("User ID");

    fireEvent.change(bracketNameInput, { target: { value: "Test Bracket" } });
    fireEvent.change(eventTypeInput, { target: { value: "Esports" } });
    fireEvent.change(bracketTypeInput, {
      target: { value: "Single Elimination" },
    });
    fireEvent.change(userIDInput, { target: { value: "user123" } });

    expect(bracketNameInput.value).toBe("Test Bracket");
    expect(eventTypeInput.value).toBe("Esports");
    expect(bracketTypeInput.value).toBe("Single Elimination");
    expect(userIDInput.value).toBe("user123");
  });
});
