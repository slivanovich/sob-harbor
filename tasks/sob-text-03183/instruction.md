{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFrancis Scott Key: Francis Scott Key (August 1, 1779January 11, 1843) was an American lawyer, author, and amateur poet from Frederick, Maryland and later Georgetown, D.C., near Washington, D.C. who wrote the lyrics for a poem entitled at first \"The Defence of Fort McHenry\", which when set to an old English gentlemens' society tune, eventually became the United States' national anthem, \"The Star-Spangled Banner\".\n\nJoseph Lutumba: Joseph Lutumba is a Congolese lyricist and the author of the Democratic Republic of the Congo's national anthem.  When the Democratic Republic of the Congo was renamed to Republic of Zaire, he was also the one who composed the national anthem known as the La Zaïroise.  The La Zaïroise was eventually replaced when the country was renamed back to the Democratic Republic of the Congo by the original national anthem \"Debout Congolais\".\n\nNational Anthem of The Mali Federation: This curious and unknown national anthem was created by the Federation's Official Law in 18/06/1960.  It has the music of the current National Anthem of Mali composed by Banzumana Sissoko (with an old intro and other notes) and lyrics of the current National Anthem of Senegal written by Léopold Sédar Senghor (slightly modified).  After separation of the two countries, Mali kept the music (because the composer was from this country) and Senegal retained the lyrics of the Federation (which was written by who would be the first Senegalese President) but removing the name \"Mali\" and others minor changes.\n\nCaleb Green: Master sergeant Caleb B. Green III is a solo vocalist with the United States Army Band.  An accomplished performer, particularly of the US national anthem, Green is often called upon to sing at important sporting events, diplomatic functions and military ceremonies.  His most notable anthem performance was at the at the Lincoln Memorial in Washington, D.C..  Prior to this his most notable outing was onstage in the TNT production \"Christmas in Washington 2008\", in which he sang \"O Holy Night\".\n\nHolliday Street Theater: The Holliday Street Theater also known as the New Theatre, New Holliday, Old Holliday, The Baltimore Theatre, and Old Drury, was a historical theatrical venue in colonial Baltimore, Maryland.  It is known for showing the first performance of Francis Scott Key's Star-Spangled Banner.\n\nE Ola Ke Alii Ke Akua: \"E Ola Ke Aliʻ i Ke Akua\", translated as \"God Save the King\", was one of Hawaii's four national anthems.  It was composed in 1860 by Prince William Charles Lunalilo, who later became King Lunalilo.  Prior to 1860, the Kingdom of Hawaii lacked its own national anthem and had used the British royal anthem \"God Save The King\".  A contest was sponsored in 1860 by Kamehameha IV, who wanted a song with Hawaiian lyrics set to the tune of the British anthem.  The winning entry was written by the 25-year-old Lunalilo and was reputed to have been written in 20 minutes.  Lunalilo was awarded 10 dollars, which later donated to the Queen's Hospital.  His composition became Hawaii's first national anthem.  It remained Hawaii's national anthem until 1866, when it was replaced by Queen Liliʻ uokalani's composition \"He Mele Lahui Hawaii\".\n\nNational Anthem of the Republic of China: The current National Anthem of the Republic of China () was adopted in 1937; previously, the Song to the Auspicious Cloud was used as the official anthem.  The current national anthem remains as the national anthem of the Republic of China government in Taiwan.  In mainland China, the anthem serves a historical role.  The national anthem of the People's Republic of China is the \"March of the Volunteers\".\n\nNational Anthem Project: The National Anthem Project was a public awareness campaign launched in 2005 as a major initiative of .  At the time of its launch, the National Anthem Project website declared \"MENC is sponsoring The National Anthem Project to revive America's patriotism by educating Americans about the importance of The Star-Spangled Banner-both the flag and the song.\"  Sponsored by MENC with major support from the Jeep brand, and other sponsors such as NAMM, Bank of America, and the Gibson Foundation, this campaign, which later used the slogan \"to restore America's voice through music education\" was MENC's most ambitious project to date.  A former First Lady, Laura Bush served as honorary chairperson, with country music's The Oak Ridge Boys as the official musical ambassadors.  The stated purpose of the project was originally \"to revive America's patriotism,\" but this was later modified to suggest that its purpose was merely to encourage more singing of the national anthem, or to bring more public attention to the role of music in American schools.\n\nList of historical national anthems: The oldest national anthem, defined as \"a song, as of praise, devotion, or patriotism\", is the Dutch national anthem \"Het Wilhelmus\", which was written between 1568 and 1572, but not then given any official status.  The first anthem to be officially proclaimed as such was \"God Save The Queen\", adopted by Great Britain in 1745.  \"Het Wilhelmus\" was declared the national anthem of the Netherlands in 1932; both of these anthems remain in use today.  A royal or imperial anthem is a song that is similar in patriotic character to a national anthem, but which specifically praises a monarch, or royal dynasty.  Some states have doubled their royal or imperial anthem as their national anthem.\n\nHimno Nacional Mexicano: The \"Mexican National Anthem\" (Spanish: \"Himno Nacional Mexicano\" ), also known as \"Mexicans, at the cry of war\" (Spanish: \"Mexicanos, al grito de guerra\" ), is the national anthem of the United Mexican States.  The anthem was first used in 1854, although it was not officially adopted \"de jure\" until 1943.  The lyrics of the national anthem, which allude to historical Mexican military victories in the heat of battle and including cries of defending the homeland, were composed by poet Francisco González Bocanegra after a Federal contest in 1853.  Later, in 1854, he asked Jaime Nunó to compose the music which now accompanies González's poem.  The anthem, consisting of ten stanzas and a chorus, effectively entered into use on September 16, 1854.\n\nQuestion: This historical theatrical venue showed the first performance of what would eventually be the US national anthem\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"venue_name\": {\n      \"type\": \"string\",\n      \"description\": \"The primary name of the historical theatrical venue.\"\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where the venue was located.\"\n    },\n    \"first_performed_song\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the song that had its first performance at this venue.\"\n    },\n    \"song_eventual_status\": {\n      \"type\": \"string\",\n      \"description\": \"The eventual status or significance of the song first performed.\"\n    },\n    \"alternative_venue_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other names by which the theatrical venue was known.\"\n    }\n  },\n  \"required\": [\n    \"venue_name\",\n    \"location\",\n    \"first_performed_song\",\n    \"song_eventual_status\",\n    \"alternative_venue_names\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "venue_name": {
        "type": "string",
        "description": "The primary name of the historical theatrical venue."
      },
      "location": {
        "type": "string",
        "description": "The city and state where the venue was located."
      },
      "first_performed_song": {
        "type": "string",
        "description": "The name of the song that had its first performance at this venue."
      },
      "song_eventual_status": {
        "type": "string",
        "description": "The eventual status or significance of the song first performed."
      },
      "alternative_venue_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other names by which the theatrical venue was known."
      }
    },
    "required": [
      "venue_name",
      "location",
      "first_performed_song",
      "song_eventual_status",
      "alternative_venue_names"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
