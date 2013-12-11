import sys
import mysql.connector

from datetime import date

class Projections:
	def __init__(self, cnx = None):
		self.league_averages = {}
		
		# Use dependency injection to determine where the database connection comes from.
		if(not cnx):
			self.cnx = mysql.connector.connect(user='fantasy', password='fantasy', host='localhost', database='basketball_reference')
		else:
			self.cnx = cnx

	##########################################################
	# Retrieves the player information in the players table.
	# Returns a dictionary of the values.
	##########################################################
	def get_player_info(self,player_id):
		cursor = self.cnx.cursor()
		query = """
			select * from players p where id = '%s'
		""" % (player_id)
	
		try:
			cursor.execute(query)
			info = {}
			for result in cursor:
				info["id"] = result[0]
				info["name"] = result[1]
				info["position"] = result[2]
				info["height"] = result[3]
				info["weight"] = result[4]
				info["url"] = result[5]
		finally:
			cursor.close()
		
		return info

	####################################################################
	# Determine the team that the player plays for, given the provided
	# season and date.
	####################################################################
	def get_team(self, player_id, season, date=date.today()):
		cursor = self.cnx.cursor()
	
		query = """
			select team from game_totals_basic where player_id = '%s' and season = %d and
				game_number = (select max(game_number) from game_totals_basic 
					where player_id = '%s' and season = %d and date <= '%s')
		""" % (player_id, season, player_id, season, date)
	
		try:
			cursor.execute(query)
			for result in cursor:
				return result[0]
		finally:
			cursor.close()

	##############################################################################
	# To calculate defensive vs a position we want to get all of the players who
	# played against a team, sum their points, and divide by the number of games
	# the team has played.
	##############################################################################
	def calculate_defense_vs_position(self, metric, position, team, season, date=date.today()):
		cursor = self.cnx.cursor()
	
		query = ""
		try:
			query = """select sum(b.%s)/(select max(game) from team_game_totals where team = '%s' and season = %d and date <= '%s') 
					from players p inner join game_totals_basic b on p.id = b.player_id 
					where b.season = %d and p.position = '%s' and b.opponent = '%s'
						and date <= '%s'""" % (metric, team, season, date, season, position, team, date)
			cursor.execute(query)
		
			for result in cursor:
				return result[0]
			
		finally:
			cursor.close()

	def calculate_pace(self, team, season):
		cursor = self.cnx.cursor()
		query = """
			select minutes_played, 0.5 * ((field_goal_attempts + 0.4 * free_throw_attempts - 1.07 * (offensive_rebounds / (offensive_rebounds + (opp_total_rebounds - opp_offensive_rebounds))) * (field_goal_attempts - field_goals) + turnovers) + (opp_field_goal_attempts + 0.4 * opp_free_throw_attempts - 1.07 * ((opp_offensive_rebounds) / (opp_offensive_rebounds + (total_rebounds - offensive_rebounds))) * (opp_field_goal_attempts - opp_field_goals) + opp_turnovers)) as "pace"
			from team_game_totals t 
			where season = %d and team = '%s'
		""" % (season, team)
	
		total = 0.0
		count = 0
		try:
			cursor.execute(query)
			for result in cursor:
				count = count + 1
				if result[0] == 240:
					total = total + result[1] 
				else:
					total = total + (result[1]/result[0])*240
		
			return total/count
		finally:
			cursor.close()

	########################################################
	# Calculates the league average for the provided stat.
	########################################################
	def calculate_league_avg(self, stat, position, season, date=date.today()):
		##########################################################
		# This calculation is somewhat expensive, so just return
		# the cached value if we've already computed it.
		##########################################################
		key = stat + "-" + position
		if key in self.league_averages:
			return self.league_averages[key]
	
		cursor = self.cnx.cursor()
		query = """
			select sum(%s)/(select max(t.game) from team_game_totals t where t.team = b.opponent and season = %d and date <= '%s') as "avg", opponent 
			from game_totals_basic b inner join players p on p.id = b.player_id 
			where season = %d and position = '%s' and date <= '%s'
			group by opponent 
			order by avg desc
		""" % (stat, season, date, season, position, date)
	
		total = 0
		count = 0
		try:
			cursor.execute(query)
			for result in cursor:
				count = count + 1
				total = total + result[0]
		finally:
			cursor.close()
	
		avg = total/count
		self.league_averages[key] = avg
	
		return avg

	def calculate_defense_factor_vs_position(self, position, team, season, league_avg = False):
		cursor = self.cnx.cursor()
		query = ""
		if league_avg:
			query = """
				select sum(b.points)/(select max(game) from team_game_totals where season = %d) 
				from players p inner join game_totals_basic b on p.id = b.player_id 
				where b.season = %d and p.position = '%s' and b.opponent = '%s'
			""" % (team, season, season, position, team)
		else:
			query = """
				select sum(b.points)/(select max(game) from team_game_totals where team = '%s' and season = %d) 
				from players p inner join game_totals_basic b on p.id = b.player_id 
				where b.season = %d and p.position = '%s' and b.opponent = '%s'
			""" % (team, season, season, position, team)
	
	
		factor = -1
		try:
			cursor.execute(query)
			for result in cursor:
				factor = result[0]
		finally:
			cursor.close()
	
		return factor

	###################################################################################
	# Retrieves season averages for a player up to a certain date so we can
	# establish a baseline for the player, prior to adjusting based on matchups, etc.
	###################################################################################
	def get_baseline(self, player_id, season, stat, date=date.today()):
		cursor = self.cnx.cursor()
		query = """
			select avg(%s) from game_totals_basic b where player_id = '%s' and season = %d and date <= '%s'
			""" % (stat, player_id, season, date)
	
		adv_query = """
			select avg(usage_pct), avg(offensive_rating), avg(defensive_rating)
			from game_totals_advanced
			where player_id = '%s' and season = %d and date <= '%s'
		""" % (player_id, season, date)
	
		avg_stat = 0
		avg_usage_pct = 0
		avg_off_rating = 0
		avg_def_rating = 0
	
		try:
			cursor.execute(query)
			for result in cursor:
				avg_stat = result[0]
		
			cursor.execute(adv_query)
			for result in cursor:
				avg_usage_pct = result[0]
				avg_off_rating = result[1]
				avg_def_rating = result[2]
		finally:
			cursor.close()
	
		return (avg_stat, avg_usage_pct, avg_off_rating, avg_def_rating)
	
	######################################################################################
	# Adjusts the specified stat for each game based on the league average at that point
	# to come up with a real, adjusted value.
	#
	# An example would be if, for the first five games of the season, a player scored
	# 10 points a game.  However, if all of the games were against top-3 defenses, then
	# those 10-point games are more impressive than 10 points vs a bottom-3 defense, 
	# and his scoring average will be adjusted accordingly.
	######################################################################################
	def normalize_player_avg_stat(self, player_id, stat, season, date=date.today()):
		cursor = self.cnx.cursor()
		player_info = self.get_player_info(player_id)
		
		league_avg = 0
		
		query = """
			select avg(b.%s) from players p inner join game_totals_basic b on p.id = b.player_id
			where p.position = '%s' and b.season = %d and b.date <= '%s'
		""" % (stat, player_info["position"], season, date)
		
		try:
			cursor.execute(query)
			
			for result in cursor:
				league_avg = result[0]
			
			# Get all game instances of desired stat for this player.
			query = """
				select %s from game_totals_basic b
				where player_id = '%s' and season = %d and date <= '%s'
			""" % (stat, player_id, season, date)
			
			cursor.execute(query)
			
			adjusted = []
			for result in cursor:
				adjusted.append( (result[0]/league_avg)*result[0] )
			
			return sum(adjusted)/len(adjusted)
		finally:
			cursor.close()
	
	def get_game_list(self, d=date.today()):
		games = []
		
		cursor = self.cnx.cursor()
		query = """
			select date, season, visitor, home from schedules where date = '%s'
		""" % (d)
		
		try:
			cursor.execute(query)
			for result in cursor:
				datepieces = result[0].split("-")
				curr = {
					"date": date(int(datepieces[0]), int(datepieces[1]), int(datepieces[2])),
					"season": result[1],
					"visitor": result[2],
					"home": result[3]
				}
				
				games.append(curr)
		finally:
			cursor.close()
			
		return games
		
	##############################################################################
	# Makes a projection for a player's stat line based on a variety of factors,
	# starting with their average for the season in each relevant stat.
	##############################################################################
	def calculate_projection(self, player_id, stat, season, opponent, date=date.today()):
		info = self.get_player_info(player_id)
		team = self.get_team(player_id, season, date)
		baselines = self.get_baseline(player_id,2013,stat, date)
	
		avg_points = baselines[0]
		adjusted_points = avg_points
	
		#######################################
		# Take pace of the game into account.
		#######################################
		team_pace = self.calculate_pace(team, season)
		opp_pace = self.calculate_pace(opponent, season)
		avg_pace = (team_pace + opp_pace)/2
		pace_factor = avg_pace/team_pace
	
		adjusted_points = float(avg_points) * float(pace_factor)
	
		######################################################################
		# Effectiveness of opponent defense, compared to the league average
		# for this player's position.
		######################################################################
		league_avg = self.calculate_league_avg(stat, info["position"], season)
		def_factor = self.calculate_defense_vs_position(stat, info["position"], opponent, season, date)

		adjusted_points = adjusted_points * float(def_factor/league_avg)
	
		return adjusted_points

	def regression(self):
		games = []
		cursor = self.cnx.cursor()
		
		try:
			# Grab all game logs
			cursor.execute("select player_id, season, game_number, date, team, home, opponent, points from game_totals_basic where season = 2013")
			
			for game in cursor:
				games.append(game)	
		finally:
			cursor.close()
		
		for game in games:
			proj_points = self.calculate_projection(game[0], "points", game[1], game[6], game[3])
			print "%s/%d/%s/%s/%s - Expected: %f, Actual: %f  (RMSE %f)" % (
				game[0],
				game[2],
				game[3],
				game[4],
				game[6],
				proj_points,
				game[7],
				(proj_points - game[7])**2
			)
	
	def run(self):
		positions = ["G","F","C"]
		teams = ["ATL","BOS","BRK","LAL"]

		id = 'anthoca01'
		game_date = date(2013,11,01)
		print self.calculate_projection(id, "points", 2013, 'BOS', game_date)

if __name__ == '__main__':
	projections = Projections()
	projections.regression()