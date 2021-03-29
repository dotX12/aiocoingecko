
class Interval:
    MINUTELY = 'minutely'
    HOURLY = 'hourly'
    DAILY = 'daily'


class MarketSortOrder:
    MARKET_CAP_DESC = 'market_cap_desc'
    GECKO_DESC = 'gecko_desc'
    GECKO_ASC = 'gecko_asc'
    MARKET_CAP_ASC = 'market_cap_asc'
    VOLUME_ASC = 'volume_asc'
    M_VOLUME_DESC = 'm_volume_desc'
    ID_ASC = 'id_asc'
    ID_DESC = 'id_desc'


class SortOrder:
    TRUST_SCORE_DESC = 'trust_score_desc'
    TRUST_SCORE_ASC = 'trust_score_asc'
    VOLUME_DESC = 'volume_desc'


class IncludeTickers:
    ALL = 'all'
    UNEXPIRED = 'unexpired'


class ProjectType:
    BOTH = 'both'
    COIN = 'coin'
    MARKET = 'market'


class StatusCategory:
    GENERAL = 'general'
    MILESTONE = 'milestone'
    PARTNERSHIP = 'partnership'
    EXCHANGE_LISTING = 'exchange_listing'
    SOFTWARE_RELEASE = 'software_release'
    FUND_MOVEMENT = 'fund_movement'
    NEW_LISTINGS = 'new_listings'
    EVENT = 'event'


class EventTypes:
    EVENT = 'Event'
    CONFERENCE = 'Conference'
    MEETUP = 'Meetup'
