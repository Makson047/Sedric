# Compliance Detection Pipeline

This project is a flexible Python pipeline for detecting regulatory compliance violations in fintech and trading companies using LLM (Anthropic Claude). It supports various types of checks: customer complaints, call recording disclosure, aggressive marketing.



## 📦 Project Structure

```plaintext
project_root/
├── main.py
├── compliance_checks.py
├── api_utils.py
├── pdf_utils.py
├── csv_utils.py
├── file_utils.py
├── prompt_utils.py
├── prompts/
│   ├── complaint_handling.txt
│   ├── call_recording_disclosure.txt
│   └── aggressive_marketing.txt
├── data_files/
│   └── ... (input data)
├── requirements.txt
└── README.md
```


## ⚙️ Requirements

- Python 3.8+
- [Anthropic API key](https://console.anthropic.com/)
- Libraries:
    - anthropic
    - python-dotenv
    - PyPDF2
    - (and standard Python libraries)

Install all dependencies:
pip install -r requirements.txt 


## 🚀 How to Run

1. Add your API key to the .env file:
ANTHROPIC_API_KEY=sk-ant-...

2. Prepare a folder with the files you want to check (see examples below).

3. Run the script (CLI):
Complaint Handling and Escalation
python main.py --case complaint --input_folder data_files\Transcriptions\Complaints

Call Recording Disclosure
python main.py --case recording --input_folder "data_files\Transcriptions\Mock Calling Disclosure"

Aggressive or Pressuring Selling Language (Marketing)
python main.py --case marketing --input_folder data_files\Marketing_Assets


## 📄 Case Descriptions
- complaint — Detection of customer complaints that were not flagged by the agent.
- recording — Detection of missing call recording disclosures in calls.
- marketing — Detection of aggressive or misleading marketing in PDF files of web pages/ads.


## 📝 Example Input Data Structure
- For complaint/recording: .txt files with call transcriptions.
- For marketing: .pdf files with marketing materials.


## 📤 Results
Saved in the corresponding CSV files:
- complaint.csv
- recording.csv
- marketing.csv
Each row contains the result for one file.


## 🧩 Extensibility
To add new types of checks:
- Add a new prompt in prompts/.
- Add a new checker in compliance_checks.py.
- Update the logic in main.py if needed.


## ❗ Tips
- Make sure all environment variables (especially ANTHROPIC_API_KEY) are set.
- For marketing PDFs, it's recommended to check the quality of the extracted text.
- When testing with a large number of files, follow the Anthropic API limits.


##  📞 Support
For development questions, open an Issue or contact the project author directly.