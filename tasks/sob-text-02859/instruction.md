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
2019 Cricket World Cup: The 2019 Cricket World Cup (officially ICC Cricket World Cup 2019) is scheduled to be hosted by England and Wales, from 30 May to 15 July 2019.  This will be the 12th Cricket World Cup competition, and the fifth time it will be held in England and Wales, following the 1975, 1979, 1983 and 1999 World Cups.

2014 ICC World Cricket League Division Three: The 2014 ICC World Cricket League Division Three was a cricket divisional tournament organised by International Cricket Council.  It formed part of the ICC World Cricket League (WCL) and qualification for the 2019 World Cup.  The top two teams in the tournament Nepal and Uganda qualified for the 2015 WCL Division Two tournament, to be held in Namibia, while the bottom two teams United States and Bermuda were relegated to the 2016 WCL Division Four tournament.

Ko Irie: Ko Irie (born 14 March 1982) is a Japanese cricketer.  A right-handed batsman, Irie first played for Japan against Samoa in the 2005/06 East Asia-Pacific Cup.  He played in the 2006 and 2007 versions of the competition, and in 2008 he made his World Cricket League debut in Division Five.  Irie has since gone on to play in the 2009 World Cricket League Division Seven and the 2011 World Cricket League Division Seven.  He has been selected in Japan's squad for the 2011 World Cricket League Division Six.  Irie has previously captained Japan.

2015 ICC World Cricket League Division Two: The 2015 ICC World Cricket League Division Two was a cricket divisional tournament organised by the International Cricket Council.  It formed part of the ICC World Cricket League and a qualification pathway for the ICC World Cup 2019.

2018 ICC World Cricket League Division Two: 2018 ICC World Cricket League Division Two is a cricket tournament that is scheduled to take place in 2018.  Oman and Canada were the top two teams in the 2017 ICC World Cricket League Division Three tournament in Uganda and were promoted as a result.  They will be joined by the bottom four teams from the ongoing 2015–17 ICC World Cricket League Championship to determine the final two spots in the 2018 Cricket World Cup Qualifier.

Masaomi Kobayashi: Masaomi Kobayashi (born 4 September 1982) is a Japanese cricketer.  A right-handed batsman who bowls right-arm medium pace, Kobayshi first played for Japan against Samoa in the 2005/06 East Asia-Pacific Cup.  He played in the 2006 and 2007 versions of the competition, and in 2008 he made his World Cricket League debut in Division Five.  Kobayashi has since gone on to play in the 2009 World Cricket League Division Seven and the 2011 World Cricket League Division Seven.  He is the current Japan captain and has been selected in Japan's squad for the 2011 World Cricket League Division Six.

Tatsuro Chino: Tatsuro Chino (born 27 March 1984) is a Japanese cricketer.  A right-handed batsman who fields as a wicket-keeper, Chino first played for Japan against Indonesia in the 2004 East Asia-Pacific Cricket Challenge.  He played in the 2005, 2006 and 2007 East Asia-Pacific Trophy's, and in 2008 he made his World Cricket League debut in Division Five.  Chino has since gone on to play in the 2009 World Cricket League Division Seven and the 2011 World Cricket League Division Seven.  He has been selected in Japan's squad for the 2011 World Cricket League Division Six.

2012–18 ICC World Cricket League: The 2012–18 ICC World Cricket League third season of ICC World Cricket League.  Following the establishment of the various leagues during ICC World Cricket League 2007–09, the competition was composed of eight divisions but in 2014, ICC reduced Division 7 and Division 8.  In addition, a series of qualifying regional tournaments played.  The divisions played in roughly consecutive order, with the lower divisions played first.  The top two from each division promotion to the following, higher division, meaning that some teams in more than one division during the tournament.  The first tournament, in September 2012, was the 2012 ICC World Cricket League Division Eight in Samoa.

ICC World Cricket League Division Two: ICC World Cricket League Division Two forms part of the World Cricket League (WCL) system.  Like all other divisions, WCL Division Two is contested as a standalone tournament rather than as an actual league.  Unlike lower divisions, however, matches in Division Two hold list-A status.

Patrick Giles-Jones: Patrick Giles-Jones (born 9 December 1982 in Waratah, New South Wales) is an Australian born Japanese cricketer.  A left-handed batsman who bowls left-arm medium pace, Giles-Jones first played for Japan against the Marylebone Cricket Club in 2005.  He played in the 2005, 2006 and 2007 East Asia-Pacific Trophy's, and in 2008 he made his World Cricket League debut in Division Five.  Giles-Jones has since gone on to play in the 2009 World Cricket League Division Seven and the 2011 World Cricket League Division Seven.  He has been selected in Japan's squad for the 2011 World Cricket League Division Six.

Question: Which cricket event is scheduled to be hosted by England and Wales, is the 12th competition in the series, and for which a possible pathway to qualification included the World Cricket League Division Two tournament?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_name": {
      "type": "string",
      "description": "The official name of the cricket event."
    },
    "host_details": {
      "type": "object",
      "properties": {
        "countries": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of countries hosting the event."
        },
        "is_fifth_time_host": {
          "type": "boolean",
          "description": "Indicates if this is the fifth time these countries are hosting the World Cup."
        }
      },
      "required": [
        "countries",
        "is_fifth_time_host"
      ],
      "additionalProperties": false
    },
    "competition_details": {
      "type": "object",
      "properties": {
        "series_number": {
          "type": "integer",
          "description": "The sequential number of this competition in its series."
        }
      },
      "required": [
        "series_number"
      ],
      "additionalProperties": false
    },
    "qualification_pathways": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "pathway_name": {
            "type": "string",
            "description": "Name of a tournament or league that served as a qualification pathway."
          }
        },
        "required": [
          "pathway_name"
        ],
        "additionalProperties": false
      },
      "description": "List of tournaments that were part of the qualification pathway for this event."
    }
  },
  "required": [
    "event_name",
    "host_details",
    "competition_details",
    "qualification_pathways"
  ],
  "additionalProperties": false
}
