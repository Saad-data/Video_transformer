
from moviepy.editor import VideoFileClip
import argparse

def video_converter(input_file, output_file, output_format, high_quality=False):
    """
    Converts a video file to a specified format with an optional high-quality setting for MP4.

    Parameters:
    - input_file (str): Path to the input video file.
    - output_file (str): Path to the output video file.
    - output_format (str): Desired output format (e.g., 'mp4', 'avi', 'png').
    - high_quality (bool): Flag to use high-quality codec for MP4 (default: False).
    """
    # Define codec options for different formats
    low_quality_mp4_codec = 'libx264'
    high_quality_mp4_codec = 'mpeg4'
    avi_codec = 'rawvideo'
    png_codec = 'png'

    # Choose the appropriate codec based on the output format and quality preference
    if output_format == 'mp4' and high_quality:
        codec = high_quality_mp4_codec
    elif output_format == 'mp4' and not high_quality:
        codec = low_quality_mp4_codec
    elif output_format == 'avi':
        codec = avi_codec
    elif output_format == 'png':
        codec = png_codec
    else:
        raise ValueError("Invalid output format. Please use 'mp4', 'avi', or 'png'.")

    # Try to convert the video and handle any potential errors
    try:
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec=codec, audio_codec='aac')
        print("Conversion completed successfully!")
    except Exception as e:
        raise ValueError("Error during conversion: ", e)

# Set up the argument parser to handle command-line arguments
parser = argparse.ArgumentParser(description='Convert video files to different formats')
parser.add_argument('-i', '--input', help='Path of the input file', required=True)
parser.add_argument('-o', '--output', help='Path of the output file', required=False)
parser.add_argument('-f', '--format', help='Format of the output file', required=False, default='mp4')
parser.add_argument('-hq', '--high_quality', help='Use high quality codec', required=False, default=True)

# Parse the arguments
args = parser.parse_args()

# Extract values from parsed arguments
path_input_file = args.input
name_input_file = args.input.split(".")[0]
name_output_file = args.output.split(".")[0] if args.output else None
output_format = args.format
high_quality = args.high_quality

# Determine the output file path if not provided
if name_output_file is None:
    path_output_file = name_input_file + "." + output_format
else:
    path_output_file = name_output_file + "." + output_format

# Display the conversion details
print("Input file: ", path_input_file)
print("Output file: ", path_output_file)
print("Output format: ", output_format)
print("High quality: ", high_quality)

# Perform the video conversion
video_converter(path_input_file, path_output_file, output_format, high_quality)
