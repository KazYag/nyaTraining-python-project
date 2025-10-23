#温度制御に使用する定数を定義する
#値は仮値。調査後決定すること
# 最適な動作温度・設定値 (OPTIMAL/TOLERANCE)
OPTIMAL_CHARGE_TEMP = 25.0       # 最適充電温度 [℃]
TOLERANCE_TEMP = 5.0            # 許容温度 [℃]
# 警報閾値 (ALERT THRESHOLD)
HIGH_ALERT_THRESHOLD = 40.0      # 高温警報出力閾値 [℃]
LOW_ALERT_THRESHOLD = 5.0        # 低温警報出力閾値 [℃]
# 停止閾値 (STOP THRESHOLD)
HIGH_STOP_THRESHOLD = 50.0       # 高温停止閾値 [℃]
LOW_STOP_THRESHOLD = 0.0         # 低温停止閾値 [℃]

MODE_HOLD = 0               # 温度変化モード: 現状維持
MODE_HEAT = 1               # 温度変化モード: 加熱レベル1
MODE_COLD = 2               # 温度変化モード: 冷却レベル1
