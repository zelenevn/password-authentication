import React, {useState} from 'react';
import Diagram from "../diagramm/Diagram";

const GeneratePasswordForm = () => {
    const [alphabet, setAlphabet] = useState("abcdefg")
    const [length, setLength] = useState(8)
    const [password, setPassword] = useState("Password")

    async function generatePass(e) {
        e.preventDefault();
        const data = {length: length, alphabet: alphabet.split('')}

        await fetch('http://localhost:8080/api/generate', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            .then(res => res.json())
            .then(res => res.join(''))
            .then(pass => setPassword(pass));
    }

    return (
        <div>
            <form>
                <label>Введите алфавит: </label>
                <input
                    type="text"
                    value={alphabet}
                    onChange={event => setAlphabet(event.target.value)}
                />
                <label>Введите длину: </label>
                <input
                    type="number"
                    min={8}
                    max={1000}
                    value={length}
                    onChange={event => setLength(parseInt(event.target.value))}
                />

                <button onClick={generatePass}>Generate password</button>
                <div>
                    Your password: {password}
                </div>
            </form>
            <Diagram password={password}/>
        </div>
    );
};

export default GeneratePasswordForm;
