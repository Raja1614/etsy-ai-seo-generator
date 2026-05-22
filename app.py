import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Etsy Image SEO Generator", page_icon="🛍️")

st.title("🛍️ Etsy Image SEO Generator")
st.write("Upload a design image and generate Etsy title, tags, and description.")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

uploaded_image = st.file_uploader(
    "Upload your design image",
    type=["png", "jpg", "jpeg", "webp"]
)

product_type = st.selectbox(
    "Select product type",
    [
        "T-Shirt",
        "Sweatshirt",
        "Hoodie",
        "Mug",
        "Poster",
        "Digital Pet Portrait",
        "Sticker",
        "Planner",
        "Other"
    ]
)

extra_info = st.text_input(
    "Extra details optional",
    placeholder="Example: dog mom, floral style, personalized gift"
)

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Design", use_container_width=True)

if st.button("Generate Etsy SEO"):
    if not uploaded_image:
        st.warning("Please upload a design image first.")
    else:
        with st.spinner("Analyzing image and generating Etsy SEO..."):

            prompt = f"""
You are an Etsy SEO expert for US buyers.

Analyze this uploaded product design image carefully.

Product type:
{product_type}

Extra details:
{extra_info}

First identify:
- Main object/design
- Text visible in design if any
- Style
- Color theme
- Target buyer
- Best Etsy niche

Then generate Etsy SEO content.

Output format:

1. Image Analysis:
Explain what the design shows in simple words.

2. Etsy Titles:
Give 5 SEO optimized Etsy titles.
Each title must be 120 to 140 characters.
Avoid trademark, brand, celebrity, movie, cartoon, sports team, or copyrighted words.

3. Etsy Tags:
Give exactly 13 Etsy tags.
Each tag must be under 20 characters.
Use US Etsy buyer keywords.

4. Product Description:
Write a high-converting Etsy description.
Make it attractive and buyer-focused.

5. Thumbnail Idea:
Give one strong thumbnail image idea for this listing.

Rules:
- No keyword stuffing
- No false claims
- No copyrighted words
- No digital terms if product is physical
- If product is digital, clearly mention digital file only
"""

            model = genai.GenerativeModel("gemini-1.5-flash")

            response = model.generate_content([prompt, image])

            st.subheader("Generated Etsy SEO")
            st.write(response.text)

            st.download_button(
                label="Download SEO Result",
                data=response.text,
                file_name="etsy_seo_result.txt",
                mime="text/plain"
            )