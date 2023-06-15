import streamlit as st
import pandas as pd
import datetime
import os
from langchain import PromptTemplate, OpenAI, LLMChain


# Configure Streamlit page
st.set_page_config(
        page_title="Charity Grant Application",
        layout="wide",
        initial_sidebar_state="expanded"
    )

api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
if api_key:
    st.sidebar.success("API key loaded", icon="🚀")
os.environ["OPENAI_API_KEY"] = api_key


def main():
    st.title("📰 Welcome to the AI Charity Grant Application Generator!")
    st.write("")
    st.write("")
    st.write("")
    description = """
    <div style="text-align: center;">
        <h3>🚀 Our application is designed to streamline the process of applying for charity grants.</h3>
    </div> """

    #     <p>We understand that writing grant applications can be time-consuming and challenging, so we've developed an AI-powered solution to assist you.</p>
    #     <p>With our AI Charity Grant Application Generator, you can quickly generate comprehensive grant applications tailored to your organization's needs. The generator utilizes advanced natural language processing techniques to analyze your input and generate a professionally written grant application.</p>
    #     <p>Simply provide us with the necessary information about your charity or organization, project details, objectives, impact, and financial requirements. Our AI model will then generate a customized grant application that showcases your organization's strengths and effectively communicates your project's value.</p>
    #     <p>Save time and effort with our intuitive interface and automated application generation. Focus on making a difference in your community while we handle the complex task of creating compelling grant applications.</p>
    #     <p>Start using the AI Charity Grant Application Generator today and increase your chances of securing funding for your important projects. ✨</p>
    # </div>
    # """
    description_1 = """
    <style>
        .description {
            text-align: center;
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            font-size: 18px;
            color: #ffffff;
        }

        .highlight {
            font-weight: bold;
            color: #0088cc;
        }

        .emoji {
            font-size: 36px;
            margin-bottom: 16px;
        }
    </style>

    <div class="description">
        <h3 class="emoji">✨</h3>
        <p>We understand that writing grant applications can be time-consuming and challenging, so we've developed an AI-powered solution to assist you.</p>
        <p>With our <span class="highlight">AI Charity Grant Application Generator</span>, you can quickly generate comprehensive grant applications tailored to your organization's needs. The generator utilizes advanced natural language processing techniques to analyze your input and generate a professionally written grant application.</p>
        <p>Simply provide us with the necessary information about your charity or organization, project details, objectives, impact, and financial requirements. Our AI model will then generate a customized grant application that showcases your organization's strengths and effectively communicates your project's value.</p>
        <p>Save time and effort with our intuitive interface and automated application generation. Focus on making a difference in your community while we handle the complex task of creating compelling grant applications.</p>
        <p>Start using the <span class="highlight">AI Charity Grant Application Generator</span> today and increase your chances of securing funding for your important projects. </p>
    </div>
    """

    
    st.write(description, unsafe_allow_html=True)
    st.write("---")
    st.markdown(description_1, unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
    <div style="text-align: center;">
        <p>Made with ❤️</p>
    </div> """, unsafe_allow_html=True)

def draft():
    #st.title("📰 Charity Grant Application")
    col1, col2 = st.columns(2)
    first_t = col1.checkbox('Fill in information.')
    second_t = col2.checkbox('Upload the information.')
    if first_t:
        st.header("Please fill out the following information.")
        col1,col3, col2 = st.columns([1,.2,1])
        st.header("General Information")
        # Charity/Organisation name
        organization_name = st.text_input("Charity/Organisation Name")
        # Charity/Company registration number
        registration_number = st.text_input("Charity/Company Registration Number")
        # Address
        address_line1 = st.text_input("Address Line 1")
        address_line2 = st.text_input("Address Line 2")
        town_city = st.text_input("Town/City")
        country = st.text_input("Country")
        postcode = st.text_input("Postcode")
        website = st.text_input("Website")

        st.header("Information about the Organisation")
        # Aims and objectives
        aims_objectives = st.text_area("Aims and Objectives")
        # Constitution (Charity, CIC, other)
        constitution = st.text_area("Constitution (Charity, CIC, other)")
        # Track record, policies and procedures
        track_record = st.text_area("Track Record, Policies and Procedures")
        # Key staff profiles and information on management
        staff_profiles = st.text_area("Key Staff Profiles and Information on Management")
        # WHO, WHAT, WHERE, HOW, WHEN: including project duration and delivery staff, key volunteers, and project partners
        project_details = st.text_area("WHO, WHAT, WHERE, HOW, WHEN (Including Project Duration, Delivery Staff, Key Volunteers, and Project Partners)")
        # The need the project addresses and the difference it will make
        project_need = st.text_area("The Need the Project Addresses and the Difference It Will Make")
        # Project milestones
        milestones = st.text_area("Project Milestones")
        # Sustainability or maintenance plan
        sustainability_plan = st.text_area("Sustainability or Maintenance Plan")
        # Total costs (revenue and capital)
        total_costs = st.text_input("Total Costs (Revenue and Capital)")
        # Awards (if any)
        awards = st.text_area("Awards (if any)")
        # Impact of the project so far
        impact = st.text_area("Impact of the Project So Far")

        # Submit button
        if st.button("Submit"):
            st.success("Application submitted successfully!")
        if st.button("Save Data"):
            # Form validation passed, create a DataFrame with the user's input values
            data = {
                "Charity/Organisation Name": [organization_name],
                "Charity/Company Registration Number": [registration_number],
                "Address Line 1": [address_line1],
                "Address Line 2": [address_line2],
                "Town/City": [town_city],
                "Country": [country],
                "Postcode": [postcode],
                "Website": [website],
                "Aims and Objectives": [aims_objectives],
                "Constitution": [constitution],
                "Track Record, Policies and Procedures": [track_record],
                "Key Staff Profiles and Information on Management": [staff_profiles],
                "WHO, WHAT, WHERE, HOW, WHEN": [project_details],
                "The Need the Project Addresses and the Difference It Will Make": [project_need],
                "Project Milestones": [milestones],
                "Sustainability or Maintenance Plan": [sustainability_plan],
                "Total Costs (Revenue and Capital)": [total_costs],
                "Awards": [awards],
                "Impact of the Project So Far": [impact]
            }

            df = pd.DataFrame(data)
            st.success("Dataframe Created successfully!")
            st.write(df)

            # Save the DataFrame as a CSV file
            #df.to_csv("grant_application.csv", index=False)

            # Download the CSV file
            # Provide download link for text file
            filename = f"CharityApplicationInfo_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
            st.download_button(
                label="Download Data",
                data=df.to_csv(),
                file_name=filename,
                #mime="text/plain"
            )
            # st.markdown("### Download CSV")
            # href = f'<a href="data:file/csv;base64,{df.to_csv(index=False).encode().decode()}">Click here to download the CSV file</a>'
            # st.markdown(href, unsafe_allow_html=True)
    elif second_t:
        # File Upload
        st.header("Upload CSV File")
        st.info("E.g. CharityApplicationInfo_2023-06-02_22-39-30.csv")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

        # Assign values from uploaded CSV file
        if uploaded_file is not None:
            try:
                uploaded_df = pd.read_csv(uploaded_file)
                st.success("CSV file uploaded successfully!")
                st.subheader("DataFrame:")
                st.write(uploaded_df)

                # Assign values back to each variable
                organization_name = uploaded_df["Charity/Organisation Name"].iloc[0]
                registration_number = uploaded_df["Charity/Company Registration Number"].iloc[0]
                address_line1 = uploaded_df["Address Line 1"].iloc[0]
                address_line2 = uploaded_df["Address Line 2"].iloc[0]
                town_city = uploaded_df["Town/City"].iloc[0]
                country = uploaded_df["Country"].iloc[0]
                postcode = uploaded_df["Postcode"].iloc[0]
                website = uploaded_df["Website"].iloc[0]
                aims_objectives = uploaded_df["Aims and Objectives"].iloc[0]
                constitution = uploaded_df["Constitution"].iloc[0]
                track_record = uploaded_df["Track Record, Policies and Procedures"].iloc[0]
                staff_profiles = uploaded_df["Key Staff Profiles and Information on Management"].iloc[0]
                project_details = uploaded_df["WHO, WHAT, WHERE, HOW, WHEN"].iloc[0]
                project_need = uploaded_df["The Need the Project Addresses and the Difference It Will Make"].iloc[0]
                milestones = uploaded_df["Project Milestones"].iloc[0]
                sustainability_plan = uploaded_df["Sustainability or Maintenance Plan"].iloc[0]
                total_costs = uploaded_df["Total Costs (Revenue and Capital)"].iloc[0]
                awards = uploaded_df["Awards"].iloc[0]
                impact = uploaded_df["Impact of the Project So Far"].iloc[0]

                # Display the assigned values
                st.markdown("""
                                <style>
                                    .description {
                                        text-align: left;
                                        font-family: 'Arial', sans-serif;
                                        line-height: 1.6;
                                        font-size: 12px;
                                        color: #0088cc;
                                    }
                                    .highlight {
                                        font-weight: bold;
                                        color: #0088cc;
                                    }
                                </style>

                                <div class="description">
                                    <h3><span class="highlight">Assigned values from uploaded CSV:</span></h3>
                                </div>
                            """,  unsafe_allow_html=True)
                st.write("Charity/Organisation Name:", organization_name)
                st.write("Charity/Company Registration Number:", registration_number)
                st.write("Address Line 1:", address_line1)
                st.write("Address Line 2:", address_line2)
                st.write("Town/City:", town_city)
                st.write("Country:", country)
                st.write("Postcode:", postcode)
                st.write("Website:", website)
                st.write("Aims and Objectives:", aims_objectives)
                st.write("Constitution:", constitution)
                st.write("Track Record, Policies and Procedures:", track_record)
                st.write("Key Staff Profiles and Information on Management:", staff_profiles)
                st.write("WHO, WHAT, WHERE, HOW, WHEN:", project_details)
                st.write("The Need the Project Addresses and the Difference It Will Make:", project_need)
                st.write("Project Milestones:", milestones)
                st.write("Sustainability or Maintenance Plan:", sustainability_plan)
                st.write("Total Costs (Revenue and Capital):", total_costs)
                st.write("Awards:", awards)
                st.write("Impact of the Project So Far:", impact)

            except Exception as e:
                st.error("Error occurred while reading the uploaded file. Please make sure it is a valid CSV file.")
    brand_button = st.button("Generate Application")
    sections = [""" ## Cover Letter

                    The cover letter is the first impression of your grant application. It should briefly introduce your organization, your project, and your request for funding. It should also highlight how your project aligns with the grantor's mission and goals.

                    - Start with a salutation that addresses the grantor by name or title.
                    - State the name of your organization and its mission statement.
                    - Summarize the main problem or need that your project aims to address and why it is important.
                    - Describe your project's objectives, activities, outcomes, and impact.
                    - Specify the amount of funding you are requesting and how it will be used.
                    - Explain how your project matches the grantor's priorities and interests.
                    Don't End with a complimentary close and signature in this section.
                    """,
                """## Executive Summary

                    The executive summary is a concise overview of your grant proposal. It should capture the attention of the grantor and persuade them to read further. It should also provide the key information that they need to make a decision.

                    - State the name of your organization and its mission statement.
                    - Summarize the main problem or need that your project aims to address and why it is important.
                    - Describe your project's objectives, activities, outcomes, and impact.
                    - Specify the amount of funding you are requesting and how it will be used.
                    - Explain how your project matches the grantor's priorities and interests.
                    - Highlight your organization's qualifications, experience, and credibility.
                    - Mention any partners or collaborators involved in your project.""",

                """## Need Statement

                    The need statement is where you demonstrate the significance and urgency of the problem or need that your project aims to address. It should provide evidence and data to support your claims and show how your project will fill a gap or create a change.

                    - Define the problem or need clearly and specifically.
                    - Provide relevant facts, statistics, examples, stories, or testimonials to illustrate the problem or need.
                    - Explain how the problem or need affects your target population or community and why they are in need of help.
                    - Identify the root causes or contributing factors of the problem or need.
                    - Show how your project will address the problem or need effectively and efficiently.""",
                """## Project Description

                    The project description is where you describe what you plan to do, how you plan to do it, and what you expect to achieve. It should provide enough details for the grantor to understand your project's design, implementation, and evaluation.

                    - State your project's objectives clearly and measurably. They should follow SMART criteria (specific, measurable, achievable, relevant, and time-bound).
                    - Outline your project's activities or methods step by step. They should be logical, realistic, and appropriate for achieving your objectives.
                    - Describe your project's outcomes or results. They should be tangible, observable, and verifiable. They should also indicate how you will measure success and impact.
                    - Explain how your project's outcomes or results will contribute to solving the problem or need that you identified in the need statement.
                    - Include a timeline or schedule for your project's activities and milestones.
                    - Include a budget or cost breakdown for your project's expenses and income. It should be realistic, accurate, and transparent. It should also show how you will use the grant funds efficiently and responsibly.""",

                """## Organization Information

                    The organization information is where you introduce your organization and its background, history, vision, values, goals, achievements, staff, board, partners, and supporters. It should demonstrate your organization's credibility, capacity, and suitability for carrying out the project.

                    - Provide a brief overview of your organization's history, vision, values, goals, achievements, staff, board, partners, and supporters.
                    - Highlight your organization's strengths, expertise, experience, reputation, recognition, awards, or accreditations that are relevant to your project or field of work.
                    - Explain how your organization's mission and goals align with those of the grantor.
                    - Provide evidence of your organization's financial stability, sustainability, accountability, transparency, and governance practices.
                    """,
                
                """## Conclusion

                    The conclusion is where you summarize your grant proposal and restate your request for funding. It should also express your gratitude and appreciation for the grantor's attention and consideration.

                    - Summarize the main points of your grant proposal: the problem or need that you aim to address; your project's objectives; activities; outcomes; impact; budget; alignment with the grantor's priorities; and organization's qualifications.
                    - Restate the amount of funding you are requesting and how it will be used.
                    - Emphasize how your project will make a difference in solving the problem or need that you identified in the need statement.
                    - Thank the grantor for their consideration and invite them to contact you for more information.
                    - End with a complimentary close and your signature.
                    """
                ]
    main_app = []
    if brand_button:
        #try:
        with open('Prompts/draftt.txt', 'r') as f:
            response = f.readlines()
        prompt = ''.join(response)
        prompt = '"""' + prompt + '"""'
        template = prompt
        prompt_template = PromptTemplate(template=template, input_variables=["section","organization_name", "registration_number", "address_line1", "address_line2", "town_city", "country", "postcode",
                                                                            "website", "aims_objectives", "constitution", "track_record", "staff_profiles", "project_details", "project_need", 
                                                                            "milestones", "sustainability_plan", "total_costs", "awards", "impact"])#, validate_template=False)
        llm_chain = LLMChain(prompt=prompt_template, llm=OpenAI(model_name="gpt-4"))
        #llm = OpenAI(model_name=model_name, temperature=temperature, streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, max_tokens=max_tokens[model_name])
        for i in range(len(sections)):
            resp = llm_chain.predict(section=sections[i],organization_name=organization_name, registration_number=registration_number, address_line1=address_line1, address_line2=address_line2, town_city=town_city, 
                                    country=country, postcode=postcode, website=website, aims_objectives=aims_objectives, constitution=constitution, track_record=track_record, staff_profiles=staff_profiles, 
                                    project_details=project_details, project_need=project_need, milestones=milestones, sustainability_plan=sustainability_plan, total_costs=total_costs, awards=awards, impact=impact)
            main_app.append("\n")
            main_app.append(resp)
        
        text = "\n".join(main_app)
        st.success(text)
        # Save output to text file with dynamic filename
        filename = f"charity_application_{organization_name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        # with open(filename, 'w', encoding="utf-8") as f:
        #     f.write(resp)

        # Provide download link for text file
        st.download_button(
            label="Download Application",
            data=text,
            file_name=filename,
            mime="text/plain"
        )
        # except:
        #     st.error("Try again! Fill in the information properly.")

def specific():
    col1, col2 = st.columns(2)
    first_t = col1.checkbox('Fill in information.')
    second_t = col2.checkbox('Upload the information.')
    if first_t:
        st.header("Please fill out the following information.")
        col1,col3, col2 = st.columns([1,.2,1])
        st.header("General Information")
        # Charity/Organisation name
        organization_name = st.text_input("Charity/Organisation Name")
        # Charity/Company registration number
        registration_number = st.text_input("Charity/Company Registration Number")
        # Address
        address_line1 = st.text_input("Address Line 1")
        address_line2 = st.text_input("Address Line 2")
        town_city = st.text_input("Town/City")
        country = st.text_input("Country")
        postcode = st.text_input("Postcode")
        website = st.text_input("Website")

        st.header("Information about the Organisation")
        # Aims and objectives
        aims_objectives = st.text_area("Aims and Objectives")
        # Constitution (Charity, CIC, other)
        constitution = st.text_area("Constitution (Charity, CIC, other)")
        # Track record, policies and procedures
        track_record = st.text_area("Track Record, Policies and Procedures")
        # Key staff profiles and information on management
        staff_profiles = st.text_area("Key Staff Profiles and Information on Management")
        # WHO, WHAT, WHERE, HOW, WHEN: including project duration and delivery staff, key volunteers, and project partners
        project_details = st.text_area("WHO, WHAT, WHERE, HOW, WHEN (Including Project Duration, Delivery Staff, Key Volunteers, and Project Partners)")
        # The need the project addresses and the difference it will make
        project_need = st.text_area("The Need the Project Addresses and the Difference It Will Make")
        # Project milestones
        milestones = st.text_area("Project Milestones")
        # Sustainability or maintenance plan
        sustainability_plan = st.text_area("Sustainability or Maintenance Plan")
        # Total costs (revenue and capital)
        total_costs = st.text_input("Total Costs (Revenue and Capital)")
        # Awards (if any)
        awards = st.text_area("Awards (if any)")
        # Impact of the project so far
        impact = st.text_area("Impact of the Project So Far")

        # Submit button
        # if st.button("Submit"):
        #     st.success("Application submitted successfully!")
        if st.button("Save Data"):
            # Form validation passed, create a DataFrame with the user's input values
            data = {
                "Charity/Organisation Name": [organization_name],
                "Charity/Company Registration Number": [registration_number],
                "Address Line 1": [address_line1],
                "Address Line 2": [address_line2],
                "Town/City": [town_city],
                "Country": [country],
                "Postcode": [postcode],
                "Website": [website],
                "Aims and Objectives": [aims_objectives],
                "Constitution": [constitution],
                "Track Record, Policies and Procedures": [track_record],
                "Key Staff Profiles and Information on Management": [staff_profiles],
                "WHO, WHAT, WHERE, HOW, WHEN": [project_details],
                "The Need the Project Addresses and the Difference It Will Make": [project_need],
                "Project Milestones": [milestones],
                "Sustainability or Maintenance Plan": [sustainability_plan],
                "Total Costs (Revenue and Capital)": [total_costs],
                "Awards": [awards],
                "Impact of the Project So Far": [impact]
            }

            df = pd.DataFrame(data)
            st.success("Dataframe Created successfully!")
            st.write(df)

            # Save the DataFrame as a CSV file
            #df.to_csv("grant_application.csv", index=False)

            # Download the CSV file
            # Provide download link for text file
            filename = f"CharityApplicationInfo_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
            st.download_button(
                label="Download Data",
                data=df.to_csv(),
                file_name=filename,
                #mime="text/plain"
            )
    elif second_t:
        # File Upload
        st.header("Upload CSV File")
        st.info("E.g. CharityApplicationInfo_2023-06-02_22-39-30.csv")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

        # Assign values from uploaded CSV file
        if uploaded_file is not None:
            try:
                uploaded_df = pd.read_csv(uploaded_file)
                st.success("Data uploaded successfully!")
                st.subheader("DataFrame:")
                st.write(uploaded_df)

                # Assign values back to each variable
                organization_name = uploaded_df["Charity/Organisation Name"].iloc[0]
                registration_number = uploaded_df["Charity/Company Registration Number"].iloc[0]
                address_line1 = uploaded_df["Address Line 1"].iloc[0]
                address_line2 = uploaded_df["Address Line 2"].iloc[0]
                town_city = uploaded_df["Town/City"].iloc[0]
                country = uploaded_df["Country"].iloc[0]
                postcode = uploaded_df["Postcode"].iloc[0]
                website = uploaded_df["Website"].iloc[0]
                aims_objectives = uploaded_df["Aims and Objectives"].iloc[0]
                constitution = uploaded_df["Constitution"].iloc[0]
                track_record = uploaded_df["Track Record, Policies and Procedures"].iloc[0]
                staff_profiles = uploaded_df["Key Staff Profiles and Information on Management"].iloc[0]
                project_details = uploaded_df["WHO, WHAT, WHERE, HOW, WHEN"].iloc[0]
                project_need = uploaded_df["The Need the Project Addresses and the Difference It Will Make"].iloc[0]
                milestones = uploaded_df["Project Milestones"].iloc[0]
                sustainability_plan = uploaded_df["Sustainability or Maintenance Plan"].iloc[0]
                total_costs = uploaded_df["Total Costs (Revenue and Capital)"].iloc[0]
                awards = uploaded_df["Awards"].iloc[0]
                impact = uploaded_df["Impact of the Project So Far"].iloc[0]
            except Exception as e:
                st.error("Error occurred while reading the uploaded file. Please make sure it is a valid CSV file.")
    
    st.header("Fund Information")
    # Name of the fund they wish to apply for
    fund_name = st.text_input("Name of the Fund")
    # Information about the fund, such as its criteria for funding
    fund_criteria = st.text_area("Information about the Fund (Criteria for Funding)")
    # Reason for why the charity believes they should be granted the funding
    reason_for_grant = st.text_area("Reason for Grant")
    # Text version of the fund criteria that they have copied and pasted
    copied_criteria = st.text_area("Fund Criteria")
    # The amount of money they are applying for
    requested_amount = st.text_input("Requested Amount")

    sp_button = st.button("Generate Application")
    sections = ["""## Cover Letter

                    The cover letter is the first impression of your grant application. It should briefly introduce your organization, your project, and your request for funding. It should also highlight how your project aligns with the grantor's mission and goals.

                    - Start with a salutation that addresses the grantor by name or title.
                    - State the name of your organization and its mission statement.
                    - Summarize the main problem or need that your project aims to address and why it is important.
                    - Describe your project's objectives, activities, outcomes, and impact.
                    - Specify the amount of funding you are requesting and how it will be used.
                    - Explain how your project matches the grantor's priorities and interests.
                    Don't End with a complimentary close and signature in this section.
                    """,
                """## Executive Summary

                    The executive summary is a concise overview of your grant proposal. It should capture the attention of the grantor and persuade them to read further. It should also provide the key information that they need to make a decision.

                    - State the name of your organization and its mission statement.
                    - Summarize the main problem or need that your project aims to address and why it is important.
                    - Describe your project's objectives, activities, outcomes, and impact.
                    - Specify the amount of funding you are requesting and how it will be used.
                    - Explain how your project matches the grantor's priorities and interests.
                    - Highlight your organization's qualifications, experience, and credibility.
                    - Mention any partners or collaborators involved in your project.""",

                """## Need Statement

                    The need statement is where you demonstrate the significance and urgency of the problem or need that your project aims to address. It should provide evidence and data to support your claims and show how your project will fill a gap or create a change.

                    - Define the problem or need clearly and specifically.
                    - Provide relevant facts, statistics, examples, stories, or testimonials to illustrate the problem or need.
                    - Explain how the problem or need affects your target population or community and why they are in need of help.
                    - Identify the root causes or contributing factors of the problem or need.
                    - Show how your project will address the problem or need effectively and efficiently.""",
                """## Project Description

                    The project description is where you describe what you plan to do, how you plan to do it, and what you expect to achieve. It should provide enough details for the grantor to understand your project's design, implementation, and evaluation.

                    - State your project's objectives clearly and measurably. They should follow SMART criteria (specific, measurable, achievable, relevant, and time-bound).
                    - Outline your project's activities or methods step by step. They should be logical, realistic, and appropriate for achieving your objectives.
                    - Describe your project's outcomes or results. They should be tangible, observable, and verifiable. They should also indicate how you will measure success and impact.
                    - Explain how your project's outcomes or results will contribute to solving the problem or need that you identified in the need statement.
                    - Include a timeline or schedule for your project's activities and milestones.
                    - Include a budget or cost breakdown for your project's expenses and income. It should be realistic, accurate, and transparent. It should also show how you will use the grant funds efficiently and responsibly.""",

                """## Organization Information

                    The organization information is where you introduce your organization and its background, history, vision, values, goals, achievements, staff, board, partners, and supporters. It should demonstrate your organization's credibility, capacity, and suitability for carrying out the project.

                    - Provide a brief overview of your organization's history, vision, values, goals, achievements, staff, board, partners, and supporters.
                    - Highlight your organization's strengths, expertise, experience, reputation, recognition, awards, or accreditations that are relevant to your project or field of work.
                    - Explain how your organization's mission and goals align with those of the grantor.
                    - Provide evidence of your organization's financial stability, sustainability, accountability, transparency, and governance practices.
                    """,
                
                """## Conclusion

                    The conclusion is where you summarize your grant proposal and restate your request for funding. It should also express your gratitude and appreciation for the grantor's attention and consideration.

                    - Summarize the main points of your grant proposal: the problem or need that you aim to address; your project's objectives; activities; outcomes; impact; budget; alignment with the grantor's priorities; and organization's qualifications.
                    - Restate the amount of funding you are requesting and how it will be used.
                    - Emphasize how your project will make a difference in solving the problem or need that you identified in the need statement.
                    - Thank the grantor for their consideration and invite them to contact you for more information.
                    - End with a complimentary close and your signature.
                    """
                ]
    main_appli = []
    if sp_button:
        #try:
        with open('Prompts/specific.txt', 'r') as f:
            response = f.readlines()
        prompt = ''.join(response)
        prompt = '"""' + prompt + '"""'
        template = prompt
        prompt_template = PromptTemplate(template=template, input_variables=["section","organization_name", "registration_number", "address_line1", "address_line2", "town_city", "country", "postcode",
                                                                            "website", "aims_objectives", "constitution", "track_record", "staff_profiles", "project_details", "project_need", 
                                                                            "milestones", "sustainability_plan", "total_costs", "awards", "impact", "fund_name", "fund_criteria", "reason_for_grant", 
                                                                            "copied_criteria", "requested_amount"])#, validate_template=False)
        llm_chain = LLMChain(prompt=prompt_template, llm=OpenAI(model_name="gpt-4"))
        #llm = OpenAI(model_name=model_name, temperature=temperature, streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, max_tokens=max_tokens[model_name])
        for i in range(len(sections)):
            resp = llm_chain.predict(section=sections[i],organization_name=organization_name, registration_number=registration_number, address_line1=address_line1, address_line2=address_line2, town_city=town_city, 
                                    country=country, postcode=postcode, website=website, aims_objectives=aims_objectives, constitution=constitution, track_record=track_record, staff_profiles=staff_profiles, 
                                    project_details=project_details, project_need=project_need, milestones=milestones, sustainability_plan=sustainability_plan, total_costs=total_costs, awards=awards, impact=impact,
                                    fund_name=fund_name, fund_criteria=fund_criteria, reason_for_grant=reason_for_grant, copied_criteria=copied_criteria, requested_amount=requested_amount)
            main_appli.append("\n")
            main_appli.append(resp)
        
        text = "\n".join(main_appli)
        st.success(text)
        # Save output to text file with dynamic filename
        filename = f"charity_application_{organization_name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        # with open(filename, 'w', encoding="utf-8") as f:
        #     f.write(resp)

        # Provide download link for text file
        st.download_button(
            label="Download Application",
            data=text,
            file_name=filename,
            mime="text/plain"
        )
# if __name__ == "__main__":
#     main()

functions = [
        "Home",
        "Draft Charity Application",
        "Specific Charity Application",
    ]



selected_function = st.sidebar.selectbox("Select Option", functions)
if selected_function == "Home":
    main()
elif selected_function == "Draft Charity Application":
    draft()
elif selected_function == "Specific Charity Application":
    specific()