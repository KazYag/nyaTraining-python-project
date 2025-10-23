from dataclasses import dataclass, field
from typing import ClassVar, Dict, Any, Tuple
from simple_pid import PID

@dataclass
class PIDConfig:
    """
    PIDコントローラーのパラメータと状態を保持するデータクラス
    """
    # --- PIDパラメータ ---
    Kp: float = 0.5
    Ki: float = 0.1
    Kd: float = 0.05
    setpoint: float = 0.0
    sample_time: float = 0.01
    output_limits: Tuple[float, float] = (-100.0, 100.0)

    # --- 実行時に変化する変数 ---
    current_value: float = 0.0
    control_output: float = 0.0
    
    # --- PIDインスタンス ---
    # __post_init__ を使い、上記パラメータからPIDインスタンスを生成します
    pid_instance: PID = field(init=False, repr=False)

    def __post_init__(self):
        self.pid_instance = PID(
            self.Kp, self.Ki, self.Kd,
            setpoint=self.setpoint,
            sample_time=self.sample_time,
            output_limits=self.output_limits
        )

    # --- メタデータ ---
    FIELD_INFO: ClassVar[Dict[str, Any]] = {
        "Kp": {"type": float, "description": "比例ゲイン"},
        "Ki": {"type": float, "description": "積分ゲイン"},
        "Kd": {"type": float, "description": "微分ゲイン"},
        "setpoint": {"type": float, "description": "目標温度"},
        "sample_time": {"type": float, "description": "サンプリング時間"},
        "output_limits": {"type": "Tuple", "description": "出力制限"},
    }
