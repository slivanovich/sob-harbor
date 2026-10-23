{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDream Street (UK TV series): Dream Street is a British children's television series that ran from 6 May 1999 to 2002 on \"CITV\".  The show is narrated by British comedian Russ Abbot, and was aimed at children aged from 2 to 7.  The show featured talking toy vehicles, which were radio controlled in real time.  The series aired back on CITV around 2008.\n\nDream Street: Dream Street was a short-lived American pop boy band that was formed in mid-1999 by Louis Baldonieri and Brian Lukow.  Dream Street later disbanded in 2002 following a legal dispute between parents of the band members and the band's managers.\n\nRuss Abbot: Russ Abbot (born Russell A. Roberts; 18 September 1947) is an English musician, comedian and actor.  He first came to public notice during the 1970s as the singer and drummer with British comedy showband the \"Black Abbots\", along with Leonard 'Lenny' Reynolds, later forging a prominent solo career as a television comedian with his own weekly show on British television.\n\nDon't Stand Another Chance: \"Don't Stand Another Chance\" is a song by American recording artist Janet Jackson, included on her second studio album, \"Dream Street\" (1984).  It was written by Janet Jackson, her brother Marlon Jackson and John Barnes.  Marlon also produced it, and provided backing vocals along with his brothers Michael, Tito, and Jackie.  \"Don't Stand Another Chance\" was released as the lead single from \"Dream Street\" on August 13, 1984 by A&M Records.\n\nDream Street (song): \"Dream Street\" is the final single released from Janet Jackson's second album \"Dream Street\", following the first three single releases, \"Two to the Power of Love\", \"Fast Girls\", and \"Don't Stand Another Chance\".  The title track was also scheduled to be released in 1984, but due to low sales the producers canceled these plans.  Thanks to the TV show \"Fame\", \"Dream Street\" did get a music video.\n\nDream Street (Dream Street album): Dream Street is the first and only album by the boy band Dream Street.  The songs \"It Happens Every Time\" and \"I Say Yeah\" were featured on Radio Disney albums.  The song \"They Don't Understand\" was featured on the \"\" soundtrack.\n\nThe Biggest Fan: The Biggest Fan is a film featuring the band Dream Street (Chris Trousdale, Jesse McCartney, Matt Ballinger, Frankie J. Galasso and Greg Raposo).  The main characters are Chris Trousdale (playing himself) and his \"Biggest Fan\" Debbie Worden (played by newcomer Kaila Amariah).  It was made in 2002 just before the band split; however, the film's release was postponed pending the outcome of a lawsuit between some of the band members and the band's management.  Chris Trousdale is prominently featured in the film, while the other Dream Street members have cameo roles in the beginning and the end of the film.  In late 2002- early 2003, Chris Trousdale promoted this film by performing and showing the film at his concerts.  After almost three years since filming for the film was complete, The Biggest Fan was finally released on DVD on May 18, 2005 (USA/Canada) and in 2007 (Australia).  The soundtrack on the other hand was released by Edel.\n\nDream Street (musical): Dream Street was a musical that ran in Las Vegas from 1983 through 1987.  Produced by Nancy and Ronnie Horowitz, conceived and written by Mark Donnelly, and choreographed and directed by Steve Merritt, \"Dream Street\" was a \"compilation\" musical, made up of well-known songs strung together with a simple narrative.  It dealt with the longings and dreams of a group of children whose neighborhood was being gentrified and who were forced to move out.\n\nDream Street (Janet Jackson album): Dream Street is the second studio album by American musician Janet Jackson, released on October 23, 1984, by A&M Records.  More pop than her debut album's \"bubblegum soul\" feel, the album wasn't the runaway success that Janet's father Joseph thought it would be, peaking at number one hundred forty-seven on the \"Billboard\" 200 in 1984.  The album did have one modest hit for Jackson, the top ten R&B single, \"Don't Stand Another Chance\", produced by brother Marlon.  Also, the video for the song \"Dream Street\", her first music video, was shot during the shooting of the TV show \"Fame\".\n\nFrankie J. Galasso: Frank J. \"Frankie\" Galasso is an American musician and actor.  He is best known as member of the boy band Dream Street.\n\nQuestion: What is the name of this English musician, comedian, and actor, who narrated Dream Street?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person.\"\n    },\n    \"professions\": {\n      \"type\": \"array\",\n      \"description\": \"A list of professions held by the person.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"role_in_show\": {\n      \"type\": \"string\",\n      \"description\": \"The role the person had in the specified TV series.\"\n    },\n    \"show_narrated\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the TV series narrated by the person.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"professions\",\n    \"role_in_show\",\n    \"show_narrated\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person."
      },
      "professions": {
        "type": "array",
        "description": "A list of professions held by the person.",
        "items": {
          "type": "string"
        }
      },
      "role_in_show": {
        "type": "string",
        "description": "The role the person had in the specified TV series."
      },
      "show_narrated": {
        "type": "string",
        "description": "The name of the TV series narrated by the person."
      }
    },
    "required": [
      "person_name",
      "professions",
      "role_in_show",
      "show_narrated"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
