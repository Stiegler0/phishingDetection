import streamlit as st
from groq import Groq
import requests
from streamlit_lottie import st_lottie


headers = {
    "authorization": st.secrets["GROQ_API_KEY"]
}
def analyze_email(client, email_content,additional_context):
    system_prompt = f"""
Analyze the following email and determine if it is a phishing attempt.
 Provide a phishing risk score between 0 and 100, 
 where 0 indicates a completely safe email and 100 indicates a definite phishing attempt. Additionally, provide a detailed explanation highlighting the key reasons for your assessment in bullet points.

**Email Content**:
{email_content}

**Output Format**:
- **Phishing Risk Score**: [Score]
- **Explanation**:
  - [Reason 1]
  - [Reason 2]
  - [Reason 3]
  - ...

Ensure that the explanation covers the following aspects, of course if they are present in the mail content:
1. **Sender's email address**: Analyze if the sender's email address is suspicious or mismatched with the legitimate domain.
2. **Language and grammar**: Check for spelling and grammar errors that are commonly found in phishing emails.
3. **Links and URLs**: Evaluate the safety of any links or URLs included in the email.
4. **Urgency and threats**: Look for language that creates a sense of urgency or threats, which are typical in phishing attempts.
5. **Requests for personal information**: Identify any requests for personal or sensitive information.
6. **Attachments**: Assess any attachments for potential risks.

Provide the analysis in a clear and concise manner. take in consideration  also if there s any additional context
"""
    if additional_context:
        system_prompt += f'''
                The user has provided this additional context:
                  {additional_context}
                 '''

    message = {
        "role":"user",
        "content":email_content
    }
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        message
    ],
    model="llama3-8b-8192",
    )
    
    analysis_result = chat_completion.choices[0].message.content
    return analysis_result



def extract_score(result):
    try:
        score_line = next(line for line in result.split('\n') if 'Phishing Risk Score' in line)
        print(f"Extracted score line: {score_line}")  # Debugging statement
        # Extract only the digits from the score line
        score_str = ''.join(filter(str.isdigit, score_line.split(': ')[1]))
        score = int(score_str)
        return score
    except ValueError as e:
        print(f"ValueError: {e}")  # Print the error message for debugging
        return None  # Or some default value
    except StopIteration as e:
        print(f"StopIteration: {e}")  # Print the error message if 'Phishing Risk Score' is not found
        return None  # Or some default value

st.set_page_config(page_title="Phishing Mails Detector", page_icon=":tada:")

def load_lottierurl(url):
    r =requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottierurl("https://lottie.host/24533c16-0328-48c2-964b-0f9f0e19c45f/3rn7GHfmpZ.json")

def main():
    client = Groq(api_key= st.secrets["GROQ_API_KEY"])

    spacer, col = st.columns([1,1])  
    with col:  
        #st.image('/home/stiegler/phishingDetection/Lorem-ipsum-logo-design-on-transparent-PNG.png')
        st_lottie(lottie_coding, height=300,key="coding")


    st.title(':red[PhishGuard:] Email Safety Checker Bot')
    st.subheader("Powered by Groq Ai, Made by @yassineJM :round_pushpin:")
    
    multiline_text = """
       Welcome the email analyzer: !!"
        """
    st.markdown(multiline_text, unsafe_allow_html=True)
    st.sidebar.title('Customization')
    st.sidebar.write("""
If you have any additional information or context about the email, you can provide it here. 
This might include details about the sender, your relationship with the organization, 
or any other relevant information that might help in assessing the email's legitimacy.
""")
    additional_context = st.sidebar.text_area("Enter additional context here (optional):")



    st.sidebar.title("FAQ:")
    multi2 = '''**Sources Used:** Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... 
            **Up-to-date Information:** Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...  

            '''
    st.sidebar.markdown(multi2)
    st.sidebar.markdown(
            """
            Follow me on:
            """
    )
    st.sidebar.write('<i class="fa-brands fa-github"></i> [@Stiegler0](https://github.com/Stiegler0)', unsafe_allow_html=True)
    st.sidebar.write('<i class="fa-brands fa-linkedin"></i> [@Yassine Jemlaoui](https://www.linkedin.com/in/yassine-jemlaoui-a4bb8b202/)', unsafe_allow_html=True)


    
            
          
    st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"/>', unsafe_allow_html=True)

    user_mail = st.text_area("Paste Your Email content here:")

    if st.button("Analyze"):
        response = analyze_email(client,user_mail,additional_context)
        st.write("Analyzing......")

        score = extract_score(response)

        if score >= 50:
            st.error("Definite phihsing",icon="🚨")
            #st.write(f" Phishing score is: {score}")
            st.write(response)

        elif score <50:
            st.success("Legitime mail", icon="✅")
            st.write(response)





    

if __name__ == "__main__":
    main()

