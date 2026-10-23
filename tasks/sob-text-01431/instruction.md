{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTulsa Philharmonic: The Tulsa Philharmonic was an American symphony orchestra located in Tulsa, Oklahoma.  The orchestra was founded in 1948 by H. Arthur Brown who was principal conductor from 1948 till 1958.  The original Tulsa Philharmonic grew out of a small group called the Tulsa Civic Symphony created in 1926-27 by Kurt Berger, a German-born and -educated musician living in Tulsa.  Many of the symphony's musicians also played in the pit orchestra for the Tulsa Little Theatre.  After its premier concert at the Akdar Theater as the Tulsa Civic Symphony in January 1927, the small orchestra was directed by Berger until 1933, when illness forced him to retire.  His daughter, Tosca Berger Kramer, briefly succeeded him.  George Baum also directed an orchestra under Works Progress Administration funding in the 1930s and 1940s.\n\nMonroe Symphony Orchestra: The Monroe Symphony (MSO) is a professional American orchestra located in Monroe, Louisiana.  The orchestra was founded in 1971 by Dr. Richard Worthington who served as musical director from 1971 until 1991.  Dr. Clay Couturiaux is the current music director.  The orchestra's season consists of classical concerts, pops concerts, and an educational concert offered to local elementary school students.  The MSO also holds the annual Marjorie Stricklin Emerging Artists Competition to promote and encourage excellence in musical performance and to provide orchestral performance opportunities for youth and young adults residing in Louisiana.\n\nMunich Philharmonic: The Munich Philharmonic (German: Münchner Philharmoniker ) is a German symphony orchestra located in the city of Munich.  It is one of Munich's four principal orchestras, along with the Bavarian Radio Symphony Orchestra, the Munich Radio Orchestra and the Bavarian State Orchestra.  Since 1985, the orchestra has been housed in the Gasteig Culture Centre.\n\nBursa State Symphony Orchestra: Bursa Regional State Symphony Orchestra is an orchestra located in Bursa.  This orchestra is the only \"state\" orchestra of Turkey.  The orchestra branched out from String Instruments Chamber Orchestra (1995), which was formed within the Uludag University and the Bursa Metropolitan Municipality established, Winds and Percussion Instruments Ensemble (1996).  The two community joined together to form the Bursa Symphonic Orchestra in 1998.\n\nBell Labs: Nokia Bell Labs (formerly named AT&T Bell Laboratories, Bell Telephone Laboratories and Bell Labs) is an American research and scientific development company, owned by Finnish company Nokia.  Its headquarters are located in Murray Hill, New Jersey, in addition to other laboratories around the rest of the United States and in other countries.\n\nVirtual Human Interaction Lab: The Virtual Human Interaction Lab (VHIL) at Stanford University was founded in 2003 by Professor Jeremy Bailenson, associate professor of communication at Stanford University.  The lab conducts research for the Communication Department.  VHIL's mission statement includes: \"The mission of the Virtual Human Interaction Lab is to understand the dynamics and implications of interactions among people in immersive virtual reality simulations (VR), and other forms of human digital representations in media, communication systems, and games.  Researchers in the lab are most concerned with understanding the social interaction that occurs within the confines of VR, and the majority of our work is centered on using empirical, behavioral science methodologies to explore people as they interact in these digital worlds.  However, oftentimes it is necessary to develop new gesture tracking systems, three-dimensional modeling techniques, or agent-behavior algorithms in order to answer these basic social questions.  Consequently, we also engage in research geared towards developing new ways to produce these VR simulations.\"\n\nLong Bay Symphony Orchestra: The Long Bay Symphony Orchestra is an American orchestra located in Myrtle Beach, South Carolina.  It was founded by Dr. Diana Swanner-Scroggins in 1988.  It is named after the long bay that stretches sixty miles along the Grand Strand region of the North and South Carolina coasts.  A professional orchestra, the Symphony has both a full orchestra and a chamber orchestra series each year.  In addition, the Symphony has played with many notable artists and groups.\n\nGolden State Pops Orchestra: The Golden State Pops Orchestra (GSPO) is an American symphony pops orchestra located in the San Pedro district of Los Angeles, California in the United States of America.  The GSPO is the resident orchestra of the Warner Grand Theatre, an Art Deco movie palace built by Warner Brothers Studios in 1931.  The orchestra performs a wide variety of musical repertoire, including classical, Broadway, pop music and even video game soundtracks.  However, the primary focus of the GSPO remains film music, a specialty of the orchestra since its founding in 2002.  The Golden State Pops Orchestra is composed of professional freelance musicians from around the Los Angeles area.\n\nSyracuse Symphony Orchestra: The Syracuse Symphony Orchestra (SSO) was a 79-member orchestra located in Syracuse, NY.  In its time it was the 43rd largest orchestra in the United States and performed a variety of programs including the Post-Standard Classics Series and M&T Bank Pops Series.  The orchestra also operated two youth orchestras in the Syracuse area: the Syracuse Symphony Youth Orchestra and the Syracuse Symphony Youth String Orchestra.\n\nHuman Digital Orchestra: The Human Digital Orchestra is a contemporary series of collaborations as part of the Experiments in Art and Technology that connects Bell Labs scientists and engineers with the artistic community by blending digital communications technology with artistic expression.  The first performance of the Human Digital Orchestra was at the first Claude Shannon Centennial Conference on the Future of the Information Age on April 28, 2016.\n\nQuestion: Where is the lab that is connected to artists by the Human Digital Orchestra located?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"lab_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the lab connected to artists.\"\n    },\n    \"connection_event\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the event or project that connects the lab to artists.\"\n    },\n    \"lab_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the lab's headquarters are located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the lab's headquarters are located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the lab's headquarters are located.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"lab_name\",\n    \"connection_event\",\n    \"lab_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "lab_name": {
        "type": "string",
        "description": "The name of the lab connected to artists."
      },
      "connection_event": {
        "type": "string",
        "description": "The name of the event or project that connects the lab to artists."
      },
      "lab_location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the lab's headquarters are located."
          },
          "state": {
            "type": "string",
            "description": "The state where the lab's headquarters are located."
          },
          "country": {
            "type": "string",
            "description": "The country where the lab's headquarters are located."
          }
        },
        "required": [
          "city",
          "state",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "lab_name",
      "connection_event",
      "lab_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
