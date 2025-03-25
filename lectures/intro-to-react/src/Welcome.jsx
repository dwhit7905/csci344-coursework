import React, {useState} from "react";
import "./Welcome.css";



export function Welcome({name, imgUrl}) {

    const [style, setStyle] = useState("card");
    const [times, setTimes] = useState(0);

    function toggleClass() {
        console.log("Change the card class !");
        if (style === "card") {
            setStyle("active-card");
        } else {
            setStyle("card");
        }
        setTimes(times + 1);
    }

    function addOne(ev) {
        setTimes(times + 1);
        ev.stopPropagation();
    }

    return <section className= "card" onClick={toggleClass}>

        <h2>Hello, {name} </h2>
        <img src={imgUrl} />
        <button onClick={addOne}>This has been clicked {times} times.</button>
    </section>
}