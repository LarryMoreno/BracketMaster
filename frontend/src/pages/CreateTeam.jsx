import { useState } from "react";
import axios from "axios";

// create team page
const CreateTeam = () => {
  // state for the team info
  const [teamName, setTeamName] = useState("");
  const [teamPlayerCount, setTeamPlayerCount] = useState("");
  const [teamLocation, setTeamLocation] = useState("");
  const [teamLeader, setTeamLeader] = useState("");
  const [bracketID, setBracketID] = useState("");

  // submitting the form
  const handleSubmit = async (e) => {
    e.preventDefault();

    const teamData = {
        teamName,
        teamPlayerCount,
        teamLocation,
        teamLeader,
        bracketID, 
    };

    try {
      const response = await axios.post(
        "http://localhost:5000/api/create-team",
        teamData
      );
      alert("Team successfuly created and added to bracket");
    } catch (error) {
      console.error("Error creating team:", error);
      alert("Failed to create team.");
    }
  };

  return (
    <div>
      <h2>Create a New Team</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Team Name"
          value={teamName}
          onChange={(e) => setTeamName(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Team Player Count"
          value={teamPlayerCount}
          onChange={(e) => setTeamPlayerCount(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Team Location"
          value={teamLocation}
          onChange={(e) => setTeamLocation(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Team Leader"
          value={teamLeader}
          onChange={(e) => setTeamLeader(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Bracket ID"
          value={bracketID}
          onChange={(e) => setBracketID(e.target.value)}
          required
        />
        <button type="submit">Create Team</button>
      </form>
    </div>
  );
};

export default CreateTeam;
