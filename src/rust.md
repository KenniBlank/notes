# Rust

```bash
rustup doc # Local Documentation
rustup update # update to the latest version
rustc --version # see the version of rust running
```

A Macro is a pre-defined sequence of automated input, designed to streamline repetitive tasks.
In Rustc:
- using a **"<u>!</u>"** means that you’re calling a macro instead of a normal function and that macros don’t always follow the same rules as functions.

## Cargo
Cargo is Rust’s build system and package manager.
- In Rust, libraries are called dependencies.
- All code must be in src folder.

Cargo Cheatsheet:
- Create Project
    ```bash
    cargo new folder_name
    # creates a new folder with cargo.toml and src which has main.rs file.
    # Also generates new git repository along with .gitignore file.

    # If a parent folder is git repo, it doesn't generate
    cargo new --vcs=git # this overrides that behavour

    cargo new --help # see availabe options
    ```

- Build Project and run execulable
    ```bash
    cargo build
    ./target/build/folder_name
    ```

- Build and run project in one step
    ```bash
    cargo run
    ```

- check for error without creating any binary
    ```bash
    cargo check # quickly checks code to make sure it compiles but doesn't produce executable
    ```

    > cargo stores build file in target/debug directory

- Building for release
    ```bash
    cargo build --release # compile with optimization
    # creates executable in target/release instead of target/debug
    ```


## Fun Part: Syntax and Learning
To obtain user input and print out as output, you must use **io** input/output library into scope.

**use std:io;**

By default, Rust has a set of items defined in the standard library that it brings into the scope of every program. This set is called the prelude. (See the Documentation)

- **Storing Values with Variables**
    ```rs
    // In Rust, variables are declared with let and they are immutable by default i.e values are constant
    let apples = 5;

    // To make a varible mutable, use mut
    let mut bananas = 5;

    use std::io;
    // Creates a mutable variable that is bound to a new, empty instance of String.
    let mut guess = String::new();

    ```

- ***crates.io* has the crates needed**
    - include the dependencies in the Cargo.toml file and it will auto download from the website. **Specify version**.
    - After downloading the dependencies, it compiles then and keeps them for further use afterwards.

- **Ensure Reproducible builds with Cargo.lock file**
    Cargo has a mechanism that ensures you can rebuild the same artifact every time you or anyone else builds your code: Cargo will use only the versions of the dependencies you specified until you indicate otherwise. For example, say that next week version 0.8.6 of the rand crate comes out, and that version contains an important bug fix, but it also contains a regression that will break your code. To handle this, Rust creates the Cargo.lock file the first time you run cargo build, so we now have this in the guessing_game directory.

- **Updating a crate to get New Version**
    ```bash
    cargo update # ignores cargo.lock and force updates with the specification in cargo.toml file.
    ```

- **See documentation of the dependencies locally**
    ```bash
    cargo doc --open # opens in the browser
    ```


## Variables:
Unless specified, all variables are immutable.

**mut**: makes variable mutable
```rs
let mut x = 5;
```

**const**: makes variable immutable forever.
```rs
const Y: u32 = 60;
// const variable_name: data_type = value;
```

> Why const and mut is different
```rs
let mut x = 3;
x = x + 1;
print!("Varible value change provides no error: {x}")

const Y: u32 = 60;
// You cannot change the set Value
```


- **Shadowing**
    We can shadow variable as:
    ```rs
    let x = 3;
    let x = x + 1; // this overshadows the value of previous declaration
    ```

- Data Types:
    Rust is a statically typed language (It must know data type of all variables at compile time).
    You will get an compilation error everytime compiler doesn't know datatype.

    - Scalar Types:
    A scalar type represents a single value. Rust has four primary scalar types:
        - integers
            ![alt text](image.png)
            > Each signed variant can store numbers from -(2<sup>n - 1</sup>) to 2<sup>n - 1</sup> - 1 inclusive.

            > The isize and usize types depend on the architecture of the computer your program is running on, which is denoted in the table as “arch”: 64 bits if you’re on a 64-bit architecture and 32 bits if you’re on a 32-bit architecture.

        - floating-points
            All floating-point numbers are signed. There are f32 and f64 floating point number with f64 as defualt for modern operating system.
        - Booleans
            true or false
        - characters
            single quote must be used. Takes 4 byte

    - Basic Numeric Operations:
        ```rs
        fn main() {
            // addition
            let sum = 5 + 10;

            // subtraction
            let difference = 95.5 - 4.3;

            // multiplication
            let product = 4 * 30;

            // division
            let quotient = 56.7 / 32.2;
            let truncated = -5 / 3; // Results in -1

            // remainder
            let remainder = 43 % 5;
        }
        ```

    - Compound Types:
        Group multiple values into one type.
        - Tuples
            Tuples have fixed length: once declared, cannot grow or shrink in size.
            Tuples with no value have special name: unit;expressions implicitly return unit value if they don't return any other value.
            ```rs
            let tup = (500, 6.4, 1)
            // Optional method for explicit declaration method:
            // let tup: (i34, f64, u8) = (500, 6.4, 1)

            let (x, y, z) = tup;
            println!("The value of Y is: {y}");
            println!("The value is ({tup.0}, {tup.1}, {tup.2})");
            ```

        - Arrays
            Every element of an array must have the same type. Arrays in Rust have fixed length.
            ```rs
            let a = [1, 2, 3, 4, 5];
            let b = ["January", "February", "March"];
            ```
            Arrays are useful when you want your data allocated on the stack rather than heap or when you want fixed number of elements.
            A ***vector*** is a similar collection type provided by the standard library that is allowed to grow or shrink in size.
