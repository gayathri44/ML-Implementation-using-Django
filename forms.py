from django import forms  
class energydata_complete(forms.Form):  
    T1 = forms.DecimalField(label="Enter T1")  
    RH1  = forms.DecimalField(label="Enter RH1")
    T2 = forms.DecimalField(label="Enter T2")  
    RH2  = forms.DecimalField(label="Enter RH2")
    T3 = forms.DecimalField(label="Enter T3")  
    RH3  = forms.DecimalField(label="Enter RH3")
    T4 = forms.DecimalField(label="Enter T4")  
    RH4  = forms.DecimalField(label="Enter RH4")
    T5 = forms.DecimalField(label="Enter T5")  
    RH5  = forms.DecimalField(label="Enter RH5")
    T6 = forms.DecimalField(label="Enter T6")  
    RH6  = forms.DecimalField(label="Enter RH6")
    T7 = forms.DecimalField(label="Enter T7")  
    RH7  = forms.DecimalField(label="Enter RH7")
    T8 = forms.DecimalField(label="Enter T8")  
    RH8  = forms.DecimalField(label="Enter RH8")
    T9 = forms.DecimalField(label="Enter T9")  
    RH9  = forms.DecimalField(label="Enter RH9")
    Press_mm_hg = forms.DecimalField(label="Enter pressure")  
    RH_out  = forms.DecimalField(label="Enter RH_out")
    Windspeed = forms.DecimalField(label="Enter windspeed")  
    
    
    
