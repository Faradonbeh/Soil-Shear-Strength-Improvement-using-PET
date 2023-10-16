import pickle

def make_prediction(al, type, dr, sn, percent, tmax):
    if percent == 0:
        return "There is not any improvement in shear strength"
    else:
        if al == "Decision Tree" :
            with open("Decision_Tree.pkl", "rb") as f:
                clf  = pickle.load(f)
                preds = clf.predict([[type, dr, sn, percent]])
            return f"""Shear strength after improvement: {round((preds.squeeze() * tmax),2)}
Improvement percentage: {round((preds.squeeze()-1)*100,2)}%"""
        elif al == "Random Forest" :
            with open("random_forest.pkl", "rb") as f:
                clf  = pickle.load(f)
                preds = clf.predict([[type, dr, sn, percent]])
            return f"""Shear strength after improvement: {round((preds.squeeze() * tmax),2)}
Improvement percentage: {round((preds.squeeze()-1)*100,2)}%"""
        elif al == "XGBoost" :
            with open("XGBoost.pkl", "rb") as f:
                clf  = pickle.load(f)
                preds = clf.predict([[type, dr, sn, percent]])
            return f"""Shear strength after improvement: {round((preds.squeeze() * tmax),2)}
Improvement percentage: {round((preds.squeeze()-1)*100,2)}%"""
        elif al == "AdaBoost" :
            with open("AdaBoost.pkl", "rb") as f:
                clf  = pickle.load(f)
                preds = clf.predict([[type, dr, sn, percent]])
            return f"""Shear strength after improvement: {round((preds.squeeze() * tmax),2)}
Improvement percentage: {round((preds.squeeze()-1)*100,2)}%"""


import gradio as gr


#Create the input component for Gradio since we are expecting 5 inputs

Algorithm = gr.Radio(["Decision Tree", "Random Forest", "XGBoost", "AdaBoost"], value="Decision Tree", label="Algorithm")
pet_type = gr.Slider(1, 3, value=1, step=1, label="PET type", info="Choose 1 for 1*1 PET, 2 for 1*5 PET, and 3 for fiber PET")
DR = gr.Slider(0.55, 0.95, step=0.2, label="Relative Density (Dr)", info="Range between 0.55 to 0.95")
SN = gr.Slider(50, 150, step=50, label="Normal Stresses (Sn)", info="Range between 50 to 150")
PPERCENT= gr.Slider(0, 2, step=0.1, label="PET Percent", info="Range between 0 to 2")
ShearStrength= gr.Slider(36.5, 144, step=0.1, label="Shear Strength (plain soil without PET)", info="Range between 36 to 144")

# We create the output
output = gr.Textbox()


app = gr.Interface(fn = make_prediction, inputs=[Algorithm, pet_type, DR, SN, PPERCENT, ShearStrength], outputs=output, 
                   title= "Soil Improvement Using PET Calculator",
                   description = """ 
This app is based on the paper 'Development of a non-destructive method to assess the shear strength of a sandy soil reinforced with polyethylene-terephthalate (PET)'
Authors: Masoud Samaei1, Roohollah Shirani Faradonbeh1,*, Morteza Alinejad Omran2, Nima Rahimpour3, Amir Bazrafshan Moghaddam2
1,* WA School of Mines: Minerals, Energy and Chemical Engineering, Curtin University, Kalgoorlie, WA 6430, Australia
2 Department of Civil Engineering, Shahrood University of Technology, Shahrood, Iran
3 Faculty of Engineering, University of Tabriz, Tabriz, Iran 

* Corresponding Author—Email: roohollah.shiranifaradonbeh@curtin.edu.au
""",
                   live=False)
app.launch()

