import unittest
from mlb.constants.mlb_constants import MLBConstants
from mlb.parsers.player_splits_parser import PlayerSplitsParser

__author__ = 'dan'


class TestPlayerSplitsParser(unittest.TestCase):
	def setUp(self):
		self.player_splits_parser = PlayerSplitsParser()

	def tearDown(self):
		self.player_splits_parser = None

	def test_parse_pitcher_splits(self):
		season = "2013"
		self.player_splits_parser.player_data = {MLBConstants.PLAYER_ID: "verlaju01", MLBConstants.POSITION: "Pitcher"}
		self.player_splits_parser.parse(open('../test_files/pitcher_splits.html'), season)

		pd = self.player_splits_parser.player_data
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.GAMES_PLAYED] == 34)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.PLATE_APPEARANCES] == 925)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.AT_BATS] == 838)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.RUNS] == 94)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.HITS] == 212)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.DOUBLES] == 38)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.TRIPLES] == 4)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.HOME_RUNS] == 19)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.STOLEN_BASES] == 21)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.CAUGHT_STEALING] == 4)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.WALKS] == 75)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.STRIKE_OUTS] == 217)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.STRIKE_OUT_TO_WALK_RATIO] == 2.89)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.BATTING_AVERAGE] == 0.253)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.ON_BASE_PERCENTAGE] == 0.315)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.SLUGGING_PERCENTAGE] == 0.376)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.OPS] == 0.691)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.TOTAL_BASES] == 315)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.DOUBLE_PLAYS_GROUNDED_INTO] == 15)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.HIT_BY_PITCH] == 4)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.SACRIFICE_HITS] == 2)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.SACRIFICE_FLIES] == 6)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.INTENTIONAL_WALKS] == 1)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.REACHED_ON_ERROR] == 6)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.BABIP] == 0.317)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.T_OPS_PLUS] == 100)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.S_OPS_PLUS] == 94)

		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.WINS] == 13)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.LOSSES] == 12)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.WIN_LOSS_PCT] == 0.520)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.ERA] == 3.46)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.GAMES_STARTED] == 34)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.GAMES_FINISHED] == 0)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.COMPLETE_GAMES] == 0)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.SHUT_OUTS] == 0)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.SAVES] == 0)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.INNINGS_PITCHED] == 218.1)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.EARNED_RUNS] == 84)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.BALKS] == 1)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.WILD_PITCHES] == 3)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.WHIP] == 1.315)
		self.assertTrue(pd[MLBConstants.PITCHER_SPLITS][season]["2013 Totals"][
							MLBConstants.STRIKE_OUTS_PER_9_INNINGS] == 8.9)

	def test_parse_batter_splits(self):
		self.player_splits_parser.player_data = {MLBConstants.PLAYER_ID: "cabremi01", MLBConstants.POSITION: "Third base"}
		self.player_splits_parser.parse(open('../test_files/batter_splits.html'), "2014")

		pd = self.player_splits_parser.player_data
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.GAMES_PLAYED] == 4)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.GAMES_STARTED] == 4)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.PLATE_APPEARANCES] == 17)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.AT_BATS] == 16)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.RUNS] == 1)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.HITS] == 6)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.DOUBLES] == 2)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.TRIPLES] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.HOME_RUNS] == 1)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.RBI] == 3)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.STOLEN_BASES] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.CAUGHT_STEALING] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.WALKS] == 1)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.STRIKE_OUTS] == 4)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.BATTING_AVERAGE] == 0.375)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.ON_BASE_PERCENTAGE] == 0.412)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.SLUGGING_PERCENTAGE] == 0.688)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.OPS] == 1.099)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.TOTAL_BASES] == 11)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.DOUBLE_PLAYS_GROUNDED_INTO] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.HIT_BY_PITCH] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.SACRIFICE_HITS] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.SACRIFICE_FLIES] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.INTENTIONAL_WALKS] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.REACHED_ON_ERROR] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.BABIP] == 0.455)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.T_OPS_PLUS] == 100)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"]["2014 Totals"][
							MLBConstants.S_OPS_PLUS] == 209)

		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.GAMES_PLAYED] == 4)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.GAMES_STARTED] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.PLATE_APPEARANCES] == 13)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.AT_BATS] == 12)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.RUNS] == 1)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.HITS] == 6)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.DOUBLES] == 2)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.TRIPLES] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.HOME_RUNS] == 1)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.RBI] == 3)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.STOLEN_BASES] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.CAUGHT_STEALING] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.WALKS] == 1)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.STRIKE_OUTS] == 2)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.BATTING_AVERAGE] == 0.5)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.ON_BASE_PERCENTAGE] == 0.538)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.SLUGGING_PERCENTAGE] == 0.917)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.OPS] == 1.455)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.TOTAL_BASES] == 11)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.DOUBLE_PLAYS_GROUNDED_INTO] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.HIT_BY_PITCH] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.SACRIFICE_HITS] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.SACRIFICE_FLIES] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.INTENTIONAL_WALKS] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.REACHED_ON_ERROR] == 0)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.BABIP] == 0.556)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.T_OPS_PLUS] == 164)
		self.assertTrue(pd[MLBConstants.BATTER_SPLITS]["2014"][MLBConstants.SPLITS_VS_RHP][
							MLBConstants.S_OPS_PLUS] == 299)


if __name__ == '__main__':
	unittest.main()