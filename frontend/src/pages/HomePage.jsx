import { Link } from "react-router-dom";

// TODO: fix styling w/ tailwind css

//Home page for bracket master
const HomePage = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-4xl font-bold mb-6">🏆 Bracket Master</h1>
      <p className="text-lg text-gray-700 mb-8">Create and manage tournament brackets easily.</p>

      <div className="flex gap-4">
        <Link to="/tournament/new" className="px-6 py-3 bg-blue-500 text-white rounded-lg shadow-md hover:bg-blue-600">
          Create Tournament
        </Link>
        <Link to="/tournaments" className="px-6 py-3 bg-gray-500 text-white rounded-lg shadow-md hover:bg-gray-600">
          View Tournaments
        </Link>
      </div>
    </div>
  );
};

export default HomePage;