import base64
import string
import streamlit as st
from pathlib import Path
import os
import json
from dotenv import load_dotenv
from utils.image_generation import generate_prompt_from_image 
from utils.image_generation import text_to_image
from utils.image_generation import image_variation_sdxl
from utils.background_removal import background_removal_titan
from PIL import Image

import logging
logger = logging.getLogger(__name__)
STYLES = ["anime", "analog-film" , "cinematic", "comic-book", "digital-art","enhance", "fantasy-art", "isometric", "line-art", "low-poly", "modeling-compound","neon-punk", "origami", "photographic", "pixel-art", "tile-texture","3d-model",]

def main():
    # load environment variables
    load_dotenv()
    
    st.set_page_config(page_title="Image Generation", )
    
    image_gen, image_variation, image_background_removal = st.tabs(['Image Generation', 'Image Variation', 'Background Removal'])
    
    with image_gen:
        st.title("Image Generation")
        st.subheader("Input title and description")
        
    
    with image_variation:
        st.title("图像变体生成")
        st.subheader("上传原图，选择变体的风格")
        
        # 初始化 session state
        if 'uploaded_file' not in st.session_state:
            st.session_state.uploaded_file = None
        if 'selected_style' not in st.session_state:
            st.session_state.selected_style = STYLES[0]
        if 'pre_prompts' not in st.session_state:
            st.session_state.pre_prompts = ""
        if 'generated_image' not in st.session_state:
            st.session_state.generated_image = None
        
        uploaded_file = st.file_uploader('choose your origin image', type=["webp", "png", "jpg", "jpeg"], key="variation_img")
        if uploaded_file is not None:
            st.session_state.uploaded_file = uploaded_file
            process_uploaded_image()
        
    with image_background_removal:
        st.title("背景移除")
        st.subheader("上传原始图片")
        File = st.file_uploader('choose your origin image', type=["webp", "png", "jpg", "jpeg"], key="background_removal_img")
        result = st.button("submit", key="submit_image_for_background_removal")
        if result:
            if File is not None:
                save_folder = os.getenv("save_folder")
                print(save_folder)
                print('filename:' + File.name)

                save_path = Path(save_folder, File.name)
                with open(save_path, mode='wb') as w:
                    w.write(File.getvalue())

                if save_path.exists():
                    file_name = save_path
                    # 显示图片功能
                    st.subheader("原始图片")
                    img = Image.open(File)
                    st.image(File, caption='Origin Image', use_column_width=True)
                    new_image = background_removal_titan(save_path)
                    st.subheader("去除背景后")
                    st.image(new_image, caption='New Image', use_column_width=True)
            else:
                st.write('请上传图片')
                    
def process_uploaded_image():
    # 创建可更新的容器
    image_container = st.empty()
    style_container = st.empty()
    prompt_container = st.empty()
    generate_button_container = st.empty()
    result_container = st.empty()

    File = st.session_state.uploaded_file
    save_folder = os.getenv("save_folder")
    save_path = Path(save_folder, File.name)
    
    with open(save_path, mode='wb') as w:
        w.write(File.getvalue())

    if save_path.exists():
        file_name = save_path
        img = Image.open(File)
        width, height = img.size

        # 显示上传的图片
        if width > 512:
            image_container.image(File, caption='Uploaded Image', width=512)
        else:
            image_container.image(File, caption='Uploaded Image', use_column_width=True)

        # 风格选择
        selected_style = style_container.selectbox("选择风格", STYLES, index=STYLES.index(st.session_state.selected_style))
        st.session_state.selected_style = selected_style

        # 生成并编辑提示词
        if st.session_state.pre_prompts == "":
            st.session_state.pre_prompts = generate_prompt_from_image(file_name, style=selected_style)
        
        pre_prompts = prompt_container.text_area("Edit Prompt:", value=st.session_state.pre_prompts)
        st.session_state.pre_prompts = pre_prompts

        # 生成新图像按钮
        if generate_button_container.button('Generate New Image'):
            new_image = image_variation_sdxl(file_name, style=selected_style, positive_prompt=pre_prompts)
            st.session_state.generated_image = new_image
            
            result_container.image(new_image, caption='Generated Image', use_column_width=True)

        # 如果之前已经生成了图像，显示它
        elif st.session_state.generated_image is not None:
            result_container.image(st.session_state.generated_image, caption='Generated Image', use_column_width=True)


if __name__ == '__main__':
    main()
