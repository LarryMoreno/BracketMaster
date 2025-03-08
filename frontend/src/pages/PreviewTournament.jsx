import { useParams, Link } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";

const PreviewTournament = () => {
  const { bracketID } = useParams(); // Get the bracketID from the URL
  const [teams, setTeams] = useState([]); // State to hold team data
  const [nextRound, setNextRound] = useState([]); // Store winners of each matchup
  const [matchupResults, setMatchupResults] = useState([]); // Track selected winners
  const [roundTitle, setRoundTitle] = useState("Bracket"); // Title for the current round

  // Fetch teams when the component mounts
  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/tournament/${bracketID}/teams`);
        setTeams(response.data.teams); // Store teams in state
        setNextRound([
          [response.data.teams[0], response.data.teams[7]],
          [response.data.teams[1], response.data.teams[6]],
          [response.data.teams[2], response.data.teams[5]],
          [response.data.teams[3], response.data.teams[4]],
        ]); // Initialize matchups
        setMatchupResults(new Array(4).fill([])); // Reset matchups
      } catch (error) {
        console.error("Error fetching teams:", error);
      }
    };

    fetchTeams();
  }, [bracketID]); // Re-run when bracketID changes

  // Handle winner selection
  const selectWinner = (team, matchupIndex) => {
    const updatedRound = [...nextRound];
    const updatedMatchups = [...matchupResults];

    updatedRound[matchupIndex] = [team]; // Store the winner in this round
    updatedMatchups[matchupIndex] = [team.teamName]; // Track selected winners
    setNextRound(updatedRound);
    setMatchupResults(updatedMatchups);
  };

  // Simulate the next round by moving winners forward
  const simulateNextRound = () => {
    if (nextRound.length === 1) {
      setRoundTitle("Champion 🏆");
      return; // Stop if only one team remains
    }

    const newMatchups = [];
    for (let i = 0; i < nextRound.length; i += 2) {
      if (nextRound[i] && nextRound[i + 1]) {
        newMatchups.push([nextRound[i][0], nextRound[i + 1][0]]);
      }
    }

    // Determine next round title
    const roundTitles = ["Bracket", "Second Round", "Finals", "Champion 🏆"];
    const currentRoundIndex = roundTitles.indexOf(roundTitle);
    const newRoundTitle = currentRoundIndex + 1 < roundTitles.length ? roundTitles[currentRoundIndex + 1] : "Champion 🏆";

    setNextRound(newMatchups);
    setMatchupResults(new Array(newMatchups.length).fill([])); // Reset matchups
    setRoundTitle(newRoundTitle);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">🏆 Tournament Preview</h1>
      <p className="text-lg text-gray-700 mb-6">Bracket ID: {bracketID}</p>

      <Link to="/tournament" className="px-6 py-3 bg-gray-500 text-white rounded-lg shadow-md hover:bg-gray-600">
        Back to Tournament Search
      </Link>
      <br />
      <Link to="/create-team" className="px-6 py-3 bg-gray-500 text-white rounded-lg shadow-md hover:bg-gray-600">
        Back to Create Team
      </Link>
      <br />
      <Link to="/remove-team" className="px-6 py-3 bg-gray-500 text-white rounded-lg shadow-md hover:bg-gray-600">
        Back to Remove Team
      </Link>

      {/* Bracket Section */}
      <div className="flex justify-center gap-12 mt-10">
        <div className="w-1/2">
          <h2 className="text-xl font-bold mb-4">{roundTitle}</h2>
          {nextRound.map((matchup, index) => (
            <div key={index} style={{ marginBottom: "20px", padding: "10px", border: "1px solid #ccc" }}>
              <div style={{ display: "flex", justifyContent: "space-between" }}>
                {matchup.map((team, teamIndex) => (
                  <div key={teamIndex}>
                    <p>{team?.teamName}</p>
                    {roundTitle !== "Champion 🏆" && (
                    <button
                      onClick={() => selectWinner(team, index)}
                      className="mt-2 px-4 py-2 bg-blue-500 text-white rounded-lg"
                      disabled={matchupResults[index].length > 0} // Disable if a winner is selected
                    >
                      Select Winner
                    </button>
                    )}
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Next Round Section */}
      {roundTitle !== "Champion 🏆" && (
      <div className="mt-8">
        <h3 className="text-xl font-bold">Next Round</h3>
        {nextRound.length > 1 &&
          nextRound.map((matchup, index) => (
            <div key={index}>
              <h4>Matchup {index + 1}</h4>
              <ul>
                {matchup.map((team, teamIndex) => (
                  <li key={teamIndex}>{team.teamName}</li>
                ))}
              </ul>
            </div>
          ))}
      </div>
    )}

    {/* Button to Simulate Next Round */}
    {roundTitle !== "Champion 🏆" && (
      <div className="mt-6">
        <button
          onClick={simulateNextRound}
          className="px-6 py-3 bg-green-500 text-white rounded-lg shadow-md hover:bg-green-600"
          disabled={nextRound.some(matchup => matchup.length !== 1)} // Disable until all winners are selected
        >
          Simulate Next Round
        </button>
      </div>

      
    )}
    </div>    
  );
}

export default PreviewTournament;