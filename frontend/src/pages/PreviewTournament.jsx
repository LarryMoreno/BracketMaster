import { useParams, Link } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";

const PreviewTournament = () => {
  const { bracketID } = useParams(); // Get the bracketID from the URL
  const [teams, setTeams] = useState([]); // State to hold team data

  // Fetch teams when the component mounts
  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/tournament/${bracketID}/teams`);
        setTeams(response.data.teams); // Store teams in state
      } catch (error) {
        console.error("Error fetching teams:", error);
      }
    };

    fetchTeams();
}, [bracketID]); // Re-run when bracketID changes

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">🏆 Tournament Preview</h1>
      <p className="text-lg text-gray-700 mb-6">Bracket ID: {bracketID}</p>
      
      <Link 
        to="/tournament"
        className="px-6 py-3 bg-gray-500 text-white rounded-lg shadow-md hover:bg-gray-600"
      >
        Back to Tournament Search
      </Link>
      <br/>
      <Link 
        to="/create-team"
        className="px-6 py-3 bg-gray-500 text-white rounded-lg shadow-md hover:bg-gray-600"
      >
        Back to Create Team
      </Link>
      <br/>
      <Link 
        to="/remove-team"
        className="px-6 py-3 bg-gray-500 text-white rounded-lg shadow-md hover:bg-gray-600"
      >
        Back to Remove Team
      </Link>

      <div className="w-1/4 bg-white shadow-md rounded-lg p-4 ml-6">
        <h2 className="text-xl font-bold mb-4">Teams in Bracket</h2>
        {teams.length > 0 ? (
          <ul>
            {teams.map((team, index) => (
              <li key={index} className="p-2 border-b">
                <p>Team Name:  {team.teamName} <br/> Location: {team.teamLocation}</p> 
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-500">No teams found.</p>
        )}
      </div>

    </div>
  );
};

export default PreviewTournament;
