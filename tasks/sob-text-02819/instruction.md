{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBaron Batch: Baron Batch (born December 21, 1987), self-styled \"The Artist\", a Pittsburgh-based entrepreneur and former American football running back who retired from the NFL in 2013.  He is known for his \"FREE\" art drops, where he posts pictures of giveaway paintings on Instagram and Twitter, leaving clues to their location.  He played college football at Texas Tech University.  Batch chose to play college football at Texas Tech University over offers from Northwestern University, Duke University, and New Mexico State University.  Batch is from Midland, Texas.  He is the owner and creator of Angry Man Salsa and creative director of Studio AM.  He is the brother of Brian Batch of the band Alpha Rev.\n\nRandy Kirk: Randall Scott Kirk (born December 27, 1964 in San Jose, California) is a former American football linebacker and special teams member who played thirteen seasons in the National Football League.  He is a 1982 graduate of Bellarmine College Prep where his team went undefeated and finished #1 in the state, and went on to play college football at San Diego State University.\n\nJohnson Bademosi: Johnson Bademosi (born July 23, 1990) is an American football cornerback and special teamer for the New England Patriots of the National Football League (NFL).  He was signed by the Browns as an undrafted free agent in 2012.  He was a member of the football, rugby, and track and field teams at Gonzaga College High School and went on to play college football for Stanford University.\n\nGeorge Thomas (American football): George Carroll Thomas, Jr. (March 4, 1928 – May 23, 1989) was an American football halfback and defensive back in the National Football League for the Washington Redskins and the New York Giants.  He was a standout high school basketball player, which led to his being recruited to play college basketball for Tulane University.  However, first year OU football coach, Jim Tatum, convinced him stay in Oklahoma and play college football at the University of Oklahoma.  Thomas was a standout for the Sooners, lettering in '46, '47,'48 and '49.  He earned All-American status in 1949 List of Oklahoma Sooners football All-Americans.  Thomas graduated from OU with a degree in Business Administration in 1950.\n\nTCU Horned Frogs football: The TCU Horned Frogs football team is the intercollegiate football team of Texas Christian University (TCU).  The Horned Frogs compete in Division I Football Bowl Subdivision (FBS), the highest level of intercollegiate athletics sanctioned by the National Collegiate Athletic Association (NCAA) in the United States.\n\nDarren Fells: Darren Andre Fells (born April 22, 1986) is an American football tight end for the Detroit Lions of the National Football League (NFL).  He did not play college football, instead playing college basketball at the University of California, Irvine.  Prior to his NFL career, he played professional basketball in several countries.  He is the brother of former NFL tight end Daniel Fells.\n\nMarcus Jackson: Marcus Jackson (born November 30, 1986) is a professional arena football and indoor football quarterback who is currently a free agent.  Jackson played college football for the TCU Horned Frogs football team.\n\nObi Egekeze: Egekeze was born in Augusta, Georgia in 1985.  He attended Westside High School in Augusta, where he was a three-year starter in football, basketball and soccer.  A placekicker and punter for the school's football team, he was selected as an all-state player as a senior.  Egekze also maintained a high school grade point average of 3.86 and was recruited to play college football by several major universities, including the University of Georgia, Ohio State University, University of Texas, and Penn State.  He accepted a scholarship to attend the University of Maryland.\n\nSeantrel Henderson: Seantrel Henderson (born January 21, 1992) is an American football offensive tackle for the Buffalo Bills of the National Football League (NFL).  He was drafted by the Bills in the seventh round of the 2014 NFL Draft.  He played college football at Miami.  Henderson attended Cretin-Derham Hall High School and originally signed a letter of intent to play college football at the University of Southern California, but was released from his commitment in July 2010 and eventually committed to the University of Miami.\n\n1891 Purdue football team: The 1891 Purdue football team was an American football team that represented Purdue University during the 1891 college football season.  The team compiled a 4–0 record in the university's fourth season fielding an intercollegiate football team.  For the 1891 season, Purdue hired Knowlton Ames as its football coach.  Ames played for Princeton from 1886 to 1889 and was considered one of the greatest players ever to play college football, after scoring 730 points for Princeton.  The 1891 Purdue team shut out all four opponents, outscoring Wabash, DePauw, Indiana, and Butler by a combined score of 192 to 0.  Purdue's 60–0 victory over Indiana was the first installment in a rivalry which later became noted for the award of the Old Oaken Bucket trophy.\n\nQuestion: For which University did Marcus Jackson play college football ? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football player.\"\n    },\n    \"university_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the university where the player played college football.\"\n    },\n    \"team_nickname\": {\n      \"type\": \"string\",\n      \"description\": \"The nickname of the university's football team.\"\n    },\n    \"ncaa_division\": {\n      \"type\": \"string\",\n      \"description\": \"The NCAA division in which the university's football team competes.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"university_name\",\n    \"team_nickname\",\n    \"ncaa_division\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the football player."
      },
      "university_name": {
        "type": "string",
        "description": "The name of the university where the player played college football."
      },
      "team_nickname": {
        "type": "string",
        "description": "The nickname of the university's football team."
      },
      "ncaa_division": {
        "type": "string",
        "description": "The NCAA division in which the university's football team competes."
      }
    },
    "required": [
      "player_name",
      "university_name",
      "team_nickname",
      "ncaa_division"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
