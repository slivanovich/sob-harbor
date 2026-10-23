{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRed Faced: \"Red Faced\" is the sixth episode in the first season of the CBS television series \"Supergirl\", which aired on November 30, 2015.  It was written by Michael Grassi and Rachel Shukert, and directed by Jesse Warn.\n\nSupergirl (film): Supergirl is a 1984 British superhero film directed by Jeannot Szwarc and written by David Odell, based on the DC Comics character of the same name and serves as a spin-off to Alexander and Ilya Salkind's \"Superman\" film series.  The film stars Helen Slater as Supergirl, along with Faye Dunaway, Mia Farrow and Peter O'Toole, with Marc McClure reprising his role as Jimmy Olsen from the \"Superman\" films.  He was the only actor to do so.  \"Supergirl\" was the first superhero film to feature a woman in the lead role.\n\nList of Supergirl characters: \"Supergirl\" is an American television series developed by Greg Berlanti, Ali Adler, and Andrew Kreisberg based on the characters created by Jerry Siegel and Joe Shuster in the \"Superman\" franchise and Al Plastino and Otto Binder's character Supergirl (Kara Zor-El).  The series stars Melissa Benoist in the titular role of Kara Zor-El / Kara Danvers / Supergirl, as well as Mehcad Brooks, Chyler Leigh, Jeremy Jordan, David Harewood, and Calista Flockhart, with Chris Wood, and Floriana Lima joining in later seasons.  In addition to original characters, several other characters from DC Comics universe also appear throughout the series.  For its first season, \"Supergirl\" aired on CBS, before moving to The CW for its second season.\n\nSupergirl (TV series): Supergirl is an American superhero action-adventure television series developed by Ali Adler, Greg Berlanti and Andrew Kreisberg (the latter two having previously created \"Arrow\" and \"The Flash\") that originally aired on CBS and premiered on October 26, 2015.  It is based on the DC Comics character Supergirl, created by Otto Binder and Al Plastino, and stars Melissa Benoist in the title role.  Supergirl is a costumed superheroine who is Superman's cousin and one of the last surviving Kryptonians.\n\nBizarro (Supergirl): \"Bizarro\" is the twelfth episode in the first season of the CBS television series \"Supergirl\", which aired on February 1, 2016.  It was written by Roberto Aguirre-Sacasa and Rachel Shukert, and directed by John Showalter.\n\nManhunter (Supergirl): \"Manhunter\" is the seventeenth episode in the first season of the CBS television series \"Supergirl\", which aired on March 21, 2016.  The episode's teleplay was written by Cindy Lichtman and Rachel Shukert, and directed by Chris Fisher.\n\nXHTV-TDT: XHTV-TDT (channel 4 virtual channel 49 digital), founded in 1950 by Romulo O'Farril, is a flagship TV station of Televisa and FOROtv.  Although FOROtv does not have any full-time affiliates, most Televisa local stations around the republic select some FOROtv programming for their broadcasting.  FOROtv is available on various cable television companies and SKY México satellite service, along with several providers in the United States as part of Televisa and Univision's partnership (albeit with local programming and sports replaced with American ads and recorded news blocks).  It is the oldest TV station in Mexico and Latin America.\n\nLegends of Tomorrow: DC's Legends of Tomorrow, or simply Legends of Tomorrow, is an American superhero action-adventure television series developed by Greg Berlanti, Marc Guggenheim, Andrew Kreisberg, and Phil Klemmer, who are also executive producers along with Sarah Schechter and Chris Fedak; Klemmer and Fedak serve as showrunners.  The series, based on the characters of DC Comics, airs on The CW and is a spin-off from \"Arrow\" and \"The Flash\", existing in the same fictional universe.  The series premiered on January 21, 2016.  In January 2017, The CW renewed the series for a third season, which is scheduled to debut on October 10, 2017.\n\nList of Supergirl episodes: \"Supergirl\" is an American superhero action-adventure drama television series developed by Ali Adler, Greg Berlanti and Andrew Kreisberg (the latter two having previously created \"Arrow\" and \"The Flash\") that originally aired on CBS and premiered on October 26, 2015.  It is based on the DC Comics character Supergirl (Kara Zor-El), created by Otto Binder and Al Plastino, and stars Melissa Benoist in the title role.  Supergirl is a costumed superheroine who is the biological cousin to Superman and one of the last surviving Kryptonians.\n\nSolitude (Supergirl): \"Solitude\" is the fifteenth episode in the first season of the CBS television series \"Supergirl\", which aired on February 29, 2016.  The episode's teleplay was written by Anna Musky-Goldwyn and James DeWille, from a story by Rachek Shukert, and directed by Dermott Downs.  The episode is named for the Superman's Fortress of Solitude in comic books and related television and film series.\n\nQuestion: Supergirl, an American superhero action-adventure televison series, written by Cindy Lichtman and Rachel Shukert aired on what TV station?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television series.\"\n    },\n    \"episode_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"episode_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the episode written by the specified individuals.\"\n        },\n        \"season_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The season number of the episode.\"\n        },\n        \"air_date\": {\n          \"type\": \"string\",\n          \"description\": \"The original air date of the episode.\"\n        },\n        \"writers\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The writers credited for the episode's teleplay.\"\n        }\n      },\n      \"required\": [\n        \"episode_title\",\n        \"season_number\",\n        \"air_date\",\n        \"writers\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"tv_station\": {\n      \"type\": \"string\",\n      \"description\": \"The television station where the series/episode aired.\"\n    }\n  },\n  \"required\": [\n    \"series_name\",\n    \"episode_details\",\n    \"tv_station\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_name": {
        "type": "string",
        "description": "The name of the television series."
      },
      "episode_details": {
        "type": "object",
        "properties": {
          "episode_title": {
            "type": "string",
            "description": "The title of the episode written by the specified individuals."
          },
          "season_number": {
            "type": "integer",
            "description": "The season number of the episode."
          },
          "air_date": {
            "type": "string",
            "description": "The original air date of the episode."
          },
          "writers": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The writers credited for the episode's teleplay."
          }
        },
        "required": [
          "episode_title",
          "season_number",
          "air_date",
          "writers"
        ],
        "additionalProperties": false
      },
      "tv_station": {
        "type": "string",
        "description": "The television station where the series/episode aired."
      }
    },
    "required": [
      "series_name",
      "episode_details",
      "tv_station"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
