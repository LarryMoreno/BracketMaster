import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import RegisterForm from "./pages/RegisterForm";
import Login from "./pages/Login";
import BracketManager from "./pages/CreateBracket";
import CreateTeamForm from "./pages/CreateTeam";
import RemoveBracketForm from "./pages/RemoveBracket";
import RemoveTeamForm from "./pages/RemoveTeam";
import TournamentForm from "./pages/Tournament";
import PreviewTournament from "./pages/PreviewTournament";

// render the pages
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/registration" element={<RegisterForm />} />
        <Route path="/login" element={<Login />} />
        <Route path="/bracket" element={<BracketManager />} />
        <Route path="/create-team" element={<CreateTeamForm />} />
        <Route path="/remove-bracket" element={<RemoveBracketForm />} />
        <Route path="/remove-team" element={<RemoveTeamForm />} />
        <Route path="/tournament" element={<TournamentForm />} />
        <Route path="/preview-tournament/:bracketID" element={<PreviewTournament />} />
      </Routes>
    </Router>
  );
}

export default App;
