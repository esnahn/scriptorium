import sys
import os
import re

def clean_filename(name):
    # Remove invalid characters for Windows filenames
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = name.strip()
    if not name:
        return "math_expr"
    # Limit length
    return name[:50].strip()

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/extract_mathml.py <input_html_file>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_dir = os.path.join(os.path.dirname(input_file), "mathml")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find all math tags using regex
    matches = list(re.finditer(r'(<math.*?</math>)', content, re.DOTALL))
    
    if not matches:
        print("No MathML found in the HTML.")
        return
        
    print(f"Found {len(matches)} MathML blocks.")
    
    for match in matches:
        math_content = match.group(1)
        
        # Compute line number where <math> starts
        line_no = content[:match.start()].count('\n') + 1
        
        # Get the text before this match
        text_before = content[:match.start()]
        
        # Remove HTML tags from the preceding text to find a label
        clean_text_before = re.sub(r'<[^>]+>', '', text_before)
        
        # Split by newlines and find the last non-empty line
        lines = [line.strip() for line in clean_text_before.split('\n') if line.strip()]
        
        if lines:
            # Take the last line as label
            raw_label = lines[-1]
            
            # If it ends with a colon, remove it
            if raw_label.endswith(':'):
                raw_label = raw_label[:-1].strip()
                
            file_label = clean_filename(raw_label)
        else:
            file_label = "math_expr"
            
        # Line number prefix makes filename unique
        filename = f"L{line_no}_{file_label}.mml"
        filepath = os.path.join(output_dir, filename)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(math_content)
            
        print(f"Saved: {filepath}")

if __name__ == "__main__":
    main()
