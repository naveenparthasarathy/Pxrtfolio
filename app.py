import streamlit as st
from PIL import Image
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Naveen Parthasarathy's Portfolio
## About me
''')

col1, col2 = st.columns([1,2])
with col1:
  image = Image.open('profile.jpeg')
  st.image(image, width=150)
with col2:
  st.markdown('**Yep, that is my food, blueberry cooler and me**')
  st.markdown('''
- A proud Tifoso since 2022 (Leclerc and Sainz made me fall in love with the sport)
- Long weekends means beach or mountains to me
- My motto? Hit the gym daily, eat guilt-free
              ''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
   <style>
.navbar-nav .nav-link {
    color: white !important;
    transition: color 0.3s ease-in-out;
    text-decoration: none !important;
}
.navbar-nav .nav-link:hover {
    color: #2E5A88 !important;
}
.navbar {
    z-index: 9999;
}
</style>         
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #008B8B;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#about-me">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects-publications">Projects|Publications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#networking-platforms">Networking platforms</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Bachelors in Technology, Computer Science Engineering** SRM Institute of Science and Technology, KTR (CHENNAI)',
'2019-2023')
st.markdown('''
- GPA: 9.0
- Graduated with First Class Distinction
''')

txt('**Intermediate** Sri Chaitanya Junior Kalsala, Hyderabad',
'2017-2019')
st.markdown('''
- Percentage scored: 92.65%
''')

#####################
st.markdown('''
## Work Experience
''')

st.markdown("#### **Supply Chain and Network Operations Analyst**, Consulting - Deloitte India *(Jun 2023–Jun 2025)*")
st.write("**Sales Forecasting and Inventory Optimisation for a tiles manufacturer**")
st.markdown('''
- Implemented techniques for cleaning, transforming and organising raw
data to identify crucial data points for accurate forecasting
- Conducted detailed data quality assessments, including stationarity
checks, to ensure the reliability and appropriate fitting of data for
modelling
- Developed and applied advanced time series forecasting models,
including ARIMA, XGBoost, and Prophet, to generate accurate
predictions
- Built a simple Streamlit application to provide a user-friendly interface
for the forecasting models
- Analysed safety stock calculations alongside senior team members to
identify pain points and propose strategic initiatives aimed at optimising
inventory levels and reducing overall stock hold
- Actively participated in problem-solving initiatives, identifying root
causes and implementing solutions that enhanced project efficiency and
outcomes
''')


st.write("**ETA & ETD Prediction for a leading steel manufacturer**")
st.markdown('''
- Performed data pre-processing, conducted data integrity checks, and
implemented quality assurance measures to ensure the reliability of
data using Python
- Played a key role in understanding and implementing machine learning
pipelines for predicting the estimated time of completion for various
processes of an order type on Google Vertex AI, covering both training
and prediction phases
- Conducted in-depth analysis of model outputs, working alongside senior
team members to derive actionable insights and thorough reports
- Developed and maintained detailed project documentation for easy
understanding and accessibility of processes and methodologies
- Actively participated in problem-solving initiatives, identifying root
causes and implementing solutions that enhanced project efficiency and
outcomes
''')


st.write("**E2E Supply Chain optimisation for an agro-produce firm**")
st.markdown('''
- Optimised inventory levels to categorise product-wise inventory
requirements and reduce holding costs
- Conducted competitor analysis to identify strategic opportunities in sales
and supply chain operations
- Contributed to the redesign of the distribution network to minimise
logistics costs and improve delivery timelines
- Conducted competitor analysis to identify strategic opportunities in sales
and supply chain operations
- Working alongside senior team members, delivered data-driven insights
through visualisations and reports to support business decisions
- Developed detailed process flow maps for easy understanding and
accessibility of processes and methodologies
''')

st.write("#### **Digital Media Management Intern**, Woke Media *(Jun 2021–Oct 2021)*")
st.markdown('''
- Managed corporate and social media content to establish and maintain
clients’ online identity
- Understood client requirements and translated them into actionable
digital strategies
- Developed campaigns aimed at boosting online visibility and
engagement
- Contributed to UX research to enhance user experience across digital
platforms
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`, `Vertex AI`')
txt3('Deep Learning', '`TensorFlow`,`PyTorch`, `Vertex AI`')
txt3('Model deployment', '`streamlit`')

#####################
st.markdown('''
## Projects|Publications
''')
txt4('Demand Forecasting using LSTM and Hybrid 1D CNN-LSTM Models', 'The objective of this project is to use Long Short-Term Memory (LSTM) neural networks with hyperparameter tuning, as well as a hybrid model comprising 1D Convolutional Neural Networks (CNNs) and Long Short-Term Memory to predict the demand for eight medicinal drugs', 'https://github.com/naveenparthasarathy/Demand_Forecasting_Methods_MajorProject')
txt4('Language detection using Naive-Bayes-Classifier', 'A language detection program to analyse and predict the language of the text being entered using the Naive Bayes predictive classifier algorithm', 'https://github.com/naveenparthasarathy/Language-detection-using-Naive-Bayes-Classifier')
txt4('Python Password Generator', 'To generate medium strength passwords using python and a simple streamlit application to generate the password','https://github.com/naveenparthasarathy/Passwordgenerator')

txt4('Demand Forecasting in Supply Chain Management using CNN-LSTM Hybrid Model', 'Journal: IEEE Explore - Year of Publication: [November, 2023]', 'https://ieeexplore.ieee.org/document/10307665')


#####################
st.markdown('''
## Networking platforms 
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/mknaveen-parthasarathy/')
txt2('GitHub', 'https://github.com/naveenparthasarathy')
