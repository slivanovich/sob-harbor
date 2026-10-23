{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHawthorne (TV series): Hawthorne (sometimes stylized HawthoRNe) is an hour-long medical drama on the TNT television network starring Jada Pinkett Smith and Michael Vartan.  It premiered on June 16, 2009.  On Thursday, September 16, 2010, it was announced that \"Hawthorne\" has been renewed for a third and final season consisting of 10 episodes.  The third and final season of the show premiered on June 14, 2011, and ended on August 16, 2011.\n\nOne Hour Photo: One Hour Photo is a 2002 American psychological thriller film written and directed by Mark Romanek and starring Robin Williams, Connie Nielsen, Michael Vartan, Gary Cole, and Eriq La Salle.  Released by Fox Searchlight Pictures, \"One Hour Photo\" received positive reviews from film critics, with praise for Romanek's writing and Cronenweth's cinematography, while Williams' against-type performance received universal critical acclaim, earning him a Saturn Award for Best Actor.\n\nMichael Vaughn: Michael C. Vaughn is a fictional character on the television series \"Alias\".  Played by Michael Vartan, Vaughn is one of Sydney Bristow's co-workers and her ongoing love interest.  He, like Sydney, is skilled in a variety of areas.  His language abilities, shown in various episodes, include French, Spanish, Italian, and others.\n\nFiorile: Fiorile is a 1993 Italian drama film about a family curse caused by greed.  The film was directed by Paolo and Vittorio Taviani, and stars Claudio Bigagli, Galatea Ranzi, and Michael Vartan.  It was entered into the 1993 Cannes Film Festival.\n\nColombiana: Colombiana is a 2011 French action film co-written and produced by Luc Besson and directed by Olivier Megaton.  The French director's best known other movies are the actions films \"Transporter 3\", \"Taken 2\" and \"Taken 3\".  The film stars Zoe Saldana in the lead role with supporting roles by Michael Vartan, Cliff Curtis, Lennie James, Callum Blue, and Jordi Mollà.  \"Colombiana\" means a woman from Colombia, and is also a genus of orchids.  The film is about Cataleya (Amandla Stenberg), a nine-year-old girl in Colombia whose family is killed by drug lord named Don Luis Sandoval (Beto Benites).  Fifteen years later, a 24-year-old Cataleya (Zoe Saldana) has become an accomplished assassin.  Even though Don Luis is now in the witness protection program in the U.S. and is guarded by many heavily armed gangsters, Cataleya uses every means at her disposal, including death threats to law enforcement officials, to find where Don Luis is hiding and avenge her family's death.  While the film received a mixed reception from critics, with more negative reviews than positive reviews, Saldana's action sequences were praised and the movie earned $61 million against a $35 million budget.\n\nVartan Gregorian: Vartan Gregorian (Armenian: Վարդան Գրիգորեան ; Persian: وارتان گرگوریان‎ ‎ , born April 8, 1934) is an Iranian-born Armenian-American academic, serving as the president of Carnegie Corporation of New York.\n\nMichael Vartan: Michael S. Vartan (born November 27, 1968) is a French-American actor, best known for his role as Michael Vaughn on the ABC television action drama \"Alias\" and also known for his role on the TNT medical drama \"Hawthorne\".\n\nThe Pallbearer: The Pallbearer is a 1996 American romantic comedy film co-written and directed by Matt Reeves and starring David Schwimmer, Gwyneth Paltrow, Toni Collette, Michael Vartan, Michael Rapaport, and Barbara Hershey.  It was screened in the Un Certain Regard section at the 1996 Cannes Film Festival.\n\nDemoted: Demoted is a 2011 American comedy film directed by J. B. Rogers and starring Michael Vartan, Sean Astin, Celia Weston and David Cross.\n\nDavid Hallyday: David Hallyday (born David Michael Benjamin Smet; 14 August 1966) is a French singer, songwriter and amateur sports car racer.  He was born in Boulogne-Billancourt and is the son of the French singers Sylvie Vartan and Johnny Hallyday.  David Hallyday is a first cousin of actor Michael Vartan.\n\nQuestion: In between Michael Vartan and Vartan Gregorian who is is a French-American actor?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who is a French-American actor.\"\n    },\n    \"actor_nationality\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The nationalities of the identified actor.\"\n    },\n    \"actor_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The profession of the identified actor.\"\n    },\n    \"other_person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the other person mentioned in the question.\"\n    },\n    \"other_person_nationality\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The nationalities of the other person.\"\n    },\n    \"other_person_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The profession of the other person.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"actor_nationality\",\n    \"actor_profession\",\n    \"other_person_name\",\n    \"other_person_nationality\",\n    \"other_person_profession\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the person who is a French-American actor."
      },
      "actor_nationality": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The nationalities of the identified actor."
      },
      "actor_profession": {
        "type": "string",
        "description": "The profession of the identified actor."
      },
      "other_person_name": {
        "type": "string",
        "description": "The name of the other person mentioned in the question."
      },
      "other_person_nationality": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The nationalities of the other person."
      },
      "other_person_profession": {
        "type": "string",
        "description": "The profession of the other person."
      }
    },
    "required": [
      "actor_name",
      "actor_nationality",
      "actor_profession",
      "other_person_name",
      "other_person_nationality",
      "other_person_profession"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
