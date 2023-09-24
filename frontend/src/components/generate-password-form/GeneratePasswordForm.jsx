import React, {useState} from 'react';

const GeneratePasswordForm = () => {
    const [alphabet, setAlphabet] = useState("abcd")
    const [length, setLength] = useState(1)
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
            .then(res => res.text())
            .then(pass=>setPassword(pass));
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
                    min={1}
                    value={length}
                    onChange={event => setLength(parseInt(event.target.value))}
                />

                <button onClick={generatePass}>Generate password</button>
                <div>
                    Your password: {password}
                </div>
            </form>
        </div>
    );
};

export default GeneratePasswordForm;
