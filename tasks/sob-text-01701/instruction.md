{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCristian Zaccardo: Cristian Zaccardo, (] , born 21 December 1981) is an Italian footballer who is currently a free agent.  He mainly plays as a centre back, although he is also capable of playing as a full-back or in midfield.  He began his club career with Italian club Bologna in 2000, and remained with the club until 2004, aside from a loan spell with Spezia.  He subsequently moved to Palermo, where he came to prominence during his four seasons at the club.  In 2008, he moved to German club VfL Wolfsburg for a season, where he won the 2008–09 Bundesliga title.  He returned to Italy the following season, joining Parma, and in 2013 he moved to Milan, before joining Carpi in 2015; he spent the 2016–17 season on loan with Vicenza in Serie B.  At international level, he represented the Italy national football team on 17 occasions between 2004 and 2007, scoring a goal; he was a member of the Italian side that won the 2006 FIFA World Cup.\n\n1. FC Magdeburg: 1.  FC Magdeburg is a German association football club based in the city of Magdeburg.  The club was founded in 1965 and spent all but one season in East Germany top flight, the DDR-Oberliga, winning three championships and seven cup titles.  It is the only East German club to have won a European title, winning the European Cup Winners' Cup in 1974.  After German reunification, the club fell on hard times and only entered professional football in 2015 when the side was promoted to the 3.  Liga.\n\nGerman Club, Sydney: The German Club (German: Der Deutscher Verein ) was a private club founded in 1853 and located in Sydney, New South Wales, at 89 Phillip Street.  Its membership was men-only and was the oldest gentlemen's club in Australia catering specifically to the German-Australian community prior to the First World War, upon which by 1915 it had closed amid a tide of Anti-German sentiment in Australia.\n\nSV Darmstadt 98: SV Darmstadt 98 is a German football club based in Darmstadt, Hesse.  The club was founded on 22 May 1898 as \"FC Olympia Darmstadt\".  Early in 1919, the association was briefly known as \"Rasen-Sportverein Olympia\" before merging with \"Darmstädter Sport Club 1905\" on 11 November that year to become \"Sportverein Darmstadt 98\".  Merger partner \"SC\" was the product of a 1905 union between \"Viktoria 1900 Darmstadt\" and \"Germania 1903 Darmstadt\".  The footballers are today part of a sports club which also offers its approximately 5,500 members athletics, basketball, cheerleading, hiking, judo, and table tennis.\n\n2012–13 FC Bayern Munich season: The 2012–13 FC Bayern Munich season was the 114th season in the club's history and the 48th consecutive season in the top flight of German football, the Bundesliga, since the promotion of the team from the Regionalliga Süd in 1965.  Before the start of the season, Bayern signed Xherdan Shaqiri, Dante, Claudio Pizarro, Mitchell Weiser, Tom Starke and Mario Mandžukić.  Bayern also added holding midfielder Javi Martínez after the first week of the Bundesliga season at the transfer deadline.  The club started the season with a nine-match winning streak.  The club would end the season claiming the Treble, winning the Bundesliga, the UEFA Champions League and the DFB-Pokal.  Bayern are the first German club to achieve the Treble and are the third European Club to complete the Treble in the last five seasons and seventh ever in European Club competition.\n\nFC Büsingen: FC Büsingen is a German association football club based in the exclave of Büsingen that competes in the Swiss league system, being the only German club to do so.  The club was founded in 1924 and has currently, as of 2008, about 215 members.\n\nBashful Felix: Bashful Felix or Felix is Right on Target (German: Schützenkönig wird der Felix) is a 1934 German comedy film directed by Carl Boese and starring Rudolf Platte, Ursula Grabley and Jakob Tiedtke.  It was made by Terra Film, with sets designed by art directors Robert A. Dietrich and Bruno Lutz.\n\nBerlin International Tournament: The Berlin International Tournament was an international ice hockey tournament held yearly in the German capital of Berlin from 1908-1910.  It was the first multi-national ice hockey tournament ever organized.  Princes Ice Hockey Club of Great Britain won the inaugural tournament.  The German club, Akademischer SC 1906 Dresden, won the second tournament.  Club des Patineurs de Paris of France won the last tournament in 1910.\n\nFelix Platte: Felix Platte (born 11 February 1996) is a German footballer who plays as a striker for Darmstadt 98.\n\nRolla High School: Rolla Senior High School in Rolla, Missouri has a population of about 1050 students.  The school's mascot is the Bulldog with the colors of maroon and silver (formerly maroon, gray, and gold).  The high school offers many clubs, including Student Council (StuCo) as part of Missouri Associations of Student Councils, Key Club, Octagon Club, DECA, FFA, FCCLA, Chess Club, Improvisation Club, Spanish Club, German Club, French Club, Latin Club, and the new addition Link Crew and HOSA Future Health Professionals.  There are two student publications at RHS: \"The Growler\" yearbook and \"The Echo\" newspaper.\n\nQuestion: Felix Platte is a member of what German club?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the footballer.\"\n    },\n    \"club_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"club_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the club the player is a member of.\"\n        },\n        \"club_country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the club is based.\"\n        }\n      },\n      \"required\": [\n        \"club_name\",\n        \"club_country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"player_position\": {\n      \"type\": \"string\",\n      \"description\": \"The primary playing position of the footballer.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"club_info\",\n    \"player_position\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the footballer."
      },
      "club_info": {
        "type": "object",
        "properties": {
          "club_name": {
            "type": "string",
            "description": "The name of the club the player is a member of."
          },
          "club_country": {
            "type": "string",
            "description": "The country where the club is based."
          }
        },
        "required": [
          "club_name",
          "club_country"
        ],
        "additionalProperties": false
      },
      "player_position": {
        "type": "string",
        "description": "The primary playing position of the footballer."
      }
    },
    "required": [
      "player_name",
      "club_info",
      "player_position"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
