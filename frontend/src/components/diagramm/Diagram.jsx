import React, {useEffect, useState} from 'react';
import styles from './Diagram.css'
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
import {Bar} from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

export const options = {
    responsive: true,
    plugins: {
        legend: {
            position: 'top',
        },
        title: {
            display: true,
            text: 'График зависимости динамики ввода парольной фразы',
        },
    },
};


const Diagram = (props) => {
    const passStr = props.password
    const passArr = props.password.split('')

    const [labels, setLabels] = useState([])
    const [dataValues, setDataValues] = useState([])
    const [enterValueTime, setEnterValueTime] = useState([])
    const [inputPass, setInputPass] = useState("")
    const [data, setData] = useState({
        labels: labels,
        datasets: [
            {
                label: 'Интервалы времени между нажатиями соседних символов в парольной фразе',
                data: dataValues,
                backgroundColor: 'rgba(132, 0, 255, 1)',
            }
        ],
    })

    useEffect(() => {
        let newLabel = []
        let newDataValues = []
        for (let i = 0; i < passArr.length - 1; i++) {
            newLabel.push(passArr[i] + "-" + passArr[i + 1])
            newDataValues.push(0)
        }
        setLabels(newLabel)
        setDataValues(newDataValues)
        setInputPass("")
        setEnterValueTime([])
    }, [props.password])


    useEffect(() => {
        if (passStr.startsWith(inputPass) && inputPass.length > 0 && inputPass.length > enterValueTime.length) {
            setEnterValueTime([...enterValueTime, Date.now()])
        }
    }, [inputPass])

    useEffect(() => {
        if (enterValueTime.length > 0) {
            let index = inputPass.length - 1
            if (index > 0) {
                let curValues = [...dataValues]
                curValues[index - 1] = enterValueTime[index] - enterValueTime[index - 1]
                setDataValues(curValues)
            }
        }
    }, [enterValueTime])

    useEffect(() => {
        setData({
            labels: labels,
            datasets: [
                {
                    label: 'Интервалы времени между нажатиями соседних символов в парольной фразе',
                    data: dataValues,
                    backgroundColor: 'rgba(132, 0, 255, 1)',
                }
            ],
        })
    }, [labels, dataValues]);

    return <div>
        <div>Введите пароль:</div>
        <input
            type="text"
            value={inputPass}
            onChange={event => setInputPass(event.target.value)}
        />
        <Bar className={styles.diagram} options={options} data={data}/>
    </div>
};


export default Diagram;