import os
import argparse

def parse_m3u(file_path):
    """Parse the M3U file and return a dictionary grouped by group-title."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    groups = {}
    current_group = None
    current_entries = []
    
    for line in lines:
        line = line.strip()
        
        # Look for lines with group-title metadata
        if line.startswith('#EXTINF:'):
            # Extract group-title
            group_title = None
            if 'group-title' in line:
                group_title = line.split('group-title="')[1].split('"')[0]
            
            # If group-title exists, assign to current_group
            if group_title:
                if group_title not in groups:
                    groups[group_title] = []
                current_group = group_title
                current_entries = groups[current_group]
            else:
                current_group = None
        elif line.startswith('http'):
            if current_group:
                current_entries.append(line)  # Save the URL of the current group
    
    return groups

def write_group_files(groups, output_dir):
    """Write each group to a separate M3U file."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for group, entries in groups.items():
        group_file_path = os.path.join(output_dir, f"{group}.m3u")
        with open(group_file_path, 'w', encoding='utf-8') as f:
            f.write('#EXTM3U\n')  # Write M3U header
            for entry in entries:
                f.write(f'#EXTINF:-1,{group}\n{entry}\n')

def main(input_m3u, output_dir):
    """Main function to parse the M3U and write separated group files."""
    groups = parse_m3u(input_m3u)
    write_group_files(groups, output_dir)

if __name__ == '__main__':
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Split M3U file by group-title.')
    parser.add_argument('input_m3u', type=str, help='Path to the input M3U file')
    parser.add_argument('output_dir', type=str
, na
