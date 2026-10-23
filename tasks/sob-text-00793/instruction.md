{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEinstein on the Beach: Einstein on the Beach is an opera in four acts (framed and connected by five \"knee plays\" or intermezzos), composed by Philip Glass and directed by theatrical producer Robert Wilson.  The opera eschews traditional narrative in favor of a formalist approach based on structured spaces laid out by Wilson in a series of storyboards.  The music was written \"in the spring, summer and fall of 1975.\"  Glass recounts the collaborative process: \"I put [Wilson’s notebook of sketches] on the piano and composed each section like a portrait of the drawing before me.  The score was begun in the spring of 1975 and completed by the following November, and those drawings were before me all the time.\"  The premiere took place on July 25, 1976, at the Avignon Festival in France.  The opera contains writings by Christopher Knowles, Samuel M. Johnson and Lucinda Childs.  It is Glass's first and longest opera score, taking approximately five hours in full performance without intermission; given the length, the audience is permitted to enter and leave as desired.\n\nPhilip Glass Ensemble: The Philip Glass Ensemble is a musical group founded by composer Philip Glass in 1968 to serve as a performance outlet for his experimental minimalist music.  The Ensemble's instrumentation became a hallmark of Glass's early minimalist style.  After Glass wrote his first opera, \"Einstein on the Beach\", for the Ensemble in 1976, he began to compose for other instrumentation more frequently, but he still retains the core ensemble instrumentation.\n\nMichael Riesman: Michael Riesman is a composer, conductor, keyboardist, and record producer, best known as Music Director of the Philip Glass Ensemble and conductor of nearly all of Glass' film scores.\n\nTara Hugo Sings Philip Glass: Tara Hugo sings Philip Glass is a 2012 album by mezzo-soprano and actress Tara Hugo of songs of composer Philip Glass.  The recording project was initiated by Glass himself who asked collaborator and producer Kurt Munkacsi to present pieces that Glass had composed for larger music ensembles as a song recital for small ensemble.  The recital album includes songs Glass had composed with or for singers Leonard Cohen (Book of Longing), Natalie Merchant, Mick Jagger and poet Allen Ginsberg.  The album also includes new arrangements by Trevor Gureckis of Glass instrumental music set to new lyrics written by Tara Hugo.\n\nPolyrock: Polyrock was an American post-punk/new wave band formed in New York City in 1978 and active until the mid-1980s.  Strongly influenced by minimalism, the group was produced by the composer Philip Glass and Kurt Munkacsi.  The band, led by singer/guitarist Billy Robertson (formerly of the group Model Citizens), had a keyboard-heavy, pattern-based sound strongly reminiscent of Glass's work; in fact, Glass performed on their first two albums.\n\nSeymour Barab: Seymour Barab (January 9, 1921 – died June 28, 2014) was an American composer of opera, songs and instrumental and chamber music, as well as a cellist, organist and pianist.  He was best known for his fairy tale operas for young audiences, such as \"Chanticleer\" and \"Little Red Riding Hood\".  He was a longtime member of the Philip Glass Ensemble.\n\nMusic for &quot;The Knee Plays&quot;: Music for \"The Knee Plays\" (1985) is an album by David Byrne composed for Robert Wilson's opera .  The album was originally released on vinyl and a remastered and expanded CD version was released in November 2007 under the title \"The Knee Plays\".\n\nMonsters of Grace: Monsters of Grace is a multimedia chamber opera in 13 short acts directed by Robert Wilson, with music by Philip Glass and libretto from the works of 13th-century Sufi mystic Jalaluddin Rumi.  The title is said to be a reference to Wilson's corruption of a line from Hamlet: \"Angels and ministers of grace defend us!\"  (1.4.39).\n\nGlass: A Portrait of Philip in Twelve Parts: Glass: A Portrait of Philip in Twelve Parts (other titles include International title Glass, Hungarian title Glass - Philip portréja 12 felvonásban) is a 2007 documentary on the life of American composer Philip Glass directed by Scott Hicks.  The film was nominated for Emmy Awards and AFI Award\n\nAkhnaten (opera): Akhnaten is an opera in three acts based on the life and religious convictions of the pharaoh Akhenaten (Amenhotep IV), written by the American minimalist composer Philip Glass in 1983.  \"Akhnaten\" had its world premiere on March 24, 1984, at the Stuttgart State Theatre, under the German title \"Echnaton\".  Paul Esswood sang the title role, German director Achim Freyer staged the opera in an abstract style with highly ritualistic movements.  The American premiere was held on October 12, 1984, at the Houston Grand Opera, where Glass's opera \"The Making of the Representative for Planet 8\" also premiered.\n\nQuestion: The Philip Glass Ensemble is a musical group founded by composer Philip Glass in 1968, his first opera is which opera in four acts (framed and connected by five \"knee plays\" or intermezzos), composed by Philip Glass, and directed by theatrical producer Robert Wilson?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"opera_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the opera.\"\n    },\n    \"composer\": {\n      \"type\": \"string\",\n      \"description\": \"The composer of the opera.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the opera.\"\n    },\n    \"premiere_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"date\": {\n          \"type\": \"string\",\n          \"format\": \"date\",\n          \"description\": \"The date of the opera's premiere in YYYY-MM-DD format.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The location of the opera's premiere.\"\n        }\n      },\n      \"required\": [\n        \"date\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"structural_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"number_of_acts\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of acts in the opera.\"\n        },\n        \"number_of_knee_plays\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of 'knee plays' or intermezzos connecting the acts.\"\n        },\n        \"approximate_duration_hours\": {\n          \"type\": \"number\",\n          \"description\": \"The approximate duration of the full performance in hours.\"\n        }\n      },\n      \"required\": [\n        \"number_of_acts\",\n        \"number_of_knee_plays\",\n        \"approximate_duration_hours\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"libretto_writers\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of individuals who contributed writings to the opera.\"\n    },\n    \"composed_for_ensemble\": {\n      \"type\": \"string\",\n      \"description\": \"The musical group for which the opera was initially written.\"\n    }\n  },\n  \"required\": [\n    \"opera_name\",\n    \"composer\",\n    \"director\",\n    \"premiere_details\",\n    \"structural_details\",\n    \"libretto_writers\",\n    \"composed_for_ensemble\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "opera_name": {
        "type": "string",
        "description": "The name of the opera."
      },
      "composer": {
        "type": "string",
        "description": "The composer of the opera."
      },
      "director": {
        "type": "string",
        "description": "The director of the opera."
      },
      "premiere_details": {
        "type": "object",
        "properties": {
          "date": {
            "type": "string",
            "format": "date",
            "description": "The date of the opera's premiere in YYYY-MM-DD format."
          },
          "location": {
            "type": "string",
            "description": "The location of the opera's premiere."
          }
        },
        "required": [
          "date",
          "location"
        ],
        "additionalProperties": false
      },
      "structural_details": {
        "type": "object",
        "properties": {
          "number_of_acts": {
            "type": "integer",
            "description": "The number of acts in the opera."
          },
          "number_of_knee_plays": {
            "type": "integer",
            "description": "The number of 'knee plays' or intermezzos connecting the acts."
          },
          "approximate_duration_hours": {
            "type": "number",
            "description": "The approximate duration of the full performance in hours."
          }
        },
        "required": [
          "number_of_acts",
          "number_of_knee_plays",
          "approximate_duration_hours"
        ],
        "additionalProperties": false
      },
      "libretto_writers": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of individuals who contributed writings to the opera."
      },
      "composed_for_ensemble": {
        "type": "string",
        "description": "The musical group for which the opera was initially written."
      }
    },
    "required": [
      "opera_name",
      "composer",
      "director",
      "premiere_details",
      "structural_details",
      "libretto_writers",
      "composed_for_ensemble"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
