{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Fog of War: The Fog of War: Eleven Lessons from the Life of Robert S. McNamara is a 2003 American documentary film about the life and times of former U.S. Secretary of Defense Robert S. McNamara illustrating his observations of the nature of modern warfare.  The film was directed by Errol Morris and features an original score by Philip Glass.  The title derives from the military concept of the \"fog of war\" depicting the difficulty of making decisions in the midst of conflict.\n\nHedgehog in the Fog: Hedgehog in the Fog (Russian: Ёжик в тумане , \"Yozhik v tumane\"; ] ) is a 1975 Soviet animated film directed by Yuriy Norshteyn, produced by the Soyuzmultfilm studio in Moscow.  The Russian script was written by Sergei Kozlov, who also published a book under the same name.  In 2006, Norshteyn published a book titled Hedgehog in the Fog, listing himself as an author alongside Kozlov.\n\nThe Fog (2005 film): The Fog is a 2005 American supernatural horror film directed by Rupert Wainwright and starring Tom Welling, Selma Blair and Maggie Grace.  It is a remake of John Carpenter's 1980 film of the same name and was produced by Carpenter and Debra Hill who co-wrote the original film.  The film's narrative follows a strange fog that sweeps in over an island town in the coast of Oregon; it brings vindictive apparitions of mariners who were murdered there 134 years prior.  The townspeople find themselves trapped and fighting for their lives while investigating the truth of their history.\n\nTyson Hesse: Tyson Hesse is an American graphic novel illustrator and animator, best known for his work on the \"Sonic the Hedgehog\" comic series from Archie Comics.  A longtime fan of the franchise, he also lead the creation of the animated cutscenes for the 2017 platform game, \"Sonic Mania\".  Hesse is the creator of the webcomic, \"Diesel\", and serves as writer and artist for the webcomic's follow-up graphic novel, \"Diesel: Ignition\".\n\nYuriy Norshteyn: Yuriy Borisovich Norshteyn, PAR (Russian: Ю́рий Бори́сович Норште́йн ), or Yuri Norstein (born 15 September 1941), is a Soviet and Russian animator best known for his animated shorts, \"Hedgehog in the Fog\" and \"Tale of Tales\".  Since 1981 he has been working on a feature film called \"The Overcoat\", based on the short story by Nikolai Gogol of the same name.  According to the \"Washington Post\", \"He is considered by many to be not just the best animator of his era, but the best of all time\".\n\nNight and Fog (1956 film): Night and Fog (French: \"Nuit et brouillard\" ) is a 1956 French documentary short film.  Directed by Alain Resnais, it was made ten years after the liberation of Nazi concentration camps.  The title is taken from the notorious \"Nacht und Nebel\" (German for \"Night and Fog\") program of abductions and disappearances decreed by the Nazis on 7 December 1941.\n\nThe Fog: The Fog (also known as John Carpenter's The Fog) is a 1980 American horror film directed by John Carpenter, who also co-wrote the screenplay and created the music for the film.  It stars Adrienne Barbeau, Jamie Lee Curtis, Tom Atkins, Janet Leigh and Hal Holbrook.  It tells the story of a strange, glowing fog that sweeps in over a small coastal town in California, bringing with it the vengeful ghosts of mariners who were killed in a shipwreck there exactly 100 years before.\n\nPeter Foldes: Peter Foldes (22 August 1924 in Budapest, Hungary – 29 March 1977 in Paris) was a director and animator of British nationality.\n\nErroneous reporting on the 2008 Mumbai attacks: During and immediately after the 2008 Mumbai attacks the news media worldwide broadcast incorrect factual information on a scale often seen in a fog of war.  Erroneous reporting on the 2008 Mumbai attacks included false information concerning the number of attackers, their nationality, their organizational affiliations, origins, and the methods of transport they had used.  Theories and speculations were openly aired by various commentators that were later proved to be wrong.  Many such speculations, such as the involvement in the attacks of the \"Deccan Mujahideen\", were widely reported by media worldwide.  Various news outlets carried opinion pieces and unattributed theories about the origins of the attackers which were unfounded.\n\nThe Hedgehog: The Hedgehog (\"Le Hérisson\") is a French film directed by Mona Achache, loosely based on the novel \"The Elegance of the Hedgehog\" by Muriel Barbery.  Made in 2008, the film was released in theatres in 2009.\n\nQuestion: Hedgehog in the Fog is directed by the animator of what nationality?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"director_nationalities\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of nationalities of the director.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"director_name\",\n    \"director_nationalities\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "director_nationalities": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of nationalities of the director."
      }
    },
    "required": [
      "film_title",
      "director_name",
      "director_nationalities"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
