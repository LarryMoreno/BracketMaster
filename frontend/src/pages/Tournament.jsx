import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

// create bracket page
const Tournament = () => {
  // state for the bracket info
  const [bracketID, setBracketID] = useState("");
  const navigate = useNavigate();

  // submitting the form
  const handleSubmit = async (e) => {
    e.preventDefault();

    const TournamentData = {
      bracketID
    };

    try {
      const response = await axios.post(
        "http://localhost:5000/tournament",
        TournamentData
      );
      alert("Tournament Found");
      navigate(`/preview-tournament/${bracketID}`);

    } catch (error) {
      console.error("Error finding Tournament:", error);
      alert("Failed to find Tournament.");
    }
  };

  return (
    <div>
        <h2>Find Tournament</h2>
        <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Bracket ID"
          value={bracketID}
          onChange={(e) => setBracketID(e.target.value)}
          required
        />
        <button type="submit">Find Tournament</button>
      </form>
    </div>
  );
};

export default Tournament;
