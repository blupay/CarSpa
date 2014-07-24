import autocomplete_light
from models import *

# This will generate a PersonAutocomplete class
autocomplete_light.register(Customer,
    # Just like in ModelAdmin.search_fields
    search_fields=['Full_Name', 'mobile_number'],
    # This will actually html attribute data-placeholder which will set
    # javascript attribute widget.autocomplete.placeholder.
    autocomplete_js_attributes={'placeholder': 'Other model name ?',},
)
