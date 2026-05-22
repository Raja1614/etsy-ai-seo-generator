import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(
    page_title="Etsy Image SEO Generator",
    page_icon="🛍️"
)

st.title("🛍️ Etsy Image SEO Generator")
st.write("Upload your design image and generate Etsy SEO.")

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Upload image
uploaded_image = st.file_uploader(
    "Upload Design Image",
    type=["png", "jpg", "jpeg", "webp"]
)

# Product type dropdown
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

# Extra details
extra_info = st.text_input(
    "Extra Details Optional",
    placeholder="Example: dog mom floral style personalized gift"
)

# Preview uploaded image
if uploaded_image:
    image = Image.open(uploaded_image).convert("RGB")
    image.thumbnail((800, 800))
    st.image(image, caption="Uploaded Design", use_container_width=True)

# Generate button
if st.button("Generate Etsy SEO"):

    if not uploaded_image:
        st.warning("Please upload an image first.")

    else:

        try:

            with st.spinner("Analyzing image and generating SEO..."):

                image = Image.open(uploaded_image).convert("RGB")
                image.thumbnail((800, 800))

                prompt = f"""
You are an Etsy SEO expert specialized in Etsy US market.

Analyze this uploaded design image carefully.

Product Type:
{product_type}

Extra Details:
{extra_info}

Generate the following:

1. Image Analysis
Explain the design simply.

2. Etsy Titles
Generate 3 SEO optimized Etsy titles.
Each title should be between 120 and 140 characters.

3. Etsy Tags
Generate exactly 13 Etsy tags.
Each tag must be under 20 characters.

4. Product Description
Write an attractive Etsy product description.

5. Thumbnail Idea
Suggest one thumbnail idea.

Rules:
- No trademark words
- No copyrighted words
- No keyword stuffing
- Use Etsy US buyer intent keywords
"""

                # Free-tier friendly Gemini model
                model = genai.GenerativeModel("gemini-1.5-flash")

                response = model.generate_content(
                    [prompt, image]
                )

                result = response.text

                st.subheader("Generated Etsy SEO")
                st.write(result)

                # Download result
                st.download_button(
                    label="Download SEO Result",
                    data=result,
                    file_name="etsy_seo_result.txt",
                    mime="text/plain"
                )

        except Exception as e:

            st.error(
                "Gemini free quota limit reached or temporary API issue. Please wait and try again later with a smaller image."
            )