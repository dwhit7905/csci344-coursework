let canvasWidth = window.innerWidth;
let canvasHeight = window.innerHeight;

// in p5.js, the function runs on page load:
function setup() {
    createCanvas(canvasWidth, canvasHeight);

    // invoke any drawing functions inside of setup.
    // functions should all go between "createCanvas()" and "drawGrid()"
    draw5Circles();
    draw5RedSquares();
    drawGrid(canvasWidth, canvasHeight);
    draw5CirclesFor();
    draw5CirclesWhile();
    drawNCircles(5);
    drawNCirclesFlexible(5, 100, 600, 200);
    drawNShapesFlexible(5, 77, 707, 207, "square")
    drawNShapesDirectionFlexible(5, 27, 807, 207, "square", "row")
}

// my first function
function draw5Circles() {
    noFill();
    // fill('red');

    let x = 100;
    let y = 200;
    let d = 50;

    let i = 0;
    while (i < 5 ) {
    circle(x, y + 50 * i , d ); 
    // circle(x, y + 10 * i , d + 10 * i); 

    i++;
    }
    // circle(100, 250, 50);
    // circle(100, 300, 50);
    // circle(100, 350, 50);
    // circle(100, 400, 50);
    
}

function draw5RedSquares() {
    fill("red");
    square(320, 200, 50); // topLeftX, topLeftY, width
    square(320, 250, 50);
    square(320, 300, 50);
    square(320, 350, 50);
    square(320, 400, 50);
}

function draw5CirclesWhile() {
    noFill();
    let count = 0; 
    let x = 200;
    let y = 200;
    let diameter = 50;
    let spacing = 50;

    while (count < 5) {
        circle(x, y, diameter);
        y += spacing;
        count++;
    }
}

function draw5CirclesFor () {
    noFill();
    let x = 400;
    let y = 200;
    let diameter = 50;
    let spacing = 50;

    for (let i = 0; i < 5; i++) {
        circle(x, y, diameter);
        y += spacing;

    }
}

function drawNCircles(n) {
    noFill();
    let x = 500;
    let y = 200;
    let diameter = 25;
    let spacing = 25;

     for (let i = 0; i < n; i++) {
        circle(x, y, diameter);
        y += spacing;
     }
}

function drawNCirclesFlexible(n, size, x, y) {
    noFill();
    let spacing = size;
     for (let i = 0; i < n; i++) {
        circle(x, y, size);
        y += spacing;
    }
}

function drawNShapesFlexible(n, size, x, y, shape) {
    fill("purple");
    let spacing = size;
     for (let i = 0; i < n; i++) {
        if (shape === "circle") {
            circle(x, y, size);
        } else {
            square(x, y, size);
        }
        y += spacing;
    }
}

function drawNShapesDirectionFlexible(n, size, x, y, shape, direction) {
    fill("green");
    let spacing = size;
     for (let i = 0; i < n; i++) {
        if (direction === "column") {
            y += spacing;
        } else {
            x += spacing;
        }

        if (shape === "circle") {
            circle(x, y, size);
        } else {
            square(x, y, size);
        }
    }
}