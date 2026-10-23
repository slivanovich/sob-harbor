{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSpookyfish: \"Spookyfish\" is the fifteenth episode in the second season of the American animated television series \"South Park\".  The 28th episode of the series overall, it originally aired on Comedy Central in the United States on October 28, 1998.  The episode was written and directed by series co-creator Trey Parker.  It was the season's Halloween special, featuring the \"spooky\" theme of having pictures of Barbra Streisand in the screen corners, accompanied with the words \"Spooky Vision\" (in response to Streisand's negative reception to the season one episode \"Mecha-Streisand\").\n\nGrey Dawn: \"Grey Dawn\" is the tenth episode in the seventh season and the 106th overall episode of the animated television series \"South Park\".  It originally aired on Comedy Central in the United States on November 5, 2003.  In the episode, senior citizens are running over people in the city of South Park, causing them to lose their driver's licenses.  Soon, the AARP comes to help them and take over the town.\n\nInto You Like a Train: \"Into You Like a Train\" is the sixth episode of the second season of the American television medical drama \"Grey's Anatomy\", and the show's fifteenth episode overall.  The episode, which would have originally served as the season two premiere, was written by Krista Vernoff and directed by Jeff Melman.  The episode was originally broadcast on the American Broadcasting Company (ABC) in the United States on October 30, 2005.  Vernoff received an Emmy nomination for Outstanding Writing for a Drama Series.  The episode's title refers to a song by The Psychedelic Furs from their Talk Talk Talk album.  The track was also covered by the band Jawbreaker as bonus track for their Dear You album 2004 reissue.\n\nThe Message (Prison Break): \"The Message\" is the thirty-seventh episode of the American television series \"Prison Break\" and is the fifteenth episode of its second season.  Originally aired on January 29, 2007, the episode was written by Zack Estrin and Karyn Usher, and was directed by Bobby Roth.  Regular cast members Robert Knepper (who plays T-Bag) and Rockmond Dunbar (who plays C-Note) do not appear in this episode.  The episode mainly features the protagonists, Michael Scofield and Lincoln Burrows, trying to reach Sara Tancredi, who may help to prove Lincoln's innocence.\n\nEmail Surveillance: \"Email Surveillance\" is the ninth episode of the second season of the American comedy television series \"The Office\", and the show's fifteenth episode overall.  Written by Jennifer Celotta, and directed by Paul Feig, the episode first aired in the United States on November 22, 2005 on NBC.  The episode guest starred Ken Jeong and Omi Vaidya.\n\nWrath of the Villains: Mad Grey Dawn: \"Wrath of the Villains: Mad Grey Dawn\" is the fifteenth episode of the second season, and 37th episode overall from the Fox series \"Gotham\".  The episode was written by Robert Hull and directed by Nick Copus.  It was first broadcast on March 21, 2016.  In the episode, Gordon and Bullock investigate a pair of clues in a museum, unaware Edward Nygma is the perpetrator.  Meanwhile, Bruce continues living in the streets with Selina and Cobblepot meets a man who knew about his mother.\n\nGotham (TV series): Gotham is an American crime drama television series developed by Bruno Heller, based on characters published by DC Comics and appearing in the Batman franchise, primarily those of James Gordon and Bruce Wayne.  The series stars Ben McKenzie as the young Gordon, while Heller executive-produces, along with Danny Cannon, who also directed the pilot.\n\nWrath of the Villains: Transference: \"Wrath of the Villains: Transference\" is the twenty-second episode and season finale of the second season, and 44th episode overall from the Fox series \"Gotham\".  This is also the last episode in the series with the subtitle \"Wrath of the Villains\".  The episode was written by developer and showrunner Bruno Heller and directed by Eagle Egilsson.  It was first broadcast on May 23, 2016.  In the episode, Lucius and Bruce are being held in a room by Nygma, ready to kill them unless they tell him information.  Meanwhile, Gordon tries to stop Professor Strange once and for all while Basil Karlo begins to fake being Gordon after his experiment.  The episode marked the end of the Strange story arc, which culminated with his arrest.  The episode is also dedicated to the memory of Doug Kraner, production designer of the show, who died on April 4, 2016 at the age of 65 of cancer.\n\nWrath of the Villains: Mr. Freeze: \"Wrath of the Villains: Mr. Freeze\" is the twelfth episode of the second season, 34th episode overall and the mid-season premiere from the FOX series \"Gotham\".  This episode is also the first episode to use the subtitle \"Wrath of the Villains\".  The episode was written by Ken Woodruff and directed by Nick Copus.  It was first broadcast in February 29, 2016 in FOX.  In the episode, having just killed Galavan, Gordon returns to the GCPD, who's currently investigating a killing spree of a man who freezes people.  Meanwhile, Cobblepot pays the consequences of killing Galavan.\n\nWrath of the Villains: A Legion of Horribles: \"Wrath of the Villains: A Legion of Horribles\" is the twenty-first episode of the second season, and 43rd episode overall from the Fox series \"Gotham\".  The episode was written by supervising producer Jordan Harper and directed by Rob Bailey.  It was first broadcast on May 16, 2016.  In the episode, after Azrael's death, Professor Strange resurrects Fish Mooney.  Meanwhile, Bruce sets out to save Selina, who has been attacked by Bridgit Pike, now calling herself \"Firefly\".  This episode marks the return of Jada Pinkett Smith to the series, after her character was killed off in the first-season finale.  On January 29, 2016 she announced her return to the series.  She previously stated that she wouldn't return for the second season.  This episode also marks the debut of Clayface.\n\nQuestion: Who developed the television series of which the fifteenth episode of the second season was \"Wrath of the Villains: Mad Grey Dawn\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"tv_series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television series.\"\n    },\n    \"episode_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the specific episode mentioned in the question.\"\n    },\n    \"season_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The season number of the episode.\"\n    },\n    \"episode_number_in_season\": {\n      \"type\": \"integer\",\n      \"description\": \"The episode number within its season.\"\n    },\n    \"developer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who developed the television series.\"\n    }\n  },\n  \"required\": [\n    \"tv_series_name\",\n    \"episode_title\",\n    \"season_number\",\n    \"episode_number_in_season\",\n    \"developer_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "tv_series_name": {
        "type": "string",
        "description": "The name of the television series."
      },
      "episode_title": {
        "type": "string",
        "description": "The title of the specific episode mentioned in the question."
      },
      "season_number": {
        "type": "integer",
        "description": "The season number of the episode."
      },
      "episode_number_in_season": {
        "type": "integer",
        "description": "The episode number within its season."
      },
      "developer_name": {
        "type": "string",
        "description": "The name of the person who developed the television series."
      }
    },
    "required": [
      "tv_series_name",
      "episode_title",
      "season_number",
      "episode_number_in_season",
      "developer_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
