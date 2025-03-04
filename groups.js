const fs = require('fs');
const path = require('path');
const readline = require('readline');

function splitByGroup(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');
  
  // Create groups directory if it doesn't exist
  const groupsDir = path.join(path.dirname(filePath), 'groups');
  if (!fs.existsSync(groupsDir)) {
    fs.mkdirSync(groupsDir);
  }
  
  // Get existing group files
  const existingFiles = fs.readdirSync(groupsDir)
    .filter(file => file.endsWith('.m3u'))
    .map(file => file.toLowerCase());
  
  const groups = {};
  
  // First line should be #EXTM3U
  const header = lines[0];
  if (!header.startsWith('#EXTM3U')) {
    throw new Error('Invalid M3U file: Missing #EXTM3U header');
  }
  
  // Process the file line by line to handle multi-line entries
  let currentGroupTitle = null;
  let currentEntry = [];
  let isInEntry = false;
  
  for (let i = 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line) continue;
    
    if (line.startsWith('#EXTINF')) {
      // Start of a new entry
      isInEntry = true;
      currentEntry = [line];
      
      // Extract the group title
      const groupMatch = line.match(/group-title="([^"]*)"/);
      currentGroupTitle = groupMatch ? groupMatch[1] : 'Unknown';
      
      // Initialize the group if it doesn't exist
      if (!groups[currentGroupTitle]) {
        groups[currentGroupTitle] = ['#EXTM3U'];
      }
    } else if (isInEntry) {
      // Add the line to the current entry
      currentEntry.push(line);
      
      // If this is a URL line (doesn't start with #), this completes the entry
      if (!line.startsWith('#')) {
        // Add all lines of the entry to the appropriate group
        groups[currentGroupTitle].push(...currentEntry);
        
        // Reset for the next entry
        isInEntry = false;
        currentEntry = [];
      }
    }
  }
  
  // Get list of current group files that should exist
  const currentGroupFiles = Object.keys(groups).map(groupTitle =>
    `${groupTitle.replace(/[^a-z0-9]/gi, '_').toLowerCase()}.m3u`
  );
  
  // Remove files for groups that no longer exist
  existingFiles.forEach(existingFile => {
    if (!currentGroupFiles.includes(existingFile)) {
      const fileToRemove = path.join(groupsDir, existingFile);
      fs.unlinkSync(fileToRemove);
      console.log(`Removed obsolete group playlist: ${existingFile}`);
    }
  });
  
  // Write each group to a separate file
  Object.entries(groups).forEach(([groupTitle, groupLines]) => {
    const safeGroupTitle = groupTitle.replace(/[^a-z0-9]/gi, '_').toLowerCase();
    const groupFilePath = path.join(groupsDir, `${safeGroupTitle}.m3u`);
    fs.writeFileSync(groupFilePath, groupLines.join('\n') + '\n');
    console.log(`Created/updated group playlist: ${groupFilePath}`);
  });
  
  // Create a summary of the split
  // Count entries properly by counting #EXTINF lines
  const summary = Object.entries(groups).map(([group, lines]) => {
    const channelCount = lines.filter(line => line.startsWith('#EXTINF')).length;
    return `${group}: ${channelCount} channels`;
  });
  
  console.log('\nPlaylist split summary:');
  console.log(summary.join('\n'));
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Please provide the path to your M3U file: ', (filePath) => {
  if (!filePath) {
    console.error('Please provide the path to your M3U file');
    process.exit(1);
  }

  try {
    splitByGroup(filePath);
  } catch (error) {
    console.error('Error splitting M3U file:', error.message);
    process.exit(1);
  } finally {
    rl.close();
  }
});
