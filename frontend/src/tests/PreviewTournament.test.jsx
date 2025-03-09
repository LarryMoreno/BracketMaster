import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import PreviewTournament from "../pages/PreviewTournament";
import '@testing-library/jest-dom'
import { BrowserRouter } from "react-router-dom";
import axios from "axios";

jest.mock("axios");

const mockTeams = {
  data: {
    teams: [
      { teamName: "Team A" },
      { teamName: "Team B" },
      { teamName: "Team C" },
      { teamName: "Team D" },
      { teamName: "Team E" },
      { teamName: "Team F" },
      { teamName: "Team G" },
      { teamName: "Team H" },
    ],
  },
};

describe("PreviewTournament Component", () => {
  beforeEach(() => {
    axios.get.mockResolvedValue(mockTeams);
  });

  test("renders tournament preview page", async () => {
    render(
      <BrowserRouter>
        <PreviewTournament />
      </BrowserRouter>
    );

    await waitFor(() => expect(screen.getByText("🏆 Tournament Preview")).toBeInTheDocument());
  });

  test("fetches and displays teams", async () => {
    render(
      <BrowserRouter>
        <PreviewTournament />
      </BrowserRouter>
    );

    await waitFor(() => expect(screen.getAllByText("Team A")[0]).toBeInTheDocument());
    await waitFor(() => expect(screen.getAllByText("Team H")[0]).toBeInTheDocument());
  });

  test("allows selecting a winner and updates state", async () => {
    render(
      <BrowserRouter>
        <PreviewTournament />
      </BrowserRouter>
    );

    await waitFor(() => expect(screen.getAllByText("Team A")[0]).toBeInTheDocument());
    
    const winnerButton = screen.getAllByRole("button", { name: "Select Winner" })[0];
    fireEvent.click(winnerButton);

    await waitFor(() => expect(screen.getByText("Next Round")).toBeInTheDocument());
  });
});