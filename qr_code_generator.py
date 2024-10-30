import os
import pandas as pd
import qrcode

# Define paths
input_folder = 'input'
output_folder = 'output'
png_folder = os.path.join(output_folder, 'png')
svg_folder = os.path.join(output_folder, 'svg')

# Create the output folders if they don't exist
os.makedirs(png_folder, exist_ok=True)
os.makedirs(svg_folder, exist_ok=True)

# Function to sanitize filenames
def sanitize_filename(name):
    """Sanitize filenames by replacing spaces and slashes."""
    return str(name).replace(" ", "_").replace("/", "_").replace("\\", "_")

# Function to save QR code images in both formats
def save_qr_images(qr, description):
    """Generate and save QR code images in PNG and SVG formats."""
    sanitized_description = sanitize_filename(description)

    # Save PNG
    png_path = os.path.join(png_folder, f'{sanitized_description}.png')
    img_png = qr.make_image(fill_color="black", back_color="white").resize((400, 400), resample=0)
    img_png.save(png_path)

    # Save SVG
    svg_path = os.path.join(svg_folder, f'{sanitized_description}.svg')
    img_svg = qr.make_image(fill_color="black", back_color="white")
    img_svg.save(svg_path)  # Adjust this line if needed for SVG handling

    return png_path, svg_path

# Function to process each file in the input directory
def process_file(filename):
    """Read input file and generate QR codes for each link."""
    file_path = os.path.join(input_folder, filename)
    df = pd.read_csv(file_path) if filename.endswith('.csv') else pd.read_excel(file_path)

    # Ensure necessary columns are present
    if {'links', 'description'}.issubset(df.columns):
        for link, description in zip(df['links'], df['description']):
            if pd.notna(link) and pd.notna(description):
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(link)
                qr.make(fit=True)
                
                save_qr_images(qr, description)
                print(f'Generated QR code for link: {link}.')

    else:
        print(f"'links' or 'description' column not found in file: {filename}")

# Main function to process all files in the input directory
def process_files():
    """Process all input files to generate QR codes."""
    for filename in os.listdir(input_folder):
        if filename.endswith(('.csv', '.xlsx')):
            process_file(filename)

if __name__ == "__main__":
    process_files()