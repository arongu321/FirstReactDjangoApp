import { Navigate } from 'react-router-dom';
import { jwtDecode } from 'jwt-decode';
import api from '../api';
import { REFRESH_TOKEN, ACCESS_TOKEN } from '../constants';
import { useState, useEffect } from 'react';

export default function ProtectedRoute({ children }) {
    const [isAuthorized, setIsAuthorized] = useState(null);

    // Check if the user is authorized when the component mounts.
    useEffect(() => {
        auth().catch(() => setIsAuthorized(false));
    }, []);

    const refreshToken = async () => {
        // Get the refresh token from the local storage.
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);

        try {
            // Send a request to the refresh token endpoint with the refresh token.
            const res = await api.post('/backend_api/token/refresh/', {
                refresh: refreshToken,
            });

            // If the request is successful, save the new access token in the local storage and set the user as authorized.
            if (res.status === 200) {
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                setIsAuthorized(true);
            } else {
                // If the request fails, set the user as not authorized.
                setIsAuthorized(false);
            }
        } catch (error) {
            console.error(error);
            setIsAuthorized(false);
        }
    };

    const auth = async () => {
        // Check if the user is authorized by checking if the access token is present in the local storage.
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (!token) {
            // If the access token is not present, the user is not authorized.
            setIsAuthorized(false);
            return;
        }

        // Decode the access token to get the expiration date.
        const decoded = jwtDecode(token);
        const tokenExpiration = decoded.exp;
        const now = Date.now() / 1000;

        // If the access token has expired, refresh the token.
        if (tokenExpiration < now) {
            await refreshToken();
        } else {
            setIsAuthorized(true);
        }
    };

    if (isAuthorized == null) {
        return <div>Loading...</div>;
    }

    // If the user is authorized, render the children components, otherwise redirect to the login page.
    return isAuthorized ? children : <Navigate to="/login" />;
}
