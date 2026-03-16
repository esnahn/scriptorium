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
        
        # Line number prefix for uniqueness
        line_no = content[:match.start()].count('\n') + 1

        # Try to find any <annotation> tag for a label
        annotation_match = re.search(r'<annotation[^>]*>(.*?)</annotation>', math_content, re.DOTALL | re.IGNORECASE)
        if annotation_match:
            raw_label = annotation_match.group(1).strip()
        else:
            # Fallback: Extract all text content from the MathML structure
            # Remove all HTML tags and keep only the inner text
            raw_label = re.sub(r'<[^>]+>', '', math_content).strip()

        # Clean up the label: normalize whitespace and remove invalid filename chars
        raw_label = " ".join(raw_label.split())
        file_label = clean_filename(raw_label)
            
        # Line number prefix makes filename unique
        filename = f"L{line_no}_{file_label}.mml"
        filepath = os.path.join(output_dir, filename)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(math_content)
            
        print(f"Saved: {filepath}")

if __name__ == "__main__":
    main()
