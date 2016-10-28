import webapp2
import cgi

form="""  
<form method="post">
	What is your birthday?
	<br>
	<label>Month<input type="type" name="month" value=%(month)s></label>
	<label>Day<input type="type" name="day" value=%(day)s></label>
	<label>Year<input type="type" name="year" value=%(year)s></label>
	<div style="color: red">%(error)s</div>
	<br>
	<br>
	<input type="submit">
</form> 
"""
def escape_html(month):
	return cgi escape(month, quote= True)

def escape_html(day):
	return cgi escape(day, quote= True)

def escape_html(year):
	return cgi escape(year, quote= True)

def valid_year(year):
		if year and year.isdigit():
			year = int(year)
			if year > 1900 and year < 2020:
				return year

def valid_day(day):
		if day and day.isdigit():
			day = int(day)
			if day > 0 and day <= 31:
				return day

months = ['Janurary','February','March','April','May','June','July','August','September','October','November','December']
month_abbvs = dict((m[:3].lower(),m) for m in months)

def valid_month(month):
		if month:
			short_month =  month[:3].lower()
			return month_abbvs.get(short_month)

class MainPage(webapp2.RequestHandler):

	def write_form(self, error="",month="",day="",year=""):
		self.response.out.write(form % {"error": error,
										"month": escape_html(month),
										"day": escape_html(day),
										"year": escape_html(year)})

	def get(self):
		self.write_form()

	def post(self):
		user_month = self.request.get('month')
		user_day = self.request.get('day')
		user_year = self.request.get('year')

		month = valid_month(user_month)
		day = valid_day(user_day)
		year = valid_year(user_year)

		if not (month and day and year):
			self.write_form("That doesn't look valid to me, friend.",
							user_month,user_year,user_day)
		else:
			self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([('/',MainPage)], debug=True)
