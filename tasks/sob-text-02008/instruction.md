{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCorey Davis (wide receiver): Corey Davis (born January 11, 1995) is an American football wide receiver for the Tennessee Titans of the National Football League (NFL).  He played college football at Western Michigan, where he became the NCAA's career receiving yards leader.  He was drafted by the Titans fifth overall in the 2017 NFL Draft.\n\nGeorge Thomas (American football): George Carroll Thomas, Jr. (March 4, 1928 – May 23, 1989) was an American football halfback and defensive back in the National Football League for the Washington Redskins and the New York Giants.  He was a standout high school basketball player, which led to his being recruited to play college basketball for Tulane University.  However, first year OU football coach, Jim Tatum, convinced him stay in Oklahoma and play college football at the University of Oklahoma.  Thomas was a standout for the Sooners, lettering in '46, '47,'48 and '49.  He earned All-American status in 1949 List of Oklahoma Sooners football All-Americans.  Thomas graduated from OU with a degree in Business Administration in 1950.\n\nPomponia Caecilia Attica: Pomponia Caecilia Attica or Caecilia Pomponia Attica (born 51 BC) was the daughter of Cicero's Epicurean friend and eques, knight, Titus Pomponius Atticus.  Her mother, Caecilia Pilea/Pilia (before ca 75 BC – 46 BC), daughter of Pileus/Pilius, was a maternal granddaughter of Marcus Licinius Crassus, a member of the First Triumvirate.  Atticus and Pilea/Pilia were married in 58 BC/56 BC, when Atticus was already 53/54 years old, and she died after 12 years of happy marriage.  Caecilia's aunt, Pomponia, married Cicero's younger brother Quintus Tullius Cicero around 70 BC.  She also had an older brother named after his father, Titus Pomponius Atticus.\n\nJohnson Bademosi: Johnson Bademosi (born July 23, 1990) is an American football cornerback and special teamer for the New England Patriots of the National Football League (NFL).  He was signed by the Browns as an undrafted free agent in 2012.  He was a member of the football, rugby, and track and field teams at Gonzaga College High School and went on to play college football for Stanford University.\n\nJamal Anderson: Jamal Sharif Anderson (born September 30, 1972) is a former American football running back of the National Football League.  He was drafted by the Atlanta Falcons in the seventh round of the 1994 NFL Draft.  He played high school football at El Camino Real High School, where he was named to the CIF Los Angeles City Section 4-A All-City first team in 1989.  He went on to play college football at Moorpark College for the Moorpark College Raiders before playing at Utah.\n\nDarren Fells: Darren Andre Fells (born April 22, 1986) is an American football tight end for the Detroit Lions of the National Football League (NFL).  He did not play college football, instead playing college basketball at the University of California, Irvine.  Prior to his NFL career, he played professional basketball in several countries.  He is the brother of former NFL tight end Daniel Fells.\n\nBaron Batch: Baron Batch (born December 21, 1987), self-styled \"The Artist\", a Pittsburgh-based entrepreneur and former American football running back who retired from the NFL in 2013.  He is known for his \"FREE\" art drops, where he posts pictures of giveaway paintings on Instagram and Twitter, leaving clues to their location.  He played college football at Texas Tech University.  Batch chose to play college football at Texas Tech University over offers from Northwestern University, Duke University, and New Mexico State University.  Batch is from Midland, Texas.  He is the owner and creator of Angry Man Salsa and creative director of Studio AM.  He is the brother of Brian Batch of the band Alpha Rev.\n\n1891 Purdue football team: The 1891 Purdue football team was an American football team that represented Purdue University during the 1891 college football season.  The team compiled a 4–0 record in the university's fourth season fielding an intercollegiate football team.  For the 1891 season, Purdue hired Knowlton Ames as its football coach.  Ames played for Princeton from 1886 to 1889 and was considered one of the greatest players ever to play college football, after scoring 730 points for Princeton.  The 1891 Purdue team shut out all four opponents, outscoring Wabash, DePauw, Indiana, and Butler by a combined score of 192 to 0.  Purdue's 60–0 victory over Indiana was the first installment in a rivalry which later became noted for the award of the Old Oaken Bucket trophy.\n\nTitus Davis: Titus Davis (born January 3, 1993) is an American football wide receiver who is currently a free agent.  He was signed by the San Diego Chargers as an undrafted free agent in 2015.  He played college football at Central Michigan.  His younger brother, Corey Davis is a wide receiver for the Tennessee Titans.\n\nSeantrel Henderson: Seantrel Henderson (born January 21, 1992) is an American football offensive tackle for the Buffalo Bills of the National Football League (NFL).  He was drafted by the Bills in the seventh round of the 2014 NFL Draft.  He played college football at Miami.  Henderson attended Cretin-Derham Hall High School and originally signed a letter of intent to play college football at the University of Southern California, but was released from his commitment in July 2010 and eventually committed to the University of Miami.\n\nQuestion: Where did the younger brother of Titus Davis play college football?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the younger brother of Titus Davis.\"\n    },\n    \"relationship_to_titus_davis\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the player to Titus Davis.\"\n    },\n    \"college_football_team\": {\n      \"type\": \"string\",\n      \"description\": \"The college football team the player played for.\"\n    },\n    \"player_position\": {\n      \"type\": \"string\",\n      \"description\": \"The player's position in American football.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"relationship_to_titus_davis\",\n    \"college_football_team\",\n    \"player_position\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the younger brother of Titus Davis."
      },
      "relationship_to_titus_davis": {
        "type": "string",
        "description": "The relationship of the player to Titus Davis."
      },
      "college_football_team": {
        "type": "string",
        "description": "The college football team the player played for."
      },
      "player_position": {
        "type": "string",
        "description": "The player's position in American football."
      }
    },
    "required": [
      "player_name",
      "relationship_to_titus_davis",
      "college_football_team",
      "player_position"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
