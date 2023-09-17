import React, {useState} from 'react';

const GeneratePasswordFrom = () => {
    const [alphabet, setAlphabet] = useState("")
    const [length, setLength] = useState(1)
    const [password, setPassword] = useState("Password")

    function generatePass() {
        fetch('http://localhost:8080/api/generate',
            {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    length: length,
                    alphabet: alphabet
                })
            })
            .then((response) => setPassword(password))
            .then((response) => console.log(response))
            .catch((err) => console.log(err))
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
                <label title={length}>Введите длину: </label>
                <input
                    type="number"
                    defaultValue={1}
                    min={1}
                    onChange={event => setLength(event.target.value)}
                />

                <button onClick={generatePass}>Generate password</button>
                <div>
                    {"Your password: " + password}
                </div>
            </form>
        </div>
    );
};

export default GeneratePasswordFrom;
