{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nShahid Hussain Bhutto: Shahid Hussain Bhutto is a Pakistani politician who served as member of the National Assembly of Pakistan.\n\nShahid Hussain: Shahid Hussain (born 29 December 1970) is a Pakistani former cricketer.  He played 78 first-class and 37 List A matches for several domestic teams in Pakistan between 1986 and 1998.\n\nShahid Balkhi: Abul Hasan Shahid ibn Hussain Jahudanaki Balkhi (Persian: ابوالحسن شهيدبن حسين جهودانکي بلخی‎ ‎ ) (died, 325 AH - 935) was a Persian theologian, philosopher, poet and sufi.  Famous Persian poet Rudaki has a poem in Balkhi's elegy.  He was born in Balkh.  Shahid Balkhi was contemporary to Ahmed ibn Sahl al-Balkhi and they had connections.  He also had conversations with Zakariya al-Razi, the well-known Persian polymath and both had objections toward the nature of the pleasure.\n\nDespoina: In Greek mythology, Despoina, Despoena or Despoine, was the daughter of Demeter and Poseidon and sister of Arion.  She was the goddess of mysteries of Arcadian cults worshipped under the title \"Despoina\", \"the mistress\" alongside her mother Demeter, one of the goddesses of the Eleusinian mysteries.  Her real name could not be revealed to anyone except those initiated to her mysteries.  Pausanias spoke of Demeter as having two daughters; Kore being born first, then later Despoina.  With Zeus being the father of Kore, and Poseidon as the father of Despoina.  Pausanias made it clear that Kore is Persephone, though he wouldn't reveal Despoina's proper name.\n\nWale Adebanwi: Professor Wale Adebanwi, (born 1969), is a Nigerian - born first Black African Rhodes Professor at Oxford University\n\nZahra Shahid Hussain: Zahra Shahid Hussain (Urdu: ‎ ) commonly known as Zara Apa, was a Pakistani activist-politician, teacher and the senior vice president of Imran Khan's Pakistan Tehreek-e-Insaf (PTI) in Sindh.  She had formerly served as the president of women's wing of the party in Sindh, and was a member of the central executive committee of the party.  On 18 May 2013, she was assassinated outside her house in the upscale Defence Housing Authority neighborhood in Karachi.\n\nShahid Hussain Bokhari: Shahid H. Bokhari (born 17 January 1952 in Lahore, Pakistan ) is a highly cited Pakistani researcher in the field of parallel and distributed computing.  He is a fellow of both IEEE and ACM.  Bokhari's ACM Fellow citation states that he received the award for his \"research contributions to automatic load balancing and partitioning of distributed processes\", while his IEEE Fellow award recognises his \"contributions to the mapping problem in parallel and distributed computing\".\n\nAl-Nayrizi: Abū’l-‘Abbās al-Faḍl ibn Ḥātim al-Nairīzī (Arabic: أبو العباس الفضل بن حاتم النيريزي‎ ‎ , Latin: \"Anaritius, Nazirius\" , 865–922) was a Persian mathematician and astronomer from Nayriz, Fars Province, Iran.\n\nShahid Hussain Bhatti: Shahid Hussain Bhatti (Urdu: ‎ ) is a Pakistani politician who is currently a member of the National Assembly of Pakistan, belonging to the Pakistan Muslim League (N).\n\nAugustine of Canterbury: Augustine of Canterbury (born first third of the 6th century – died probably 26 May 604) was a Catholic Benedictine monk who became the first Archbishop of Canterbury in the year 597.  He is considered the \"Apostle to the English\" and a founder of the Catholic Church in England.\n\nQuestion: Between Al-Nayrizi and Shahid Hussain Bokhari, who was born first?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_a_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person being compared.\"\n    },\n    \"person_a_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the first person.\"\n    },\n    \"person_b_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person being compared.\"\n    },\n    \"person_b_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the second person.\"\n    },\n    \"earlier_born_person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who was born first.\"\n    },\n    \"comparison_statement\": {\n      \"type\": \"string\",\n      \"description\": \"A statement comparing the birth years of the two individuals.\"\n    }\n  },\n  \"required\": [\n    \"person_a_name\",\n    \"person_a_birth_year\",\n    \"person_b_name\",\n    \"person_b_birth_year\",\n    \"earlier_born_person_name\",\n    \"comparison_statement\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_a_name": {
        "type": "string",
        "description": "The name of the first person being compared."
      },
      "person_a_birth_year": {
        "type": "integer",
        "description": "The birth year of the first person."
      },
      "person_b_name": {
        "type": "string",
        "description": "The name of the second person being compared."
      },
      "person_b_birth_year": {
        "type": "integer",
        "description": "The birth year of the second person."
      },
      "earlier_born_person_name": {
        "type": "string",
        "description": "The name of the person who was born first."
      },
      "comparison_statement": {
        "type": "string",
        "description": "A statement comparing the birth years of the two individuals."
      }
    },
    "required": [
      "person_a_name",
      "person_a_birth_year",
      "person_b_name",
      "person_b_birth_year",
      "earlier_born_person_name",
      "comparison_statement"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
