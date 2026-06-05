import csv,os
def log_row(path,row):
    new=not os.path.exists(path)
    with open(path,'a',newline='') as f:
        w=csv.writer(f)
        if new:w.writerow(['timestamp','azimuth','elevation','tilt_angle','efficiency_estimate_%'])
        w.writerow(row)
