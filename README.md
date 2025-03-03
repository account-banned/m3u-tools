# M3U Tools

A collection of scripts to manipulate and convert M3U playlists. These tools help in cleaning up, sorting, splitting into groups, and updating the README for M3U playlists.

## Requirements

- Node.js (for running JavaScript scripts)
- Git (for committing and pushing changes)

## Scripts

### cleanup-m3u.js
Cleans up the M3U file by trimming whitespace, replacing multiple spaces with a single space, and ensuring a single newline at the end of the file.

### sort-m3u.js
Sorts the entries in the M3U file (uncommented in the workflow).

### groups.js
Splits the M3U file into group-specific playlists and saves them in the `groups` directory.

### readme-m3u.js
Updates the README file with comprehensive playlist information, including statistics and available playlists.

## Usage

1. **Run the scripts**: Use the provided bash script to run the necessary scripts.
   ```sh
   ./validate.sh
   ```

2. **Commit changes**: The script will automatically commit and push any changes made by the scripts.

## License

This project is licensed under the MIT License.