# M3U Tools

A collection of scripts to manipulate and convert M3U files. These tools help in splitting M3U files into groups, adding group titles, and converting M3U playlists to other formats.

## Requirements

- Node.js (for running JavaScript scripts)
- Python 3.x (for running Python scripts)
- pandas library (for `convert_m3u.py`)

## Scripts

### JavaScript Scripts

#### groups.js
Splits the M3U file into group-specific playlists and saves them in the `groups` directory.

**Dependencies**:
- Node.js

**Example Usage**:
```sh
node /path/to/m3u-tools/groups.js /path/to/your.m3u
```

### Python Scripts

#### convert_m3u.py
Converts M3U playlists to other formats using the pandas library.

**Dependencies**:
- Python 3.x
- pandas library

**Example Usage**:
```sh
python3 /path/to/m3u-tools/convert_m3u.py /path/to/your.m3u
```

#### add_group_title.py
Adds a 'group-title' field to M3U entries.

**Dependencies**:
- Python 3.x

**Example Usage**:
```sh
python3 /path/to/m3u-tools/add_group_title.py /path/to/your.m3u "Your Group Title"
```

## License

This project is licensed under the MIT License.