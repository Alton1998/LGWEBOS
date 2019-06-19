from django.contrib import admin
from .models import Heart
# Register your models here.
@admin.register(Heart)
class HeartAdmin(admin.ModelAdmin):
    exclude = ['target']
    search_fields = ['pk','age','sex','chest_pain_type','resting_blood_pressure_in_mm_HG','serum_cholestrol_in_mg_dl','is_fasting_blood_sugar_greater_than_120_mg_dl','resting_electrocardiograph','maximum_heart_rate_achieved','exercise_induced','ST_depression_induced_by_exrecise_relative_to_rest','slope_Type','number_of_major_vessels_colored_by_fluoroscopy','thal','target']
    list_display =['pk','age','sex','chest_pain_type','resting_blood_pressure_in_mm_HG','serum_cholestrol_in_mg_dl','is_fasting_blood_sugar_greater_than_120_mg_dl','resting_electrocardiograph','maximum_heart_rate_achieved','exercise_induced','ST_depression_induced_by_exrecise_relative_to_rest','slope_Type','number_of_major_vessels_colored_by_fluoroscopy','thal','target']
    list_filter = ['age','sex','chest_pain_type','resting_blood_pressure_in_mm_HG','serum_cholestrol_in_mg_dl','is_fasting_blood_sugar_greater_than_120_mg_dl','resting_electrocardiograph','maximum_heart_rate_achieved','exercise_induced','ST_depression_induced_by_exrecise_relative_to_rest','slope_Type','number_of_major_vessels_colored_by_fluoroscopy','thal','target']





#admin.site.register(Heart)