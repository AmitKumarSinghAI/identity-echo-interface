# Identity Echo Interface

## MirAI School of Technology - Virtual Summer Internship 2026

### AI Builder Track - Assignment 1

This is my **first assignment** completed during the **Virtual Summer Internship 2026 at MirAI School of Technology** under the **"AI Builder" Track**.

The project is called **"The Identity Echo Interface"**. It is an interactive web application developed using **Streamlit** that collects user inputs, validates the data, and generates a personalized response.

---

## Project Overview

The Identity Echo Interface demonstrates the fundamentals of building interactive web applications using Streamlit.

The application allows users to:

* Enter their name
* Enter a message
* Submit information using the Transmit button
* Receive a personalized transmission response
* View estimated token usage based on message length

---

## Features

✅ Streamlit-based interactive user interface
✅ Name input field
✅ Message input field
✅ Button-controlled execution
✅ Input validation using Python conditional logic
✅ Error handling for missing name
✅ Warning handling for missing message
✅ Personalized success message using f-string
✅ Token cost estimation system

---

## Technologies Used

* Python
* Streamlit

---

## Project Structure

```
identity-echo-interface/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Required Python packages
└── README.md           # Project documentation
```

---

## Installation and Setup

### Clone the repository

```bash
git clone https://github.com/AmitKumarSinghAI/identity-echo-interface
```

### Move into the project directory

```bash
cd identity-echo-interface
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application locally

```bash
streamlit run app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

## Deployment

The application is deployed using **Streamlit Community Cloud**.

Live Demo:

```
https://identity-echo-interface-srsntvwrxjgqvfcbbry2dm.streamlit.app/
```


## How It Works

1. The user enters their name.
2. The user enters a message.
3. The user clicks the **Transmit** button.
4. The application checks the input:

   * If the name field is empty, an error message is displayed.
   * If the message field is empty, a warning message is displayed.
   * If both fields contain data, a successful transmission message is generated.
5. The application estimates token consumption using the message character length.

---

## Learning Outcomes

Through this assignment, I learned:

* How to build interactive applications using Streamlit.
* How to collect and process user inputs.
* How to implement conditional statements in Python.
* How to create simple frontend interfaces without traditional HTML and JavaScript.
* How to deploy a Streamlit application using Streamlit Community Cloud.

---

## Internship Information

**Organization:** MirAI School of Technology
**Program:** Virtual Summer Internship 2026
**Track:** AI Builder Track
**Assignment:** Assignment 1 - The Identity Echo Interface

---

## Author

**Amit Kumar Singh Kurmi**