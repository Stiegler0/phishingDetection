# Ai based chatbot: Phishing Detection App

## Access the App:

You can access the Phishing Detection App online at the following link:
[Phishing Detection App](https://phishingdetectionapp.streamlit.app/)

## Description:
The Phishing Detection App is a user-friendly tool designed to  analyze emails and determine if they are phishing attempts. It takes prompts from users as email content, analyzes them, and provides a phishing risk score ranging from 0 to 100. A score of 0 indicates a safe email, while a score of 100 suggests a definite phishing attempt. The app also offers a detailed explanation, highlighting key reasons for the assessment in bullet points.

## Features
**Email Analysis:** Input email content into the app to receive a phishing risk score and detailed explanation.

**Phishing Risk Score:**  Obtain a score ranging from 0 to 100, indicating the likelihood of the email being a phishing attempt.

**Explanation:**  Receive a clear and concise explanation, covering various aspects of the email content.

**Additional Context:**  Users can provide additional context besides the email content to enhance the analysis.

## Output Format
**Phishing Risk Score:** [Score]
**Explanation:**
[Reason 1]
[Reason 2]
[Reason 3]
...
Ensure that the explanation covers the following aspects present in the email content:

**Sender's Email Address**

**Language and Grammar**

**Links and URLs**

**Urgency and Threats**

**Requests for Personal Information**

**Attachments**


## Running Locally
To run the Phishing Detection App locally, follow these steps:

### Prerequisites

**Python 3.x installed on your machine.**

**Git installed on your machine.**

```
git clone https://github.com/Stiegler0/phishingDetection
cd phishing-detection-app
```

Install the required Python packages:
```
pip install -r requirements.txt
```

Fix the API Key:

You need to set up the API key for the groq cloud provider. Create a  .streamlit folder and inside creat secrects.toml file  add your API key:

```
GROQ_API_KEY = "You Api key"
```

## Captures:
![image](https://github.com/Stiegler0/phishingDetection/assets/145070468/9011df82-f3ff-4eca-98f9-8230faf070fa)

![image](https://github.com/Stiegler0/phishingDetection/assets/145070468/632d593b-2b29-490a-ad71-852ed4c8a81a)

![image](https://github.com/Stiegler0/phishingDetection/assets/145070468/304eea9e-1a27-4c2c-a8b8-1547f291f68d)


![image](https://github.com/Stiegler0/phishingDetection/assets/145070468/dce21254-54f2-41f0-82a5-3a7f56216e73)


## Future Improvements
**Front-End Design:** Enhance the user experience by improving the front-end design of the application, making it more visually appealing and user-friendly.

**Integration with RAG Models:** Explore the integration of RAG (Retrieval-Augmented Generation) models to further enhance the accuracy of phishing detection. By training the model on external data, we can potentially improve the app's ability to identify phishing attempts with greater precision.

## Contributing
Contributions to the improvement of the Phishing Detection App are welcome! If you have any suggestions or feedback, please feel free to reach out or contribute directly on the GitHub repository.
