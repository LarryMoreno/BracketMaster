import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
// import TournamentPage from "./pages/TournamentPage";
// TODO: implement page for tournaments

// render the pages
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        {/* add this back when tournmanent page is done <Route path="/tournament/:id" element={<TournamentPage />} /> */}
      </Routes>
    </Router>
  );
}

export default App;