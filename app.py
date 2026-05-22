import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Etsy AI SEO Generator",
    page_icon="🛍️"
)

st.title("🛍️ Etsy AI SEO Generator")
st.write("Generate Etsy SEO titles, tags, and descriptions using AI.")

product_name = st.text_input("Enter your Etsy product idea")

if st.button("Generate SEO"):

    if not product_name.strip():
        st.warning("Please enter a product idea.")

    else:

        prompt = f"""
You are an Etsy SEO expert specialized in Etsy US Print-on-Demand products.

Generate SEO content for this product:

{product_name}

Need output:

1. Etsy Title
- Between 120 to 140 characters
- High converting
- SEO optimized
- No trademark words

2. Etsy Tags
- Give exactly 13 tags
- Each tag under 20 characters

3. Product Description
- Attractive
- Buyer focused
- Easy to read
- Good conversion style
"""

        with st.spinner("Generating SEO content..."):

            client = Groq(
                api_key=st.secrets["GROQ_API_KEY"]
            )

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama-3.1-8b-instant"
            )

            result = chat_completion.choices[0].message.content

            st.subheader("Generated SEO Content")
            st.write(result)