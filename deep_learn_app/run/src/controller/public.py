#!/usr/bin/env python3

from flask import Blueprint,render_template,request,session,redirect,url_for,Flask,send_file
from werkzeug import secure_filename
import os
import src.models.model as model

controller = Blueprint('public',__name__,static_folder='static',static_url_path='/static')

@controller.route('/',methods=['GET','POST'])
def frontpage():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        if request.files['fileselect']:
            text_file = request.files['fileselect']
            filename = secure_filename(text_file.filename)
            text_file.save("data/data.json")
            model.train()
            session['inputs'] = model.labels()
            message="Your model has been trained, ask away!"
            return render_template('query.html',message=message,inputs=session['inputs'])
        else:
            
            return render_template('homepage.html')

@controller.route('/query',methods=['GET','POST'])
def query():
    if request.method == 'GET':
        message = "Your model has been trained, ask away!"
        return render_template('query.html',message=message,inputs=session['inputs'])
    elif request.method == 'POST':
        predict_ask=[]
        for i in session['inputs']:
            predict_ask.append(request.form[i])
        message = model.predict(predict_ask)
        return render_template('query.html',message=message,inputs=session['inputs'])

@controller.route('/view',methods=['GET','POST'])
def view():
    if request.method == 'GET':
        message = "Your model has been trained, ask away!"
        return render_template('view.html',message=message,inputs=session['inputs'])
    elif request.method == 'GET':
        message = "Your model has been trained, ask away!"
        return render_template('view.html',message=message,inputs=session['inputs'])
        
        # predict_ask=[]
        # for i in session['inputs']:
        #     predict_ask.append(request.form[i])
        # message = model.predict(predict_ask)
        # return render_template('view.html',message=message,inputs=session['inputs'])


# @controller.route('/download')
# def download():
#     return send_file('/Users/kkim2250/Desktop/Project_TextSum/run/src/static/textfile1.txt', as_attachment=True, attachment_filename="textfile1.txt")


# @controller.route('/out',methods=['GET','POST'])
# def printpage():
#     if request.method == 'GET':
#         message = session['text']
#         return render_template('printpage.html', message=message)
#     elif request.method == 'POST':
#         text_file = request.file['upload']
#         text = request.form['summ']
#         if text_file:
#             return render_template('printpage.html', message=message)
#         elif text:
#             return render_template('printpage.html', message=message)
