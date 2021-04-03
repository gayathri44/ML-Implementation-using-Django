from django.shortcuts import render  
from mlimplementation.forms import energydata_complete  
  
def predictdata(response):  
    # Here we just create an object for the StudentForm Class and fetch data and send to output.html
    if response.method == 'POST':
        data = energydata_complete(response.POST) 
        if data.is_valid():
            T1 = data.cleaned_data['T1']
            RH1 = data.cleaned_data['RH1']
            T2 = data.cleaned_data['T2']
            RH2 = data.cleaned_data['RH2']
            T3 = data.cleaned_data['T3']
            RH3 = data.cleaned_data['RH3']
            T4 = data.cleaned_data['T4']
            RH4 = data.cleaned_data['RH4']
            T5 = data.cleaned_data['T5']
            RH5 = data.cleaned_data['RH5']
            T6 = data.cleaned_data['T6']
            RH6 = data.cleaned_data['RH6']
            T7 = data.cleaned_data['T7']
            RH7 = data.cleaned_data['RH7']
            T8 = data.cleaned_data['T8']
            RH8 = data.cleaned_data['RH8']
            T9 = data.cleaned_data['T9']
            RH9 = data.cleaned_data['RH9']
            Press_mm_hg = data.cleaned_data['Press_mm_hg']
            RH_out = data.cleaned_data['RH_out']
            Windspeed = data.cleaned_data['Windspeed']


            print(T1,RH1,T2,RH2,T3,RH3,T4,RH4,T5,RH5,T6,RH6,T7,RH7,T8,RH8,T9,RH9,Press_mm_hg,RH_out,Windspeed)
              
              
              


              


            return render(response, 'output.html', {'message1': T1,'message2' : RH1,'message3': T2,'message4': RH2,'message5':T3,'message6': RH3,'mesaage7': T4,'message8': RH4,'message9': T5,'message10': RH5,'message11': T6,'message12': RH6,'message13': T7,'message14': RH7,'message15': T8,'message16': RH8,'message17': T9,'message18': RH9,'message19': Press_mm_hg,'message20': RH_out,'message_21': Windspeed})
        else:
            return render(response, 'predict.html', {'form': data})

    else:
        data = energydata_complete() 
        return render(response, 'predict.html', {'form': data})