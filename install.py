# Simple Installer for Eagle Accounting System

import os
import sys

def main():
    print("Welcome to the Eagle Accounting System Installer!")
    
    # Check if the necessary directories exist
    if not os.path.exists('EagleAccounting'):
        os.makedirs('EagleAccounting')
        print("Created directory: EagleAccounting")
    else:
        print("Directory already exists: EagleAccounting")

    # Simulating installation process
    try:
        with open('EagleAccounting/config.ini', 'w') as config:
            config.write('[Settings]\n')
            config.write('AppName=Eagle Accounting System\n')
            config.write('Version=1.0\n')
            print("Configuration file created.")
    except Exception as e:
        print(f"Failed to create configuration file: {e}")
        sys.exit(1)

    print("Eagle Accounting System installed successfully!")

if __name__ == '__main__':
    main()