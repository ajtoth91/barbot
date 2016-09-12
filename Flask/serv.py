from flask import Flask, render_template, request
from datetime import datetime
from lists.bac_list import bac_list
import pytz, os.path, datetime
from list_manager import *
from class_definitions import *

app= Flask(__name__)
app.jinja_env.trim_blocks=True
app.jinja_env.lstrip_blocks=True


@app.route('/')
def hello_word():
  return 'Hello, world!'

@app.route('/admin', methods=['POST'])
def save_config():
  #save pump data
  pump_list=load_pumps()
  for i, pumpData in enumerate(pump_list):
    pump_list[i].BOTTLE.spirit_type= request.form['Spirit'+str(i)]
    pump_list[i].BOTTLE.name_of_bottle= request.form['Name'+str(i)]
    pump_list[i].BOTTLE.size_of_bottle= request.form['Size'+str(i)]
    pump_list[i].BOTTLE.amount_left= request.form['Amount_left'+str(i)]
    pump_list[i].BOTTLE.ABV= request.form['ABV'+str(i)]
    if request.form['is_Commercial']=='False':
      pump_list[i].BOTTLE.price_shot=0;
    else:
      #it is selected Commercial; see if that is what was saved.
      config_file=open('admin_config.cfg','r')
      saved_timezone=config_file.readline().rstrip()
      saved_country=config_file.readline().rstrip()
      saved_isCommercial=config_file.readline().rstrip()
      config_file.close()
      #if the last saved config was Commercial, we loaded with a Price form and can successfully read from it.
      if saved_isCommercial == request.form['is_Commercial']:
        pump_list[i].BOTTLE.price_shot= request.form['Price'+str(i)]

  config_file = open('admin_config.cfg','w')
  config_file.write(request.form['Time_Zone'] + '\n')
  config_file.write(request.form['Country'] + '\n')
  config_file.write(request.form['is_Commercial'])
  config_file.close()

  file_garnishes=open('./lists/garnishes_selected.lst','w')
  selected_garnishes=request.form.getlist('garnishes')
 
  selected_garnishes= [x.encode('utf-8') for x in selected_garnishes]#gelist returns unicode strings
  save_garnishes(selected_garnishes)  
 
  print "UTC Offset: " +  datetime.datetime.now(pytz.timezone(request.form['Time_Zone'])).strftime('%z')

  save_pumps(pump_list)

  print ingredient_available('Vodka') 
  print ingredient_available('Cherry') 
  return render_template('admin_console.html',
       time_zones=pytz.common_timezones,
       bac_list=bac_list,
       legal_bac=bac_list[request.form['Country']],
       is_Commercial=request.form['is_Commercial'],
       selected_timezone=request.form['Time_Zone'],
       selected_country=request.form['Country'],
       list_pourable_all=list_pourable_all,
       pump_list=pump_list,
       garnish_list=garnish_list,
       selected_garnishes=selected_garnishes)

@app.route('/admin')
def admin():
  if (os.path.exists('./lists/garnishes_selected.lst')):
    selected_garnishes=load_garnishes()
  else:
    print "there are no garnishes"
    #create an empty garnish file
    file_sel_garnishes=open('.lists/garnishes_selected.list','w')
    file_sel_garnishes.write('')
    file_sel_garnishes.close()
  if (os.path.exists("./admin_config.cfg")):
    config_file=open('admin_config.cfg','r')
    saved_timezone=config_file.readline().rstrip()
    saved_country=config_file.readline().rstrip()
    saved_isCommercial=config_file.readline().rstrip() 
    return render_template('admin_console.html',
         time_zones=pytz.common_timezones,
         bac_list=bac_list, 
         legal_bac=bac_list[saved_country], 
         is_Commercial=saved_isCommercial, 
         selected_timezone=saved_timezone,
         selected_country=saved_country,
         list_pourable_all=list_pourable_all,
         pump_list=load_pumps(),
         garnish_list=garnish_list,
         selected_garnishes=load_garnishes())

  #else:No admin_config has been saved, show a clean Admin Console page.

  return render_template('admin_console.html',time_zones=pytz.common_timezones,bac_list=bac_list,is_Commercial=False,list_pourable_all=list_pourable_all, pump_list=create_pump_list(), garnish_list= garnish_list) #as of 09-04, Also need to create an empty "./lists/garnish_sel.lst" file

@app.route('/client')
def client():
 return is_ingredient_available('Vodka')
