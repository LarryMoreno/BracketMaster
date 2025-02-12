import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
// import TournamentPage from "./pages/TournamentPage";
// TODO: implement page foe tournaments

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        {/* <Route path="/tournament/:id" element={<TournamentPage />} /> */}
      </Routes>
    </Router>
  );
}

export default App;