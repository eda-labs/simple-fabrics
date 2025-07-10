#!/usr/bin/env python3

class DbTopoOverlayState:
    def __init__(self,
                 db_value,):
        self.db_value = db_value

    def set_metadata(self,
                     ui_name: str,
                     ui_description: str,):
        self.db_value['ui_name'] = ui_name
        self.db_value['ui_description'] = ui_description
        return self

    def set_metadata_i18n(self,
                          ui_name_key: str,
                          ui_description_key: str,):
        self.db_value['ui_name_key'] = ui_name_key
        self.db_value['ui_description_key'] = ui_description_key
        return self
