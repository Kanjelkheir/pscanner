# Pscanner (Port Scanner)

Pscanner is a simple, yet effective, multithreaded port scanner written in Python. It allows you to scan a target host for open TCP ports within a specified range.

## Features

- **Fast Scanning**: Utilizes multithreading to scan multiple ports concurrently, significantly speeding up the scanning process.
- **Customizable Port Range**: Specify a range of ports to scan on the target host.
- **Simple Command-Line Interface**: Easy to use with clear command-line arguments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x
- `uv` (for dependency management, as indicated by `uv.lock`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Kanjelkheir/pscanner.git
   cd pscanner
   ```

2. **Install dependencies using `uv`:**

   ```bash
   uv sync
   ```

## Usage

To run the port scanner, you need to provide the target host and the port range.

```bash
uv run main.py --host [TARGET_HOST] --port [START_PORT]/[END_PORT]
```

**Example:**

To scan ports 1 to 1024 on `localhost`:

```bash
uv run main.py --host localhost --port 1/1024
```

To scan ports 80 to 443 on `example.com`:

```bash
uv run main.py --host example.com --port 80/443
```

### Arguments

- `--host`: The target host or IP address to scan. (Required)
- `--port`: The range of ports to scan, specified as `START_PORT/END_PORT`. (Required)
  - `START_PORT` and `END_PORT` should be integers between 1 and 65535.

## How it Works

Pscanner uses Python's `socket` module to attempt a TCP connection to each port within the specified range on the target host. If a connection is successfully established, the port is considered open. To enhance performance, `threading` is used to perform these connection attempts concurrently.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details (if one exists, otherwise consider adding one).
