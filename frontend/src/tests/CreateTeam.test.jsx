import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import CreateTeam from "../pages/CreateTeam";
import axios from "axios";

jest.mock("axios");

describe("CreateTeam Component", () => {
  test("updates input values on change", () => {
    render(<CreateTeam />);

    const teamNameInput = screen.getByPlaceholderText("Team Name");
    fireEvent.change(teamNameInput, { target: { value: "Warriors" } });
    expect(teamNameInput.value).toBe("Warriors");
  });

  test("submits the form successfully", async () => {
    axios.post.mockResolvedValue({ data: { message: "Team successfully created and added to bracket" } });
    window.alert = jest.fn();

    render(<CreateTeam />);

    fireEvent.change(screen.getByPlaceholderText("Team Name"), { target: { value: "Warriors" } });
    fireEvent.change(screen.getByPlaceholderText("Team Player Count"), { target: { value: "5" } });
    fireEvent.change(screen.getByPlaceholderText("Team Location"), { target: { value: "New York" } });
    fireEvent.change(screen.getByPlaceholderText("Team Leader"), { target: { value: "John Doe" } });
    fireEvent.change(screen.getByPlaceholderText("Bracket ID"), { target: { value: "12345" } });

    fireEvent.click(screen.getByText("Create Team"));

    await waitFor(() => expect(axios.post).toHaveBeenCalledTimes(1));
    expect(window.alert).toHaveBeenCalledWith("Team successfuly created and added to bracket");
  });

  test("shows error alert on failed request", async () => {
    axios.post.mockRejectedValue(new Error("Request failed"));
    window.alert = jest.fn();

    render(<CreateTeam />);

    fireEvent.change(screen.getByPlaceholderText("Team Name"), { target: { value: "Warriors" } });
    fireEvent.change(screen.getByPlaceholderText("Team Player Count"), { target: { value: "5" } });
    fireEvent.change(screen.getByPlaceholderText("Team Location"), { target: { value: "New York" } });
    fireEvent.change(screen.getByPlaceholderText("Team Leader"), { target: { value: "John Doe" } });
    fireEvent.change(screen.getByPlaceholderText("Bracket ID"), { target: { value: "12345" } });

    fireEvent.click(screen.getByText("Create Team"));

    await waitFor(() => expect(axios.post).toHaveBeenCalledTimes(2));
    expect(window.alert).toHaveBeenCalledWith("Failed to create team.");
  });
});
