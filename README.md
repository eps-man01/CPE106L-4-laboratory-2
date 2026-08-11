# CPE106L - Laboratory Activity 2: Strings, Lists, Tuples, and Dictionaries

An interactive Python command-line application simulating a North-South Commuter Railway (NSCR) ticket vending machine at Tutuban Station. This project demonstrates core CRUD operations using Python's fundamental data structures.

---

## Project Overview

The **NSCR Ticket Machine Simulator** allows passengers to select  destinations, choose train service tiers, purchase single-journey or stored-value tickets, search active bookings, revise details, and view service specifications.

NOTE: This program only covers the northbound stations of the mainline, with Tutuban Station as a starting point for the user. Furthermore, this is not 100% accurate to NSCR-related information as it is still under construction IRL (Expected completeion - 2032). Expect that the station names and codes, offerred train services, and other information are subject to change once the railway project is completed.

---

## Repository Structure

```text
.
├── README.md           # Project documentation and execution guide
├── src/
│   └── main.py         # Main interactive Python application       
└── screenshots/        # Execution outputs and program screenshots
```

---

## Program Features & Data Structures

- **Strings (`str`):** Handles passenger names, station titles, and input sanitization methods (`.strip()`, `.title()`).
- **Lists (`list`):** Stores ordered station listings (`STATIONS`) to enable numerical indexing without complex conditional branching.
- **Tuples (`tuple`):** Encapsulates immutable route pairs `("Tutuban", dest_name)` and static train service descriptions.
- **Dictionaries (`dict`):** Serves as the primary database (`tix`) mapping passenger names to their respective ticket details.

---

## Menu Operations

1. **Issue Ticket (Create):** Captures passenger details, destination selection, and service tier to generate a new record.
2. **Find Ticket (Read):** Searches the database by passenger name and displays formatted booking details.
3. **Edit Ticket (Update):** Allows users to revise ticket parameters by re-issuing booking details.
4. **Train Information (Display):** Outlines stop coverage, travel speeds, and fare tiers across Commuter, Commuter Express, and Airport Limited-Express services.

---

## Requirements & Environment Setup

### Prerequisites
- Python 3.10+
- Linux / WSL (Ubuntu)
- Visual Studio Code (VS Code)

---

## How to Run

Execute the main Python script from the root directory of the project:

```bash
python3 src/main.py
```
