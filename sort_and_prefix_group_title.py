import argparse
import re

def sort_and_prefix_group_title(m3u_file, prefix):
    entries = []
    current_entry = []

    with open(m3u_file, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('#EXTINF:'):
                if current_entry:
                    entries.append(current_entry)
                current_entry = [line]
            else:
                current_entry.append(line)
        if current_entry:
            entries.append(current_entry)

    def get_group_title(entry):
        match = re.search(r'group-title="([^"]*)"', entry[0])
        return match.group(1) if match else ''

    entries.sort(key=get_group_title)

    with open(m3u_file, 'w', encoding='utf-8') as file:
        file.write("#EXTM3U\n")
        for entry in entries:
            extinf_line = entry[0]
            match = re.search(r'(group-title=")([^"]*)(")', extinf_line)
            if match:
                new_group_title = f'{match.group(1)}{prefix}{match.group(2)}{match.group(3)}'
                extinf_line = extinf_line.replace(match.group(0), new_group_title)
            file.write(extinf_line)
            for line in entry[1:]:
                file.write(line)

def main():
    parser = argparse.ArgumentParser(description="Sort M3U entries by 'group-title' and add a prefix to the 'group-title'.")
    parser.add_argument("m3u_file", help="Path to the M3U file")
    parser.add_argument("prefix", help="Prefix to add to the group-title")
    
    args = parser.parse_args()
    sort_and_prefix_group_title(args.m3u_file, args.prefix)
    print(f"Sorted entries by 'group-title' and added prefix '{args.prefix}' to all entries in {args.m3u_file}")

if __name__ == "__main__":
    main()
