// Your code here.

function toggleMenu() {
    const nav = document.querySelector(".nav-links");
    const button = document.querySelector(".menu-toggle");

    // nav.className = "nav-links active";

    nav.classList.toggle("active");
    button.classList.toggle("active");


    // if (nav.className === "nav-links active") {
    //     nav.className = "nav-links";
    // } else {
    //     nav.className
    // }
 }