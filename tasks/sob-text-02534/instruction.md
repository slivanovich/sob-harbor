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
Ughelli Township Stadium: Ughelli Township Stadium is a stadium in Ughelli, Nigeria.  It is currently used mostly for football matches and is the temporary home stadium of Ocean Boys FC.  The stadium has a capacity of 5,000 people and was built in 2002.  It hosted matches for the 2006 Women's African Football Championship and for the 2008 WAFU U-20 Championship

2016 OFC U-20 Championship: The 2016 OFC U-20 Championship was the 13th edition of the OFC U-20 Championship, the biennial international youth football tournament organized by the Oceania Football Confederation (OFC) for players aged 19 and below (despite the name remaining as U-20 Championship).  This year the tournament was held in Vanuatu for the first time.

WAFU U-20 Championship: The WAFU U-20 Championship is an association football tournament that is contested between West African nations.  It was funded by The Economic Community Of West African States.

A Trip to Jamaica: A Trip to Jamaica is a Nigerian comedy drama film directed by Robert Peters, starring Ayo Makun, Funke Akindele, Nse Ikpe Etim and Dan Davies.  The film received mainly mixed to negative reviews from critics, however, it was a huge box office success, breaking the earlier record set by "30 Days in Atlanta".  The movie had its worldwide premiere on September 25, 2016 in Lagos State.  The event also featured a celebrity football game involving ex-internationals, like Kanu Nwankwo, Jay Jay Okocha, Peter Rufai, Joseph Yobo and Stephen Appiah.  The film tells a story about the adventures of a newly engaged couple in their relatives residence outside Nigeria, and how the secrets of their host led to the eventual breakup of their union amidst the culture shock of the new country and living with upper-class citizens.

2009 CONCACAF U-20 Championship: The 2009 CONCACAF U-20 Championship was the biannual CONCACAF youth championship tournament for under-20 national teams.  The 2009 edition was held in Trinidad and Tobago.  All matches were played at Dwight Yorke Stadium in Bacolet, Tobago and Marvin Lee Stadium in Macoya, Trinidad.  The CONCACAF U-20 Championship traditionally serves as the CONCACAF qualifier for the FIFA U-20 World Cup, and under the 2009 tournament format the four semifinalists qualified for the 2009 FIFA U-20 World Cup, which was hosted by Egypt from 25 September to 16 October 2009.

2009 CONCACAF U-20 Championship qualifying: The 2009 CONCACAF U-20 Championship qualifying tournament determined the Caribbean and Central American Under-20 association football national teams that would participate in the 2009 CONCACAF U-20 Championship, which itself will qualify national teams to the 2009 FIFA U-20 World Cup.  Qualification began on 14 May 2008.  The final round of qualification was a one-game playoff on 2 March 2009, between the runner-up from the Caribbean zone, St Vincent and the Grenadines, and the 3rd-place finisher from the Central American zone, Honduras.  The three North American zone nations, Canada, Mexico, and the United States, as well as tournament hosts Trinidad and Tobago, were automatically entered into the final tournament without need for qualification.

Delta Force F.C.: Delta Force F.C. is a football team based in Asaba, Delta State, Nigeria.  They play at Jay Jay Okocha Stadium.

Jay-Jay Okocha: Augustine Azuka "Jay-Jay" Okocha (born 14 August 1973) is a Nigerian former professional footballer who played as an attacking midfielder.  A quick and skillful playmaker, who is widely regarded as the best Nigerian player of his generation and one of the greatest African players of all time, Okocha was known for his confidence, technique, creativity, and dribbling skills, as well as his use of feints, in particular the stepover.  Due to his skill, he was described as being 'so good that they named him twice' (a line immortalised in a terrace chant while Okocha played for Bolton Wanderers).  He is a dual Nigerian-Turkish citizen, having acquired Turkish citizenship as "Muhammet Yavuz" while playing for Süper Lig team Fenerbahçe.

2010 CONCACAF Women's U-20 Championship: The 2010 CONCACAF Women's U-20 Championship was the fifth edition of the CONCACAF Women's U-20 Championship.  The tournament was hosted by Guatemala, and all matches were played at the Estadio Cementos Progreso.  The United States were the defending champions, having won the 2008 tournament, their second regional championship at the under-20 level.  The top three sides at the 2010 tournament earned qualification to the 2010 FIFA U-20 Women's World Cup.  The tournament was won by the United States, who defeated Mexico in the final, 1–0.  Costa Rica secured the final qualification position by defeating Canada in the third place match, 1–0.

Jay Jay Okocha Stadium: Jay Jay Okocha Stadium is a stadium in Ogwashi-Uku, Anioma, Nigeria named after former Super Eagles captain Jay-Jay Okocha.  It is currently used mostly for football matches and is the home stadium of Delta Force F.C. Renamed after Okocha in June 2008, the stadium has a capacity of 8,000 people and hosted matches for the 2008 WAFU U-20 Championship won by Ghana.

Question: Which country won the 2008 WAFU U-20 Championship at the Jay Jay Okocha Stadium?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "championship_name": {
      "type": "string",
      "description": "The name of the football championship."
    },
    "year": {
      "type": "integer",
      "description": "The year the championship was held."
    },
    "winning_country": {
      "type": "string",
      "description": "The country that won the championship."
    },
    "host_stadium": {
      "type": "string",
      "description": "The stadium where the championship matches were hosted."
    },
    "stadium_location": {
      "type": "string",
      "description": "The location of the host stadium."
    }
  },
  "required": [
    "championship_name",
    "year",
    "winning_country",
    "host_stadium",
    "stadium_location"
  ],
  "additionalProperties": false
}
