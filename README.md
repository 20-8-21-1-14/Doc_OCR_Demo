# Document AI Streamlit App

This Streamlit application enables users to upload PDF or image files and utilizes Google Cloud's Document AI to extract text from these documents. It's designed to showcase how machine learning models can be applied to understand and process document content effectively.

## Features

- **File Upload**: Supports uploading of PDF and image files through a user-friendly web interface.
- **Document Processing**: Uses Google Cloud's Document AI for robust text extraction from uploaded documents.
- **Streamlit Interface**: Offers an intuitive and straightforward interface built with Streamlit, enhancing user experience.

## Prerequisites

To use or contribute to this project, you'll need:

- Python 3.6 or later.
- An active Google Cloud account.
- A Google Cloud project with the Document AI API enabled.
- A service account associated with your Google Cloud project, assigned the Document AI API User role, and a JSON key file for authentication.

## Installation

Follow these steps to get your development environment set up:

1. **Clone the Repository**

   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```
2.  **Create an Anaconda Environment**
    
    You can create an Anaconda environment with all the necessary packages by running:
    
    ```bash 
    conda create --name docai_streamlit python=3.8
    conda activate docai_streamlit
    ```
    Adjust the `python=3.8` as necessary to match your preferred Python version.
    
3.  **Install Dependencies**
    
    After activating your environment, install the required packages:
    
    ```bash
    pip install -r requirements.txt 
    ```
    Alternatively, if you prefer using conda for all installations and the packages are available in the Conda repositories, you can use:
    
    ```bash
    conda install --file requirements.txt 
    ```
    Note: Not all Python packages are available through conda, so you might still need to use pip for some.
    
4.  **Environment Variables**
    
    Copy the `.env.example` file to a new file named `.env`, and fill in your Google Cloud project details and the path to your service account key.
    
    ```plaintext
    PROJECT_ID=your-project-id
    LOCATION=your-project-location
    PROCESSOR_ID=your-processor-id
    GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service/account/key.json` 
    ```

## Usage

To run the application, execute:

bashCopy code

`streamlit run app.py`