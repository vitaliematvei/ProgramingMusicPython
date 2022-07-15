
def determinate_interval(interval):
	if interval == 1:
		return "minor 2nd up or major 7th down\n"
	elif interval == 2:
		return "major 2nd up or minor 7th down\n"
	elif interval == 3:
		return "minor 3nd up or major 6th down\n"
	elif interval == 4:
		return "major 3nd up or minor 6th down\n"
	elif interval == 5:
		return "perfect 4nd up or perfect 5th down\n"
	elif interval == 6:
		return "augmented 4th\n"
	elif interval == 7:
		return "perfect 5th up or perfect 4th down\n"
	elif interval == 8:
		return "minor 6th up or major 3rd down\n"
	elif interval == 9:
		return "major 6th up or minor 3th down\n"
	elif interval == 10:
		return "minor 7th up or major 2nd down\n"
	elif interval == 11:
		return "major 7th up or minor 2nd down\n"
	else:
		return "unison \n"
