#!/data/data/com.termux/files/usr/bin/python

# -*- coding: utf-8 -*-

import json
import os

# File paths for data storage
REFRIGERANTS_FILE = "refrigerants_gr.json"
BRANDS_FILE = "brands_gr.json"
ISSUES_FILE = "issues_gr.json"
PARTS_FILE = "parts_gr.json"
E_ERRORS_FILE = "e_errors_gr.json"

# Load data from JSON files or create default data
def load_data(file_path, default_data):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        with open(file_path, 'w') as file:
            json.dump(default_data, file, indent=4)
        return default_data

# Default data tailored for the Greek market
refrigerants_data = [
    {"type": "R410A", "hot_pressure": "250 psi", "cold_pressure": "120 psi"},
    {"type": "R32", "hot_pressure": "280 psi", "cold_pressure": "110 psi"},
    {"type": "R134a", "hot_pressure": "270 psi", "cold_pressure": "115 psi"},
    {"type": "R22", "hot_pressure": "240 psi", "cold_pressure": "125 psi"},
    {"type": "R407C", "hot_pressure": "260 psi", "cold_pressure": "118 psi"}
]

brands_data = {
    "top": [
        "Daikin", "Mitsubishi Electric", "Fujitsu", "LG", "Samsung",
        "Panasonic", "Carrier", "Trane", "Lennox", "Hitachi",
        "Sharp", "Toshiba", "Gree", "Electrolux", "Haier",
        "Sanyo", "Bryant", "American Standard", "York", "Maytag"
    ],
    "worst": [
        "Hisense", "TCL", "Kelvinator", "Whirlpool", "Rinnai",
        "Olsen", "General Electric", "Westinghouse", "Heil", "Bosch",
        "Amana", "Coleman", "Goodman", "Ducane", "Ruud",
        "Comfortmaker", "Janitrol", "Tempstar", "Payne", "Day & Night"
    ]
}

issues_data = [
    {"issue": "Air conditioner not cooling", 
     "solution": "Check the air filters. If they are dirty, clean or replace them. Dirty filters can block airflow, causing the system to work harder and reduce its efficiency. Regular maintenance includes changing filters every few months."},
    
    {"issue": "Air conditioner making noise", 
     "solution": "Inspect the fan blades and motor. Noises may come from loose components or debris caught in the fan. Tighten any loose screws and remove debris carefully. If the noise continues, consider lubricating or replacing the fan motor."},
    
    {"issue": "Air conditioner not turning on", 
     "solution": "Check the power supply. Look for tripped circuit breakers or blown fuses. Ensure the thermostat settings are correct. If it runs on batteries, replace them. Additionally, make sure the outdoor unit is clean and not blocked by debris."},
    
    {"issue": "Air conditioner leaking water", 
     "solution": "Clear any blocked drain pipes. Water leakage can occur from a clogged drain line or low refrigerant levels. Regular maintenance should include checking the drain line and clearing blockages as needed."},
    
    {"issue": "Air conditioner freezing up", 
     "solution": "Ensure proper airflow. Check that air vents are open and unobstructed. Clean or replace air filters to prevent ice formation on evaporator coils. If low refrigerant levels are suspected, contact a technician for a leak test and refill."},
    
    {"issue": "Air conditioner emitting bad smell", 
     "solution": "Clean or replace air filters. Inspect the drain pan for mold or algae growth. A bad smell often indicates mold buildup. Use a mixture of water and vinegar to clean the drain pan and coils if necessary."},
    
    {"issue": "Air conditioner not blowing air", 
     "solution": "Check the fan motor and capacitor. Ensure the thermostat is functioning correctly and set to a lower temperature than the ambient room temperature. Verify that the system is not in 'fan only' mode."},
    
    {"issue": "Air conditioner running but not cooling", 
     "solution": "Check refrigerant levels. Inspect for leaks, as low refrigerant can hinder the cooling process. Make sure the compressor is running and that no blockages are preventing airflow."},
    
    {"issue": "Air conditioner producing weak airflow", 
     "solution": "Clean air vents. Check for closed or blocked ducts. If the problem persists, the blower fan may be malfunctioning and should be inspected or replaced."},
    
    {"issue": "Air conditioner thermostat problems", 
     "solution": "Check for loose connections and recalibrate the thermostat if needed. Ensure that it is away from direct sunlight or drafts, which can lead to incorrect readings."},
    
    {"issue": "Air conditioner cycling on and off", 
     "solution": "Inspect the thermostat settings and the system's capacity. If the unit is too large for the space, it may cycle excessively. Consider having a professional assess the size and efficiency of your unit."},
    
    {"issue": "Air conditioner compressor not working", 
     "solution": "Check the compressor wiring and connections. Test the compressor to see if it is receiving power. If it is faulty, it will need to be replaced by a qualified technician."},
    
    {"issue": "Air conditioner condenser fan not working", 
     "solution": "Check the fan motor and wiring connections. If the motor is defective, it should be replaced to prevent overheating and potential system failure."},
    
    {"issue": "Air conditioner not cooling enough", 
     "solution": "Clean evaporator coils and check for refrigerant leaks. Ensure that air filters are clean and that the unit is appropriately sized for the space it is cooling."},
    
    {"issue": "Air conditioner tripping the circuit breaker", 
     "solution": "Check for electrical faults and loose connections. Overloaded circuits can cause breakers to trip. If this happens frequently, consult an electrician to assess your electrical system."}
]

parts_data = [
    {"part": "Compressor", "function": "The heart of the cooling system, the compressor pumps refrigerant through the system, enabling heat exchange and cooling."},
    {"part": "Condenser Coil", "function": "This component removes heat from the refrigerant, allowing it to condense back into a liquid. It is crucial for releasing heat outdoors."},
    {"part": "Evaporator Coil", "function": "Absorbs heat from indoor air, causing the refrigerant to evaporate and cool the air before it circulates back into the room."},
    {"part": "Expansion Valve", "function": "Regulates the flow of refrigerant into the evaporator coil. It helps control the cooling effect by adjusting the refrigerant pressure."},
    {"part": "Thermostat", "function": "Monitors and controls the indoor temperature, ensuring the system operates efficiently and maintains comfort."},
    {"part": "Fan Motor", "function": "Circulates air over the evaporator and condenser coils, promoting efficient heat exchange and maintaining airflow."},
    {"part": "Capacitor", "function": "Stores and provides extra power to start the compressor and fan motors, helping them function smoothly."},
    {"part": "Contactor", "function": "Acts as a switch to control the flow of electricity to the compressor and fan motor, ensuring they operate only when needed."},
    {"part": "Air Filter", "function": "Removes dust, pollen, and debris from the air, ensuring clean airflow and improving indoor air quality."},
    {"part": "Refrigerant", "function": "The working fluid that cools and dehumidifies the air by undergoing phase changes within the system."},
    {"part": "Ductwork", "function": "Distributes conditioned air throughout the building, ensuring even temperature and comfort in every room."},
    {"part": "Condensate Drain Line", "function": "Removes condensation produced by the evaporator coil to prevent overflow and maintain system efficiency."},
    {"part": "Heat Exchanger", "function": "Transfers heat between refrigerant and air, facilitating efficient cooling and heating as needed."},
    {"part": "Solenoid Valve", "function": "Controls the flow of refrigerant in heat pump systems, directing it to the appropriate coils based on operating conditions."},
    {"part": "Defrost Control Board", "function": "Activates defrost mode in heat pump systems to prevent ice buildup on coils during cold weather."}
]

e_errors_data = {
    "E1": "This error indicates a problem with the air conditioner's power supply. Check for tripped circuit breakers or blown fuses. If the circuit breaker has tripped, reset it. If fuses are blown, replace them with ones that have the same rating.",
    "E2": "Indoor temperature sensor fault. Check the wiring for any loose connections or damage. If the sensor is malfunctioning, replace it according to the manufacturer's instructions.",
    "E3": "Outdoor temperature sensor fault. Inspect the sensor for any physical damage or wiring issues. A faulty sensor may need to be replaced for the system to function correctly.",
    "E4": "Communication error between indoor and outdoor units. Check the connection cables for damage or loose connections. Ensure both units are correctly powered and functioning.",
    "E5": "High-pressure protection activated. This may indicate a refrigerant blockage or an overcharged system. Have a certified technician inspect the system to diagnose and resolve the issue.",
    "E6": "Refrigerant overcharge or undercharge detected. This can affect system performance. Have a certified technician inspect the refrigerant levels and adjust them as necessary.",
    "E7": "Compressor overload detected. This may indicate a problem with the compressor or electrical system. Check for electrical faults and ensure the compressor is not overheating.",
    "E8": "General system malfunction. Reset the unit and check for any error codes that may appear. If the problem persists, consult a professional technician for diagnosis."
}

# Load data
refrigerants = load_data(REFRIGERANTS_FILE, refrigerants_data)
brands = load_data(BRANDS_FILE, brands_data)
issues = load_data(ISSUES_FILE, issues_data)
parts = load_data(PARTS_FILE, parts_data)
e_errors = load_data(E_ERRORS_FILE, e_errors_data)

def show_menu():
    print("\nWelcome to the Air Conditioner Maintenance Program")
    print("Please choose an option from the menu below:")
    print("1. Refrigerants and Their Pressure Levels")
    print("2. Top and Worst Air Conditioner Brands")
    print("3. Common Issues and Their Solutions")
    print("4. Air Conditioner Parts and Their Functions")
    print("5. E-Errors and Troubleshooting Steps")
    print("6. Exit the Program")

def refrigerants_and_pressures():
    print("\nRefrigerants and Their Pressure Levels:")
    for refrigerant in refrigerants:
        print(f"Type of Refrigerant: {refrigerant['type']}")
        print(f"Hot Pressure: {refrigerant['hot_pressure']}")
        print(f"Cold Pressure: {refrigerant['cold_pressure']}\n")  # Adding an empty line for readability

def top_and_worst_brands():
    print("\nTop Air Conditioner Brands:")
    for brand in brands['top']:
        print(f"- {brand}")

    print("\nWorst Air Conditioner Brands:")
    for brand in brands['worst']:
        print(f"- {brand}")

def common_issues():
    print("\nCommon Issues and Solutions for Air Conditioners:")
    for issue in issues:
        print(f"Issue: {issue['issue']}")
        print(f"Solution: {issue['solution']}\n")
        print()  # Adding an empty line for readability

def air_conditioner_parts():
    print("\nAir Conditioner Parts and Their Functions:")
    for part in parts:
        print(f"Part: {part['part']}")
        print(f"Function: {part['function']}\n")  # Adding an empty line for readability

def e_errors():
    print("\nE-Errors and Their Meanings:")
    for error_code, description in e_errors.items():
        print(f"{error_code} Issue: {description.split('.')[0]}")  # Displaying the issue
        print(f"{error_code} Solution: {description.split('.')[1].strip()}\n")  # Displaying the solution

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            refrigerants_and_pressures()
        elif choice == '2':
            top_and_worst_brands()
        elif choice == '3':
            common_issues()
        elif choice == '4':
            air_conditioner_parts()
        elif choice == '5':
            e_errors()
        elif choice == '6':
            print("Exiting the program. Thank you for using the Air Conditioner Maintenance Program!")
            break
        else:
            print("Invalid choice. Please try again by selecting a number between 1 and 6.")

if __name__ == "__main__":
    main()
