# config.py
class SystemThresholds:
    """
    システムの動作閾値を定義するクラス
    """
    # 最適充電温度 (℃)
    OPTIMAL_CHARGE_TEMP: float = 45.0       # バッテリーの最適充電温度 
    # 許容温度差 (℃)
    # 安定温度とみなすための目標との差分
    ALLOWABLE_TEMP_DIFFERENCE: float = 3.0  #S4に遷移するための許容温度差（通常温度+-3℃）

    # 温度変化ディレイ時間 (ms)
    # 安定温度を更新する際のインターバル
    TEMP_UPDATE_DELAY_MS: int = 1000    

    # --- 予約値 ---
    # 高温警報出力閾値 (℃)
    HIGH_TEMP_ALARM_THRESHOLD: float = 60.0 #S5に遷移するための高温警報閾値

    # 低温警報出力閾値 (℃)
    LOW_TEMP_ALARM_THRESHOLD: float = -20.0 #S5に遷移するための低温警報閾値

    # 高温停止閾値 (℃)
    HIGH_TEMP_STOP_THRESHOLD: float = 85.0  #S6に遷移するための高温停止閾値

    # 低温停止閾値 (℃)
    LOW_TEMP_STOP_THRESHOLD: float = -40.0  #S6に遷移するための低温停止閾値