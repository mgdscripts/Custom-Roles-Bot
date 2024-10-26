
# Custom Role Management Bot for Discord

This bot provides slash commands for users to create and customize personal roles in a Discord server. Users can modify the role name, color, and icon, provided they have the required role permissions.

## Features

- **Slash Commands** for easy role management:
  - `/role name`: Create or update a role with a custom name.
  - `/role colour`: Update the color of an existing role.
  - `/role icon`: Add an emoji or image as an icon for a role.
- Automatically deletes a user's custom role if they lose the required permissions.

## Commands

| Command        | Description                              | Usage Example           |
|----------------|------------------------------------------|--------------------------|
| `/role name`   | Creates or updates a custom role name.   | `/role name MyRoleName` |
| `/role colour` | Updates the color of a custom role.      | `/role colour blue`      |
| `/role icon`   | Adds an icon to a custom role.           | `/role icon 🌟`          |

## Setup Instructions

### Prerequisites
- Python 3.8+
- [Py-cord](https://github.com/Pycord-Development/pycord) (Latest version)
- Other libraries: `requests`, `re`

### Installation
1. Clone the repository or download the source code.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
