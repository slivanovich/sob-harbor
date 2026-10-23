{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJohan Vonlanthen: Johan Vonlanthen Benavídez (born 1 February 1986 in Santa Marta, Colombia) is a Swiss footballer who plays as a winger for Swiss Promotion League side Wil.  His stepfather is a Swiss national, giving him the right to play for that country.\n\nTranquillo Barnetta: Tranquillo Barnetta (] ; born 22 May 1985) is a Swiss professional footballer who plays as a midfielder for St. Gallen.  He usually plays out wide as a left winger but can also play in the centre as an attacking midfielder, or even in a more withdrawn role as a central midfielder.  Barnetta is known for his \"extreme pace, mobility and creativity\".  Prior to moving to the MLS, Barnetta played football for several Swiss and German clubs.  At international level, he has amassed 75 caps for the Swiss national team, representing his nation in three FIFA World Cups, and two UEFA European Football Championships.\n\nAnthony Minichiello: Anthony Minichiello (born 24 May 1980) is an Australian former professional rugby league footballer who captained the Sydney Roosters of the National Rugby League, and retired having set records for most games and most tries in the club's history.  An Australian and Italian international as well as a New South Wales State of Origin representative winger turned fullback, he played his entire career with the Roosters, with whom he won the 2002 and 2013 NRL Premierships, before retiring at the conclusion of the club's 2014 campaign.  Minichiello also won the Golden Boot Award for international player of the year in 2005, and is the brother of fellow Italian international, Mark Minichiello.\n\nGrzegorz Lato: Grzegorz Bolesław Lato (born 8 April 1950 in Malbork) is a retired Polish footballer and manager who played as a winger.  He was the leading scorer at the 1974 World Cup.  Lato's playing career coincided with the golden era of Polish football, which began with Olympic gold in Munich in 1972 and ended a decade later with third place at the 1982 World Cup in Spain, a repeat of the Poles' impressive finish in 1974 in Germany.  He is the only Polish player ever to win the Golden Boot at a World Cup.\n\nMohamed Barakat: Mohamed Barakat (Arabic: محمد بركات‎ ‎ ; born 20 November 1976) is a retired Egyptian footballer.  A right-footed playmaker, Barakat usually played as an offensive right winger or attacking midfielder for Egyptian club Al-Ahly and the Egyptian National Team.  He is considered by many as one of the most talented players in Africa.  Barakat's hallmarks are surging runs from midfield which often disrupt opposing defences, as well as his box-to-box work ethic, which makes him an important figure both in defence and attack.  Thanks to his noticeable achievements and talent, his fans have given him the nickname \"The Mercurial\" (Arabic: بركات الزئبقي‎ ‎ ) .  He reached his peak in 2005 and 2006, helping his club Al-Ahly to win the CAF Champions League 2005 and CAF Champions League 2006 and Egypt win their fifth African Cup of Nations Egypt 2006.  However, in 2006 his career was marred by a long spell of injuries.\n\nNike Mercurial Vapor: The Mercurial Vapor is a football boot manufactured by Nike.  The boot is known for being lightweight.  Because of this, the boot is endorsed by many players for whom speed is part of their game, notably wingers or strikers, such as Cristiano Ronaldo, Franck Ribéry, Luiz Adriano, Zlatan Ibrahimović, Didier Drogba, Jesús Navas, Luka Modrić, Arturo Vidal, Douglas Costa, Xherdan Shaqiri, Raheem Sterling, Stephan El Shaarawy, Eden Hazard, Alexis Sánchez, Carlos Bacca and Philippe Coutinho, among others.\n\nGreg Inglis: Gregory Paul Inglis (born 15 January 1987) is an Australian professional rugby league footballer currently playing for the South Sydney Rabbitohs of the National Rugby League.  A Queensland State of Origin and Australian international representative outside back, he previously played for the Melbourne Storm, with whom he won two grand finals, a Clive Churchill Medal and the Golden Boot Award; he is an indigenous Australian.  Inglis is a versatile back, having played in several positions during his career.  He originally played on the wing or in the centres for the Storm, occasionally filling in at fullback when injuries demanded.  Between 2007 and early 2009 he played at five-eighth for the Melbourne Storm before he switched to centre when Brett Finch arrived at the club, where he played for the remainder of his time there until the end of 2010.  Inglis' representative matches for Queensland and Australia have been as a winger, centre, and fullback.  In November 2009, Inglis won the Golden Boot Award as the world's best player – presented to him by \"Rugby League World\" magazine, becoming the third consecutive Storm player to win it, after Cameron Smith (2007) and Billy Slater (2008).\n\nAdam Taggart: Adam Jake Taggart (born 2 June 1993) is an Australian football (soccer) player who is currently signed to Perth Glory and who has played for the Australia national team.  Taggart is a striker and is a former holder of the Nike A-League Golden Boot award, scoring 16 goals in 25 appearances for the Jets during the 2013–14 A-League season.\n\nKevin Volland: Kevin Volland (born 30 July 1992) is a German footballer who plays as a winger or sometimes a striker for Bayer Leverkusen.  He gained prominence at the 2015 UEFA European Under-21 Championship where he was awarded the Silver Boot.\n\nXherdan Shaqiri: Xherdan Shaqiri (] ; born 10 October 1991) is a Swiss professional footballer who plays as a winger for Premier League club Stoke City, and the Switzerland national team.\n\nQuestion: This Swiss winger and endorser of the Nike Mercurial Vapor boot was born when?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the footballer.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the footballer.\"\n    },\n    \"primary_position\": {\n      \"type\": \"string\",\n      \"description\": \"The primary playing position of the footballer.\"\n    },\n    \"boot_endorsed\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football boot endorsed by the player.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the footballer in 'Day Month Year' format.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"nationality\",\n    \"primary_position\",\n    \"boot_endorsed\",\n    \"birth_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The full name of the footballer."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the footballer."
      },
      "primary_position": {
        "type": "string",
        "description": "The primary playing position of the footballer."
      },
      "boot_endorsed": {
        "type": "string",
        "description": "The name of the football boot endorsed by the player."
      },
      "birth_date": {
        "type": "string",
        "description": "The birth date of the footballer in 'Day Month Year' format."
      }
    },
    "required": [
      "player_name",
      "nationality",
      "primary_position",
      "boot_endorsed",
      "birth_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
