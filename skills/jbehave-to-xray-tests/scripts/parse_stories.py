import re
import json
import sys

def parse_stories(file_paths):
    results = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            parts = re.split(r'Scenario:\s+', content)
            
            for part in parts[1:]:
                lines = part.strip().split('\n')
                if not lines:
                    continue
                
                title = lines[0].strip()
                if title.startswith('[TEST-'):
                    continue
                    
                meta_line = ""
                meta_index = -1
                for i, line in enumerate(lines[1:4]):
                    if line.strip().startswith('Meta:'):
                        meta_line = line.strip()
                        meta_index = i + 1
                        break
                
                steps = []
                start_steps = meta_index + 1 if meta_index != -1 else 1
                for line in lines[start_steps:]:
                    stripped = line.strip()
                    if stripped.startswith('Scenario:'):
                        break
                    steps.append(line)
                    
                description = "\n".join(steps).strip()
                
                results.append({
                    "file_path": file_path,
                    "original_title": title,
                    "meta_line": meta_line,
                    "description": description
                })
        except Exception as e:
            print(f"Error reading {file_path}: {e}", file=sys.stderr)
            
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 parse_stories.py <path_to_story_file_1> <path_to_story_file_2> ...", file=sys.stderr)
        sys.exit(1)
    parse_stories(sys.argv[1:])
