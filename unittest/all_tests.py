import unittest
import test_fantasy_point_calculator
import test_import_salaries
import test_projections
import test_basketballreference_team_gamelog_parser
import test_vegas_odds
import test_rg_player_stats

##########################
# FantasyPointCalculator
##########################
suite = unittest.TestLoader().loadTestsFromTestCase(test_fantasy_point_calculator.TestFantasyPointCalculator)
unittest.TextTestRunner(verbosity=2).run(suite)

##################
# SalaryImporter
##################
suite = unittest.TestLoader().loadTestsFromTestCase(test_import_salaries.TestSalaryImporter)
unittest.TextTestRunner(verbosity=2).run(suite)

###############
# Projections
###############
suite = unittest.TestLoader().loadTestsFromTestCase(test_projections.TestProjections)
unittest.TextTestRunner(verbosity=2).run(suite)

#######################
# Team Gamelog Parser
#######################
suite = unittest.TestLoader().loadTestsFromTestCase(test_basketballreference_team_gamelog_parser.TestBasketballReferenceTeamGameLogParser)
unittest.TextTestRunner(verbosity=2).run(suite)

##############
# Vegas Odds
##############
suite = unittest.TestLoader().loadTestsFromTestCase(test_vegas_odds.TestVegasOdds)
unittest.TextTestRunner(verbosity=2).run(suite)

###################
# RG Player Stats
###################
suite = unittest.TestLoader().loadTestsFromTestCase(test_rg_player_stats.TestRGPlayerStats)
unittest.TextTestRunner(verbosity=2).run(suite)