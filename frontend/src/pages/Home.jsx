import { useState, useEffect } from 'react';
import api from '../api';
import Note from '../components/Note';
import '../styles/Home.css';

export default function Home() {
    // Set the initial state of the notes and the content and title of the note
    const [notes, setNotes] = useState([]);
    const [content, setContent] = useState('');
    const [title, setTitle] = useState('');

    // Get the notes from the API when the component mounts
    useEffect(() => {
        getNotes();
    }, []);

    // Get the notes from the API
    const getNotes = () => {
        api.get('/backend_api/notes/')
            .then((res) => res.data)
            .then((data) => {
                setNotes(data);
            })
            .catch((error) => alert(error));
    };

    // Delete a note by its ID
    const deleteNote = (id) => {
        // Send a request to the delete note endpoint with the note ID
        api.delete(`/backend_api/notes/delete/${id}/`)
            .then((res) => {
                if (res.status === 204) {
                    alert('Note was deleted!');
                } else {
                    alert('Failed to delete note!');
                }
                getNotes();
            })
            .catch((error) => alert(error));
    };

    // Create a note
    const createNote = (e) => {
        e.preventDefault();
        // Send a request to the create note endpoint with the content and title of the note
        api.post('backend_api/notes/', { content, title })
            .then((res) => {
                if (res.status === 201) {
                    alert('Note was created!');
                } else {
                    alert('Failed to create note!');
                }
                getNotes();
            })
            .catch((error) => alert(error));
    };

    return (
        <div>
            <div>
                <h2>Notes</h2>
                {notes.map((note) => (
                    <Note key={note.id} note={note} onDelete={deleteNote} />
                ))}
            </div>
            <h2>Create a Note</h2>
            <form onSubmit={createNote}>
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)}
                    value={title}
                />
                <label htmlFor="content">Content:</label>
                <br />
                <textarea
                    id="content"
                    name="content"
                    required
                    onChange={(e) => setContent(e.target.value)}
                    value={content}
                ></textarea>
                <br />
                <input type="submit" value="Submit"></input>
            </form>
        </div>
    );
}
