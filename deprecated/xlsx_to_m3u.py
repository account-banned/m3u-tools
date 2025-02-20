import re
import pandas as pd
import argparse

def parse_m3u(m3u_file):
    channels = []
    
    with open(m3u_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for i in range(len(lines)):
        if lines[i].startswith('#EXTINF:'):
            match = re.search(r'group-title="(.*?)"', lines[i])
            group = match.group(1) if match else "Unknown"
            
            channel_name = lines[i].split(',')[-1].strip()
            
            if i + 1 < len(lines):
                stream_url = lines[i + 1].strip()
            else:
                stream_url = ""
            
            channels.append([group, channel_name, stream_url])
    
    return channels

def save_to_xlsx(channels, output_file):
    df = pd.DataFrame(channels, columns=['Group', 'Channel Name', 'Stream Link'])
    df.to_excel(output_file, index=False)

def main():
    parser = argparse.ArgumentParser(description="Convert M3U file to XLSX.")
    parser.add_argument("input_file", help="Path to the input M3U file")
    parser.add_argument("output_file", help="Path to the output XLSX file")

    args = parser.parse_args()

    channels = parse_m3u(args.input_file)
    save_to_xlsx(channels, args.output_file)

    print(f"Conversion complete! Saved to {args.output_file}")

if __name__ == "__main__":
    main()
