{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLe Vin de solitude: Le Vin de solitude, published in English as The Wine of Solitude, is a novel by Russian Jewish author Irène Némirovsky (1903 – 1942), who died in the Holocaust.  It is considered to be partly autobiographical and tells the story of the protagonist, Hélène Karol, who shares much of Némirovsky's early history.  \"Le Vin de solitude\" was originally published in France in 1935.  Following the success of Némirovsky's posthumously published work \"Suite Française\" in 2004, it was translated and published in English in 2011.\n\nSuite Française (film): Suite Française is a 2015 British-French-Belgian romantic World War II drama film directed by Saul Dibb and co-written with Matt Charman.  It is based on the second part of Irène Némirovsky's 2004 novel of the same name.  The film stars Michelle Williams, Kristin Scott Thomas, Matthias Schoenaerts, Sam Riley, Ruth Wilson, Lambert Wilson and Margot Robbie.  It concerns a romance between a French villager and a German soldier during the early years of the German occupation of France.  \"Suite Française\" was filmed on location in France and Belgium.  It was released theatrically in the UK on 13 March 2015 and will premiere in the US through Lifetime cable network on 22 May 2017.\n\nSuite française (Némirovsky novel): Suite française (] , \"French Suite\") is the title of a planned sequence of five novels by Irène Némirovsky, a French writer of Ukrainian-Jewish origin.  In July 1942, having just completed the first two of the series, Némirovsky was arrested as a Jew and detained at Pithiviers and then Auschwitz, where she was murdered, a victim of the Holocaust.  The notebook containing the two novels was preserved by her daughters but not examined until 1998.  They were published in a single volume entitled \"Suite française\" in 2004.\n\nSusan Straight: Susan Straight (born October 19, 1960) is an American writer.  She was a National Book Award finalist for the novel \"Highwire Moon\" in 2001.\n\nIrène Némirovsky: Irène Némirovsky (] ; 24 February 1903 – 17 August 1942) was a novelist of Ukrainian Jewish origin born in Kiev Ukraine under the Russian Empire; she lived more than half her life in France and wrote in French, but was denied French citizenship.  Arrested as a Jew under the racial laws – which did not take into account her conversion to Roman Catholicism – she died at Auschwitz at the age of 39.  Successful in her day, she is now best known for the posthumously published \"Suite française.\n\nJonathan M. Weiss: Jonathan Mark Weiss (born May 3, 1942) is an American scholar of French literature and social science whose extensive publications include literary and theatre criticism, essays on Franco-American relations, a short story, and most recently the biography of Irène Némirovsky.\n\nLe Bal (novella): Le Bal is the title of collection of 2 novellas written by Irène Némirovsky.  Published in France in 1930, it has been recently re-issued, due to the increasing interest in and popularity of the author's work, following the discovery and publication of Suite Française.\n\nDavid Golder (film): David Golder is a 1931 French drama film directed by Julien Duvivier and starring Harry Baur, Paule Andral and Jackie Monnier.  It is an adaptation of Irène Némirovsky's 1929 novel \"David Golder\", about a self-made Jewish businessman.\n\nDavid Golder: David Golder is writer Irène Némirovsky's first novel.  It was re-issued in 2004 following the popularity of the Suite Française notebooks discovered in 1998.  \"David Golder\" was first published in France in 1929 and won instant acclaim for the 26-year-old author.\n\nPithiviers internment camp: Pithiviers internment camp was a Nazi transit camp in Pithiviers, France during the Second World War.  Children were separated there from their parents; the adults were processed and deported to concentration camps farther away, usually Auschwitz.  This was the fate of the novelist Irène Némirovsky.\n\nQuestion: Who was denied French Citizenship, Susan Straight or Irène Némirovsky?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_denied_citizenship\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who was denied citizenship.\"\n    },\n    \"country_of_citizenship_denied\": {\n      \"type\": \"string\",\n      \"description\": \"The country whose citizenship was denied.\"\n    },\n    \"citizenship_status_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the citizenship status for the identified person.\"\n    },\n    \"other_person_in_question\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the other person mentioned in the question.\"\n    },\n    \"other_person_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the other person mentioned in the question.\"\n    }\n  },\n  \"required\": [\n    \"person_denied_citizenship\",\n    \"country_of_citizenship_denied\",\n    \"citizenship_status_description\",\n    \"other_person_in_question\",\n    \"other_person_nationality\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_denied_citizenship": {
        "type": "string",
        "description": "The name of the person who was denied citizenship."
      },
      "country_of_citizenship_denied": {
        "type": "string",
        "description": "The country whose citizenship was denied."
      },
      "citizenship_status_description": {
        "type": "string",
        "description": "A description of the citizenship status for the identified person."
      },
      "other_person_in_question": {
        "type": "string",
        "description": "The name of the other person mentioned in the question."
      },
      "other_person_nationality": {
        "type": "string",
        "description": "The nationality of the other person mentioned in the question."
      }
    },
    "required": [
      "person_denied_citizenship",
      "country_of_citizenship_denied",
      "citizenship_status_description",
      "other_person_in_question",
      "other_person_nationality"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
