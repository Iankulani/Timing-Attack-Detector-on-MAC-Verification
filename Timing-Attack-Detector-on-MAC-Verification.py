# -*- coding: utf-8 -*-
"""
Created on Tue Feb  27 08:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Timing Attack Detector")
print(Fore.GREEN+font)

import time
import re

# Simulated MAC address for valid MAC address check
VALID_MAC_ADDRESS = "ec::f7:2b:a1:e4::f8"

# Function to simulate MAC address validation (with timing differences)
def validate_mac_address(user_mac):
    # Simulate a small delay for incorrect MAC addresses
    if user_mac == VALID_MAC_ADDRESS:
        # For correct MAC address, simulate a shorter time delay
        time.sleep(0.01)
        return True
    else:
        # For incorrect MAC address, simulate a longer time delay
        time.sleep(0.1)
        return False

# Function to detect timing attack based on repeated MAC address verification
def detect_timing_attack():
    
    
    # Prompt user for the MAC address to test
    user_mac = input("Enter the MAC address to verify:").strip()

    # Validate the MAC address format
    if not re.match(r"([0-9A-Fa-f]{2}[:]){5}[0-9A-Fa-f]{2}", user_mac):
        print("Invalid MAC address format. Please enter a valid MAC address.")
        return

    # Start the detection process
    print("\nVerifying the MAC address...")
    
    # Measure the time it takes for validation (start time)
    start_time = time.time()
    
    # Validate the MAC address and detect if it's valid or not
    is_valid = validate_mac_address(user_mac)
    
    # Measure the time after validation (end time)
    end_time = time.time()

    # Calculate the time taken for the operation
    time_taken = end_time - start_time
    print(f"Time taken to validate MAC address: {time_taken:.4f} seconds")

    # Check if the time difference is suspicious
    if time_taken > 0.05:  # If the time exceeds a certain threshold, it's suspicious
        print("\n[ALERT] Potential Timing Attack detected! The system is taking an unusually long time for incorrect MAC address validation.")
    else:
        print("[INFO] MAC address verification completed without suspicious timing delay.")

# Main function to start the process
def main():
    # Start detecting timing attacks
    detect_timing_attack()

if __name__ == "__main__":
    main()
