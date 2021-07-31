import pandas as pd


def dateranges(start_date, end_date):
    end_date   = end_date + pd.Timedelta(days=1)
    time_frame = pd.date_range(start_date, end_date, periods=4)
    
    sd_func = lambda sd: sd.isoformat()
    ed_func = lambda ed: (ed-pd.Timedelta(days=1)).replace(hour=00).isoformat()
    
    pairs_time_frame = [[sd_func(sd), ed_func(ed)] for sd, ed in zip(time_frame[::1], time_frame[1::1])]
    
    return pairs_time_frame
	
