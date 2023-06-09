import re
import streamlit as st 

from PIL import Image

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

image=Image.open('img.png')
st.image(image,width=190,)
st.write('''
# ***Iyed Touati***

''')
st.markdown('<h1 style="color: #13C7F0;  font-size: 44;border: border-radius: 10px; font-weight: bolder;" >Resume</h1>', unsafe_allow_html=True)

st.markdown('<h2 style="color: #f09139;">Summary</h2>', unsafe_allow_html=True)






st.info("""
- Experienced Educator
- Strong verbal and written communication skills 

""")

#Navigation
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #f09139;">
  <a class="navbar-brand" href="https://www.facebook.com/iyed.touati.432002/" target="_blank">Iyed Touati</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Contact">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
def txt(a,b):
    col1,col2=st.columns([1,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)
def txt0(a):
    col1,col2=st.columns([1,1])
    with col1:
        st.markdown(a)
def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def html(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
def txt3(a, html):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(html,unsafe_allow_html=True)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)


st.markdown('<h3 style="color: #f09139;">Education</h3>', unsafe_allow_html=True)
      
html( '- **Baccalaureate** ','  ##### *Lycee Hammam Sousse 2*')
txt('  -  ###### *2017-2021*   ',"")
st.info('''
*Moyenne:14*
''',icon="ℹ️")    

txt(
    '-  **Currently Studying Computer Science**',
    ' ###### *ISITCOM*'
    )
txt0(' - ###### *2021 - Present*')
st.info('''
  *Moyenne:13*
''',icon="ℹ️")    
st.markdown('<h3 style="color: #f09139;">Projects</h3>', unsafe_allow_html=True)

txt3('- Recommedation System',"""
<a  href="https://github.com/luckyman147/myprojects/tree/main/sklearn/projects/recommendation_system" >Link</a>
""")
txt3('- Fake news',"""
<a  href="https://drive.google.com/drive/folders/1wHI3Es8wOczPiSKmeVQU9-S8Lbp3FRjR" >Link</a>
""")
txt3('- Diabetes ',"""
<a  href="https://github.com/luckyman147/myprojects/tree/main/sklearn/projects/diabetes" >Link</a>
""")
txt3("""- Face detection ""","""
<a  href="https://github.com/luckyman147/myprojects/tree/main/images.config/opencv/facedetect/facedetect" >Link</a>
""")
txt3("""- Hand detection ""","""
<a  href="https://drive.google.com/drive/folders/1P1rUu1ABs6ceU62KxLsVSMGUPKUKbtbr" >Link</a>
""")
txt3("""- object detection ""","""
<a  href="https://drive.google.com/drive/folders/1-xAGjo-go328MMi-6lssr6cSBHk83tls" >Link</a>
""")
txt3("""- Similar images ""","""
<a  href="https://github.com/luckyman147/myprojects/tree/main/images.config/opencv/similar/similar" >Link</a>
""")


#####################
st.markdown('<h3 style="color: #f09139;">Skills</h3>', unsafe_allow_html=True)

txt3('Programming', '`Python`, `R`')
txt3('Data processing', '`SQL`, `pandas`, `numpy`,`spark`')
txt3('Data visualization', '`matplotlib`, `seaborn`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`, `Pytorch`')
txt3('Web development', '`Flask`, `HTML`, `CSS`,`Django`')
txt3('Model deployment', '`streamlit`')
txt3(' Mobile developement', '`Flutter`')

#####################
st.markdown('<h3 style="color: #f09139;">Social media</h3>', unsafe_allow_html=True)

txt2('LinkedIn', 'https://www.linkedin.com/in/iyed-touati-41a088226/')
txt2('Facebook', 'https://www.facebook.com/iyed.touati.432002/')
txt2('GitHub', 'https://github.com/luckyman147')


st.markdown('<h3 style="color: #f09139;">Contact us</h3>', unsafe_allow_html=True)
txt2('Gmail', 'iyedtouato@gmail.com')

password='iwkmaopzfeixeeyp'
def extract_name_from_email(email):
    # Extract the name part before the @ symbol using regular expressions
    name_match = re.match(r'([^@]+)', email)
    if name_match:
        name = name_match.group(1)
        return name
    else:
        return None
frmm=st.text_input('Write your gmail ')
email='iyedtouato@gmail.com'
if st.button("Send Email"):
    try:
        # Create a multipart message
        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = frmm
        msg["Subject"] = 'Thank you for visiting my portfolio'
        name=extract_name_from_email(frmm)
        message=message = f"""Dear {name},

I hope this email finds you well. I wanted to take a moment to express my sincere gratitude for visiting my portfolio. It was a pleasure to have you explore my work and learn more about my skills and experience.

I appreciate the time you dedicated to reviewing my projects, achievements, and qualifications. Your interest in my portfolio means a lot to me, and I'm glad you found value in my work.

If you have any further questions or would like to discuss potential collaborations or opportunities, please feel free to reach out. I'm always open to connecting with like-minded individuals in the industry.

Once again, thank you for your visit. Your support and interest in my portfolio are truly appreciated. I look forward to staying in touch and potentially working together in the future.

Best regards,

Iyed Touati
"""
        # Attach the message to the email
        msg.attach(MIMEText(message, "plain"))

        # Create SMTP session
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            # Start TLS for security
            server.starttls()
            # Login to the email account
            server.login(email, password)
            # Send email
            server.sendmail(email, frmm, msg.as_string())
        
        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Error occurred while sending the email: {e}")

          
