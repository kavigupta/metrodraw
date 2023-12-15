from metropy.render import render
from metropy.schemes import MBTA, Retro, Terminal

from metropy.model.coord import Coord
from metropy.model.railmap import Railmap


def red_line(rm, downtown_crossing):
    rl = rm.line(downtown_crossing, "red", "Red Line")
    rl.station("Downtown Crossing")
    rl.station("South", "rd")
    rl.stations("Broadway", "Andrew", "JFK/UMass", direction="d", loc="r")

    south_split = rl.segment("d")

    rl.grid(0.5)
    rl.station("Savin Hill", "dl", loc="l")
    rl.stations("Fields Corner", "Shawmut", direction="d")
    rl.station("Ashmont", "d", kind="major")
    rl.stations("Cedar Grove", direction="d", ang=0, loc="l")
    rl.segment("d")

    rl.stations(
        "Butler",
        "Milton",
        "Central Ave",
        "Valley Rd",
        "Capen St",
        direction="l",
        loc="d",
        ang=90,
    )

    rl.station("Mattapan", "l", kind="major", loc="l", ang=0)

    rl.goto(south_split)
    rl.stations(
        "North Quincy",
        "Wollaston",
        "Quincy Center",
        "Quincy Adams",
        direction="dr",
        loc="r",
    )
    rl.station("Braintree", "d", kind="major")
    rl.grid(1)

    rl.goto(downtown_crossing)

    park = rl.station("Park St", "lu", loc="r")

    rl.stations(
        "Charles/MGH",
        "Kendall/MIT",
        "Central",
        "Harvard",
        direction="lu",
        loc="l",
    )

    rl.station("Porter", "lu", loc="u")

    rl.station("Davis", "l", loc="u", ang=0)

    rl.station("Alewife", "l", kind="major", loc="l")

    return park


def orange_line(rm, downtown_crossing):
    ol = rm.line(downtown_crossing, "orange", "Orange Line")

    state = ol.station("State", "ur", loc="r")
    haymarket = ol.station("Haymarket", "uu", loc="r")
    north = ol.station("North", "u", loc="r")

    ol.station("Community College", "uu")
    ol.grid(0.5)
    ol.stations("Sullivan Sq", "Assembly", "Wellington", "Malden Center", direction="u")
    ol.station("Oak Grove", "u", kind="major")
    ol.grid(1)

    ol.goto(downtown_crossing)
    ol.stations("Chinatown", "Tufts Medical Ctr", direction="ld")
    ol.grid(0.5)
    ol.stations(
        "Back Bay",
        "Mass. Ave",
        "Ruggles",
        "Roxbury Crossing",
        "Jackson Sq",
        "Stony Brook",
        "Green St",
        direction="ld",
    )
    ol.station("Forest Hills", "ld", kind="major")
    ol.grid(1)

    return state, haymarket, north


def green_line(rm, park, haymarket, north):
    gl = rm.line(park, "green", "Green Line")

    govt_center = gl.station("Gov't\nCenter", "ur", loc="l", segment_label="B, C, D, E")

    gl.interlining("l")
    gl.segment(haymarket, "D, E")
    gl.segment(north)
    gl.no_interlining(keep_pos=True)

    gl.grid(0.5)

    gl.stations("Science Park/West End", direction="ul", loc="l")
    gl.stations("Lechmere", direction="ul")

    union_square_junction = gl.segment("ul")
    gl.stations("East Somerville", "Gilman Sq", "Magoun Sq", "Ball Sq", direction="ul")
    gl.station("Medford/Tufts", "ul", kind="major")
    gl.goto(union_square_junction)
    gl.grid(1)
    gl.station("Union Sq", "l", kind="major", loc="l")

    gl.goto(park)
    gl.station("Boylston", "ld", loc="d", ang=0)
    _, copley, _, kenmore = gl.stations(
        "Arlington",
        "Copley",
        "Hynes Ctr",
        "Kenmore",
        direction="l",
        loc="ur",
        ang=45,
    )
    gl.goto(copley)
    gl.grid(0.5)
    gl.segment("ld")
    gl.station("Prudential", "d", ang=0, loc="l")
    gl.station("Symphony", "d")
    gl.stations(
        "Northeastern",
        "MFA",
        "Longwood Medical",
        "Brigham Circle",
        "Fenwood Rd",
        "Mission Park",
        "Riverway",
        "Back of the Hill",
        direction="dl",
    )
    gl.station("Heath St", "dl", kind="major")
    gl.grid(1)

    gl.goto(kenmore)
    gl.grid(0.5)
    gl.station("Fenway", "ld", loc="l", ang=0)
    gl.stations(
        "Longwood",
        "Brookline Village",
        "Brookline Hills",
        "Beaconsfield",
        "Reservoir",
        "Chesnut Hill",
        "Newton Centre",
        "Newton Highlands",
        "Eliot",
        "Waban",
        "Woodland",
        direction="dl",
    )
    gl.station("Riverside", "dl", kind="major")
    gl.grid(1)

    gl.goto(kenmore)

    gl.station("St. Mary's St", "lll", loc="u", ang=0)
    gl.grid(0.5)
    gl.stations(
        "Hawes St",
        "Kent St",
        "St. Paul St",
        "Coolidge Corner",
        "Summit Ave",
        "Brandon Hall",
        "Fairbanks",
        "Washington Sq",
        "Tappan St",
        "Dean Rd",
        "Englewood Ave",
        direction="ld",
        loc="l",
        ang=0,
    )
    gl.station("Cleveland Circle", "ld", kind="major")
    gl.grid(1)

    gl.goto(kenmore)
    gl.station("Blanford St", "lu", loc="u", ang=90)
    gl.grid(0.5)
    gl.stations(
        "BU East",
        "BU Central",
        "Amory St",
        "Babcock St",
        "Packards Corner",
        "Harvard Ave",
        "Griggs St",
        "Allston St",
        "Warren St",
        "Washington St",
        "Sutherland Rd",
        "Chiswick Rd",
        "Chestnut Hill Ave",
        "South St",
        direction="l",
        loc="u",
        ang=90,
    )
    gl.station("Boston College", "l", kind="major", loc="l", ang=0)
    gl.grid(1)

    return govt_center


def blue_line(rm, state, govt_center):
    bl = rm.line(state, "blue", "Blue Line")
    bl.segment(govt_center)
    bl.station("Bowdoin", "u", kind="major")

    bl.goto(state)

    bl.stations(
        "Aquarium",
        "Maverick",
        "Airport",
        direction="ur",
        loc="r",
        ang=0,
    )
    bl.grid(0.5)
    bl.stations(
        "Wood Island",
        "Orient Heights",
        "Suffolk Downs",
        "Beachmont",
        "Revere Beach",
        direction="ur",
    )
    bl.station("Wonderland", "ur", kind="major")
    bl.grid(1)


def mbta():
    rm = Railmap()

    downtown_crossing = Coord(0, 0)

    park = red_line(rm, downtown_crossing)
    state, haymarket, north = orange_line(rm, downtown_crossing)
    govt_center = green_line(rm, park, haymarket, north)
    blue_line(rm, state, govt_center)

    rm.propagate_positioning()

    return rm


render(mbta(), "eg/mbta-default.png", scheme=MBTA(), font_size=10, lw=0.25)
render(mbta(), "eg/mbta-retro.png", scheme=Retro(), font_size=10, lw=0.25)
render(mbta(), "eg/mbta-terminal.png", scheme=Terminal(), font_size=10, lw=0.25)
