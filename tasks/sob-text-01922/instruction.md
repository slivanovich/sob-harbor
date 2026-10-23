{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNobel Prize in Literature: Since 1901, the Nobel Prize in Literature (Swedish: \"Nobelpriset i litteratur\" ) has been awarded annually to an author from any country who has, in the words of the will of Alfred Nobel, produced \"in the field of literature the most outstanding work in an ideal direction\" (original Swedish: \"den som inom litteraturen har producerat det mest framstående verket i en idealisk riktning\").  Though individual works are sometimes cited as being particularly noteworthy, here \"work\" refers to an author's work as a whole.  The Swedish Academy decides who, if anyone, will receive the prize in any given year.  The academy announces the name of the chosen laureate in early October.  It is one of the five Nobel Prizes established by the will of Alfred Nobel in 1895; the others are the Nobel Prize in Chemistry, Nobel Prize in Physics, Nobel Peace Prize, and Nobel Prize in Physiology or Medicine.\n\nStern–Gerlach Medal: The Stern–Gerlach Medal is the most prestigious German Award for experimental physicists, named after the scientists of the Stern–Gerlach experiment, Otto Stern and Walther Gerlach.\n\nNobel Prize in Physics: The Nobel Prize in Physics (Swedish: \"Nobelpriset i fysik\" ) is a yearly award given by the Royal Swedish Academy of Sciences for those who conferred the most outstanding contributions for mankind in the field of physics.  It is one of the five Nobel Prizes established by the will of Alfred Nobel in 1895 and awarded since 1901; the others being the Nobel Prize in Chemistry, Nobel Prize in Literature, Nobel Peace Prize, and Nobel Prize in Physiology or Medicine.\n\nList of Nobel laureates in Chemistry: The Nobel Prize in Chemistry (Swedish: \"Nobelpriset i kemi\" ) is awarded annually by the Royal Swedish Academy of Sciences to scientists in the various fields of chemistry.  It is one of the five Nobel Prizes established by the 1895 will of Alfred Nobel, who died in 1896.  These prizes are awarded for outstanding contributions in chemistry, physics, literature, peace, and physiology or medicine.  As dictated by Nobel's will, the award is administered by the Nobel Foundation and awarded by a committee that consists of five members elected by the Royal Swedish Academy of Sciences.  The first Nobel Prize in Chemistry was awarded in 1901 to Jacobus Henricus van 't Hoff, of the Netherlands.  Each recipient receives a medal, a diploma and a monetary award prize that has varied throughout the years.  In 1901, van 't Hoff received 150,782 SEK, which is equal to 7,731,004 SEK in December 2007.  The award is presented in Stockholm at an annual ceremony on December 10, the anniversary of Nobel's death.\n\nOtto Stern: Otto Stern (17 February 1888 – 17 August 1969) was a German physicist and Nobel laureate in physics.  He was the second most nominated person for a Nobel Prize with 82 nominations in the years 1925–1945 (most times nominated is Arnold Sommerfeld with 84 nominations), ultimately winning in 1943.\n\nList of Nobel laureates by university affiliation: This list of Nobel laureates by university affiliation shows the university affiliations of winners of the Nobel Prize and the Nobel Memorial Prize in Economic Sciences since 1901 (total 881 individual laureates).  Although this list does not include organizations which were awarded the Nobel prize or any individuals in those organizations, a person who received the Nobel prize while working at a research organization formally affiliated with or operated by a university is counted as an affiliate of that university.  Universities are listed in descending order according to the number of affiliates, while only the top 50 universities are shown explicitly with their ranking.\n\nList of Danish Nobel laureates: This is a list of Danish Nobel laureates.  Since the Nobel Prize was established per the will of Swedish inventor Alfred Nobel in 1895, 12 of the prize winners have been from Denmark.  The first Danish Nobel laureate was Niels Ryberg Finsen, who won a Nobel Prize for medicine in 1903 for his work in using light therapy to treat diseases.  The most recent Danish Nobel Prize winner was Jens Skou who won the prize in chemistry for his discovery over the enzyme, Na+/K+-ATPase in 1997.  To date, of the 13 Nobel Prizes won by Danish people, 5 have been for medicine, 3 have been for physics, 3 have been for literature, 1 has been for chemistry and one has been for peace.\n\nAda Yonath: Ada E. Yonath (Hebrew: עדה יונת‎ ‎ , ] ) (born 22 June 1939) is an Israeli crystallographer best known for her pioneering work on the structure of the ribosome.  She is the current director of the Helen and Milton A. Kimmelman Center for Biomolecular Structure and Assembly of the Weizmann Institute of Science.  In 2009, she received the Nobel Prize in Chemistry along with Venkatraman Ramakrishnan and Thomas A. Steitz for her studies on the structure and function of the ribosome, becoming the first Israeli woman to win the Nobel Prize out of ten Israeli Nobel laureates, the first woman from the Middle East to win a Nobel prize in the sciences, and the first woman in 45 years to win the Nobel Prize for Chemistry.  However, she said herself that there was nothing special about a woman winning the Prize.\n\nRamón Menéndez Pidal: Ramón Menéndez Pidal (] ; 13 March 1869 - 14 November 1968) was a Spanish philologist and historian.  He worked extensively on the history of the Spanish language and Spanish folklore and folk poetry.  One of his main topics was the history and legend of El Cid.  He was nominated for a Nobel Prize 151 times, the most nominated person, three times more than the second most nominated person, André Malraux.\n\nList of Nobel laureates in Physiology or Medicine: The Nobel Prize in Physiology or Medicine (Swedish: \"Nobelpriset i fysiologi eller medicin\" ) is awarded annually by the Swedish Karolinska Institute to scientists and doctors in the various fields of physiology or medicine.  It is one of the five Nobel Prizes established by the 1895 will of Alfred Nobel (who died in 1896), awarded for outstanding contributions in chemistry, physics, literature, peace, and physiology or medicine.  As dictated by Nobel's will, the award is administered by the Nobel Foundation and awarded by a committee that consists of five members and an executive secretary elected by the Karolinska Institute.  While commonly referred to as the Nobel Prize in Medicine, Nobel specifically stated that the prize be awarded for \"physiology or medicine\" in his will.  Because of this, the prize can be awarded in a broader range of fields.  The first Nobel Prize in Physiology or Medicine was awarded in 1901 to Emil Adolf von Behring, of Germany.  Each recipient receives a medal, a diploma and a monetary award that has varied throughout the years.  In 1901, von Behring received 150,782 SEK, which is equal to 7,731,004 SEK in December 2008.  In 2013, the prize was awarded to James E. Rothman, Randy W. Schekman and Thomas C. Südhof; they were recognised \"after discovering how cells precisely transport material\".  The award is presented in Stockholm at an annual ceremony on December 10, the anniversary of Nobel's death.\n\nQuestion: What award is named after the second most nominated person for a Nobel Prize?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"award_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the award.\"\n    },\n    \"named_after_person\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the person after whom the award is named.\"\n    },\n    \"person_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"full_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the individual.\"\n        },\n        \"nobel_nominations_count\": {\n          \"type\": \"integer\",\n          \"description\": \"The total number of Nobel Prize nominations received by the person.\"\n        },\n        \"nobel_prize_winner\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the person won a Nobel Prize.\"\n        },\n        \"nobel_prize_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the person won the Nobel Prize, if applicable.\"\n        },\n        \"nobel_prize_category\": {\n          \"type\": \"string\",\n          \"description\": \"The category of the Nobel Prize won, if applicable.\"\n        }\n      },\n      \"required\": [\n        \"full_name\",\n        \"nobel_nominations_count\",\n        \"nobel_prize_winner\",\n        \"nobel_prize_year\",\n        \"nobel_prize_category\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"award_name\",\n    \"named_after_person\",\n    \"person_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "award_name": {
        "type": "string",
        "description": "The name of the award."
      },
      "named_after_person": {
        "type": "string",
        "description": "The full name of the person after whom the award is named."
      },
      "person_details": {
        "type": "object",
        "properties": {
          "full_name": {
            "type": "string",
            "description": "The full name of the individual."
          },
          "nobel_nominations_count": {
            "type": "integer",
            "description": "The total number of Nobel Prize nominations received by the person."
          },
          "nobel_prize_winner": {
            "type": "boolean",
            "description": "Indicates if the person won a Nobel Prize."
          },
          "nobel_prize_year": {
            "type": "integer",
            "description": "The year the person won the Nobel Prize, if applicable."
          },
          "nobel_prize_category": {
            "type": "string",
            "description": "The category of the Nobel Prize won, if applicable."
          }
        },
        "required": [
          "full_name",
          "nobel_nominations_count",
          "nobel_prize_winner",
          "nobel_prize_year",
          "nobel_prize_category"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "award_name",
      "named_after_person",
      "person_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
