import streamlit as st
import numpy as np
import cv2
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from io import BytesIO
from ui import inject_css_and_js, render_header, render_footer

st.set_page_config(page_title="Color Picker 🎨", layout="wide")

inject_css_and_js()
render_header()

# ===== Fungsi =====

def get_dominant_colors(image, k=5):
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (150, 150))
    img = img.reshape((-1, 3))
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(img)
    return model.cluster_centers_.astype(int)

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(rgb)

def generate_palette_image(hex_colors):
    width, height = 600, 100
    bar_width = width // len(hex_colors)
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    for i, hex_code in enumerate(hex_colors):
        rgb = tuple(int(hex_code[j:j+2], 16) for j in (1, 3, 5))
        draw.rectangle([i * bar_width, 0, (i+1) * bar_width, height], fill=rgb)

    return image

# ===== Upload UI =====

uploaded_file = st.file_uploader("📁 Unggah Gambar Anda", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="📷 Gambar yang Diupload", use_container_width=True)

    with st.spinner("🎯 Menganalisis warna dominan..."):
        dominant_colors = get_dominant_colors(image, k=5)
        hex_colors = [rgb_to_hex(c).upper() for c in dominant_colors]

        st.subheader("🎨 5 Warna Dominan")
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                hex_code = hex_colors[i]
                st.markdown(f"""
                    <div class='color-box' style='background-color:{hex_code}' onclick="copyToClipboard('{hex_code}')"></div>
                    <div class='hex-label'>{hex_code}</div>
                """, unsafe_allow_html=True)
                st.code(f"RGB{tuple(dominant_colors[i])}")

    # Generate dan download palet sebagai PNG
    st.subheader("🖼️ Unduh Palet sebagai Gambar")
    palet_img = generate_palette_image(hex_colors)
    buf = BytesIO()
    palet_img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button("📥 Download PNG", byte_im, file_name="palette.png", mime="image/png")

render_footer()
