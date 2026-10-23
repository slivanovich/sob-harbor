{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOtis Nixon: Otis Junior Nixon (born January 9, 1959) is an American former professional baseball center fielder.  He played in Major League Baseball (MLB) for the New York Yankees, Cleveland Indians, Montreal Expos, Atlanta Braves, Boston Red Sox, Texas Rangers, Toronto Blue Jays, Los Angeles Dodgers, and Minnesota Twins between 1983 and 1999.  He has stolen the most bases for a player who has never appeared in an MLB All-Star game since the All-Star Game was inaugurated in 1933.\n\nAndrew Brackman: Andrew Warren Brackman (born December 4, 1985) is an American former professional baseball pitcher.  He signed a four-year, $4.55 million-dollar deal with $3.35-million signing bonus as the New York Yankees' first-round choice (30th overall pick) of the 2007 Major League Baseball Draft.  Brackman is represented by sports agent Scott Boras.  He is listed as 6 foot 10 inches tall and weighs 230 pounds.\n\nVernon Wells: Vernon Michael Wells III (born December 8, 1978) is an American former professional baseball center fielder.  He played in Major League Baseball (MLB) for the Toronto Blue Jays, the Los Angeles Angels of Anaheim, and the New York Yankees.\n\nScott Boras: Scott Dean Boras (born November 2, 1952) is an American sports agent, specializing in baseball.  He is the founder, owner and president of the Boras Corporation, a sports agency based in Newport Beach, California that represents roughly 175 professional baseball clients, including many of the game's highest-profile players.  Boras has brokered many record-setting contracts since 1982, and many of his clients, including Shin-Soo Choo, Jacoby Ellsbury, Prince Fielder, Matt Holliday, Alex Rodriguez (until 2010), Max Scherzer, and Jayson Werth are among the highest paid in the game.  Since 2013, Forbes magazine has named Boras the \"Most Powerful Sports Agent in the World.\"\n\nAaron Hicks: Aaron Michael Hicks (born October 2, 1989) is an American professional baseball center fielder for the New York Yankees of Major League Baseball (MLB).  He made his MLB debut on April 1, 2013 with the Minnesota Twins.\n\nMickey Mantle: Mickey Charles Mantle (October 20, 1931 – August 13, 1995), nicknamed The Commerce Comet and The Mick, was an American professional baseball player.  Mantle played his entire Major League Baseball (MLB) career with the New York Yankees as a center fielder and first baseman, from 1951 through 1968.  Mantle was one of the best players and sluggers, and is regarded by many as the greatest switch hitter in baseball history.  Mantle was inducted into the National Baseball Hall of Fame in 1974 and was elected to the Major League Baseball All-Century Team in 1999.\n\nJacoby Ellsbury: Jacoby McCabe Ellsbury ( ; born September 11, 1983) is an American professional baseball center fielder for the New York Yankees of Major League Baseball (MLB).  He played in MLB for the Boston Red Sox from 2007 through 2013, and joined the Yankees before the 2014 season.\n\nAndruw Jones: Andruw Rudolf Jones (] ; born April 23, 1977) is a Curaçaoan retired professional baseball outfielder and designated hitter.  He played in Major League Baseball (MLB) most notably for the Atlanta Braves.  Jones also played for the Los Angeles Dodgers, Texas Rangers, Chicago White Sox, and New York Yankees, and in Nippon Professional Baseball (NPB) for the Tohoku Rakuten Golden Eagles.  Jones was a noted defensive specialist for most of his career and won the Rawlings Gold Glove Award for outfielders every year from 1998 through 2007.  Jones had an elite arm in addition to fielding.  He appeared in the All-Star Game five times, and he won both the Hank Aaron Award and a Silver Slugger Award for outfielders in 2005.  In 2002, he was the inaugural National League (NL) All-Star Final Vote winner.  While primarily a center fielder throughout his career, Jones transitioned to designated hitter and fourth outfielder role for the Rangers, White Sox, and Yankees.\n\nKevin Pillar: Kevin Andrew Pillar ( ) (born January 4, 1989) is an American professional baseball center fielder for the Toronto Blue Jays of Major League Baseball (MLB).  Pillar was an All-American center fielder in college.  He set the NCAA Division II record with a 54-game hitting streak in 2010, and established his school's all-time record with a career batting average of .367.  Pillar was drafted by the Blue Jays in the 32nd round (979th overall) of the 2011 Major League Baseball draft.\n\nTorii Hunter: Torii Kedar Hunter ( ; born July 18, 1975) is an American former professional baseball center fielder and right fielder.  He played in Major League Baseball (MLB) for the Minnesota Twins, Los Angeles Angels of Anaheim and Detroit Tigers from 1997 through 2015.  Hunter was a five-time All-Star, won nine consecutive Gold Glove Awards as a center fielder and was a two-time Silver Slugger Award winner.\n\nQuestion: Scott Dean Boras, is an American sports agent, specializing in baseball, Boras has brokered many record-setting contracts since 1982, and many of his clients, including Jacoby McCabe Ellsbury, an American professional baseball center fielder for the New York Yankees, of which organization?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"agent_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the sports agent.\"\n    },\n    \"client_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the client represented by the agent.\"\n    },\n    \"client_team\": {\n      \"type\": \"string\",\n      \"description\": \"The professional baseball team the client plays for.\"\n    },\n    \"client_league_organization\": {\n      \"type\": \"string\",\n      \"description\": \"The major league organization the client's team belongs to.\"\n    }\n  },\n  \"required\": [\n    \"agent_name\",\n    \"client_name\",\n    \"client_team\",\n    \"client_league_organization\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "agent_name": {
        "type": "string",
        "description": "The name of the sports agent."
      },
      "client_name": {
        "type": "string",
        "description": "The name of the client represented by the agent."
      },
      "client_team": {
        "type": "string",
        "description": "The professional baseball team the client plays for."
      },
      "client_league_organization": {
        "type": "string",
        "description": "The major league organization the client's team belongs to."
      }
    },
    "required": [
      "agent_name",
      "client_name",
      "client_team",
      "client_league_organization"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
