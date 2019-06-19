from django.db import models
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import  keras
NEW_MODEL=keras.models.load_model('my_model11.h5')
print('model loaded')
class Heart(models.Model):
    age = models.PositiveIntegerField()
    Gender = (
        (1, 'male'),
        (0, 'female'),
    )
    sex = models.PositiveIntegerField(choices=Gender)
    cp_type = (
        (0, 'Type 0'),
        (1, 'Type 1'),
        (2, 'Type 2'),
        (3, 'Type 3'),
    )
    chest_pain_type = models.PositiveIntegerField(choices=cp_type)
    resting_blood_pressure_in_mm_HG=models.PositiveIntegerField()
    serum_cholestrol_in_mg_dl=models.PositiveIntegerField()
    fbs=((1,'Greater than 120 mg/dl'),
         (0, 'Less than 120 mg/dl'),
         )
    is_fasting_blood_sugar_greater_than_120_mg_dl=models.PositiveIntegerField(choices=fbs)
    rest_ecg=((0,'Type 0'),
              (1,'Type 1'),
              (2,'Type 2'),)
    resting_electrocardiograph=models.PositiveIntegerField(choices=rest_ecg)
    maximum_heart_rate_achieved=models.PositiveIntegerField()
    exang=((1,'YES'),
           (0,'NO'))
    exercise_induced=models.PositiveIntegerField(choices=exang)
    ST_depression_induced_by_exrecise_relative_to_rest=models.FloatField()
    slope_Type=models.PositiveIntegerField(choices=rest_ecg)
    number_of_major_vessels_colored_by_fluoroscopy=models.PositiveIntegerField()
    thal_type=((3,'Normal'),
               (6,'Fixed Defect'),
               (7,'Reversable Defect'))
    thal=models.PositiveIntegerField(choices=thal_type)
    target_choices=((1,'Yes'),
                    (0,'No'))
    target=models.PositiveIntegerField(choices=target_choices)

    def save(self, *args, **kwargs):
        df=pd.DataFrame(columns=['age','sex','chest_pain_type','resting_blood_pressure_in_mm_HG','serum_cholestrol_in_mg_dl','is_fasting_blood_sugar_greater_than_120_mg_dl','resting_electrocardiograph','maximum_heart_rate_achieved','exercise_induced','ST_depression_induced_by_exrecise_relative_to_rest','slope_Type','number_of_major_vessels_colored_by_fluoroscopy','thal'],data=[[self.age,self.sex,self.chest_pain_type,self.resting_blood_pressure_in_mm_HG,self.serum_cholestrol_in_mg_dl,self.is_fasting_blood_sugar_greater_than_120_mg_dl,self.resting_electrocardiograph,self.maximum_heart_rate_achieved,self.exercise_induced,self.ST_depression_induced_by_exrecise_relative_to_rest,self.slope_Type,self.number_of_major_vessels_colored_by_fluoroscopy,self.thal]])
        NEW_MODEL = keras.models.load_model('my_model11.h5')
        print('model loaded')
        print(NEW_MODEL)
        print("Model Displayed")
        if NEW_MODEL.predict(x=df)[0][0]> 0.85:
            self.target=1
        else:
            self.target=0
        super().save(*args, **kwargs)  # Call the "real" save() method.

