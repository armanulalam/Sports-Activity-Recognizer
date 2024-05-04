from fastai.vision.all import *
import gradio as gr


labels = (
    'archery', 
    'baseball swing', 
    'basketball shot', 
    'boxing jab', 
    'cricket batting', 
    'cycling sprint', 
    'golf swing', 
    'horse riding gallop', 
    'ice hockey slapshot', 
    'rowing', 
    'rugby tackle', 
    'skiing parallel', 
    'soccer kick', 
    'surfing cutback', 
    'volleyball spike'
<<<<<<< HEAD
)
=======
    )
>>>>>>> 58a1984901fec7cc0c718d031d88d82e54ddd653

model = load_learner('sports-action-recognizer-version3.pkl')

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(labels, map(float, probs)))

image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label(num_top_classes=3)
examples = [
    'img1.jpg',
    'img2.jpg',
    'img4.jpg',
    'img5.jpg'
    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False,share=True)