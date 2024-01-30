import streamlit as st
from dotenv import load_dotenv
from utils import *


def main():
    load_dotenv()

    st.set_page_config(page_title="Invoice Extraction Bot")
    st.title("Invoice Extraction LLM... 💁 ")
    st.subheader("Extracting invoice data")


    # Upload the Invoices (pdf files)
    pdf = st.file_uploader("Upload invoices (PDF)", type=["pdf"],accept_multiple_files=True)

    submit=st.button("Extract Data")

    if submit:
        with st.spinner('Wait for it...'):
            df=create_docs(pdf)
            st.write(df.head())

            data_as_csv= df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download data as CSV", 
                data_as_csv, 
                "invoice-data.csv",
                "text/csv",
                key="download-tools-csv",
            )
        st.success("Save your time ❤️ John Tan")


#Invoking main function
if __name__ == '__main__':
    main()
