
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
   ```

### Configuration
1. Update the `server_id` and `required_role_id` variables with your server and role IDs.
2. Replace the placeholder in `bot.run('')` with your bot's token.

### Color Map
This bot supports a predefined set of color names (e.g., "red", "blue", "green") and hex color codes (e.g., `#FF5733`). Check the `color_map` dictionary for all supported color names.

## Usage

1. Start the bot:
   ```bash
   python main.py
   ```
2. Use the `/role` commands directly in the Discord server.

### Example Workflow
1. **Create a Custom Role**: Use `/role name MyCustomRole`.
2. **Add Color**: Use `/role colour red` or `/role colour #FF0000`.
3. **Add Icon**: Use `/role icon 🌟` or `/role icon (emoji URL)`.

## Error Handling

- If the bot encounters permission issues, it will send a message to the user or log the error.
- Use the `/role name` command first to create the role if the bot cannot find an existing custom role for the user.

### Additional Notes
- Ensure the bot has permission to manage roles in your server.
- Users need the `required_role_id` role to utilize these commands.

---

This bot was designed to help Discord server members customize their roles efficiently. Contributions and suggestions are welcome!
