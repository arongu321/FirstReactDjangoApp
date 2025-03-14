import React from 'react';
import api from '../api';
import { useNavigate } from 'react-router-dom';
import { ACCESS_TOKEN, REFRESH_TOKEN } from '../constants';
import '../styles/Form.css';
import LoadingIndicator from './LoadingIndicator';

export default function Form({ route, method }) {
    // Set the initial state of the username and password.
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');

    // Set the initial state of the loading state.
    const [loading, setLoading] = React.useState(false);

    // Get the navigate function from the useNavigate hook.
    const navigate = useNavigate();

    const name = method === 'login' ? 'Login' : 'Register';

    // Handle the form submission.
    const handleSubmit = async (e) => {
        setLoading(true);
        e.preventDefault();

        try {
            // Send a request to the login or register endpoint with the username and password.
            const res = await api.post(route, {
                username,
                password,
            });

            if (method == 'login') {
                // If the request is successful for login, save the access and refresh tokens in the local storage and navigate to the home page.
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
                navigate('/');
            } else {
                // If the request is successful for registration, navigate to the login page.
                navigate('/login');
            }
        } catch (error) {
            // If the request fails, show an alert with the error message.
            alert(error);
        } finally {
            // Set the loading state to false.
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>{name}</h1>
            <input
                type="text"
                className="form-input"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="username"
            />
            <input
                type="password"
                className="form-input"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="password"
            />
            {loading && <LoadingIndicator />}
            <button type="submit" className="form-button">
                {name}
            </button>
        </form>
    );
}
