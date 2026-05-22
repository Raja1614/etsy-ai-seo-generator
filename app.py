import streamlit as st
import requests

st.set_page_config(page_title="Etsy AI SEO Generator", layout="centered")

st.title("Etsy AI SEO Generator")
st.write("Free local AI tool for Etsy POD sellers")

product_type = st.text_input("Product Type", "T-shirt")
niche = st.text_input("Niche", "Dog Mom")
design_text = st.text_input("Design Text", "My Dog Is My Therapist")
style = st.text_input("Style", "Minimalist funny pet lover design")

if st.button("Generate Etsy SEO"):

    prompt = f"""
    Act as an expert Etsy SEO specialist for US Print-on-Demand sellers.

    Product Details:
    Product Type: {product_type}
    Niche: {niche}
    Design Text: {design_text}
    Style: {style}

    IMPORTANT RULES:
    - Do not use trademarked words.
    - Do not use copyrighted phrases.
    - Do not use irrelevant keywords.
    - Focus on Etsy US buyer search behavior.
    - Output must be clean and ready to copy.

    Generate the output in this exact format:

    ETSY TITLES:
    - Give 5 high-converting Etsy SEO titles.
    - Each title must be between 130 and 140 characters.
    - Use strong buyer-intent keywords naturally.
    - Avoid keyword stuffing.

    ETSY TAGS:
    - Give exactly 13 Etsy tags.
    - Each tag must NOT exceed 20 characters.
    - Optimize tags to use 18–20 characters when possible.
    - Use unique buyer search phrases.
    - Avoid repeating the same keywords.

    DESCRIPTION:
    - Write a high-converting Etsy product description.
    - Include emotional opening.
    - Include product details.
    - Include gift use cases.
    - Include clear closing CTA.

    PINTEREST:
    - Give 3 Pinterest titles.
    - Give 3 Pinterest descriptions.

    THUMBNAIL TEXT IDEAS:
    - Give 5 short thumbnail text ideas.
    """

    with st.spinner("Generating Etsy SEO content..."):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()["response"]

    st.subheader("Generated Etsy SEO Content")
    st.write(result)

    st.download_button(
        label="Download SEO Content",
        data=result,
        file_name="etsy_seo_content.txt",
        mime="text/plain"
    )