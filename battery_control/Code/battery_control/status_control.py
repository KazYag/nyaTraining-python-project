from enum import Enum

class BatteryState(Enum):
    """
    バッテリー温度制御システムの動作状態を定義します。
    """
    STATE_INIT = 0              # S0: 初期動作
    STATE_NORMAL_MONITOR = 1    # S1: 通常監視
    STATE_HIGH_TEMP_CTRL = 2    # S2: 高温制御
    STATE_LOW_TEMP_CTRL = 3     # S3: 低温制御
    STATE_CHARGE_GUIDE = 4      # S4: 最適充電誘導
    STATE_SAFE_ALERT = 5        # S5: 異常警告
    STATE_SAFE_STOP = 6         # S6: 安全停止
