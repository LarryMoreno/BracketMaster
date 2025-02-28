import { render, screen } from "@testing-library/react";
import { BrowserRouter as Router } from "react-router-dom";
import HomePage from "../pages/HomePage";
import '@testing-library/jest-dom';

describe("HomePage Component", () => {
  // Test to check if the HomePage renders correctly
  test("renders the homepage with title, description, and navigation buttons", () => {
    render(
      <Router>
        <HomePage />
      </Router>
    );

    // Check if the title is rendered
    expect(screen.getByText("🏆 Bracket Master")).toBeInTheDocument();

    // Check if the description is rendered
    expect(screen.getByText("Create and manage tournament brackets easily.")).toBeInTheDocument();

    // Check if all navigation buttons are rendered
    expect(screen.getByRole("link", { name: /Create Tournament/i })).toBeInTheDocument();
    expect(screen.getByRole("link", { name: /Login/i })).toBeInTheDocument();
    expect(screen.getByRole("link", { name: /Registration/i })).toBeInTheDocument();
    expect(screen.getByRole("link", { name: /Bracket/i })).toBeInTheDocument();
  });

  // Test to check if the navigation links have the correct routes
  test("navigation links have the correct href attributes", () => {
    render(
      <Router>
        <HomePage />
      </Router>
    );

    // Check the "Create Tournament" link
    const createTournamentLink = screen.getByRole("link", { name: /Create Tournament/i });
    expect(createTournamentLink).toHaveAttribute("href", "/tournament/new");

    // Check the "Login" link
    const loginLink = screen.getByRole("link", { name: /Login/i });
    expect(loginLink).toHaveAttribute("href", "/login");

    // Check the "Registration" link
    const registrationLink = screen.getByRole("link", { name: /Registration/i });
    expect(registrationLink).toHaveAttribute("href", "/registration");

    // Check the "Bracket" link
    const bracketLink = screen.getByRole("link", { name: /Bracket/i });
    expect(bracketLink).toHaveAttribute("href", "/bracket");
  });
});