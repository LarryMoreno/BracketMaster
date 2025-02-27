import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import RegisterForm from "./pages/RegisterForm";
import Login from "./pages/Login";
import BracketManager from "./pages/CreateBracket";

// render the pages
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/registration" element={<RegisterForm />} />
        <Route path="/login" element={<Login />} />
        <Route path="/bracket" element={<BracketManager />} />
      </Routes>
    </Router>
  );
}

export default App;
