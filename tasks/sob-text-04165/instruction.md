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
Larry Silverstein: Larry A. Silverstein (born May 30, 1931) is an American businessman.

7 World Trade Center: 7 World Trade Center (7 WTC) refers to two buildings that have existed at the same location within the World Trade Center site in Lower Manhattan, New York City.  The current structure is the second building to bear that name and address in the World Trade Center complex.  The original structure, part of the original World Trade Center, was completed in 1987 and was destroyed in the September 11 attacks.  The current building opened in May 2006.  Both buildings were developed by Larry Silverstein, who holds a ground lease for the site from the Port Authority of New York and New Jersey.

World Trade Center (2001–present): The World Trade Center is a partially completed complex of buildings in Lower Manhattan, New York City, U.S., replacing the original seven World Trade Center buildings on the same site that were damaged or destroyed in the September 11 attacks.  The site is being rebuilt with five new skyscrapers, a memorial and museum to those killed in the attacks, and a transportation hub.  One World Trade Center, the tallest building in the United States and North America, is the lead building for the new complex, reaching more than 100 stories upon its completion in November 2014.

Lower Corner Historic District: The Lower Corner Historic District encompasses a small village center in the town of Sandwich, New Hampshire.  Lower Corner is a rural village that is strung along New Hampshire Route 109 on either side of its junction with School House Road, about one mile from the main village of Center Sandwich.  The village was developed relatively early in Sandwich's history, although its oldest buildings now date to the early 19th century.  There are 25 contributing structures, mostly residences.  There are two buildings built as stores, including one of brick; all the other buildings are wood frame.  The district was listed on the National Register of Historic Places in 1986.

World Trade Center site: The World Trade Center site, formerly known as "Ground Zero" after the September 11 attacks, is a 14.6-acre (5.9 ha) area in Lower Manhattan in New York City.  The previous World Trade Center complex stood on the site until it was destroyed in the September 11 attacks.  The Port Authority of New York and New Jersey (PANYNJ), Silverstein Properties, and the Lower Manhattan Development Corporation (LMDC) oversee the reconstruction of the site according to a master plan by Studio Daniel Libeskind.  The site is bounded by Vesey Street to the north, the West Side Highway to the west, Liberty Street to the south, and Church Street to the east.  The Port Authority owns the site's land (except for 7 World Trade Center).  Developer Larry Silverstein holds the lease to retail and office space in four of the site's buildings.

American Appraisal: American Appraisal is a company which employs roughly 300 people in 60 locations around the world.  Publicly notable projects conducted by American Appraisal include, for example, a "fresh start" valuation of MCI's assets after its chapter 11 bankruptcy filing or the retrospective valuation of the World Trade Center for Larry Silverstein's court case.

Southbridge Towers: Southbridge Towers is a large housing cooperative development located in Lower Manhattan, consisting of four 27-story towers and five six-story buildings.  The complex was built between 1961 and 1971 by Tishman Realty & Construction as a subsidized co-op under the Mitchell-Lama housing program.  The complex is located in Lower Manhattan in New York City south of the entrance ramp to the Brooklyn Bridge between Pearl Street, Frankfort Street, Gold Street, and Fulton Street.  It contains 1,651 apartments with a total of 331577 sqft of floor area.

Construction of the World Trade Center: The construction of New York City's first World Trade Center complex was conceived as an urban renewal project, spearheaded by David Rockefeller, to help revitalize Lower Manhattan.  The project was developed by the Port Authority of New York and New Jersey, which hired architect Minoru Yamasaki who came up with the specific idea for twin towers.  After extensive negotiations, the New Jersey and New York state governments, which oversee the Port Authority, agreed to support the World Trade Center project, which was built at the site of Radio Row in the Lower West Side of Manhattan, New York City.  To make the agreement acceptable to New Jersey, the Port Authority agreed to take over the bankrupt Hudson & Manhattan Railroad, which brought commuters from New Jersey to the Lower Manhattan site and, upon the Port Authority's takeover of the railroad, was renamed PATH.

April 1956 tornado outbreak: The April 1956 tornado outbreak was a large, deadly tornado outbreak that affected the Great Plains, parts of the South, and the upper Midwest in the contiguous United States.  Occurring from April 2–3, 1956, the outbreak produced 47 tornadoes, including an F5 tornado that devastated the Hudsonville and Standale, Michigan areas in the U.S. state of Michigan on April 3.  It was one of three tornadoes to move across southwest Lower Michigan on that day.  A fourth tornado struck north of the Manistee area.  The Hudsonville-Standale tornado killed 18 and injured 340.  In addition to confirmed tornadoes, there were several unconfirmed but possible tornadoes.  An F2 may have hit east of Ogdensburg, Wisconsin, destroying a general store and a rural school.  Nine barns were damaged or destroyed as well.  A tornado may have also overturned two buildings and uprooted trees near Pana, Illinois.  In addition to a confirmed F2 tornado near Topeka, Indiana, two other unconfirmed tornadoes may have hit northwest of LaGrange and at Emma, destroying or damaging numerous buildings, including a home and a barn that were blown down, and throwing (but not injuring) two people from a horse and buggy.

World Trade Center (1973–2001): The original World Trade Center was a large complex of seven buildings in Lower Manhattan, New York City, United States.  It featured the landmark twin towers, which opened on April 4, 1973, and were destroyed as a result of the September 11 attacks in 2001.  At the time of their completion, the "Twin Towers"—the original 1 World Trade Center, at 1368 ft ; and 2 World Trade Center, at 1,362 ft —were the tallest buildings in the world.  The other buildings in the complex included the Marriott World Trade Center (3 WTC), 4 WTC, 5 WTC, 6 WTC, and 7 WTC.  All these buildings were built between 1975 and 1985, with a construction cost of $400 million ($ in 2014 dollars).  The complex was located in New York City's Financial District and contained 13400000 sqft of office space.

Question: On what day of which month were the two buildings in Lower Manhattan, developed by the American businessman Larry Silverstein, destroyed?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "destruction_event": {
      "type": "object",
      "properties": {
        "day": {
          "type": "integer",
          "description": "The day of the month the destruction occurred."
        },
        "month": {
          "type": "string",
          "description": "The month the destruction occurred."
        },
        "year": {
          "type": "integer",
          "description": "The year the destruction occurred."
        },
        "event_name": {
          "type": "string",
          "description": "The name of the event that caused the destruction."
        }
      },
      "required": [
        "day",
        "month",
        "year",
        "event_name"
      ],
      "additionalProperties": false
    },
    "developer_involved": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the businessman who developed the building(s)."
        },
        "role": {
          "type": "string",
          "description": "The role of the businessman in relation to the building(s)."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "destroyed_buildings_developed_by_silverstein": {
      "type": "array",
      "description": "A list of buildings developed by Larry Silverstein that were destroyed.",
      "items": {
        "type": "object",
        "properties": {
          "building_name": {
            "type": "string",
            "description": "The name of the destroyed building."
          },
          "location": {
            "type": "string",
            "description": "The location of the destroyed building."
          }
        },
        "required": [
          "building_name",
          "location"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "destruction_event",
    "developer_involved",
    "destroyed_buildings_developed_by_silverstein"
  ],
  "additionalProperties": false
}
