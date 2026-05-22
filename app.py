import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(
    page_title="Etsy Image SEO Generator",
    page_icon="🛍️"
)

st.title("🛍️ Etsy Image SEO Generator")
st.write("Upload your design image and generate Etsy SEO instantly.")

# Gemini API Key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Upload image
uploaded_image = st.file_uploader(
    "Upload Design Image",
    type=["png", "jpg", "jpeg", "webp"]
)

# Product type
product_type = st.selectbox(
    "Select Product Type",
    [
        "T-Shirt",
        "Sweatshirt",
        "Hoodie",
        "Poster",
        "Mug",
        "Sticker",
        "Digital Pet Portrait",
        "Planner",
        "Other"
    ]
)

# Optional details
extra_info = st.text_input(
    "Extra Details (Optional)",
    placeholder="Example: dog mom floral style personalized gift"
)

# Show uploaded image
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Design", use_container_width=True)

# Generate button
if st.button("Generate Etsy SEO"):

    if not uploaded_image:
        st.warning("Please upload an image first.")

    else:

        with st.spinner("Analyzing image and generating SEO..."):

            prompt = f"""
You are an Etsy SEO expert specialized in Etsy US market.

Analyze the uploaded design image carefully.

Product Type:
{product_type}

Extra Details:
{extra_info}

First understand:
- design style
- visible text
- target audience
- color theme
- niche
- emotional appeal

Then generate:

1. Image Analysis
Explain what the image/design contains.

2. Etsy Titles
Generate 5 high-converting Etsy titles.
Each title should be 120-140 characters.

3. Etsy Tags
Generate exactly 13 Etsy tags.
Each tag must be under 20 characters.

4. Product Description
Write an attractive Etsy description.

5. Thumbnail Idea
Suggest one high-converting thumbnail idea.

Rules:
- No trademark words
- No copyrighted content
- No keyword stuffing
- Use buyer-focused SEO keywords
"""

            model = genai.GenerativeModel("gemini-2.0-flash")

            response = model.generate_content(
                [prompt, image]
            )

            result = response.text

            st.subheader("Generated Etsy SEO")
            st.write(result)

            # Download button
            st.download_button(
                label="Download SEO Result",
                data=result,
                file_name="etsy_seo_result.txt",
                mime="text/plain"
            )