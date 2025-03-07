import { useState } from "react";
import axios from "axios";

// create bracket page
const RemoveTeam = () => {
  // state for the bracket info
  const [teamID, setTeamID] = useState("");
  const [bracketID, setBracketID] = useState("");

  // submitting the form
  const handleSubmit = async (e) => {
    e.preventDefault();

    const removeTeamData = {
      teamID,
      bracketID
    };

    try {
      const response = await axios.post(
        "http://localhost:5000/api/remove-team",
        removeTeamData
      );
      alert("Team successfully removed from bracket!");
    } catch (error) {
      console.error("Error removing team from bracket:", error);
      alert("Failed to remove team from bracket.");
    }
  };

  return (
    <div>
      <h2>Remove Team from Bracket</h2>
      <form onSubmit={handleSubmit}>
      <input
          type="text"
          placeholder="Team ID"
          value={teamID}
          onChange={(e) => setTeamID(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Bracket ID"
          value={bracketID}
          onChange={(e) => setBracketID(e.target.value)}
          required
        />
        <button type="submit">Remove Bracket</button>
      </form>
    </div>
  );
};

export default RemoveTeam;
