import base64
import string
import streamlit as st
from pathlib import Path
import os
import json
from dotenv import load_dotenv
from utils.listing_voc_prompt import image_to_text, text_to_text, gen_listing_prompt, gen_voc_prompt
from utils.listing_voc_agents import create_listing

from PIL import Image

import logging
logger = logging.getLogger(__name__)

def main():
    # load environment variables
    load_dotenv()
    
    st.set_page_config(page_title="AI Listing", )
    language_options = ['English', 'Chinese']
    language_lable = st.sidebar.selectbox('Select Language', language_options)
    
    mode_lable = 'PE'
    # default listing container that houses the image upload field
    with st.container():
        # header that is shown on the web UI
        st.subheader('Listing写作')

        # the image upload field, the specific ui element that allows you to upload an image
        # when an image is uploaded it saves the file to the directory, and creates a path to that image
        File = st.file_uploader('商品图片', type=["webp", "png", "jpg", "jpeg"], key="new")
        brand = st.text_input("品牌", 'The Peanutshell')
        features = st.text_input("商品关键词", "The Peanutshell Crib Mobile for Boys or Girls, Unicorn, Stars, Rainbow, Montessori Inspired")

        #asin = st.text_input("参考热卖商品 Amazon ASIN", 'B0BZYCJK89')

        st.divider()

        asin_label = ['B0BZYCJK89', 'B0BGYWPWNC', 'B0CX23V2ZK']
        asin = st.selectbox('请选择参考热卖商品', asin_label)

        filename = './data/' + 'asin_' + asin + '_product.json'
        with open(filename, 'r', encoding='utf-8') as file:
            product_data = file.read()
            
        product_results = json.loads(product_data)
        
        as_title = product_results['results'][0]['content']['title']
        as_bullet = product_results['results'][0]['content']['bullet_points']
        as_des = product_results['results'][0]['content']['description']

        expander = st.expander('详细信息')
        expander.write('Title:')
        expander.write(as_title)

        expander.write('Bullet Points:')
        expander.write(as_bullet)

        expander.write('Description:')
        expander.write(as_des)

        #expander.write(as_title+'\n'+as_bullet+'\n'+as_des)

        # this is the button that triggers the invocation of the model, processing of the image and/or question
        result = st.button("Submit")

        # if the button is pressed, the model is invoked, and the results are output to the front end
        if result:
            # if an image is uploaded, a file will be present, triggering the image_to_text function
            if File is not None:
                # the image is displayed to the front end for the user to see
                # st.image(File)
                # determine the path to temporarily save the image file that was uploaded
                save_folder = os.getenv("save_folder")
                print(save_folder)
                print('filename:' + File.name)

                # create a posix path of save_folder and the file name
                save_path = Path(save_folder, File.name)
                # write the uploaded image file to the save_folder you specified
                with open(save_path, mode='wb') as w:
                    w.write(File.getvalue())

                # once the save path exists...
                if save_path.exists():
                    # write a success message saying the image has been successfully saved
                    # st.success(f'Image {File.name} is successfully saved!')
                    # running the image to text task, and outputting the results to the front end
                    file_name = save_path

                    if mode_lable == 'PE':
                        system_prompt, user_prompt = gen_listing_prompt(asin, 'com', brand, features, language_lable)
                        print('system_prompt:' + system_prompt)
                        print('user_prompt:' + user_prompt)
                        
                        output = image_to_text(file_name, system_prompt, user_prompt)
                        #st.write(output)
                    elif mode_lable == 'Agent':
                        response = create_listing(asin, file_name, brand, features)
                        print(response)
                        rslist = str(response['output']).rsplit('>')
                        output = rslist[-1]

                    print("output:" + output)
                    data = json.loads(output)

                    st.write("Title:\n")
                    st.write(data['title'])

                    # #get all string from bullet points data['bullets']
                    st.write("Bullet Points:\n")
                    bullet_points = ""
                    for item in data['bullets']:
                        bullet_points += "• " + item + "\n\n"
                    st.markdown(bullet_points)

                    st.write("Description:\n")
                    st.write(data['description'])
                    
                    # removing the image file that was temporarily saved to perform the question and answer task
                    os.remove(save_path)

                    #st.rerun()
            # if an Image is not uploaded, but a question is, the text_to_text function is invoked
            else:
                # running a text to text task, and outputting the results to the front end
                st.write('select product image')
    

if __name__ == '__main__':
    main()
