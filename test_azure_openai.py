# Set up your Gemini API key
# Get your key from: https://aistudio.google.com/app/apikey
import os
from getpass import getpass
import sys

import langextract_edit_edit as lx
import textwrap

# Ensure console can handle Unicode on Windows terminals
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# Define the extraction task
prompt = textwrap.dedent("""\
    Extract characters, emotions, and relationships in order of appearance.
    Use exact text for extractions. Do not paraphrase or overlap entities.
    Provide meaningful attributes for each entity to add context.""")

# Provide a high-quality example
examples = [
    lx.data.ExampleData(
        text="ROMEO. But soft! What light through yonder window breaks? It is the east, and Juliet is the sun.",
        extractions=[
            lx.data.Extraction(
                extraction_class="character",
                extraction_text="ROMEO",
                attributes={"emotional_state": "wonder"}
            ),
            lx.data.Extraction(
                extraction_class="emotion",
                extraction_text="But soft!",
                attributes={"feeling": "gentle awe"}
            ),
            lx.data.Extraction(
                extraction_class="relationship",
                extraction_text="Juliet is the sun",
                attributes={"type": "metaphor"}
            ),
        ]
    )
]


# Simple extraction from a short text
input_text = "Lady Juliet gazed longingly at the stars, her heart aching for Romeo"

result = lx.extract(
    text_or_documents=input_text,
    prompt_description=prompt,
    examples=examples,
    model_id="gpt-4o",
)

# Display results
print(f"Extracted {len(result.extractions)} entities:\n")
for extraction in result.extractions:
    print(f"• {extraction.extraction_class}: '{extraction.extraction_text}'")
    if extraction.attributes:
        for key, value in extraction.attributes.items():
            print(f"  - {key}: {value}")



# Save results to JSONL
lx.io.save_annotated_documents([result], output_name="romeo_juliet.jsonl", output_dir=".")

# Generate interactive visualization
html_content = lx.visualize("romeo_juliet.jsonl")

# Display in notebook
print("Interactive visualization (hover over highlights to see attributes):")
html_content

# Save visualization to file (for downloading)
with open("romeo_juliet_visualization.html", "w", encoding="utf-8") as f:
    # Handle both Jupyter (HTML object) and non-Jupyter (string) environments
    content = html_content.data if hasattr(html_content, 'data') else html_content
    if isinstance(content, bytes):
        content = content.decode('utf-8', errors='replace')
    f.write(content)

print("✓ Visualization saved to romeo_juliet_visualization.html")
print("You can download this file from the Files panel on the left.")


# Try your own text
your_text = """
JULIET: O Romeo, Romeo! wherefore art thou Romeo?
Deny thy father and refuse thy name;
Or, if thou wilt not, be but sworn my love,
And I'll no longer be a Capulet.
"""

custom_result = lx.extract(
    text_or_documents=your_text,
    prompt_description=prompt,
    examples=examples,
    model_id="gpt-4o",
)

print("Extractions from your text:\n")
for e in custom_result.extractions:
    print(f"• {e.extraction_class}: '{e.extraction_text}'")
    if e.attributes:
        for key, value in e.attributes.items():
            print(f"  - {key}: {value}")