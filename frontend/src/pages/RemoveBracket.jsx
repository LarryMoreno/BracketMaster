import { useState } from "react";
import axios from "axios";

// create bracket page
const RemoveBracket = () => {
  // state for the bracket info
  const [bracketID, setBracketID] = useState("");

  // submitting the form
  const handleSubmit = async (e) => {
    e.preventDefault();

    const bracketData = {
      bracketID
    };

    try {
      const response = await axios.post(
        "http://localhost:5000/api/remove-bracket",
        bracketData
      );
      alert("Bracket successfully removed!");
    } catch (error) {
      console.error("Error removing bracket:", error);
      alert("Failed to remove bracket.");
    }
  };

  return (
    <div>
      <h2>Remove a Bracket</h2>
      <form onSubmit={handleSubmit}>
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

export default RemoveBracket;
