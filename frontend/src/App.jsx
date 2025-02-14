import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import RegisterForm from "./pages/RegisterForm"
// import TournamentPage from "./pages/TournamentPage";
// TODO: implement page for tournaments

// render the pages
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/registration" element={<RegisterForm />} />
        {/* add this back when tournmanent page is done <Route path="/tournament/:id" element={<TournamentPage />} /> */}
      </Routes>
    </Router>
  );
}

export default App;