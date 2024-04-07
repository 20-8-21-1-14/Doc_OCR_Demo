import streamlit as st
from google.cloud import documentai_v1 as documentai
from google.oauth2 import service_account
from google.api_core.client_options import ClientOptions
import io
import json


# # Function to authenticate and process the document
def process_document(file, project_id, location, processor_id):
    # Authenticate with the service account
    # credentials = service_account.Credentials.from_service_account_file(credentials_path)

    # Create a client
    client = documentai.DocumentProcessorServiceClient(client_options=ClientOptions(
            api_endpoint=f"{location}-documentai.googleapis.com"
        ))
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
    # with open('service/amazing-thought-405501-cf4272beee21.json', 'r') as config_file:  # Fixed the file extension
    #     config = json.load(config_file)

    # PROJECT_ID = config['project_id']
    # LOCATION = "us"
    # CREDENTIALS_PATH =  'service/amazing-thought-405501-cf4272beee21.json'

    PROJECT_ID = "ocr-rd-417002"
    LOCATION = "us" 
    # processor_id = "YOUR_PROCESSOR_ID" # Create processor before running sample
    # processor_version = "rc"

    st.title('Upload Document for Processing')

    uploaded_file = st.file_uploader("Choose a PDF file or an image", type=['pdf', 'jpg', 'png'])
    
    if uploaded_file:
        selected_processor = st.radio(
            "Choose Processor:",
            ("Fee Processor", "Contact Info Processor"),
            key="processor_selector"  # Unique key for this widget
        )

        # Get processor ID based on selection
        if selected_processor == "Fee Processor":
            processor_id = "fcda2565aff06991"  # Replace with actual ID
            processor_version = "pretrained-foundation-model-v1.0-2023-08-22"
        else:
            processor_id = "your-cont-info-processor-id"  # Replace with actual ID

        text = process_document(uploaded_file, PROJECT_ID, LOCATION, processor_id)

        st.write('Extracted Text:')
        st.write(text)
    else:
        st.error("Please upload a PDF file or an image.")