# YouTube Video Summarizer

This web application uses [Streamlit](https://streamlit.io/), [Langchain](https://python.langchain.com/), and [Hugging Face](https://huggingface.co/) models to take a YouTube video link and return a summarization of its content. The core modules used in this project are the 'YoutubeLoader' from Langchain Agents and the 'philschmid/bart-large-cnn-samsum' model from Hugging Face.<br>

https://github.com/mehdi0807/youtube-video-summarizer/assets/92737907/6afba09a-ceab-4a71-bc5e-8e37aa58faf5



## How it works

1. The user provides a YouTube video link in the web application.
2. The 'YoutubeLoader' module retrieves the transcript of the provided YouTube video.
3. The 'philschmid/bart-large-cnn-samsum' model is used to summarize the transcript.
4. The summarized content is displayed to the user.

## Usage

### Prerequisites

Make sure you have the following dependencies installed:

```bash
- Python 3.7+
- pip
- virtualenv (optional but recommended)
```
## Installation

To set up and run the YouTube Video Summarizer, follow these steps:

1. **Clone the GitHub repository:**

    ```bash
    git clone https://github.com/your-username/youtube-video-summarizer.git
    cd youtube-video-summarizer
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    virtualenv venv
    source venv/bin/activate
    ```

3. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Authentication:**

   To use this application, you need to set up Hugging Face API authentication. Create a `.env` file in the root directory of the project and add the following line, replacing `{YOUR HF API KEY}` with your actual Hugging Face API key:

    ```plaintext
    authorization = "Bearer {YOUR HF API KEY}"
    ```

5. **Running the Application:**

   Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

The application should open in your web browser. You can then input a YouTube video link and click the "Summarize" button to generate a summary of the video's content.

This process will start the application and allow you to interact with it using your web browser. Enjoy using the YouTube Video Summarizer!
