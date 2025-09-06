# robco_example

# GOAL
- A small simulation of a robot cell with multiple sensors and a controller
- Create a Python adapter for each device
- Demonstrate integration and troubleshooting
- Documentation

# SCENARIO: Integrating a robot cell with:
- Temperature & Humidity sensor
- Distance sensor
- Camera
- Controller


# APPROACH
- Each sensor runs as a separate server
- Each sensor has a python adapter client
- The robot controller can query any sensor on demand
- The adapters must handle connection errors
- Integration and example usage
