{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5e4bd4f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "st.title(\"first render plateform model\")\n",
    "tv_input = st.number_input(\"TV\",min_value=0,max_value = 1000, step = 1)\n",
    "radio_input =st.number_input(\"Radio\",min_value=0,max_value = 1000, step = 1)\n",
    "newpaper_input =st.number_input(\"newPaper\",min_value=0,max_value = 1000, step = 1)\n",
    "import pickle as pkl\n",
    "file1=open(\"preprocessor.pkl\",\"rb\")\n",
    "sc = pkl.load(file1)\n",
    "file2=open(\"model.pkl\",\"rb\")\n",
    "model_1 = pkl.load(file2)\n",
    "input1 = sc.transform([[tv_input,radio_input,newpaper_input]])\n",
    "\n",
    "if st.button(\"Predict\"):\n",
    "    pred = model_1.predict(input1)\n",
    "    st.text(pred)\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
