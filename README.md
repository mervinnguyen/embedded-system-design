 Embedded System Design

> Production-grade embedded system design walkthroughs : architecture, implementation, and analysis across real-world firmware domains.

**Author:** Mervin Nguyen  
**Contact:** mervinnguyenembedded@gmail.com | [LinkedIn](https://linkedin.com/in/mervin-nguyen) | [Portfolio](https://mervin-nguyen.vercel.app)

---

## Overview

This repository documents end-to-end embedded system design across six core domains. Each module covers the full design lifecycle: requirements analysis, hardware/software partitioning, architecture decisions, implementation, and validation strategy.

Each design reflects the same engineering discipline applied in production systems : safety-critical fault detection, real-time scheduling, power-constrained sensor nodes, and deterministic motor control.

---

## Repository Structure

```
embedded-system-design/
├── automotive-can-network/         # CAN bus architecture for 10-ECU vehicle network
│   ├── src/                        # Simulation code, DBC files, bus load analysis
│   ├── docs/                       # Architecture diagrams, design decisions
│   └── tests/                      # Validation scripts
│
├── data-logging-system/            # Embedded data logger: 100 samples/sec, 7-day storage
│   ├── src/                        # Circular buffer, FatFs integration, USB CDC
│   ├── docs/
│   └── tests/
│
├── motor-control-system/           # BLDC motor controller with FOC, closed-loop PID
│   ├── src/                        # FOC algorithm, ISR architecture, safety interlocks
│   ├── docs/
│   └── tests/
│
├── battery-iot-sensor-node/        # Battery-powered sensor node with 5-year lifetime target
│   ├── src/                        # Duty cycling, LoRa/BLE, OTA firmware update
│   ├── docs/
│   └── tests/
│
├── multi-mcu-system/               # Main + 3 peripheral MCU distributed architecture
    ├── src/                        # Inter-MCU communication, synchronization
    ├── docs/
    └── tests/

```

---

## Modules

### 1. [Automotive CAN Network](./automotive-can-network/)
Design a communication network for a vehicle with 10 ECUs: engine control, transmission, ABS, airbag, body control, instrument cluster, infotainment, ADAS camera, parking sensors, and OBD-II diagnostic port.

**Key topics:** Bus segmentation, message ID prioritization, gateway design, bus load analysis, diagnostics, fault confinement.

---

### 2. [Data Logging System](./data-logging-system/)
Design an embedded data logger recording 100 samples/sec for 7 days with Flash storage, circular buffering, and USB offload.

**Key topics:** Circular buffer design, FatFs FAT32 integration, eMMC/Flash wear leveling, USB CDC, power-safe writes, overflow handling.

---

### 3. [Motor Control System](./motor-control-system/)
Design a BLDC motor controller with closed-loop speed control, Field-Oriented Control (FOC) algorithm, real-time ISR architecture, and safety interlocks.

**Key topics:** FOC algorithm, Clarke/Park transforms, PWM generation, encoder feedback, PID tuning, deadband compensation, fault shutdown sequencing.

---

### 4. [Battery-Powered IoT Sensor Node](./battery-iot-sensor-node/)
Design a battery-powered environmental sensor node targeting a 5-year lifetime with LoRa/BLE communication and OTA firmware update capability.

**Key topics:** Duty cycling, sleep/wake state machines, LoRa link budget, BLE advertisement, OTA bootloader architecture, CRC validation, power budgeting.

---

### 5. [Multi-MCU System](./multi-mcu-system/)
Design a distributed system with a main controller and 3 peripheral MCUs for sensor acquisition, inter-MCU communication, and synchronization.

**Key topics:** SPI/I2C/UART protocol selection, master-slave arbitration, clock synchronization, fault detection across nodes, DMA chaining, message framing.

---

### 6. [Embedded System Design — Interview Methodology](./interview-methodology/)
A structured framework for approaching embedded system design interviews: requirements analysis, HW/SW partitioning, architecture patterns, and common failure modes.

**Key topics:** Clarifying constraints, partitioning decisions, real-time vs. non-real-time tradeoffs, common interview mistakes and how to avoid them.

---

## Status

| Module | Status |
|---|---|
| Automotive CAN Network | 🔄 In Progress |
| Data Logging System | 🔄 In Progress |
| Motor Control System | 🔄 In Progress |
| Battery IoT Sensor Node | 🔄 In Progress |
| Multi-MCU System | 🔄 In Progress |
| Interview Methodology | 🔄 In Progress |

---

## License

MIT License — see [LICENSE](./LICENSE) for details.
