import streamlit as st
from groq import Groq

st.set_page_config(page_title="Etsy AI SEO Generator", page_icon="🛍️")

st.title("🛍️ Etsy AI SEO Generator")
st.write("Generate Etsy titles, tags, and descriptions using AI.")

product_name = st.text_input("Enter your product name or idea")

if st.button("Generate SEO"):
    if not product_name.strip():
        st.warning("Please enter a product name.")
    else:
        prompt = f"""
You are an Etsy SEO expert specialized in US Print-on-Demand listings.

Product idea:
{product_name}

Create:

1. Etsy Title
- 120 to 140 characters
- SEO optimized
- Buyer-focused
- No trademark/copyright words

2. Etsy Tags
- 13 tags
- Each tag under 20 characters
- Etsy US buyer intent keywords

3. Description
- Attractive Etsy product description
- Clear benefits
- Good for conversion
- No keyword stuffing
"""

        with st.spinner("Generating SEO content..."):
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama3-8b-8192",
            )

            result = chat_completion.choices[0].message.content
            st.write(result)