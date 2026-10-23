{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMr. Lonely: \"Mr. Lonely\" is a song co-written and recorded by Bobby Vinton.  The song was first released on Vinton's 1962 album \"Roses Are Red\".\n\n911 / Mr. Lonely: \"911 / Mr. Lonely\" is a song by American rapper Tyler, The Creator.  It was released on June 30, 2017 alongside, \"Who Dat Boy\" through Columbia Records, as the lead singles from his fourth studio album \"Flower Boy\".  The song was produced by Tyler himself and features vocals from Frank Ocean, The Internet's Steve Lacy and Norwegian singer Anna of the North.\n\nBobby Vinton Sings for Lonely Nights: Bobby Vinton Sings for Lonely Nights is Bobby Vinton's eleventh studio album, released in 1965.  This album was released to capitalize on the success of Vinton's big hit \"Mr. Lonely\" and his album of the same name by containing only songs that refer to loneliness.  There were two singles from this album: \"Long Lonely Nights\" (previously a minor hit for Lee Andrews & the Hearts then for Clyde McPhatter in 1957 and then for The Four Seasons in 1964) and Vinton's self-penned \"L-O-N-E-L-Y\".  Cover versions include \"Saturday Night (Is the Loneliest Night of the Week)\", \"All Alone Am I\", \"Oh, How I Miss You Tonight\", \"In the Still of the Night\", \"I'll Walk Alone\" and \"Have You Ever Been Lonely (Have You Ever Been Blue?) \".\n\nFlower Boy: Flower Boy (alternatively titled Scum Fuck Flower Boy) is the fourth studio album by American rapper Tyler, The Creator.  The album, which is his first under a major record label, was released on July 21, 2017, by Columbia Records.  Although the album's production was handled entirely by Tyler, The Creator himself, it features guest vocals from a range of artists, including Frank Ocean, ASAP Rocky, Anna of the North, Lil Wayne, Kali Uchis, Steve Lacy, Estelle, Jaden Smith and Rex Orange County.\n\nMr. Lonely: His Greatest Songs Today: Mr. Lonely: His Greatest Songs Today is a collection of previously recorded songs by Bobby Vinton for Curb Records.  The first five tracks might be misleading to people of the baby boomer generation, as they are not the singles that Vinton had during the 1960s and the year of 1974 but re-recordings that Vinton made for Curb.  For this collection, five songs were taken from Vinton's self-explanatory album and four from his album \"Timeless\".  Re-recorded versions of \"Mr. Lonely\" and \"Roses Are Red\" make their first album appearance on this collection.\n\nYoo Min-kyu: Yoo Min-kyu (born September 18, 1987) is a South Korean actor.  Yoo began working as a runway and magazine model in 2006.  He then joined and won the audition competition \"Flower Boy Casting: Oh!  Boy\" in 2011, which led to his acting debut in the television series \"Shut Up Flower Boy Band\" in 2012.  In 2014, Yoo played leading roles in Kim Jho Gwangsoo's indie film \"One Night\" (part of the omnibus \"One Night Only\"), and another cable series \"Be Arrogant\".\n\nLonely (Akon song): \"Lonely\" (also known as \"Mr. Lonely\") is a song by Senegalese-American R&B and rapper Akon; it appears on his debut album, \"Trouble\".  The single was released in 2005 and was his first worldwide hit.  It reached number one in several countries, including in the United Kingdom and Germany (where it stayed there for eight weeks), and Australia.  It was also highly popular in France where it reached number two, and in the United States when it peaked at #4.  An edited version was on Radio Disney and on \"Radio Disney Jams, Vol.  8\".\n\nWho Dat Boy: \"Who Dat Boy\" is a song by American rapper Tyler, The Creator.  It was released on June 30, 2017 alongside, \"911 / Mr. Lonely\" through Columbia Records, as the lead singles from his fourth studio album \"Flower Boy\".  The song features vocals from ASAP Rocky.\n\nMr. Lonely (album): Mr. Lonely is Bobby Vinton's tenth studio album, released in 1964.  It was released right after the success of his fourth and final #1 US hit \"Mr. Lonely,\" a 1962 song that was released as a single after its appearance on \"Bobby Vinton's Greatest Hits\".  Cover versions on this album include \"Laughing on the Outside (Crying on the Inside)\" and \"I'll Never Smile Again\".  After the success of the single, Vinton released \"Bobby Vinton Sings for Lonely Nights\", an album of songs devoted to the subject of loneliness.\n\nFlower Boys Next Door: The series aired on tvN from January 7 to February 26, 2013 on Mondays and Tuesdays at 23:00 for 16 episodes.  Directed by Jung Jung-hwa (who previously helmed \"Flower Boy Ramyun Shop\") and written by movie screenwriter Kim Eun-jung (\"Gabi\", \"Hwang Jin-yi\"), it is the third installment of cable channel tvN's \"Oh!  Boy\" series of Flower Boy programming targeted at the teenage demographic.\n\nQuestion: What kind of artist does 911 / Mr. Lonely and Flower Boy have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_artist_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of artist that is common to both works.\"\n    },\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist common to both works.\"\n    },\n    \"works_involved\": {\n      \"type\": \"array\",\n      \"description\": \"A list of the works (songs/albums) that the artist is associated with.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  },\n  \"required\": [\n    \"common_artist_type\",\n    \"artist_name\",\n    \"works_involved\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_artist_type": {
        "type": "string",
        "description": "The type of artist that is common to both works."
      },
      "artist_name": {
        "type": "string",
        "description": "The name of the artist common to both works."
      },
      "works_involved": {
        "type": "array",
        "description": "A list of the works (songs/albums) that the artist is associated with.",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "common_artist_type",
      "artist_name",
      "works_involved"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
