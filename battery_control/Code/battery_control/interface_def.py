# interface_def.py
from dataclasses import dataclass
from typing import ClassVar, Dict, Any
from .status_control import BatteryState

@dataclass
class ControlData:
     """
     #I/Fで使用するデータを定義するデータクラス
     """
    # 変数名
     current_temperature: float = 0.0       # 現在の温度
     target_temperature: float = 0.0        # 目標の温度    
     battery_sensor_error: bool = False     # バッテリーセンサーエラー
     cell_sensor_error: bool = False        # セルセンサーエラー
   
     system_state: BatteryState = BatteryState.STATE_INIT    # システム状態
     temperature_change_rate: int = 0    # 温度変化率   
     temperature_change_mode: int = 0   # 温度変化モード
   
     # --- メタデータ ---
     FIELD_INFO: ClassVar[Dict[str, Any]] = {
        "current_temperature": {"type": float, "unit": "°C", "min": -40.0, "max": 125.0, "description": "現在の温度"},
        "target_temperature": {"type": float, "unit": "°C", "min": -40.0, "max": 125.0, "description": "目標の温度"},
        "battery_sensor_error": {"type": bool, "description": "バッテリーセンサーエラー"},
        "cell_sensor_error": {"type": bool, "description": "セルセンサーエラー"},
        "system_state": {"type": "BatteryState", "description": "現在のシステム状態"},
    }