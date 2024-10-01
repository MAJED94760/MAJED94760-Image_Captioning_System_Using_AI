
# Image-to-Text Conversion System Using AI

## Project Description
This project utilizes artificial intelligence to convert text from images into editable text. The system employs the BLIP model for text extraction and the MarianMT model for translating extracted text from English to Arabic.

## Objectives
- Convert text from images into machine-readable text.
- Support text translation into Arabic using a translation model.
- Provide an interactive interface using Gradio for user interaction.

## Features
- High-quality text extraction from images.
- Translation of extracted text to Arabic.
- User-friendly interface for uploading images and selecting language.

## Tools Used
- **Programming Language**: Python
- **Framework**: PyTorch
- **Key Libraries**: Hugging Face Transformers, Gradio, PIL
- **Models**:
  - **BLIP**: For analyzing images and extracting text.
  - **MarianMT**: For translating text from English to Arabic.

## How to Run the Project
1. Clone the repository from [GitHub Repository](#) (Add your link here).
2. Install the required libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the project using the command:
   ```bash
   python app.py
   ```
4. Use the Gradio interface to upload images and select the desired language (English or Arabic).

## Example of Running the Project
- Upload an image containing printed or handwritten text.
- The system will extract the text and display it in the user interface.
- If Arabic is selected, the extracted text will be translated.

## Expected Results
- The text extracted from the image will be displayed in the user interface.
- If Arabic is selected, the text will be translated using the translation model.

## Challenges Overcome
- Handling low-quality or noisy images was a challenge, and the system was improved using advanced image analysis libraries.



