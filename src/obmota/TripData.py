# -*- coding: utf-8 -*-

import attrs


def tripdata_validator(instance, attribute, value):
    valid_hex_value_set = set('0123456789abcdefABCDEFxXh ')
    if not all(c in valid_hex_value_set for c in value):
        raise ValueError(f"The string contains characters which are not compatible with an hexadecimal representation")
    parsed = value.replace(" ", "")     #TODO: there must be a better way to write this
    parsed = parsed.replace("0x","")
    parsed = parsed.replace("0X","")
    parsed = parsed.replace("h","")     #TODO: this should be done only if 'h' is at the beginning of the string
    
    if len(parsed) != 128:
        raise ValueError(f"The string must be 64 bytes long!")
    
    int(parsed, 16)         # raises value error if the parsed string is not a valid hexadecimal
    

@attrs.define
class TripData():
    """
    A valid payload of Trip Data according to OBM OTA schemas.
    
    :param str payload: The original string passed to the constructor, expects an hexadecimal representation
    """
    payload: str = attrs.field(validator=[attrs.validators.instance_of(str),tripdata_validator])
    byte_set: list = attrs.field(default=attrs.Factory(lambda self: list(bytes.fromhex(self.payload.replace(" ", "").replace("0x","").replace("0X","").replace("h",""))), takes_self=True))
    # the following decoding is taken from the draft appendix to EU7 norm
    vehicle_odometer_value              = attrs.field(default=attrs.Factory(lambda self: self.byte_set[0:3], takes_self=True))
    OBM_trip_distance                   = attrs.field(default=attrs.Factory(lambda self: self.byte_set[4:5], takes_self=True))
    OBM_trip_time                       = attrs.field(default=attrs.Factory(lambda self: self.byte_set[6:7], takes_self=True))
    idle_time                           = attrs.field(default=attrs.Factory(lambda self: self.byte_set[8:9], takes_self=True))
    distance_specific_NOx               = attrs.field(default=attrs.Factory(lambda self: self.byte_set[10:11], takes_self=True))
    fuel_consumed_volume                = attrs.field(default=attrs.Factory(lambda self: self.byte_set[12:13], takes_self=True))
    net_electrical_energy_consumed      = attrs.field(default=attrs.Factory(lambda self: self.byte_set[14:15], takes_self=True))
    net_electrical_energy_into_battery  = attrs.field(default=attrs.Factory(lambda self: self.byte_set[16:17], takes_self=True))
    regeneration_distance_ratio         = attrs.field(default=attrs.Factory(lambda self: self.byte_set[18], takes_self=True))
    monitored_AES_distance_ratio        = attrs.field(default=attrs.Factory(lambda self: self.byte_set[19], takes_self=True))
    reagent_inhibited_ratio             = attrs.field(default=attrs.Factory(lambda self: self.byte_set[20], takes_self=True))
    modelled_data_distance_ratio        = attrs.field(default=attrs.Factory(lambda self: self.byte_set[21], takes_self=True))
    speed_urban_slow_ratio              = attrs.field(default=attrs.Factory(lambda self: self.byte_set[22], takes_self=True))
    speed_urban_ratio                   = attrs.field(default=attrs.Factory(lambda self: self.byte_set[23], takes_self=True))
    speed_rural_ratio                   = attrs.field(default=attrs.Factory(lambda self: self.byte_set[24], takes_self=True))
    speed_motorway_ratio                = attrs.field(default=attrs.Factory(lambda self: self.byte_set[25], takes_self=True))
    distance_EV_ratio                   = attrs.field(default=attrs.Factory(lambda self: self.byte_set[26], takes_self=True))
    ambient_temperature_low_ratio       = attrs.field(default=attrs.Factory(lambda self: self.byte_set[27], takes_self=True))
    ambient_temperature_high_ratio      = attrs.field(default=attrs.Factory(lambda self: self.byte_set[28], takes_self=True))
    altitude_high_ratio                 = attrs.field(default=attrs.Factory(lambda self: self.byte_set[29], takes_self=True))
    outside_extended_conditions_ratio   = attrs.field(default=attrs.Factory(lambda self: self.byte_set[30], takes_self=True))
    MI_status                           = attrs.field(default=attrs.Factory(lambda self: self.byte_set[31], takes_self=True))
    NOx_to_fuel_mass_ratio              = attrs.field(default=attrs.Factory(lambda self: self.byte_set[32:33], takes_self=True))
    SCR_inducement_state                = attrs.field(default=attrs.Factory(lambda self: self.byte_set[34], takes_self=True))
    monitoring_status_NOx               = attrs.field(default=attrs.Factory(lambda self: self.byte_set[35], takes_self=True))
    monitoring_status_PM                = attrs.field(default=attrs.Factory(lambda self: self.byte_set[36], takes_self=True))
    monitoring_status_generic           = attrs.field(default=attrs.Factory(lambda self: self.byte_set[37], takes_self=True))
    OBM_inducement_and_tampering_status = attrs.field(default=attrs.Factory(lambda self: self.byte_set[38], takes_self=True))
    # reserved for expansion parameters are omitted
    manufacturer_reserved_0             = attrs.field(default=attrs.Factory(lambda self: self.byte_set[49], takes_self=True))
    manufacturer_reserved_1             = attrs.field(default=attrs.Factory(lambda self: self.byte_set[50], takes_self=True))
    manufacturer_reserved_2             = attrs.field(default=attrs.Factory(lambda self: self.byte_set[51], takes_self=True))
    manufacturer_reserved_3             = attrs.field(default=attrs.Factory(lambda self: self.byte_set[52], takes_self=True))
    manufacturer_reserved_4             = attrs.field(default=attrs.Factory(lambda self: self.byte_set[53], takes_self=True))
    manufacturer_reserved_5             = attrs.field(default=attrs.Factory(lambda self: self.byte_set[54], takes_self=True))
    manufacturer_reserved_6             = attrs.field(default=attrs.Factory(lambda self: self.byte_set[55], takes_self=True))
    manufacturer_reserved_7             = attrs.field(default=attrs.Factory(lambda self: self.byte_set[56], takes_self=True))
    manufacturer_reserved_8             = attrs.field(default=attrs.Factory(lambda self: self.byte_set[57], takes_self=True))
    manufacturer_reserved_9             = attrs.field(default=attrs.Factory(lambda self: self.byte_set[58], takes_self=True))
    OBM_trip_hash_validity_status       = attrs.field(default=attrs.Factory(lambda self: self.byte_set[59], takes_self=True))
    OBM_trip_hash_value                 = attrs.field(default=attrs.Factory(lambda self: self.byte_set[60:63], takes_self=True))
    
    def __repr__(self):
        return f"""\
    TripData:\n
    --------------------
    vehicle_odometer_value               : 
    OBM_trip_distance                    : 
    OBM_trip_time                        : 
    idle_time                            : 
    distance_specific_NOx                : 
    fuel_consumed_volume                 : 
    net_electrical_energy_consumed       : 
    net_electrical_energy_into_battery   : 
    regeneration_distance_ratio          : 
    monitored_AES_distance_ratio         : 
    reagent_inhibited_ratio              : 
    modelled_data_distance_ratio         : 
    speed_urban_slow_ratio               : 
    speed_urban_ratio                    : 
    speed_rural_ratio                    : 
    speed_motorway_ratio                 : 
    distance_EV_ratio                    : 
    ambient_temperature_low_ratio        : 
    ambient_temperature_high_ratio       : 
    altitude_high_ratio                  : 
    outside_extended_conditions_ratio    : 
    MI_status                            : 
    NOx_to_fuel_mass_ratio               : 
    SCR_inducement_state                 : 
    monitoring_status_NOx                : 
    monitoring_status_PM                 : 
    monitoring_status_generic            : 
    OBM_inducement_and_tampering_status  : 
    # reserved for expansion parameters  : 
    manufacturer_reserved_0              : 
    manufacturer_reserved_1              : 
    manufacturer_reserved_2              : 
    manufacturer_reserved_3              : 
    manufacturer_reserved_4              : 
    manufacturer_reserved_5              : 
    manufacturer_reserved_6              : 
    manufacturer_reserved_7              : 
    manufacturer_reserved_8              : 
    manufacturer_reserved_9              : 
    OBM_trip_hash_validity_status        : 
    OBM_trip_hash_value                  : 
               """