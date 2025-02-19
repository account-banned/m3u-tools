# **m3u-tools**
   Tools.....for m3u and the such. 

## **convert_m3u.py**
   A python script to convert xlsx to m3u/m3u to xlsx
   
   m3u to xlsx, outputs a matching xlsx file.
    `python3 convert_m3u.py <playlist_name>.m3u`

   xlsx to m3u, outputs a matching m3u file.
    `python3 convert_m3u.py <playlist_name>.xlsx`

## **split_m3u.py**
   A python script to split an m3u file based on 'group-title'
Usage

    python split_m3u.py <playlist_name>.m3u <output_directory>
    
This will output the files to the<output_directory> directory.

    python split_m3u.py <playlist_name>.m3u

This will output the files to the current directory where the script is run.   
