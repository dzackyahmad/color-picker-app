import streamlit as st

def inject_css_and_js():
    st.markdown("""
        <style>
            .main-title {
                text-align: center;
                font-size: 42px;
                font-weight: bold;
                color: #444;
                margin-bottom: 6px;
            }
            .sub-title {
                text-align: center;
                font-size: 18px;
                color: #888;
                margin-bottom: 30px;
            }
            .color-box {
                width: 100%;
                height: 100px;
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
                cursor: pointer;
            }
            .hex-label {
                text-align: center;
                margin-top: 8px;
                font-weight: bold;
                color: #333;
            }
            footer {
                text-align: center;
                font-size: 16px;
                padding: 20px 0;
                margin-top: 40px;
                border-top: 1px solid #ddd;
                color: #666;
            }
        </style>
        <script>
            function copyToClipboard(text) {
                navigator.clipboard.writeText(text).then(function() {
                    alert('✅ Copied to clipboard: ' + text);
                }, function(err) {
                    alert('❌ Failed to copy text: ', err);
                });
            }
        </script>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown("<div class='main-title'>🎨 Dominant Color Picker</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Upload gambar dan dapatkan warna dominan dan palet siap pakai</div>", unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <footer>
            Dibuat oleh <strong>Dzacky Ahmad</strong> – <strong>140810230043</strong><br>
            Tugas Praktikum AI: Color Picker Generator from Image – 2025
        </footer>
    """, unsafe_allow_html=True)
