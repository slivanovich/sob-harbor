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
West Palm Beach Christian Convention Center: West Palm Beach Christian Convention Center (originally known as West Palm Beach Auditorium) is a 5,000-seat multi-purpose arena in West Palm Beach, Florida at the intersection of North Congress Avenue and Palm Beach Lakes Boulevard.  It was built in 1965 as the West Palm Beach Auditorium and was designed by famed architect Bertrand Goldberg.  It was home to the West Palm Beach Blaze ice hockey team, Florida Bobcats arena football team and Florida Hammerheads roller hockey team.  It hosted the twelfth WWF In Your House pay-per-view in 1996.  The Fort Lauderdale Strikers played their indoor soccer games here in the early 1980s.  It was also host to innumerable concerts from different rock acts.

Palm Beach Outlets: Palm Beach Outlets is a 440,000 square foot outlet shopping center in West Palm Beach, Florida.  Opened on February 14, 2014, it was developed on the site of the former Palm Beach Mall.  Palm Beach Outlets features over 100 stores including Saks Fifth Avenue OFF 5TH, Ann Taylor, Banana Republic, Brooks Brothers, J.Crew, Kenneth Cole, Nike, Tommy Hilfiger, Under Armour, and Vera Bradley.

West Palm Beach Sheriffs: The West Palm Beach Sheriffs were a minor league baseball team, based in West Palm Beach, Florida, as a member of the early Florida State League in 1928.  They were the first team to represent West Palm Beach inside of Florida State League.  The city would not host another FSL team until the West Palm Beach Indians arrived in 1940.  The team folded in 1928, when the FSL went on a hiatus.

Ann Inc.: Ann Inc. is an American group of specialty apparel retail chain stores for women.  The company headquartered in New York City and currently operates as a subsidiary of Ascena Retail Group.  The stores offer classic styled suits, separates, dresses, shoes and accessories.  The brand is marketed under five divisions: Ann Taylor, Loft, Lou & Grey, Ann Taylor Factory and Loft Outlet.

West Palm Beach Expos: The West Palm Beach Expos were a Florida State League minor league baseball team that existed from 1969 to 1997.  Located in West Palm Beach, Florida, they were affiliated with the Montreal Expos and they played their home games at West Palm Beach Municipal Stadium.  However the team was first established in 1965, as the West Palm Beach Braves, and affiliated with the Milwaukee Braves in 1965 and the Atlanta Braves from 1966 to 1968.  The Braves played their home games at Mack Field.

Palm Tran: Palm Tran is the public transit bus system run by the Palm Beach County Government, serving Palm Beach County, Florida.  During fiscal year 2015, Palm Tran provided 10,773,132 one-way passenger trips and 889,056 paratransit trips to Palm Beach County.  Palm Tran also serves a portion of Broward County, Florida where it overlaps with Broward County Transit.  Palm Tran has four main facilities (North Campus in West Palm Beach, South Campus in Delray Beach, Palm Tran Connection/Military Trail and the Belle Glade Facility) with its main headquarters in West Palm Beach on Electronics Way.  The current Executive Director is Clinton B. Forbes.

Reid Moore Jr.: Reid Moore Jr. (born September 27, 1934) is an American former politician in the state of Florida who served two non-consecutive terms in the Florida House of Representatives and as Mayor of West Palm Beach.  Born in Tennessee, he earned a law degree from the University of Virginia before moving to Florida in 1959.  Moore soon became involved with local politics in West Palm Beach, beginning with serving as a member of the Greater West Palm Beach Chamber of Commerce Board of Directors in 1963.  Two years later, he mounted a successful campaign for city commissioner, an office he would hold from 1965 to 1969.  During his tenure, he was chosen by his fellow commissioners to be Mayor of West Palm Beach from 1967 to 1968, as the city operated under the Council–manager form of government at the time.

West Palm Beach mayoral election, 1991: The West Palm Beach mayoral election took place on November 5, 1991, to elect a mayor for West Palm Beach, Florida.  Officially, elections for mayor of West Palm Beach are nonpartisan.  Prior to this election, the city operated under a council–manager government system since 1919, with the city commissioners choosing the mayor, a mostly ceremonial office that had less power than the city manager.  However, in March 1991, voters approved a referendum to allow a strong mayor and to transition the city government to a mayor-council structure.  Thus, it was the first direct election for mayor of West Palm Beach since 1919.

Palm Beach Day Academy: Palm Beach Day Academy is a coeducational independent day school located in Palm Beach and West Palm Beach, Florida, USA.  An enrollment of over 500 students in pre-kindergarten 2 year olds to ninth grade is drawn from Palm Beach and West Palm Beach and the outlying communities as far south as Manalapan, as far west as Wellington and as far north as Jupiter.

WPEC: WPEC is the CBS-affiliated television station for the Gold and Treasure Coasts of South Florida in the United States.  Licensed to West Palm Beach, it broadcasts a high definition digital signal on VHF channel 13 (or virtual channel 12 via PSIP) from a transmitter southeast of Wellington along US 441/SR 7, in unincorporated Palm Beach County.  Owned by the Sinclair Broadcast Group, the station is sister to Fort Pierce-licensed CW affiliate WTVX, Palm Beach-licensed Class A MyNetworkTV affiliate WTCN-CA and Stuart-licensed Class A Azteca América affiliate WWHB-CA.  All of the television outlets share studios together on Fairfield Drive in Mangonia Park (with a West Palm Beach postal address).  On cable, WPEC can be seen on Comcast Xfinity channel 9 (in Martin, Palm Beach, Okeechobee, and southern St. Lucie counties) and channel 12 (in Indian River and northern St. Lucie counties), and in high definition on digital channel 433.

Question: What is one of the five divisions of Ann Inc. which has store in Palm Beach Outlets in West Palm Beach, Florida?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company."
    },
    "division_name": {
      "type": "string",
      "description": "The name of the division of the company that has a store in the specified outlet."
    },
    "outlet_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the outlet shopping center."
        },
        "city": {
          "type": "string",
          "description": "The city where the outlet is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the outlet is located."
        }
      },
      "required": [
        "name",
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "is_division_present_in_outlet": {
      "type": "boolean",
      "description": "Indicates if the specified division has a store in the outlet."
    }
  },
  "required": [
    "company_name",
    "division_name",
    "outlet_details",
    "is_division_present_in_outlet"
  ],
  "additionalProperties": false
}
