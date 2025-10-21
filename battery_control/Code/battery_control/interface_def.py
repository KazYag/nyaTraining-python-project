#I/Fで使用するデータを定義する
from dataclasses import dataclass       # dataclassを使用するためのインポート
from StatusControl import BatteryTempState  # StatusControlを使用するためのインポート
from typing import ClassVar, Dict,Any  # ListとOptionalを使用するためのインポート
@dataclass
class ControlData:
    #I/Fで使用するデータを定義する
    S32_currentTempurature:float = 0.0  # 現在の温度
    S32_targetTempurature:float = 0.0   # 目標の温度
    U16_temperature_change_rate = 0     # 温度変化率
    bl_battery_sensor_Error:bool = False # バッテリーセンサーエラー
    bl_cell_sensor_Error:bool = False    # セルセンサーエラー

#項目名と型などの定義情報
    FIELD_INFO: ClassVar[Dict[str, Any]] = {
        "S32_currentTempurature": {"type": float, "unit": "°C", "min": -40.0, "max": 125.0, "description": "現在の温度"},
        "S32_targetTempurature": {"type": float, "unit": "°C", "min": -40.0, "max": 125.0, "description": "目標の温度"},
        "U16_temperature_change_rate": {"type": int, "unit": "%", "min": 0, "max": 100, "description": "温度変化率"},
        "bl_battery_sensor_Error": {"type": bool, "description": "バッテリーセンサーエラー"},
        "bl_cell_sensor_Error": {"type": bool, "description": "セルセンサーエラー"}, 
    }
class StatusControl:    # 状態を表す定数クラス
    U1_bateryTempStatus:int = 0  # バッテリー温度状態




#FIELD_INFOは各フィールドの型、単位、最小値、最大値、説明を含む辞書