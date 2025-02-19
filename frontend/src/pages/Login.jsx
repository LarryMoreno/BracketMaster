import { useState } from "react";
import axios from "axios";

// basic login
const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
          // get the res from backend
            const response = await axios.post("http://127.0.0.1:5000/login", { email, password });
            localStorage.setItem("token", response.data.token);
            setMessage("Login successful!");
            console.log("login successfull!")
        } catch (error) {
            setMessage("Invalid credentials.");
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
                <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                <button type="submit">Login</button>
            </form>
            <p>{message}</p>
        </div>
    );
};

export default Login;
