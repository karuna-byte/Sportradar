from database.base_repository import BaseRepository


class TeamAnalysisViewModelRepository(BaseRepository):

    # Fetch all team info method
    def fetch_all_team_info(self, param=None):
        query = """
        select t.team_id as TeamId, t.market as MarketName, t.name as TeamName, t.alias as TeamNameAlias, t.founded as Founded, 
        t.mascot as Mascot, t.fight_song FightSong, t.championships_won as ChampionshipsWon, c.name as ConferenceName, 
        c.alias as Conference_Alias, v.name as VenueName, v.state as VenueState, v.country as VenueCountry,
        d.name as DivisionName, d.alias as DivisionNameAlias
        from teams t
        join conferences c on t.conference_id = c.conference_id 
        join venues v on t.venue_id = v.venue_id
        join divisions d on t.division_id = d.division_id
        order by t.market;
        """
        return self.get_all(query, param)

    # Fetch all players info method
    def fetch_all_players_info(self, param=None):
        query = """
        select concat(t.market, ' ', t.name) as TeamName, p.first_name as PalyerFirstName, p.last_name as PlayerLastName, p.abbr_name as  AbbreviationName,
        p.birth_place as BirthPlace, p.position as Position, p.height as Height, p.weight as Weight, p.status as Status, 
        p.eligibility as Eligibility
        from players p
        join teams t on p.team_id = t.team_id order by t.name;
        """
        return self.get_all(query, param)

    # Fetch seasons info method
    def fetch_seasons_info(self, param=None):
        query = """
        select year as SeasonYear, start_date as StartDate, end_date as EndDate, status Status, type_code as TypeCode from seasons;
        """
        return self.get_all(query, param)

    # Fetch team roster method
    def fetch_team_roster(self, team_id):
        query = """
        select first_name as FirstName, last_name as LastName, abbr_name as AbbrevationName, birth_place as BirthPlace,
        position as Position, height as Height, weight as Weight, status as Status, eligibility as Eligibility
        from players where team_id = %s;
        """
        params = (team_id,)
        return self.get_all(query, params)

    # Fetch venue info method
    def fetch_venue_info(self):
        query = """
        select name as VenueName, city as City, state as State, country as Country, zip as Zip, address as Address,
        capacity as Capacity, surface as Surface, roof_type as RoofType, latitude as Latitude, longitude as Longitude
        from venues;
        """
        params = ()
        return self.get_all(query, params)

    # Fetch coach info method
    def fetch_coach_info(self):
        query = """
        select concat(t.market, ' ', t.name) as TeamName, c.full_name as CoachName, c.position as Position
        from coaches c
        join teams t on c.team_id = t.team_id;
        """
        params = ()
        return self.get_all(query, params)

    # Fetch ranking info method
    def fetch_ranking_info(self):
        query = """
        select concat(t.market, ' ', t.name) as TeamName, s.year as Season, r.poll_name as PollName, r.week as Week, r.ranking as Ranking, r.prev_rank as PreviousRanking, r.points as Points,
        r.fp_votes as FP_Votes, r.wins as Wins, r.losses as Losses, r.ties as Ties
        from rankings r
        join teams t on r.team_id = t.team_id
        join seasons s on r.season_id = s.season_id;
        """
        params = ()
        return self.get_all(query, params)
