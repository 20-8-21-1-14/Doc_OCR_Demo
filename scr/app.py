import streamlit as st
from google.cloud import documentai_v1 as documentai
from google.oauth2 import service_account
import io


# Function to authenticate and process the document
def process_document(file, project_id, location, processor_id, credentials_path):
    # Authenticate with the service account
    credentials = service_account.Credentials.from_service_account_file(credentials_path)

    # Create a client
    client = documentai.DocumentProcessorServiceClient(credentials=credentials)
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

    # Read the file content
    content = file.getvalue()

    # Configure the process request
    document = {"content": content, "mime_type": "application/pdf"}
    request = {"name": name, "raw_document": document}

    # Process the document
    result = client.process_document(request=request)
    return result.document.text


selected_processor = st.radio("Choose Processor:", ("Fee Processor", "Contact Info Processor"))


if __name__=='__main__':
    st.title('Upload Document for Processing')

    uploaded_file = st.file_uploader("Choose a PDF file or an image", type=['pdf', 'jpg', 'png'])
    
    if uploaded_file is None:
        st.error("Please upload a PDF file or an image.")
    else:
        # Get processor ID based on selection
        if selected_processor == "Fee Processor":
            processor_id = "your-fee-processor-id"  # Replace with actual ID
        else:
            processor_id = "your-cont-info-processor-id"  # Replace with actual ID

    if uploaded_file is not None and selected_processor is not None:
    # Set your Google Cloud Project details
        PROJECT_ID = 'your-project-id'
        LOCATION = 'us'
        PROCESSOR_ID = processor_id
        CREDENTIALS_PATH = 'scr/config/amazing-thought-405501-3fb66bba89ef.json'

        # Process the uploaded file
        text = process_document(uploaded_file, PROJECT_ID, LOCATION, PROCESSOR_ID, CREDENTIALS_PATH)

         # Display the extracted text
        st.write('Extracted Text:')
        st.write(text)
    assert text is None, 'No text extracted'
    