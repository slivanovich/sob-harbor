{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBattle of Verona (1799): Battle of Verona on 26 March 1799 saw a Habsburg Austrian army under Pál Kray fight a First French Republic army led by Barthélemy Louis Joseph Schérer.  The battle encompassed three separate combats on the same day.  At Verona, the two sides battled to a bloody draw.  At Pastrengo to the west of Verona, French forces prevailed over their Austrian opponents.  At Legnago to the southeast of Verona, the Austrians defeated their French adversaries.  The battle was fought during the War of the Second Coalition, part of the French Revolutionary Wars.  Verona is a city on the Adige River in northern Italy.\n\nSveinn Rúnar Sigurðsson: Sveinn Rúnar Sigurðsson (born 24 December 1976) studied the piano under Ferenc Utassy, Jon Sigurdsson and Pavel Manazek.  Since the age of 16 he has composed music in styles ranging from modern classics to pop.  He composed two Eurovision Song Contest entries for his country, Iceland, 'Heaven' in 2004 and 'Ég les í lófa þínum' in 2007.  He holds a degree in Medicine (M.D) and stock trading.\n\nAashiqui 2 (soundtrack): Aashiqui 2 is the soundtrack to the 2013 Bollywood romance film of the same name, directed by Mohit Suri and starring Aditya Roy Kapoor and Shraddha Kapoor in the lead roles.  The album was produced by Bhushan Kumar and Mahesh Bhatt under the banner T-Series and Vishesh Films.  the songs of the film were mostly composed by Jeet Gannguli, although Mithoon and Ankit Tiwari composed two songs each (including both versions) as guest composers.  Irshad Kamil wrote lyrics for most of songs on the album.  Sandeep Nath wrote both versions of \"Sunn Raha Hai\", while Mithoon wrote \"Tum Hi Ho\" and Sanjay Masoom wrote \"Bhula Dena\".  Arijit Singh sang six of the songs on the album.  The music became very popular after its release on 8 April 2013, with songs \"Tum Hi Ho\" and \"Sunn Raha Hai\" topping the charts across various platforms in India.  Jeet Gannguli reused the tune from his own Bengali composition \"Mon Hariye Beghorey\" for \"Milne Hai Mujhse Aayi\".\n\nVerona Porta Nuova railway station: Verona Porta Nuova is the main railway station of Verona.  It is one of the two stations serving central Verona; the other station, Verona Porta Vescovo, is located at the east of the city.\n\nGalt MacDermot: Arthur Terence Galt MacDermot (born December 18, 1928) is a Canadian-American composer, pianist and writer of musical theatre.  He won a Grammy Award for the song \"African Waltz\" in 1960.  His most successful musicals have been \"Hair\" (1967; its cast album also won a Grammy) and \"Two Gentlemen of Verona\" (1971).  MacDermot has also written music for film soundtracks, jazz and funk albums, and classical music, and his music has been sampled in hit hip-hop songs and albums.  He is best known for his work on \"Hair\", and in particular three of the songs from the show; \"Aquarius\", \"Let the Sunshine In\", and \"Good Morning Starshine\", all three of which were number one hits in 1969.\n\nVersus de Verona: The Versus de Verona, also Carmen Pipinianum or Rhythmus Pipinianus (\"Ritmo Pipiniano\"), was a medieval Latin poetic encomium on the city of Verona, composed during the Carolingian Renaissance, between 795 and 806.  It was modeled on the \"Laudes Mediolanensis civitatis\" (c.738), which is preserved today only in a Veronese manuscript.  The anonymous \"Versus\" have been ascribed to Pacificus, archdeacon at Verona from 803 until his death in 846, but this ascription is unlikely.  The poem consists of thirty-three strophes and three verses.\n\nAnupam Roy: Anupam Roy (Bengali: অনুপম রায় ; born 29 March 1982) is an Indian lyricist, music composer and singer from Kolkata, West Bengal.  He is best known for his song \"Amake Amar Moto Thakte Dao (আমাকে আমার মতো থাকতে দাও)\", which appeared on the soundtrack to the 2010 film \"Autograph\".  Since then, he has gone on to compose, write lyrics and sing for many Bengali films.  In 2015, he made his Bollywood debut, composing the songs and score for Piku.  He was nominated for the Filmfare Award for Best Music Director, and won the Filmfare Award for Best Background Score.  In 2016, he composed two songs for the Hindi film Pink.  In 2017, he composed for the Hindi films Running Shaadi (one song) and Dear Maya.  He is a recipient of 64th National Film Award for Best Lyrics for the song \"Tumi Jaake Bhalobasho\".\n\nGualfardo of Verona: Saint Gualfardo of Verona (or Wolfhard of Augsburg) (1070–1127) was a Swabian artisan, trader, and hermit who lived around Verona.  A hagiographical \"vita\" (biography) was composed, according to the Bollandists, within decades of his death, probably towards the end of the twelfth century.  In the early sixteenth century he was venerated as the patron saint of the harnessmakers' guild at Verona.\n\nViolin Sonata in F minor (Mendelssohn): The Violin Sonata in F minor, Op.  4, for violin and piano was composed by Felix Mendelssohn in 1825 and is the only one to carry an opus number.  Mendelssohn composed two other violin sonatas, both in F major, that are without opus numbers.\n\nTwo Gentlemen of Verona (musical): Two Gentlemen of Verona is a rock musical, with a book by John Guare and Mel Shapiro, lyrics by Guare and music by Galt MacDermot, based on the Shakespeare comedy of the same name.\n\nQuestion: Who composed Two gentleman of Verona?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"musical_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the musical.\"\n    },\n    \"composer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who composed the music for the musical.\"\n    },\n    \"musical_type\": {\n      \"type\": \"string\",\n      \"description\": \"The genre or type of the musical.\"\n    },\n    \"year_premiered\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the musical premiered.\"\n    },\n    \"based_on_source\": {\n      \"type\": \"string\",\n      \"description\": \"The original work or source material the musical is based on.\"\n    }\n  },\n  \"required\": [\n    \"musical_title\",\n    \"composer\",\n    \"musical_type\",\n    \"year_premiered\",\n    \"based_on_source\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "musical_title": {
        "type": "string",
        "description": "The title of the musical."
      },
      "composer": {
        "type": "string",
        "description": "The name of the person who composed the music for the musical."
      },
      "musical_type": {
        "type": "string",
        "description": "The genre or type of the musical."
      },
      "year_premiered": {
        "type": "integer",
        "description": "The year the musical premiered."
      },
      "based_on_source": {
        "type": "string",
        "description": "The original work or source material the musical is based on."
      }
    },
    "required": [
      "musical_title",
      "composer",
      "musical_type",
      "year_premiered",
      "based_on_source"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
