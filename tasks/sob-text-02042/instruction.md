{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPrinz Louis Ferdinand: Prinz Louis Ferdinand is a 1927 German silent historical film directed by Hans Behrendt and starring Kurt Junker, Christa Tordy, Hans Stüwe and Jenny Jugo.  It was based on the life of Prince Louis Ferdinand of Prussia (1772–1806).  It was part of the series of Prussian films made during Weimar Germany.\n\nThe New Land (1924 film): The New Land (German:Neuland) is a 1924 German silent historical film directed by Hans Behrendt and starring Otto Gebühr, Reinhold Schünzel and Aud Egede-Nissen.  It depicts the discovery of the Americas by Christopher Columbus.  It premiered in Berlin on 12 August 1924.\n\nDanton (1931 film): Danton is a 1931 German historical drama film directed by Hans Behrendt and starring Fritz Kortner, Lucie Mannheim and Gustaf Gründgens.  It depicts the dramatic downfall and execution of Georges Danton in 1794 at the hands of Maximilien Robespierre.\n\nWedding at Lake Wolfgang: Wedding at Lake Wolfgang (German: Hochzeit am Wolfgangsee) is a 1933 German musical film directed by Hans Behrendt and starring Hugo Schrader, Gustl Gstettenbaur and Oskar Sima.  Made at the end of the Weimar Republic it had release problems due to Nazi objections to the film's Jewish director.\n\nKohlhiesel's Daughters (1930 film): Kohlhiesel's Daughters (German: Kohlhiesels Töchter) is a 1930 German comedy film directed by Hans Behrendt and starring Henny Porten, Fritz Kampers and Leo Peukert.  It is an adaptation of the play \"Kohlhiesel's Daughters\" by Hanns Kräly, which has been made into a number of films.  The film was a significant success at the box office, establishing the silent actress Porten as a sound star.  Porten plays the role of twin sisters, one of whom is vicacious and the other unpleasant.\n\nThe Heath Is Green (1932 film): The Heath Is Green (German: Grün ist die Heide) is a 1932 German musical film directed by Hans Behrendt and starring Camilla Spira, Peter Voß and Theodor Loos.  Three men go on holiday to a cabin in the middle of a heath.  Soon growing bored they venture out to investigate their surroundings.\n\nScott Sanders (director): Scott Sanders is an American screenwriter and film director.  He is best known for his work with the films \"Black Dynamite\" and \"Thick as Thieves\".\n\nFräulein Lilli: Fräulein Lilli or Miss Lilli is a 1936 Austrian comedy film directed by Hans Behrendt, Robert Wohlmuth and Max Neufeld.  It starred Franciska Gaal, Hans Jaray and S.Z. Sakall.  It was Gaal's last European film, although she did briefly start work in 1946 on \"Renee XIV\", before it was abandoned during filming.\n\nHans Behrendt: Hans Behrendt (28 September 1889 – 1942) was a German actor, screenwriter and film director.\n\nThe Trousers: The Trousers (German:Die Hose) is a 1927 German silent comedy film directed by Hans Behrendt and starring Werner Krauss, Jenny Jugo and Rudolf Forster.  It was based on a play by Carl Sternheim.  Art direction was by Heinrich Richter and Franz Schroedter.  The film is notable for the performance of Veit Harlan, later the director who made the controversial antisemitic \"Jew Suss\", as a Jewish barber in a film made by a director who would later died in the holocaust.\n\nQuestion: Hans Behrendt and Scott Sanders, have which mutual occupations?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person.\"\n    },\n    \"person_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person.\"\n    },\n    \"mutual_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of occupations shared by both individuals.\"\n    },\n    \"number_of_mutual_occupations\": {\n      \"type\": \"integer\",\n      \"description\": \"The count of mutual occupations found.\"\n    }\n  },\n  \"required\": [\n    \"person_1_name\",\n    \"person_2_name\",\n    \"mutual_occupations\",\n    \"number_of_mutual_occupations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1_name": {
        "type": "string",
        "description": "The name of the first person."
      },
      "person_2_name": {
        "type": "string",
        "description": "The name of the second person."
      },
      "mutual_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of occupations shared by both individuals."
      },
      "number_of_mutual_occupations": {
        "type": "integer",
        "description": "The count of mutual occupations found."
      }
    },
    "required": [
      "person_1_name",
      "person_2_name",
      "mutual_occupations",
      "number_of_mutual_occupations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
