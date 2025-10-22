from simple_pid import PIDControlData                      #加熱冷却処理用のPIDコントローラをインポート

@dataclass PIDControlData:
class ControlData:
    #I/Fで使用するデータを定義するデータクラス
    # 変数名
    pid: PID = pid                      # PIDコントローラインスタンス
    Kp: float = 0.5                     # 比例ゲイン
    Ki: float = 0.1                     # 積分ゲイン
    Kd: float = 0.05                    # 微分ゲイン
    setpoint: float = 0                 # 目標温度
    current_value: float = 0              # 現在の温度
    sample_time: float = 0.01             # サンプリング時間（秒）
    output_limits: tuple = (-100, 100)   # 出力制限（最小値、最大値）
    control: float = 0                    # PIDコントロール出力
    # --- メタデータ ---
    FIELD_INFO: ClassVar[Dict[str, Any]] = {
        "Kp": {"type": float, "unit": "", "min": 0.0, "max": 100.0, "description": "比例ゲイン"},
        "Ki": {"type": float, "unit": "", "min": 0.0, "max": 100.0, "description": "積分ゲイン"},
        "Kd": {"type": float, "unit": "", "min": 0.0, "max": 100.0, "description": "微分ゲイン"},
        "setpoint": {"type": float, "unit": "°C", "min": -40.0, "max": 125.0, "description": "目標温度"},
        "current_value": {"type": float, "unit": "°C", "min": -40.0, "max": 125.0, "description": "現在の温度"},
        "sample_time": {"type": float, "unit": "秒", "min": 0.001, "max": 10.0, "description": "サンプリング時間"},
        "output_limits": {"type": "tuple", "unit": "", "description": "出力制限（最小値、最大値）"},
    }
