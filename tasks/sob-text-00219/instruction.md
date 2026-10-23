{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Roussos Phenomenon EP: The Roussos Phenomenon EP is a popular EP by Demis Roussos.\n\nRewired (Mike + The Mechanics album): Rewired is the sixth studio album by Mike + The Mechanics, released in 2004.  This was the first album released by the band following the death of the co-lead singer Paul Young.  Partly because of this, the album was credited to \"Mike + The Mechanics + Paul Carrack\".  It is the only Mike + The Mechanics album to date with only one lead vocalist.\n\nDemis Roussos: Artemios \"Demis\" Ventouris-Roussos ( ; Greek: Αρτέμιος \"Ντέμης\" Βεντούρης-Ρούσσος , 15 June 1946 – 25 January 2015) was a Greek singer and performer who had international hit records as a solo performer in the 1970s after having been a member of Aphrodite's Child, a progressive rock group that also included Vangelis.\n\nAphrodite's Child: Aphrodite's Child was a Greek progressive rock band formed in 1967, by Vangelis Papathanassiou (keyboards), Demis Roussos (bass guitar and vocals), Loukas Sideras (drums and vocals), and Silver Koulouris (guitar).\n\nGepy &amp; Gepy: Giampiero Scalamogna (13 June 1943 – 3 July 2010), best known as Gepy & Gepy, was an Italian singer, songwriter, producer and arranger.  For his powerful voice visually combined to his robust physique he was paired to Barry White and Demis Roussos.\n\nNelly Mazloum: Nelly Mazloum (9 June 1929 - 21 February 2003), an Egyptian of Italian and Albanian origin, was an actress, choreographer, dancer, and teacher of ballet, modern dance, Egyptian folkloric dance, traditional oriental dance and the creator of the oriental dance technique.  She was a pioneer, in that she was the first to apply Egypt's traditional legacy of Folkloric Dances into a dramatised artistic form.  Known for her sense of humour, she was known in Egypt in the 1930s as a child prodigy and from the 1940syo the 1960s for her many appearances in Egyptian films, her folkloric shows on Egyptian TV, and her company the \"Nelly Mazloum Arabic Troupe of Dancers\".  She is mother of singer Demis Roussos with Albanian origin.\n\nOn écrit sur les murs: \"On écrit sur les murs\" (English: \"We write on the walls\") is a song by Demis Roussos from the album \"On écrit sur les murs\" (1988).  It was written by Romano Musumarra and Jean-Marie Moreau.  The song was adapted by Worlds Apart in 2007 and by Kids United in 2015 on the album \"Un monde meilleur\".  In two different years, les Enfoirés adapted that song & so did RAFFY in 2016.  The song had been rewritten as On Dessine Sur les Murs (WE draw on the walls); a Despicable Me minion version.\n\nTim Howar: Tim Howar (born 24 November 1969 in Spirit River, Alberta) is a Canadian actor, singer and dancer, known as a London-based rock vocalist with Mike + The Mechanics.\n\nThirsty Work: Thirsty Work is the twenty-first studio album by English Rock band Status Quo.  It yielded three hit singles, \"I Didn't Mean It\" (No. 21), \"Sherri Don't Fail Me Now\" (No. 38), and the uncharacteristic ballad \"Restless\" (No. 39).  \"Sorry\" had originally been recorded by Demis Roussos and released on his 1980 album \"Man of the World\", with Francis Rossi and Bernie Frost on all instruments and backing vocals.\n\nNorbert Daum: Daum was born in Braunau am Inn.  He studied the violin, guitar, and piano as well as composition and conducting.  Between 1965 and 1971, he was a member of the beat band The Substitutes.  Since 1971, Daum has lived in Munich, where he met composer and producer Ralph Siegel, for whom he wrote orchestrations in countless productions.  As a freelancer, Daum wrote more than 3000 orchestrations and worked with numerous artists in all genres, varying from crossover and outright classical music to German folk music and with artists such as Vicky Leandros, Karel Gott, Demis Roussos, and Die Jungen Tenöre.  He arranged Gilbert Bécaud’s 1985 French chart success ‘Desiree’.  He also worked in film and television music.\n\nQuestion: Who known as a London-based rock vocalist with Mike + The Mechanics, Tim Howar or Demis Roussos?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who is the London-based rock vocalist with Mike + The Mechanics.\"\n    },\n    \"role\": {\n      \"type\": \"string\",\n      \"description\": \"The specific role or description of the person within the band.\"\n    },\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band the person is associated with.\"\n    },\n    \"is_correct_person\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if this person is the correct answer to the question.\"\n    },\n    \"other_person_mentioned\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the other person mentioned in the question.\"\n    },\n    \"other_person_association_with_band\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the other person mentioned is associated with the specified band based on the context.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"role\",\n    \"band_name\",\n    \"is_correct_person\",\n    \"other_person_mentioned\",\n    \"other_person_association_with_band\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who is the London-based rock vocalist with Mike + The Mechanics."
      },
      "role": {
        "type": "string",
        "description": "The specific role or description of the person within the band."
      },
      "band_name": {
        "type": "string",
        "description": "The name of the band the person is associated with."
      },
      "is_correct_person": {
        "type": "boolean",
        "description": "Indicates if this person is the correct answer to the question."
      },
      "other_person_mentioned": {
        "type": "string",
        "description": "The name of the other person mentioned in the question."
      },
      "other_person_association_with_band": {
        "type": "boolean",
        "description": "Indicates if the other person mentioned is associated with the specified band based on the context."
      }
    },
    "required": [
      "person_name",
      "role",
      "band_name",
      "is_correct_person",
      "other_person_mentioned",
      "other_person_association_with_band"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
