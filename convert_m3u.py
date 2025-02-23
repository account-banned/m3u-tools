import re
import pandas as pd
import argparse
import os

def parse_m3u(m3u_file):
    channels = []
    attribute_keys = set()
    
    with open(m3u_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for i in range(len(lines)):
        if lines[i].startswith('#EXTINF:'):
            attributes = {}
            match = re.findall(r'(\w+)="(.*?)"', lines[i])
            for key, value in match:
                attributes[key] = value
                attribute_keys.add(key)
            
            channel_name = lines[i].split(',')[-1].strip()
            attributes['channel_name'] = channel_name
            attribute_keys.add('channel_name')
            
            stream_urls = []
            j = i + 1
            while j < len(lines) and not lines[j].startswith('#EXTINF:'):
                if lines[j].strip().startswith('http'):
                    stream_urls.append(lines[j].strip())
                j += 1
            for idx, url in enumerate(stream_urls):
                attributes[f'stream-url.{idx+1}'] = url
                attribute_keys.add(f'stream-url.{idx+1}')
            
            channels.append(attributes)
    
    return channels, attribute_keys

def save_to_xlsx(channels, attribute_keys, output_file):
    df = pd.DataFrame(channels)
    df = df.reindex(columns=list(attribute_keys))
    df.to_excel(output_file, index=False)

def create_m3u_from_xlsx(xlsx_file, m3u_file):
    df = pd.read_excel(xlsx_file)
    
    with open(m3u_file, 'w', encoding='utf-8') as file:
        file.write("#EXTM3U\n")
        
        for _, row in df.iterrows():
            attributes = []
            for col in df.columns:
                if col not in ['channel_name'] and pd.notna(row[col]) and not col.startswith('stream-url'):
                    attributes.append(f'{col}="{row[col]}"')
            
            channel_name = row.get("channel_name", "Unknown")
            
            extinf_line = f'#EXTINF:-1 {" ".join(attributes)},{channel_name}\n'
            file.write(extinf_line)
            for col in df.columns:
                if col.startswith('stream-url') and pd.notna(row[col]):
                    file.write(row[col] + "\n")
    
    print(f"Conversion complete! Saved to {m3u_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert between M3U and XLSX.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", nargs='?', help="Path to the output file (optional)")
    
    args = parser.parse_args()
    base_name, ext = os.path.splitext(args.input_file)
    
    if ext.lower() == ".m3u":
        args.output_file = args.output_file or f"{base_name}.xlsx"
        channels, attribute_keys = parse_m3u(args.input_file)
        save_to_xlsx(channels, attribute_keys, args.output_file)
    elif ext.lower() == ".xlsx":
        args.output_file = args.output_file or f"{base_name}.m3u"
        create_m3u_from_xlsx(args.input_file, args.output_file)
    else:
        print("Unsupported file type. Please provide an .m3u or .xlsx file.")
        return
    
    print(f"Conversion complete! Saved to {args.output_file}")

if __name__ == "__main__":
    main()
