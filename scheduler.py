from datetime import datetime,timedelta,timezone
import yaml,time
from src.sun_tracker import SunTracker
from src.panel_controller import PanelController
from src.logger import log_row
def run_scheduler(demo=False):
    cfg=yaml.safe_load(open('config.yaml'))
    tracker=SunTracker()
    ctrl=PanelController()
    now=datetime.now(timezone.utc)
    steps=96 if demo else 1
    for i in range(steps):
        dt=now+timedelta(minutes=i*15)
        az,el=tracker.calculate(cfg['location']['latitude'],cfg['location']['longitude'],dt)
        tilt=max(0,min(90,el))
        ctrl.move_to(tilt)
        log_row('data/panel_log.csv',[dt.isoformat(),round(az,2),round(el,2),round(tilt,2),round(max(0,min(100,el)),2)])
        if demo: time.sleep(5/96)
