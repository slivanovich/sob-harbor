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
Dwayne Provo: Dwayne Provo is a Canadian athlete, school administrator, and politician.  Provo was born in North Preston, Nova Scotia (one of Canada's largest Black communities) and attended university at Saint Mary's University where he played Canadian football and was drafted in 1995 by the Saskatchewan Roughriders.  He went on to play professional football in the Canadian Football League for 8 years (as well as a brief stint in the National Football League).  Since retiring from football he has taken further university studies and worked as a school administrator.  In the 2006 Nova Scotia election, he ran as the Progressive Conservative candidate for the riding of Preston, but finished second to Liberal Keith Colwell.  In 2009, he ran again but placed third behind Colwell and New Democrat Janet Sutcliffe.  He is a cousin to boxer Kirk Johnson and hockey player Evander Kane.

William H. Ray House: The William H. Ray House is a historic house located at 415 South University Avenue in Provo, Utah.  A prominent non-Mormon in Provo, Utah, William H. Ray was one of the founders of the State Bank of Provo.  A financier, banker, and broker, Ray organized the Ray Investment Company as an insurance and real estate brokerage firm.  The William Ray House, which was built around 1898, "Combines Romanesque Revival elements with classical detailing in a personalized manner (Historic Provo 2002)."  The William H. Ray House was added to the National Register of Historic Places in 1982 and was designated to the Provo City Historic Landmark Register on April 28, 1995.

Provo West Co-op: The Provo West Cooperative Mercantile Institution is a historic building located in Provo, Utah.  It is listed on the National Register of Historic Places.  Built to encourage trading among the Latter Day Saints, the Provo West Co-op was one of the first stores built in the city under the cooperative merchandising movement sponsored by The Church of Jesus Christ of Latter-day Saints of the late 1800s.  Provo West Co-op was designated to the Provo City Historic Landmarks Registry on March 21, 1996.

John E. Booth House: The John E. Booth House is a historic house located in Provo, Utah.  John E. Booth was a significant Provoan, and was extensively involved in Provo's community and religious affairs.  Located at 59 West and 500 North and less than one acre in size, the John E. Booth House was built in 1900, and happens to be the only 2 ⁄ -story Victorian Mansion in Provo, Utah.  This house is significant not only as a Victorian mansion, but because its "Bricks were individually painted to create a variegrated design effect" (Historic Provo p. 10).  The house was added to the National Register of Historic Places in 1982.  The house was designated to the Provo City Historic Landmark Register on May 26, 1995.

Jack Roslovic: John "Jack" Roslovic (born January 29, 1997) is an American professional ice hockey player, who is currently playing with the Manitoba Moose in the American Hockey League (AHL) as a prospect to the Winnipeg Jets of the National Hockey League (NHL).  He was selected in the first round, 25th overall by the Jets in the 2015 NHL Entry Draft.  The Jets acquired the draft pick in a trade that sent Evander Kane and Zach Bogosian to the Buffalo Sabres in exchange for Tyler Myers, Drew Stafford, Joel Armia, and Brendan Lemieux.

Provo station (Utah Transit Authority): Provo station is an intermodal transit station in Provo, Utah, United States.  It is served by the Utah Transit Authority's (UTA) FrontRunner commuter rail line as well as local and intra-county buses.  It is the southern terminus of the commuter rail system, with service running north as far as Ogden.  The station is also known as Provo Intermodal Hub, Provo Central Station, or Provo CRS.  It is part of the "FrontRunner" South extension.

List of people from Provo, Utah: This is a list of notable people from Provo, Utah.  This list includes notable individuals born and raised in Provo, those who currently live in Provo, and those who lived for a significant period in Provo.

Race and ethnicity in the NHL: The National Hockey League evolved from a mono-ethnic and primarily Canadian professional athletic league to span North America.  The distribution of ethnic groups has been gradually changing since the inception of the NHL.  The league consists of a variety of players from varying nationalities and diverse backgrounds.  Once known as a league riddled with racism and exclusiveness, the NHL has made positive steps toward a more diverse and inclusive institution.  According to statistics, gathered by www.quanthockey.com, the NHL began its expansion of player nationalities in the 1970s, where players hailed from the United States, Sweden, and Finland.  The share of Canadians in the league dropped to 75% by the 1980s and is now slightly less than 50%.  The NHL is composed of 93% of players who designate themselves as white with the remaining 7% of varying ethnicities.  The NHL currently has 32 players of African-American descent.  Some notable NHL stars of African-American descent are Dustin Byfuglien, Evander Kane, and Joel Ward.

Provo College: Provo College specializes in career education.  The College was formerly accredited by the Accrediting Council for Independent Colleges and Schools (ACICS).  Provo College offers bachelor's degrees, associate degrees and diplomas in fields such as nursing, physical therapy assisting, medical assisting, criminal justice, business administration.  Provo College offers programs on the campus and online.The Bachelor of Science in Nursing degree at Provo College is accredited by the Commission on Collegiate Nursing Education, One Dupont Circle, NW, Suite 530, Washington, DC 20036, 202-887-6791.  More at www.ccneaccreditation.org.  The campus is located at 1450 West 820 North in Provo, Utah.

Evander Kane: Evander Frank Kane (born August 2, 1991) is a Canadian professional ice hockey left winger currently playing for the Buffalo Sabres of the National Hockey League (NHL).  Kane was selected fourth overall in the first round of the 2009 NHL Entry Draft by the Atlanta Thrashers.

Question: Dwayne Provo is what to Evander Kane?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "relationship_summary": {
      "type": "string",
      "description": "A summary of the relationship between the two individuals."
    },
    "person_a": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of roles or professions of the first person."
        },
        "sports_involved_in": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of sports the first person was involved in."
        }
      },
      "required": [
        "name",
        "roles",
        "sports_involved_in"
      ],
      "additionalProperties": false
    },
    "person_b": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of roles or professions of the second person."
        },
        "sports_involved_in": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of sports the second person was involved in."
        }
      },
      "required": [
        "name",
        "roles",
        "sports_involved_in"
      ],
      "additionalProperties": false
    },
    "relationship_type": {
      "type": "string",
      "description": "The specific type of relationship between the two individuals."
    }
  },
  "required": [
    "relationship_summary",
    "person_a",
    "person_b",
    "relationship_type"
  ],
  "additionalProperties": false
}
