{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1993 Stockholm Open: The 1993 Stockholm Open was a men's tennis tournament played on indoor hard courts.  It was the 25th edition of the Stockholm Open and was part of the ATP Super 9 of the 1993 ATP Tour.  It took place at the Stockholm Globe Arena in Stockholm, Sweden, from 25 October through 1 November 1993.\n\n25th Mountain Battery: The 25th Mountain Battery was an artillery battery of the British Indian Army.  Raised in 1827, as the Bombay Foot Artillery, the 25th is the oldest Indian Mountain Battery, and the only one that served in the Second Sikh War at the Siege of Multan.  The 25th was also the first Battery to serve outside India, when it took part in the 1868 Expedition to Abyssinia.  They next took part in the Second Burmese War.  In 1896, the Battery was back in Africa, taking part in the Battle of Suakin in the Sudan Campaign.  By 1897, the Battery had returned to the Frontier, and served in the Second Division of the Tirah Campaign.  In World War I, The 25th served on the Frontier, the Persian Seistan Cordon in 1917 and during the last mopping up operations in the Mesopotamia Campaign in 1917–1918.  During the inter-war years, the 25th only saw active service against the Fakir of Ipi in the Waziristan campaign 1936–1939.\n\nPremonition (2006 film): Premonition (French: Le Pressentiment ) is a 2006 French drama film directed by and starring Jean-Pierre Darroussin, and based on the novel \"Le Pressentiment\" by Emmanuel Bove.  It won the Louis Delluc Prize for Best First Film in 2006 and the award for Best First French Film from the French Syndicate of Cinema Critics in 2007.\n\nMohan Krishna Indraganti: Mohana Krishna Indraganti is an Indian film director known for his works predominantly in Telugu cinema.  His debut directorial venture \"Grahanam\" (2005) fetched him eleven awards including the National Film Award for Best First Film of a Director, the Nandi Award for Best First Film of a Director and the Gollapudi Srinivas Award for Best First Film of a Director.  The film was also showcased in the Indian panorama section of the 2005 International Film Festival of India.  He holds a Master of Fine Arts degree from York University.\n\nIt's Easier for a Camel...: It's Easier for a Camel... (French: Il est plus facile pour un chameau... ) is a 2003 French comedy film written, directed by and starring Valeria Bruni Tedeschi.  It was entered into the 25th Moscow International Film Festival.  It won the Louis Delluc Prize for Best First Film in 2003.\n\nAll Is Forgiven (film): All Is Forgiven (French: Tout est pardonné ) is a 2007 French drama film written and directed by Mia Hansen-Løve.  It was screened in the Directors’ Fortnight section of the 2007 Cannes Film Festival.  It won the Louis Delluc Prize for Best First Film.  It was also nominated for the César Award for Best First Feature Film at the 2008 César Awards.\n\nThe Silent Holy Stones: The Silent Holy Stones () is a 2006 Tibetan feature film written and directed by Pema Tseden.  \"The Silent Holy Stones\" is about the tale of a young Lama who comes from a remote monastery is enthusiastic about life, eager to learn, and curious about everything.  The film won the Best Directorial Debut at the 25th Golden Rooster Awards, Asian New Talent Award for Best Director at the 8th Changchun Film Festival, and Best First Feature at the 13th Beijing College Student Film Festival.  The film was released on June 1, 2006, in China.\n\n25th Battalion (Australia): The 25th Battalion was an infantry unit of the Australian Army.  Raised in early 1915 as part of the Australian Imperial Force during the First World War, the battalion fought at Gallipoli and in the trenches along the Western Front, before being disbanded in early 1919.  In mid-1921, it was re-formed as a part-time unit based in the state of Queensland.  Throughout the 1930s, the battalion was merged briefly with the 49th Battalion as a result of manpower shortages, but was later re-raised in its own right.  During the Second World War, the 25th deployed to New Guinea where they fought the Battle of Milne Bay in August and September 1942.  Later in the war, the 25th took part in the Bougainville Campaign.  During the post-war period, the 25th Battalion became part of the Royal Queensland Regiment, variously forming battalion or company-sized elements, before being merged with the 49th Battalion to form the 25th/49th Battalion, Royal Queensland Regiment.\n\nJuly Jung: Jung Joo-ri (born 1980), also known as July Jung, is a South Korean film director and screenwriter.  Jung's directorial debut feature \"A Girl at My Door\" won the Best First Film at the 25th Stockholm International Film Festival.  She also won the Best New Director at the 23rd Buil Film Awards and Best Director/Screenwriter at the 15th Women in Film Korea Awards in 2014, and Best Screenplay at the 2nd Wildflower Film Awards and Best New Director for film at the 51st Baeksang Arts Awards in 2015.\n\nA Girl at My Door: A Girl at My Door () is a 2014 South Korean drama film directed by July Jung and stars Bae Doona as a policewoman who takes in an abused girl played by Kim Sae-ron.  The film screened in the Un Certain Regard section at the 2014 Cannes Film Festival.\n\nQuestion: Who starred in the film that won the Best First Film at the 25th Stockholm?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film that won the award.\"\n    },\n    \"award_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the award won by the film.\"\n    },\n    \"award_edition\": {\n      \"type\": \"integer\",\n      \"description\": \"The edition number of the film festival or award.\"\n    },\n    \"award_festival\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film festival where the award was presented.\"\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of actors who starred in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"award_name\",\n    \"award_edition\",\n    \"award_festival\",\n    \"starring_actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film that won the award."
      },
      "award_name": {
        "type": "string",
        "description": "The name of the award won by the film."
      },
      "award_edition": {
        "type": "integer",
        "description": "The edition number of the film festival or award."
      },
      "award_festival": {
        "type": "string",
        "description": "The name of the film festival where the award was presented."
      },
      "starring_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of actors who starred in the film."
      }
    },
    "required": [
      "film_title",
      "award_name",
      "award_edition",
      "award_festival",
      "starring_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
