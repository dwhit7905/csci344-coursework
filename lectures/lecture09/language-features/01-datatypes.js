// Data Type Demo 1: use typeof to find out what type you have
// copy this code and run it in your browser console:
printHeading("Data Type Demo 1: typeof");
console.log(typeof "hello world!");
console.log(typeof true);
console.log(typeof false);
console.log(typeof null); // this one's weird (longer discussion here (only if you're curious): https://stackoverflow.com/questions/18808226/why-is-typeof-null-object)
console.log(typeof undefined);
console.log(typeof 23.4);
console.log(typeof 4500);
console.log(typeof [1, 3, 4, 6]);
console.log(typeof { name: "Lester", species: "dog", age: 15 });

// Data Type Demo 2: converting between types:
// String(), Number(), Boolean()

printHeading("Data Type Demo 2: converting between types");
console.log(123, typeof 123, String(123), typeof String(123));
console.log("123", typeof "123", Number("123"), typeof Number("123"));
console.log("true", typeof "true", Boolean("true"), typeof Boolean("true"));

// Data Types Demo 3: Examples of Objects

printHeading("Object Demo 1");

const person = {
    firstName: "John",
    lastName: "Doe",
    age: 50,
    getFullName: function () {
        return this.firstName + " " + this.lastName;
    },
    printGreeting: function () {
        // another way to add methods to a function:
        console.log("Hello", this.getFullName() + "!");
    },
};

console.log(person.getFullName(), person.age);
person.printGreeting();
console.log(typeof person);

// Data Types Demo 4: Examples of Objects
printHeading("Object Demo 2");

class Person {
    constructor(firstName, lastName, age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    getFullName = function () {
        return this.firstName + " " + this.lastName;
    };

    printGreeting() {
        // another way to add methods to a function:
        console.log("Hello", this.getFullName() + "!");
    }
}

const charles = new Person("Charles", "Johnson", 35);
const juana = new Person("Juana", "Muñoz", 61);
console.log(juana.getFullName(), juana.age);
juana.printGreeting();
console.log(charles.getFullName(), charles.age);
charles.printGreeting();

// helper function:
function printHeading(message) {
    console.log("\n");
    console.log(Array(60).join("*"));
    console.log(message);
    console.log(Array(60).join("*"));
}
