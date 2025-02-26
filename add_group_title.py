import argparse
import re

def add_group_title(m3u_file, group_title):
    with open(m3u_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    with open(m3u_file, 'w', encoding='utf-8') as file:
        for line in lines:
            if line.startswith('#EXTINF:'):
                if 'group-title=' not in line:
                    match = re.search(r'(tvg-logo="[^"]*")', line)
                    if match:
                        line = line.replace(match.group(1), match.group(1) + f' group-title="{group_title}"')
            file.write(line)

def main():
    parser = argparse.ArgumentParser(description="Add 'group-title' field to M3U entries.")
    parser.add_argument("m3u_file", help="Path to the M3U file")
    parser.add_argument("group_title", help="Group title to add")
    
    args = parser.parse_args()
    add_group_title(args.m3u_file, args.group_title)
    print(f"Added 'group-title=\"{args.group_title}\"' to all entries in {args.m3u_file}")

if __name__ == "__main__":
    main()
