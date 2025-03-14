import axios from 'axios';
import { ACCESS_TOKEN } from './constants';

// Create an axios instance and set the base URL to the API URL from the .env file.
const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
});

// Add an interceptor to the axios instance to add the Authorization header with the access token to each request.
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default api;
