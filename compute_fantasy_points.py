import sys
import mysql.connector

site = "DRAFT_DAY"
for arg in sys.argv:
	if arg == "import_salaries.py":
		pass
	else:
		pieces = arg.split("=")
		if pieces[0] == "site":
			site = pieces[1]


cnx = mysql.connector.connect(user='fantasy', password='fantasy', host='localhost', database='basketball_reference')
cnx_insert = mysql.connector.connect(user='fantasy', password='fantasy', host='localhost', database='basketball_reference')

cursor = cnx.cursor()
query = ("Select * from game_totals_basic t left join fantasy_points p on t.id = p.id where p.id is NULL;")
cursor.execute(query)

for (result) in cursor:
	player_id = result[1]
	season = result[2]
	game_number = result[3]
	field_goals = result[12]
	field_goal_attempts = result[13]
	three_point_field_goals = result[15]
	three_point_field_goal_attempts = result[16]
	free_throws = result[18]
	free_throw_attempts = result[19]
	total_rebounds = result[23]
	assists = result[24]
	steals = result[25]
	blocks = result[26]
	turnovers = result[27]
	points = result[29]
	
	missed_shots = (field_goal_attempts - field_goals) + (three_point_field_goal_attempts - three_point_field_goals) + (free_throw_attempts - free_throws)

	fantasy_points = points + (total_rebounds * 1.25) + (assists * 1.5) + (steals * 2) + (blocks * 2) - (turnovers * 0.5) - (missed_shots * 0.25)
	
	# 1 point bonus for 3 pointer made
	fantasy_points = fantasy_points + three_point_field_goals
	
	triple_or_double_double = 0
	criteria = [points, total_rebounds, assists, steals, blocks]
	for c in criteria:
		if c >= 10:
			triple_or_double_double = triple_or_double_double + 1

	if triple_or_double_double == 2:
		fantasy_points = fantasy_points + 1
	elif triple_or_double_double == 3:
		fantasy_points = fantasy_points + 2
	
	cursor2 = cnx_insert.cursor()
	insert_query = ("insert into fantasy_points (player_id, site, season, game_number, points) values ('%s','%s',%d,%d,%f)") % (player_id, site, season, game_number, fantasy_points)
	cursor2.execute(insert_query)
	cursor2.close()
	
cursor.close()