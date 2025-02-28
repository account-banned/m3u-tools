# M3U Tools

This folder contains several scripts to manipulate and convert M3U files.

## Requirements

- Python 3.x
- pandas library (for `convert_m3u.py`)

You can install the required library using pip:

```sh
pip install pandas
```

## Scripts

### 1. `converter.py`

Convert between `.xlsx`, `.csv`, and `.m3u` file formats.

#### Usage

```sh
python converter.py input_file output_format
```

#### Example Commands

```sh
python converter.py input.xlsx m3u
python converter.py input.csv m3u
python converter.py input.m3u xlsx
python converter.py input.m3u csv
```

### 2. `split_m3u.py`

Split an M3U file into multiple M3U files based on the `group-title`.

#### Usage

```sh
python split_m3u.py input.m3u output_dir
```

#### Example Command

```sh
python split_m3u.py input.m3u output_directory
```

### 3. `sort_and_prefix_group_title.py`

Sort M3U entries by `group-title` and add a prefix to the `group-title`.

#### Usage

```sh
python sort_and_prefix_group_title.py m3u_file prefix
```

#### Example Command

```sh
python sort_and_prefix_group_title.py input.m3u "Prefix_"
```

### 4. `convert_m3u.py`

Convert between M3U and XLSX formats.

#### Usage

```sh
python convert_m3u.py input_file [output_file]
```

#### Example Commands

```sh
python convert_m3u.py input.m3u
python convert_m3u.py input.xlsx
```

### 5. `add_group_title.py`

Add a `group-title` field to M3U entries.

#### Usage

```sh
python add_group_title.py m3u_file group_title
```

#### Example Command

```sh
python add_group_title.py input.m3u "New Group Title"
```

## Example Input File

### input.xlsx or input.csv

| group-title | tvg-id | tvg-logo | channel_name | stream-url                |
|-------------|--------|----------|--------------|---------------------------|
| Group 1     | id1    | logo1    | Channel 1    | http://example.com/stream1 |
| Group 2     | id2    | logo2    | Channel 2    | http://example.com/stream2 |

## Example Output File

### input.m3u

```
#EXTM3U
#EXTINF:-1 group-title="Group 1" tvg-id="id1" tvg-logo="logo1",Channel 1
http://example.com/stream1
#EXTINF:-1 group-title="Group 2" tvg-id="id2" tvg-logo="logo2",Channel 2
http://example.com/stream2
```

## License

This project is licensed under the MIT License.