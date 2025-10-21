from simple_pid import PID                      #加熱冷却処理用のPIDコントローラをインポート
# Create a PID controller with specific gains
pid = PID(Kp=1.0, Ki=0.1, Kd=0.05, setpoint=0)  # PIDコントローラを作成


