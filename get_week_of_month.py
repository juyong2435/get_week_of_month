import calendar
import datetime
import sys


def get_week_of_month(year, month, day):
	date = datetime.date(year, month, day)
	first_date = datetime.date(year, month, 1)
	v_last_date_of_month = date.replace(day=calendar.monthrange(year, month)[1])
	v_last_date_of_previous_month = first_date - datetime.timedelta(days=1)
	v_month_week_count = len(calendar.monthcalendar(date.year, date.month))

	v_rtn_week_no = 1
	v_rtn_month = date.month
	# 월의 첫 주
	if date.day in calendar.monthcalendar(date.year, date.month)[0]:
		if datetime.date(year, month, 1).isoweekday() in [5, 6, 7]:
			v_first_date_of_previous_month = datetime.date(v_last_date_of_previous_month.year, v_last_date_of_previous_month.month, 1)
			v_add_week_no = 0 if v_first_date_of_previous_month.isoweekday() in [1, 2, 3, 4] else -1
			v_rtn_week_no = len(calendar.monthcalendar(v_last_date_of_previous_month.year, v_last_date_of_previous_month.month)) + v_add_week_no
			v_rtn_month = v_last_date_of_previous_month.month

	# 월의 마지막 주
	elif date.day in calendar.monthcalendar(date.year, date.month)[v_month_week_count-1]:
		if v_last_date_of_month.isoweekday() in [1,2,3]:
			v_rtn_month = (v_last_date_of_month + datetime.timedelta(days=1)).month
			v_rtn_week_no = 1
		else:
			v_rtn_week_no = 0

			v_week_idx = 0
			while v_week_idx < v_month_week_count:
				for v_day in calendar.monthcalendar(date.year, date.month)[v_week_idx]:
					if v_day > 0 and v_week_idx == 0 and datetime.date(date.year, date.month, v_day).isoweekday() == 4:
						v_rtn_week_no += 1

					if v_day > 0 and datetime.date(date.year, date.month, v_day).isoweekday() == 1:
						v_rtn_week_no += 1

				if date.day in calendar.monthcalendar(date.year, date.month)[v_week_idx]:
					break

				v_week_idx += 1
	# 월 중간
	else:
		if datetime.date(year, month, 1).isoweekday() in [5, 6, 7]:
			v_rtn_week_no = 0

		v_week_idx = 1
		while v_week_idx < v_month_week_count:
			for v_day in calendar.monthcalendar(date.year, date.month)[v_week_idx]:
				if v_day > 0 and datetime.date(date.year, date.month, v_day).isoweekday() == 1:
					v_rtn_week_no += 1

			if date.day in calendar.monthcalendar(date.year, date.month)[v_week_idx]:
				break

			v_week_idx += 1

	print(f'일자: {date} 월: {v_rtn_month} 주차: {v_rtn_week_no}')


if __name__ == "__main__":
	args = sys.argv

	year = int(args[1])
	month = int(args[2])
	day = int(args[3])

	get_week_of_month(year, month, day)
