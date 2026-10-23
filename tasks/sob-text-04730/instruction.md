{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Night Shift (concert): The Night Shift is the name given to a series of concerts run by the Orchestra of the Age of Enlightenment.  As a Resident Orchestra at the Southbank Centre, the first Night Shift took place on 22 May 2006 at the Queen Elizabeth Hall.  Since then there have been fifteen further concerts at venues including the Queen Elizabeth Hall, Royal Festival Hall, The Roundhouse and the Corn Exchange, Brighton Dome.\n\nGeneral Hospital: Night Shift: General Hospital: Night Shift is an American prime time serial that first aired on Soapnet for a 13-episode run from July 12, 2007 to October 4, 2007.  A spin-off of the ABC Daytime soap opera \"General Hospital\", the show is SOAPnet's first original scripted drama series and follows the nighttime adventures of familiar and new characters around the hospital.  As of March 2008, the first season of the series was \"SOAPnet's most watched series ever,\" with ABC Daytime and SOAPnet President Brian Frons noting that \"Night Shift\" drew more than 1 million new viewers to the channel during its first season.  With its reruns gaining higher ratings than those of \"General Hospital\" on SOAPnet, a second season was expected, though Frons noted that the same crew producing two shows had taken its toll.\n\nNight Shift (film): Night Shift is a 1982 American comedy film, directed by Ron Howard, concerning a timid night shift morgue employee whose life is turned upside down by a free-spirited entrepreneur.  It stars Howard's \"Happy Days\" co-star Henry Winkler along with Michael Keaton, in his first starring role, and Shelley Long.  Also appearing are Richard Belzer and Clint Howard.  A young Kevin Costner has a brief scene as \"Frat Boy #1\", Shannen Doherty appears as a Bluebell scout, Vincent Schiavelli plays a man who delivers a sandwich to Winkler's character, and Charles Fleischer has a brief role as one of the jail prisoners.\n\nJill Flint: Jill Flint (born November 25, 1977) is an American television and film actress, best known for her role of Jill Casey in the USA Network TV series \"Royal Pains\", and as the popular character Lana Delaney on CBS's award-winning series \"The Good Wife\".  She also plays one of the lead characters, Dr. Jordan Alexander in the NBC medical drama \"The Night Shift\".\n\nMichael Guerin: Michael Guerin is a fictional character created by Melinda Metz for the young adults book series \"Roswell High\" and adapted by Jason Katims for the 1999-2002 American science fiction television series \"Roswell\".  He was portrayed by actor Brendan Fehr in the television series.\n\nBrendan Fehr: Brendan Jacob Joel Fehr (born October 29, 1977) is a Canadian film and television actor, perhaps best known for portraying Michael Guerin in the WB television series Roswell, and for portraying Laboratory Tech in .  In 2008, Fehr won a Gemini Award for \"Hottest Canadian Male TV Star\".  Brendan currently plays Dr. Drew Alister on the NBC drama The Night Shift.\n\nList of The Night Shift episodes: \"The Night Shift\" is an American medical drama television series created by Gabe Sachs and Jeff Judah.  The series premiered on May 27, 2014, on NBC, and stars Eoin Macken, Jill Flint, Ken Leung, Brendan Fehr, Daniella Alonso, Robert Bailey Jr., Jeananne Goossen, J.R. Lemon, and Freddy Rodriguez as the staff who work the late night shift in the ER at San Antonio Medical Center.  On November 17, 2016, NBC renewed the series for a fourth season, which premiered on June 22, 2017.\n\nNight Shift (UK TV series): Night Shift was a late-twentieth-century television series that portrayed people who work the night shift (work during the night).\n\nNæturvaktin: Næturvaktin (English: \"The Night Shift\") is an Icelandic television show.  It is the first in a trilogy, its sequels being \"Dagvaktin\" (\"The Day Shift\") and \"Fangavaktin\" (\"The Prison Shift\").  The series was first shown in 2007 on Stöð 2, on Sundays from 16 September – 9 December.  In the same year, the series won an Edda Award for \"Best TV Series\".  It was also selected \"The Most Popular TV Series\" by a direct audience vote.\n\nThe Night Shift (TV series): The Night Shift is an American medical drama series that premiered on May 27, 2014, on NBC.  The series was created by Gabe Sachs and Jeff Judah, and follows the lives of the staff who work the late night shift in the emergency room at San Antonio Memorial Hospital.\n\nQuestion: The character Michael Guerin in the tv series \"Roswell\" is played by an actor that plays what role on \"The Night Shift\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"original_character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character in the original series.\"\n    },\n    \"original_series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the original television series.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who played the original character.\"\n    },\n    \"target_series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the target television series.\"\n    },\n    \"role_in_target_series\": {\n      \"type\": \"string\",\n      \"description\": \"The role played by the actor in the target series.\"\n    }\n  },\n  \"required\": [\n    \"original_character_name\",\n    \"original_series_name\",\n    \"actor_name\",\n    \"target_series_name\",\n    \"role_in_target_series\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "original_character_name": {
        "type": "string",
        "description": "The name of the character in the original series."
      },
      "original_series_name": {
        "type": "string",
        "description": "The name of the original television series."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who played the original character."
      },
      "target_series_name": {
        "type": "string",
        "description": "The name of the target television series."
      },
      "role_in_target_series": {
        "type": "string",
        "description": "The role played by the actor in the target series."
      }
    },
    "required": [
      "original_character_name",
      "original_series_name",
      "actor_name",
      "target_series_name",
      "role_in_target_series"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
