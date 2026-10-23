{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGreat Plague of Marseille: The Great Plague of Marseille was the last of the significant European outbreaks of bubonic plague.  Arriving in Marseille, France in 1720, the disease killed 100,000 people in the city and the surrounding provinces.  However, Marseille recovered quickly from the plague outbreak.  Economic activity took only a few years to recover, as trade expanded to the West Indies and Latin America.  By 1765, the growing population was back at its pre-1720 level.\n\nPaneriai: Paneriai (Polish: \"Ponary\" , Yiddish: פאנאר‎ /Ponar) is a neighborhood of Vilnius, situated about 10 kilometres away from the city center.  It is the largest elderate in the Vilnius city municipality.  It is located on low forested hills, on the Vilnius-Warsaw road.  Paneriai was the site of the Ponary massacre, a mass killing of as many as 100,000 people from Vilnius and nearby towns and villages during World War II.\n\nNazi hunter: A Nazi hunter is a private individual who tracks down and gathers information on alleged former Nazis, SS members, and Nazi collaborators who were involved in the Holocaust, typically for use at trial on charges of war crimes and crimes against humanity.  Prominent Nazi hunters include Simon Wiesenthal, Tuviah Friedman, Serge and Beate Klarsfeld, Ian Sayer, Yaron Svoray, Elliot Welles, and Efraim Zuroff.\n\nPonary massacre: The Ponary massacre (Polish: \"zbrodnia w Ponarach\" ) was the mass murder of up to 100,000 people by German SD, SS and Lithuanian Nazi collaborators, such as the Ypatingasis būrys units,\n\nHenneicke Column: The Henneicke Column was a group of Dutch Nazi collaborators working in the investigative division of the \"Central Bureau for Jewish Emigration\" (Zentralstelle für jüdische Auswanderung), with headquarters in Amsterdam, during the Nazi Germany occupation of the Netherlands in World War II .\n\nThe Holocaust in Latvia: The Holocaust in Latvia refers to the war crimes of Nazis and Nazi collaborators victimizing Jews during the occupation of Latvia by Nazi Germany.\n\nThe Darkroom of Damocles: The Darkroom of Damocles (Dutch: De donkere kamer van Damokles ) is a war novel by the Dutch writer Willem Frederik Hermans, published in 1958.  Osewoudt, an Amsterdam cigar store owner living under the Nazi occupation, makes his acquaintance with the mysterious Dorbeck, who claims to be involved in the Resistance movement.  Dorbeck enlists Osewoudt for dangerous attacks on the Gestapo and Dutch Nazi collaborators.  After the Nazi defeat Dorbeck has disappeared, though Osewoudt needs him to prove his involvement.  An immediate success since it was first published, the novel has been printed in numerous editions and is one of the greatest World War II novels.  The book has been translated into English twice, in 1962 by Roy Edwards, and again in 2007 by Ina Rilke.  It was adapted into the 1963 film \"Like Two Drops of Water\", directed by Fons Rademakers.\n\nGlinciszki massacre: The Glinciszki massacre was a mass murder of Polish civilians by the Nazi-subordinated Lithuanian Auxiliary Police Battalion, committed on 20 June 1944 in the village of Glinciszki (now Glitiškės, Vilnius District Municipality, Lithuania) during the occupation of Poland in World War II.  In the massacre, 39 hostages died, including 11 women (one in advanced stage of pregnancy), 11 children (some as young as 3 years old), and 6 elderly men.  They were executed as a collective punishment for the death of four Lithuanian Nazi policemen on the previous evening, during the skirmish with the Polish resistance units of the 5th Brigade of Armia Krajowa commanded by Lieutenant Wiktor Wiącki.  The massacre triggered an act of reprisal by the Polish partisans against Lithuanian civilians in Dubingiai two days later.\n\nThe Holocaust: The Holocaust, also referred to as the Shoah, was a genocide in which Adolf Hitler's Nazi Germany and its World War II collaborators killed some six million European Jews.  The victims included 1.5 million children and constituted about two-thirds of the nine million Jews in Continental Europe.  A broader definition of the Holocaust includes non-Jewish victims such as the Roma, ethnic Poles, other Slavic ethnic groups, and the disabled and mentally ill.  An even broader definition includes Soviet citizens and prisoners of war, homosexuals, Jehovah's Witnesses, black people, and political opponents of the Nazis.\n\nDubingiai massacre: The Dubingiai massacre was a mass murder of 20–27 Lithuanian civilians in the town of Dubingiai (Dubinki) on 23 June 1944.  The massacre was carried out by the 5th Brigade of Armia Krajowa (AK), a Polish resistance group, in a reprisal for the Glinciszki (Glitiškės) massacre of 20 June.  The Dubingiai massacre started a wider AK operation in which units beyond the 5th Brigade were involved.  In total, 70–100 Lithuanians were killed by the end of June 1944 in Dubingiai and the neighbouring villages of Joniškis, Inturkė, Bijutiškis, and Giedraičiai.  While Nazi collaborators were ostensibly the prime targets, the victims included the elderly, children, and even infants.  Further conflicts between Lithuanian and Polish units were prevented by the Soviet capture of Vilnius in mid-July.\n\nQuestion: What was the name of the famous event where Lithuanian Nazi collaborators killed 100,000 in Paneriai?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the historical event.\"\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The primary location where the event took place.\"\n    },\n    \"number_of_victims\": {\n      \"type\": \"integer\",\n      \"description\": \"The approximate number of people killed in the event.\"\n    },\n    \"perpetrators\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Groups identified as responsible for the event.\"\n    }\n  },\n  \"required\": [\n    \"event_name\",\n    \"location\",\n    \"number_of_victims\",\n    \"perpetrators\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_name": {
        "type": "string",
        "description": "The name of the historical event."
      },
      "location": {
        "type": "string",
        "description": "The primary location where the event took place."
      },
      "number_of_victims": {
        "type": "integer",
        "description": "The approximate number of people killed in the event."
      },
      "perpetrators": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Groups identified as responsible for the event."
      }
    },
    "required": [
      "event_name",
      "location",
      "number_of_victims",
      "perpetrators"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
