import { useState } from "react";
import axios from "axios";

// create bracket page
const CreateBracket = () => {
  // state for the bracket info
  const [bracketName, setBracketName] = useState("");
  const [eventType, setEventType] = useState("");
  const [bracketType, setBracketType] = useState("");
  const [userID, setUserID] = useState("");

  // submitting the form
  const handleSubmit = async (e) => {
    e.preventDefault();

    const bracketData = {
      bracketName,
      eventType,
      bracketType,
      userID,
    };

    try {
      const response = await axios.post(
        "http://localhost:5000/api/brackets",
        bracketData
      );
      alert("Bracket created successfully!");
    } catch (error) {
      console.error("Error creating bracket:", error);
      alert("Failed to create bracket.");
    }
  };

  // TODO: double check if we should use dropdowns instead for certain fields like event type
  // and have options to select from (esports, college tournament, etc.)
  return (
    <div>
      <h2>Create a New Bracket</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Bracket Name"
          value={bracketName}
          onChange={(e) => setBracketName(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Event Type"
          value={eventType}
          onChange={(e) => setEventType(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Bracket Type"
          value={bracketType}
          onChange={(e) => setBracketType(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="User ID"
          value={userID}
          onChange={(e) => setUserID(e.target.value)}
          required
        />
        <button type="submit">Create Bracket</button>
      </form>
    </div>
  );
};

export default CreateBracket;
