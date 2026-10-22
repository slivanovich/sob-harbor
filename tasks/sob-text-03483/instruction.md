Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Church of the Holy Innocents (Albany, New York): The former Church of the Holy Innocents, later known as Church of the Nativity of our Virgin Lady, was originally an Episcopal church located on North Pearl Street (New York State Route 32) in Albany, New York, United States.  It and an adjacent chapel were built in the mid-19th century in an early Gothic Revival style designed by Frank Wills.  It was listed on the National Register of Historic Places in 1978.

Greater Allen A. M. E. Cathedral of New York: The Greater Allen Cathedral of New York is an African Methodist Episcopal church located in Jamaica, Queens, New York.  The congregation currently has over 23,000 members, making it one of the largest churches in the United States.  The church's budget exceeds $34 million annually and it operates a 750-student private school, as well as numerous commercial and social service enterprises.  It also holds a number of expansive commercial and residential properties and coordinates a number of subsidiary organizations.  It has been named one of the nation's most productive religions and urban development institutions, and is one of the Borough of Queens largest private sector employers.  The church has been pastored by Floyd Flake and his wife Elaine for over three decades.  Floyd Flake is also the president of Wilberforce University and a former United States Congressman.

Eilardus Westerlo: Eilardus Westerlo (October 30, 1738, Kantens, Netherlands – December 26, 1790, Albany, New York) was a Dutch Reformed minister who worked in the United States.  He spent his career, from October 1760 until December 1790, as pastor of the Dutch Reformed Church in Albany.  During this period, the United States fought for its independence, and the Dutch Reformed Church in North America gained its independence from the mother church in the Netherlands.

First Church in Albany (Reformed): The First Reformed Church, also known as First Church in Albany or North Dutch Church, is located at North Pearl (New York State Route 32) and Orange streets in Albany, New York, United States.  It is a member congregation of the Reformed Church in America.  The building was designed by Philip Hooker and built in 1798.  It was listed on the National Register of Historic Places in 1974.

Pitkin Tunnel: The Pitkin Tunnel or Pitkin Street Tunnel is a below-ground-level, roofed but not entirely enclosed roadway, in downtown New Haven, Connecticut, United States.  It accommodates simultaneous motor vehicle traffic in both directions.  The tunnel runs from the eastbound one-way Elm Street between Church and Orange Streets ( ), with the southbound lanes of State Street between Court and Chapel Streets ( ) across from State Street station.  It passes under Orange Street.  It runs under or next to the New Haven City Hall and County Courthouse and the Federal Courthouse on Church Street, the local Emergency Operations Center, and at least three more buildings that house banks and the headquarters of United Illuminating, the electric utility serving much of New Haven and Fairfield counties.

Palace Theatre (Albany, New York): The Palace Theatre is an entertainment venue in downtown Albany, New York, located on the corner of Clinton Avenue (US 9) and North Pearl Street (NY 32).  The 2,844 seat theater is owned by the City of Albany and run by the Palace Performing Arts Center, Inc - a 501(c)(3) non-profit organization.  The Palace Theatre hosts more than 150 events annually, from public performances such as concerts, plays, educational programs, live comedy and a classic movie series to private events such as weddings, dance competitions, corporate events and graduations.  It is also the annual home of the Albany Symphony Orchestra.

Franklin Street Presbyterian Church and Parsonage: Franklin Street Presbyterian Church and Parsonage is a historic Presbyterian church located at 100 West Franklin Street at Cathedral Street, northwest corner in Baltimore, Maryland, United States.  The church is a rectangular Tudor Gothic building dedicated in 1847, with an addition in 1865.  The front features two 60 foot flanking octagonal towers are also crenelated and have louvered belfry openings and stained glass Gothic-arched windows.  The parsonage has walls of brick, heavy Tudor-Gothic window hoods, and battlements atop the roof and was built in 1857.  This church was incorporated in 1844 by a group of men from the First Presbyterian Church then located at the northwest corner of East Fayette Street and North Street (now Guilford Avenue) in downtown (later relocated in 1854 to West Madison Street and Park Avenue in Mount Vernon-Belvedere neighborhood after selling their previous third church building of 1790-95 to the Federal Government which built a U.S. Courthouse there [to 1889, replaced again 1932] dedicated in 1860 by President James Buchanan).  They felt the need for a new church in that fast-growing northern section of the city formerly "Howard's Woods" of Col. John Eager Howard's (Revolutionary War commander of the famed "Maryland Line" regiment of the Continental Army) country estate "Belvedere" (mansion located at intersection of North Calvert and East Chase Streets, razed 1875) where the Washington Monument was erected with its four surrounding park squares just two blocks from their new building.  Franklin Street Church was also located on "Cathedral Hill" in the southern part of the community bordering downtown and across the street from the old Baltimore Cathedral (Basilica of the National Shrine of the Assumption of the Blessed Virgin Mary) erected 1806-1821 and designed by Benjamin Latrobe.  Later in 1882-1886, philanthropist Enoch Pratt founded his central library for the new Enoch Pratt Free Library then facing West Mulberry Street at Cathedral, a block south which was replaced in 1931-33 by a new central library building encompassing the entire block and now directly across Franklin Street from the F.S.P.C.  In 1973, the two historic congregations reunited to form The First and Franklin Street Presbyterian Church and was centered at the First Church site on West Madison and Park.  The Franklin Street building was used by the merged congregation for a time and then sold to a fundamentalist independent Protestant congregation and later re-sold to the present "New Unity Church Ministries".  Across Cathedral Street to the northeast was the 1820s era Greek Revival home designed by Robert Mills (who also did the Washington Monument two blocks away) which later was occupied by the original Maryland Club, an exclusive Southern-leaning dining and leisure society of gentlemen, founded 1857 that was once threatened by Massachusetts Militia Gen. Benjamin F. Butler, U.S.A. when he occupied Baltimore at the beginning of the Civil War on May 13, 1861, and fortified Federal Hill with a Fort and cannons overlooking the harbor and city, "to put a shot into it" if he spied a reputed rebel flag flying or any discontent to declared martial law.  The Club later moved to North Charles and East Eager Streets in 1892 and mansion was later replaced by the former Central Building of the Young Men's Christian Association of Central Maryland (YMCA) which was closed in the 1980s and the building renovated as the Mount Vernon Hotel and Cafe.

WNYT (TV): WNYT is the NBC-affiliated television station for the Capital District of New York State and Western New England.  Licensed to Albany, it broadcasts a high definition digital signal on VHF channel 12 (or virtual channel 13.1 via PSIP) from a transmitter on the Helderberg Escarpment west of New Salem, a hamlet of New Scotland.  The station is owned by Hubbard Broadcasting as part of a duopoly with Pittsfield, MA-licensed MyNetworkTV affiliate WNYA and the two outlets share studios at the WNYT Broadcast Center on North Pearl Street (along NY 32) in Menands (with an Albany postal address).

WNYA: WNYA is the MyNetworkTV-affiliated television station for the Capital District of New York State and Western New England.  Licensed to Pittsfield, Massachusetts, it broadcasts a high definition digital signal on VHF channel 13 (or virtual channel 51.1 via PSIP) from a transmitter on the Helderberg Escarpment west of New Salem, New York (a hamlet of New Scotland).  The station is owned by Hubbard Broadcasting as part of a duopoly with NBC affiliate WNYT and the two television outlets share studios on North Pearl Street, along NY 32/Wolfert Avenue, in Menands (with an Albany postal address).  Syndicated programming on WNYA includes "Family Feud", "The Wendy Williams Show" and among others.

Trinity Wesleyan Church (Evansville): Trinity Wesleyan Church is a Wesleyan church located in Evansville, Indiana.  It was founded as the East Side Full Gospel Tabernacle in 1931 by the Rev. A. L. Luttrull, who led the church until 1953.  For many years it was the home of New Trinity Bible School, and a daily morning radio broadcast on WGBF.  The church is currently pastored by the Rev. Duane F. Allison.

Question: What was the nationality of the man who pastored the church located at North Pearl and Orange streets in Albany, New York?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "church_name": {
      "type": "string",
      "description": "The name of the church identified by the location."
    },
    "church_location": {
      "type": "object",
      "properties": {
        "street_address": {
          "type": "string",
          "description": "The street address of the church."
        },
        "city": {
          "type": "string",
          "description": "The city where the church is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the church is located."
        }
      },
      "required": [
        "street_address",
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "pastor_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the pastor."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the pastor."
        },
        "role": {
          "type": "string",
          "description": "The role of the individual in the church."
        },
        "tenure_start_year": {
          "type": "integer",
          "description": "The start year of the pastor's tenure."
        },
        "tenure_end_year": {
          "type": "integer",
          "description": "The end year of the pastor's tenure."
        }
      },
      "required": [
        "name",
        "nationality",
        "role",
        "tenure_start_year",
        "tenure_end_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "church_name",
    "church_location",
    "pastor_details"
  ],
  "additionalProperties": false
}
