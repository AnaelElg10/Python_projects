```markdown
# Python Scripting Project

## Features

- **Automated Compilation**: Compiles Go game projects using the `go build` command.
- **Directory Organization**: Copies game project directories from a source to a target location, maintaining structure.
- **Metadata Generation**: Creates a JSON file (`metadata.json`) in the target directory, listing all game names and the total number of games.

## Getting Started

### Prerequisites

- Python 3.x
- Go (if compiling Go projects)

### Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/yourusername/PSP.git
```

Navigate to the PSP directory:

```sh
cd PSP
```

### Usage

Run the script from the command line, providing the source and target directories as arguments:

```sh
python get_game_data.py <source_directory> <target_directory>
```

For example:

```sh
python get_game_data.py ./data ./target
```

This command will process all game projects in the `./data` directory, compile them if applicable, and organize them into the `./target` directory, along with generating the `metadata.json` file.

## Contributing

Contributions to the PSP Game Data Management Tool are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open source and available under the MIT License.
```