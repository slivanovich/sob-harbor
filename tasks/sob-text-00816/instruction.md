{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWichita Force: The Wichita Force are a professional indoor football team based in Wichita, Kansas.  They are members of the Champions Indoor Football league.  The team was founded in 2014 as an expansion franchise.  The Force's home games are played at Intrust Bank Arena.  Former Wichita Wild head coach Paco Martinez and his staff were hired by the Force.\n\n2016 Wichita Force season: The 2016 Wichita Force season is the franchise's 2nd season as a professional indoor football franchise and second as a member of Champions Indoor Football (CIF).  One of nine teams in the CIF for the inaugural 2016 season, the Wichita Force is owned by Wichita Indoor Football LLC, led by managing partner Marv Fisher.  The Force clinched their first division title with a 44-30 victory over the Sioux City Bandits.\n\nFIU Arena: FIU Arena (formerly known as Sunblazer Arena, Golden Panther Arena, Pharmed Arena, and U.S. Century Bank Arena) is a 5,000-seat multi-purpose arena at Florida International University in Miami, Florida.  It was opened on February 1, 1986, and is home to the FIU Panthers basketball and volleyball teams.  It was originally named Sunblazer Arena, but was renamed Golden Panther Arena when FIU's athletic teams changed their nickname from Sunblazers to Golden Panthers in 1987.  It was renamed Pharmed Arena in 2004, and then was briefly named FIU Arena in 2008 before being renamed to U.S. Century Bank Arena.  However, the facility reverted to its prior and current name in 2014.\n\nWichita Thunder: The Wichita Thunder are a minor league hockey team based in Wichita, Kansas.  The team played in the Central Hockey League from 1992 until 2014, and then in the ECHL since the 2014–15 season.  From 1992 until December 2009 the Thunder played in the Britt Brown Arena located in the northern Wichita suburb of Park City.  In January 2010 (the second half of the 2009–10 season), the team began playing its home games at the newly built Intrust Bank Arena.\n\n2015 Wichita Force season: The 2015 Wichita Force season is the team's first season as a professional indoor football franchise and first as a member of Champions Indoor Football (CIF).  One of nine teams in the CIF for the inaugural 2015 season, the Wichita Force is owned by Wichita Indoor Football LLC, led by managing partner Marv Fisher.  The Force play their home games at the Intrust Bank Arena in Wichita, Kansas, under the direction of head coach Paco Martinez.\n\nWebster Bank Arena: The Webster Bank Arena (formerly The Arena at Harbor Yard) is a 10,000-seat multi-purpose arena at 600 Main Street in Bridgeport, Connecticut, built alongside The Ballpark at Harbor Yard.  The Arena opened on October 10, 2001 and is managed by Harbor Yard Sports and Entertainment.  Webster Bank entered into a 10-year $3.5 million agreement with the City of Bridgeport for naming rights of the Arena on January 6, 2011.\n\nIntrust Bank Arena: Intrust Bank Arena is a 15,004-seat multi-purpose arena in Wichita, Kansas, United States.  It is located on the northeast corner of Emporia and Waterman streets in downtown Wichita.\n\nErnesto Lacayo: Ernesto Lacayo (born May 5, 1989) is an American football kicker who is currently a free agent.  He played college football at Hastings College (NAIA), where he holds all kicking records in Hastings College History.  Ernesto went undrafted in the 2011 NFL draft and signed with the Nebraska Danger (IFL) after the draft.  After one year with the Danger, Ernesto then signed with the Louisiana Swashbucklers (PIFL) 2013.  After the Swashbucklers folded in 2013, Ernesto then signed with the Wichita Wild (CPIFL) in 2014.  Ernesto set an All-Arena/Indoor record of 30 field goals made in a season, and set a CPIFL record with a 55-yard field goal against the Salina Bombers.  Ernesto also kicked a 51-yard game-winning field goal against the Dodge City Law to put the Wild in the CPIFL Championship.  In 2014, Ernesto then signed with the Wichita Force (CIF) for the 2015 season, where he played only 10 games before being called up to play for the Las Vegas Outlaws (arena football) (AFL) in 2015.  In 11 games with the Outlaws, Ernesto led the league point after touchdown percentage connecting on 54-of-59 (91.5%).  In 2016, Ernesto signed with the Portland Steel (AFL).\n\nDowntown Wichita: Downtown Wichita is the central business district of Wichita, Kansas, United States.  The political and financial hub of the city, it is home to several of the area’s major landmarks and event venues including the Epic Center, Century II Performing Arts & Convention Center, Intrust Bank Arena, and the Old Town entertainment district.\n\nWichita Stealth: The Wichita Stealth was an arena football team.  They played their home games at the Kansas Coliseum in Wichita, Kansas.  They originally began play in the Indoor Football League as a 2000 expansion team known as the Wichita Warlords before the league folded, in which they moved to the af2 and became the Stealth.  They only got to the playoffs once during their five-year existence, where they had an early exit (courtesy of the Hawaiian Islanders).  After an 8-8 season in 2004, the team officially disbanded and ceased all operations.  After Intrust Bank Arena opened, there were rumors that the Stealth might be reincarnated, but the talks died down, and nothing ever surfaced.  Now the Wichita Force of Champions Indoor Football, play there.\n\nQuestion: Wichita Force plays at Intrust Bank Arena that seat how many people>?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"arena_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the arena.\"\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where the arena is located.\"\n    },\n    \"seating_capacity\": {\n      \"type\": \"integer\",\n      \"description\": \"The total seating capacity of the arena.\"\n    },\n    \"team_playing_there\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the team that plays its home games at this arena.\"\n    }\n  },\n  \"required\": [\n    \"arena_name\",\n    \"location\",\n    \"seating_capacity\",\n    \"team_playing_there\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "arena_name": {
        "type": "string",
        "description": "The name of the arena."
      },
      "location": {
        "type": "string",
        "description": "The city and state where the arena is located."
      },
      "seating_capacity": {
        "type": "integer",
        "description": "The total seating capacity of the arena."
      },
      "team_playing_there": {
        "type": "string",
        "description": "The name of the team that plays its home games at this arena."
      }
    },
    "required": [
      "arena_name",
      "location",
      "seating_capacity",
      "team_playing_there"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
