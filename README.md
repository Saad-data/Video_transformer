
# Video Transformer

Welcome to Video Transformer! This handy script allows you to easily convert video files from one format to another using the powerful MoviePy library. With a straightforward command-line interface, you can specify input and output files, select the output format, and opt for high-quality conversion (specific to .mp4).

## Getting Started

### Installation

First, ensure you have the required dependencies installed. Use pip to install them:

\`\`\`sh
pip install moviepy
pip install argparse
\`\`\`

### How to Use

Here's a breakdown of the command-line options available:

- \`-i, --input\`: The input file name (required).
- \`-o, --output\`: The output file name (optional).
- \`-f, --format\`: The output file format (optional, default is mp4).
- \`-hq, --high_quality\`: Enable high-quality codec (optional, default is True).

### Example

Here’s an example of how to run the script:

\`\`\`sh
python video_converter.py -i input_video.webm -o output_video.mp4 -f mp4 -hq True
\`\`\`

In this example:
- \`input_video.webm\` is the input file.
- \`output_video.mp4\` is the desired name for the output file.
- \`mp4\` is the chosen format for the output file.
- \`True\` specifies that you want to use the high-quality codec.

Feel free to customize these options based on your needs. Enjoy converting your videos effortlessly!
