{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDan Fouts: Daniel Francis Fouts (born June 10, 1951) is a former American football quarterback who played in the National Football League (NFL).  Fouts played his entire professional career with the San Diego Chargers from 1973 through 1987.  He was one of the most prolific passing quarterbacks during the 1970s and 1980s, but the Chargers were unable to make it to the Super Bowl during his fifteen-year career.  He led the NFL in passing yards four straight years from 1979 to 1982, and became the first player in history to throw for 4,000 yards in three consecutive seasons.\n\nLouie Kelcher: Louis James Kelcher (born August 23, 1953) is a retired American football player who played most of his career with the San Diego Chargers.  His primary position was defensive tackle, where his honors included being a four-time All-Pro and a three-time Pro Bowl selection.  His outstanding performance made him one of the team's most popular players from 1975-83.  Kelcher was inducted into the San Diego Chargers Hall of Fame, and is a member of the franchise's 40th and 50th Anniversary Teams.  He was a graduate of Southern Methodist University and French High School in Beaumont, Texas.\n\nJohn Hendy (American football): John Hendy is a former professional American football player who played defensive back for two seasons for the San Diego Chargers* John H. Hendy American football player San Diego Chargers 1985 to 1987 Drafted by the San Diego Chargers in the 3rd round (69th overall) of the 1985 NFL Draft.  Voted First Team NFL All-Rookie at cornerback 1985 was also named AFC Player of the Week 14 for his 2 interception game returning one 75 yards for a touchdown against Buffalo Bills.  Also coached successfully at Wilcox High School as an assistant for 7 years helping earn the schools 2 CCS championships\n\nNatrone Means: Natrone Jermaine Means (born April 26, 1972) is a former professional American Football running back who played for the San Diego Chargers, Jacksonville Jaguars, and Carolina Panthers of the NFL from 1993 to 2000.  He was selected by the Chargers in the 2nd round (41st overall) of the 1993 NFL Draft.  In 1994, he was selected to the Pro Bowl during San Diego's Super Bowl season.  He is a member of the San Diego Chargers 50th Anniversary Team.  Means was nicknamed Natrone \"Refried\" Means and, later, \"Natrone Means Business\" by ESPN's Chris Berman,\n\nBaltic Robinson 2001: Baltic Robinson: 2001, was the second version of \"Expedition Robinson\", or \"Survivor\" to air in the Baltic region of Europe.  This season premiered in October 2001 and aired until December 15, 2001.  Like in the first season, the three tribes were divided based on the contestants country of origin.  Along with this, each tribe was given the name of the country of its contestants origin in that country's native language.  For an unknown reason there were only twelve contestants when this season started as opposed to the usual fifteen.  When it came time for the merge a joker, Siiri Kuusmann from Estonia, entered the competition.  As another twist, at the fifth tribal council two players were eliminated instead of the usual one.  Due to the medical emergency that saw Vidmantas Lietuvninkas evacuation from the game, Linas Samaška from Lithuania became the first finalist of the season in episode eight.  By the end of the same episode, Māris Sveiduks also became a finalist when the only other contestant from Latvia that remained, Anna Steina, was voted out at tribal council.  As Māris won the final immunity challenge in episode nine, he and he alone would vote to determine who of Siiri Kuusmann and Viive Rižski would be the finalist from Estonia and the final contestant through to the final.  When it came time for the final a combination of votes cast by jurors, votes cast by the public, and penalty votes from plank decided the winner.  Ultimately, Māris Sveiduks of Latvia who won the season with just 2 votes against him, the runner up was Estonian Siiri Kuusmann with 13 votes against her and the second runner up was Lithuanian Linas Samaška with 19 votes against him.\n\nKris Dielman: Kristopher M. Dielman (born February 3, 1981) is a former American football guard who played for the San Diego Chargers of the National Football League (NFL) for nine seasons.  He played college football for Indiana University.  The San Diego Chargers signed him as an undrafted free agent in 2003, and he played his entire professional career for the Chargers.  He was selected to the Pro Bowl four times, and was a member of the Chargers 50th Anniversary Team.\n\nIranian presidential election, 2009: Iran's tenth presidential election was held on 12 June 2009, with incumbent Mahmoud Ahmadinejad running against three challengers.  The next morning the Islamic Republic News Agency, Iran's news agency, announced that with two-thirds of the votes counted, Ahmadinejad had won the election with 62% of the votes cast, and that Mir-Hossein Mousavi had received 34% of the votes cast.  There were large irregularities in the results and people were surprised by them, which resulted in protests of millions of Iranians, across every Iranian city and around the world and the emergence of the opposition Iranian Green Movement.\n\nSan Diego Chargers 50th Anniversary Team: The San Diego Chargers (known now as the Los Angeles Chargers) announced their 50th anniversary team in 2009 to honor the top players and coaches in the history of the National Football League team.  The Chargers were founded in 1959 as part of the American Football League.  The anniversary team included 53 players and coaches selected from 103 nominees.  The Chargers originally stated that only 50 members would be selected; the group is still sometimes referred to as the 50 Greatest Chargers.  Online voting by fans accounted for 50 percent of the voting results; votes from Chargers Hall of Famers and five members of the local media made up for the other 50 percent.  Over 400,000 votes were cast online.  Dan Fouts and LaDainian Tomlinson received the first and second most votes, respectively.  The team features eight Pro Football Hall of Fame members and 11 players that were active on the 2009 Chargers team.\n\nMike Scifres: Michael T. Scifres (born October 8, 1980) is an American football punter.  He has played the majority of his career with the San Diego Chargers, and is included on the Chargers 50th Anniversary Team.\n\nSan Diego Chargers 40th Anniversary Team: The San Diego Chargers announced their 40th Anniversary Team in 2000 to honor the top players and coaches in the history of the National Football League team.  The Chargers began play in 1960 as part of the American Football League.  The anniversary team included 31 players and coaches voted on by fans and a media panel.  The team became the Los Angeles Chargers after relocating in 2017.\n\nQuestion: The San Diego Chargers announced their 50th anniversary team and with over 400,000 votes cast online The player who received the most votes was also the first player in history to throw how many yards in three consecutive seasons?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_most_votes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the player who received the most votes for the anniversary team.\"\n        },\n        \"team_anniversary\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the anniversary team the player was selected for.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"team_anniversary\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"passing_record\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"yards_thrown\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of yards thrown in consecutive seasons.\"\n        },\n        \"consecutive_seasons\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of consecutive seasons this record was achieved.\"\n        },\n        \"record_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the passing record.\"\n        }\n      },\n      \"required\": [\n        \"yards_thrown\",\n        \"consecutive_seasons\",\n        \"record_description\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"online_votes_cast\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of online votes cast for the anniversary team.\"\n    }\n  },\n  \"required\": [\n    \"player_most_votes\",\n    \"passing_record\",\n    \"online_votes_cast\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_most_votes": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the player who received the most votes for the anniversary team."
          },
          "team_anniversary": {
            "type": "string",
            "description": "The name of the anniversary team the player was selected for."
          }
        },
        "required": [
          "name",
          "team_anniversary"
        ],
        "additionalProperties": false
      },
      "passing_record": {
        "type": "object",
        "properties": {
          "yards_thrown": {
            "type": "integer",
            "description": "The number of yards thrown in consecutive seasons."
          },
          "consecutive_seasons": {
            "type": "integer",
            "description": "The number of consecutive seasons this record was achieved."
          },
          "record_description": {
            "type": "string",
            "description": "A description of the passing record."
          }
        },
        "required": [
          "yards_thrown",
          "consecutive_seasons",
          "record_description"
        ],
        "additionalProperties": false
      },
      "online_votes_cast": {
        "type": "integer",
        "description": "The total number of online votes cast for the anniversary team."
      }
    },
    "required": [
      "player_most_votes",
      "passing_record",
      "online_votes_cast"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
