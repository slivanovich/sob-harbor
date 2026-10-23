{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJake Kumerow: Jake Kumerow (born February 17, 1992) is an American football wide receiver who is currently a free agent.  He was signed by the Cincinnati Bengals as an undrafted free agent in 2015.  He played college football at Wisconsin–Whitewater.  His father is former Miami Dolphins first round pick Eric Kumerow.  He is the cousin of current Los Angeles Chargers defensive end Joey Bosa and Ohio State defensive end Nick Bosa.\n\nList of Melissa &amp; Joey episodes: \"Melissa & Joey\" is an American television sitcom starring Melissa Joan Hart and Joey Lawrence.  The series revolves around Melanie \"Mel\" Burke (Hart), an up-and-coming local politician who hires Joseph \"Joe\" Longo (Lawrence), a recently divorced commodities broker, as the nanny for her niece and nephew.  The series premiered on August 17, 2010 on ABC Family.\n\nMelissa &amp; Joey: Melissa & Joey is an American sitcom television series starring Melissa Joan Hart and Joey Lawrence that aired for four seasons between 2010 and 2015 on ABC Family.  The series follows local politician Mel Burke (Hart) and Joe Longo (Lawrence), whom Mel hires to look after her niece (Taylor Spreitler) and nephew (Nick Robinson) after a Ponzi scheme leaves Joe broke.\n\nBosa: Bosa is a town and \"comune\" in the province of Oristano (until May 2005 it was in the province of Nuoro), part of the Sardinia region of Italy.  Bosa is situated about two-thirds of the way up the west coast of Sardinia, on a small hill, about 3 km inland on the north bank of the Temo River.  The town has maintained a population of around 8,000 people for a significant amount of time, but has an urban character that has differentiated it from other locations in Sardinia.  Agriculture and fishing play an important part in the city economy, thanks to the river valley near the coast surrounded by hills and highland plateaus.\n\nEric II of Denmark: Eric II the Memorable (Danish: \"Erik II Emune\" ) (  1090 – 18 September 1137) was king of Denmark between 1134 and 1137.  Eric was an illegitimate son of Eric I of Denmark, who ruled Denmark from 1095 to 1103.  Eric the Memorable rebelled against his uncle Niels of Denmark, and was declared king in 1134.  He punished his adversaries severely, and rewarded his supporters handsomely.  He was killed by a subject in 1137 and was promptly succeeded by his nephew Eric III of Denmark.\n\nLero-Lero: Lero-Lero, released in 2010, is the first solo album from Brazilian artist, Luísa Maita off, U.S. based, independent label, Cumbancha.  The album features a variety of sounds from samba and bosa nova to western jazz and downtempo electronic.  Maita's array of cultural influences play a large role in the structure of the album, \"Something that defines Lero, Lero is its urban style.  Originally from São Paulo, Luísa Maita brings to her work her own life experience growing up in one the largest cities in the world.\"  Lero-Lero precedes two different remixed versions of the album: Maita Remixed and Maita Remixed DJ Edition.\n\nSagipa: Sagipa or Zaquesazipa (died 1539, Bosa, New Kingdom of Granada) was the fifth and last ruler (\"zipa\") of Bacatá, currently known as the Colombian capital Bogotá, as of 1537.  He was the brother of his predecessor Tisquesusa but the traditional faction of the Muisca considered him an usurper as his nephew Chiayzaque, the \"cacique\" of Chía, was the legitimate successor of Tisquesusa.  His \"zaque\" counterpart in the northern part of the Muisca territory was Aquiminzaque, the last surviving ruler of the Muisca.  The daughter of Sagipa, named as Magdalena de Guatavita, married conquistador Hernán Venegas Carrillo, one of the first mestizo marriages in the New Kingdom of Granada.\n\nJohn Bosa: John Wilfred Bosa (born January 10, 1964) is a former professional American football defensive end who played three seasons in the National Football League (NFL) for the Miami Dolphins.  He played football for Keene High School in Keene, New Hampshire and received a full athletic scholarship to play football for the Boston College Eagles.\n\nEric Kumerow: Eric Palmer Kumerow (born April 17, 1965) is a former American football linebacker who played three seasons for the Miami Dolphins and one season with the Chicago Bears in the National Football League.  Despite being a first round draft pick (16th overall), his brief NFL career has been widely criticized as a disappointment.  He retired after only three seasons without ever starting an NFL game, and registering only five quarterback sacks.  He is the grandson of Chicago Outfit mob boss Tony Accardo, the brother-in-law of former Miami Dolphins first-round pick John Bosa, and the uncle of Los Angeles Chargers defensive end Joey Bosa.  He now resides in the Chicago suburb of Bartlett, Illinois.\n\nJoey Bosa: Joseph Anthony Bosa (born July 11, 1995) is an American football defensive end for the Los Angeles Chargers of the National Football League (NFL).  He played college football at Ohio State, and was selected by the Chargers third overall in the 2016 NFL Draft.\n\nQuestion: What college did Eric Kumerow's nephew, Joey Bosa, play for?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"nephew_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of Eric Kumerow's nephew.\"\n    },\n    \"college_played_for\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the college the nephew played football for.\"\n    },\n    \"current_nfl_team\": {\n      \"type\": \"string\",\n      \"description\": \"The current NFL team the nephew plays for.\"\n    },\n    \"position\": {\n      \"type\": \"string\",\n      \"description\": \"The playing position of the nephew.\"\n    }\n  },\n  \"required\": [\n    \"nephew_name\",\n    \"college_played_for\",\n    \"current_nfl_team\",\n    \"position\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "nephew_name": {
        "type": "string",
        "description": "The name of Eric Kumerow's nephew."
      },
      "college_played_for": {
        "type": "string",
        "description": "The name of the college the nephew played football for."
      },
      "current_nfl_team": {
        "type": "string",
        "description": "The current NFL team the nephew plays for."
      },
      "position": {
        "type": "string",
        "description": "The playing position of the nephew."
      }
    },
    "required": [
      "nephew_name",
      "college_played_for",
      "current_nfl_team",
      "position"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
