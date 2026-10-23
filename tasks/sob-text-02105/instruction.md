{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMohammed Omer: Mohammed Omer (Arabic: محمد عمر‎ ‎ ), (born 1984) is a Palestinian journalist.  He has reported for numerous media outlets, including: The New York Times, the \"Washington Report on Middle East Affairs,\"; Al Jazeera; New Statesman; Pacifica Radio; Electronic Intifada; The Nation; Inter Press Service; Free Speech Radio News; Vermont Guardian; ArtVoice Weekly; the Norwegian Morgenbladet; and Dagsavisen;\n\nAbu Mohammed Saleh al-Magiri: Abu Mohammed Salih (also Silih) or Abu Mohammed Saleh ibn Yansaran Said ibn Gafiyan al-Doukkali al-Magiri (sometimes spelled al-Majiri) (1153–1234) was a Sufi leader from Morocco and one of the successors of Abu Madyan.  He was the patron saint of Safi and lived during the reign of the Almohad dynasty.  Born into a prominent family of Banu Majir Berbers from the hill country of southern Doukkala, later in his life he spent twenty years in Alexandria and, when he returned to Morocco, founded a ribat in Safi.  The Sufi brotherhood of the Magiriyyun derives from him.  He wrote a \"Talqin al-wird\" and the ribat in Safi, where Abou Mohammed was buried, continued to play an important role until the end of the 15th century.  One of Salih's teachers was Abu Abdallah Mohammed Amghar from El Jadida.\n\nMoner Mohammad Abu Salha: Moner Mohammad Abu Salha (also Munir Mohammed Abou Saleha aka Abu Hurayra al-Amriki) was an American suicide bomber who killed himself and several Syrian troops with a truck bomb in Ariha, Syria in the name of al-Nusra Front.\n\nBob Hawke: Robert James Lee Hawke {'1': \", '2': \", '3': \", '4': \"} (born 9 December 1929) is an Australian politician who was the Prime Minister of Australia and the Leader of the Labor Party from 1983 to 1991.\n\nMenachem Froman: Rabbi Menachem Froman (also spelled \"Menahem\" and \"Fruman\"; Hebrew: מנחם פרומן‎ ‎ ‎; 1 June 1945 – 4 March 2013) was an Israeli Orthodox rabbi and a peacemaker and negotiator with close ties to Palestinian religious leaders from the PLO and Hamas.  A founding member of Gush Emunim, he served as the chief rabbi of Tekoa in the West Bank.  He was well known for promoting and leading interfaith dialogue between Israeli Jews and Palestinians, focusing on using religion as a tool and source for recognizing the humanity and dignity of all Palestinians.  His pregnant daughter-in-law was injured in an attack on January 18, 2016.  Together with a Palestinian journalist close to Hamas, Rabbi Froman drafted a ceasefire agreement between Israel and the Hamas government in the Gaza Strip, known as the Froman-Amayreh Agreement.  The agreement was endorsed by Hamas government, but it did not receive any official response from the Israeli government.\n\nRabai al-Madhoun: Rabai al-Madhoun (born 1945) is a Palestinian journalist, novelist and writer.  He was born in the village of al-Majdal in Palestine, near Ashkelon in present-day Israel.  His family was driven out of Palestine in the 1948 Palestinian exodus.  Madhoun grew up in the refugee camp of Khan Younis located in the Gaza Strip.  He went to Alexandria University for higher education, and in 1973 turned to journalism as a career.  He was also involved with the Palestinian liberation struggle in the 1970s as a member of the Democratic Front for the Liberation of Palestine, but quit politics in 1980 to focus on writing full-time.  As a journalist, he worked in Beirut (Lebanon),Nicosia (Cyprus) and later on in London where he is now based.  Currently a British citizen, Madhoun is an editor at the \"Al-Sharq Al-Awsat\" newspaper.\n\nLisa Taraki: Lisa Taraki is a Palestinian journalist, teacher and sociologist.  She was born to an American mother and Afghan father, but now lives in Ramallah with her Palestinian husband and child.  She is associate professor of sociology at Birzeit University in the West Bank.  Taraki has called for an academic boycott of Israel.\n\nEl Al Flight 253 attack: El Al Flight 253, was a Boeing 707 en route from Tel Aviv, Israel, to New York City, United States when it was attacked by two Palestinian terrorists as it was about to depart from a layover in Athens, Greece on December 26, 1968.  One passenger, Israeli Leon Shirdan, 50, of Haifa, a marine engineer, was shot dead.  He was survived by his wife and then 15-year-old daughter.  Two unidentified women were injured, one by a bullet, the other as she leaped from the jet when the door was opened.  The two terrorists were 19-year-old Naheb H. Suleiman, born in Tripoli, Libya, of Palestinian parents, and 25-year-old Mahmoud Mohammad Issa Mohammad, born in 1943 in Palestine.  They were members of the Lebanese-based militant organization Popular Front for the Liberation of Palestine The two Arabs dashed out of the transit lounge of Athens Airport just as the Israeli plane, parked 200 yards away, was preparing to take off.  The plane had flown in earlier from Tel Aviv.  Mahmoud Mohammed Issa Mohammed fired at the plane for more than a minute with a submachine gun, killing one; while the other threw two hand grenades, creating panic aboard the plane carrying 10 crew members and 41 passengers.  The two men were taken into custody by Greek authorities.  Mahmoud Mohammed Issa Mohammad, was sentenced to 17 years and 5 months behind bars.  He was freed after less than 4 months after another Palestinian terrorist group hijacked a Greek airliner and demanded his release.  Subsequently he successfully hid his terrorist past and emigrated to Canada.  Once Canadian authorities learned of his crime, a protracted extradition process culminated in his extradition to Lebanon in 2013.\n\nMunif Mohammed Abou Rish: Munif Mohammed Abou Rish was a Palestinian journalist, who in 1974 planned to assassinate Bob Hawke, the federal president of the Australian Labor Party, who later became prime minister of Australia.  He also planned to assassinate the Israeli ambassador to Australia, and several prominent Jewish figures in Australia.\n\nMuhammad al-Qiq: Muhammad al-Qiq or Mohammed al-Qeeq (Arabic: محمد القيق‎ ‎ ) is a Palestinian Journalist, Correspondent and reporter at the Saudi News Agency Almajd TV Network.  He went on a hunger strike in protest against his being incarcerated under Israeli administrative detention (internment without trial or charge).\n\nQuestion: Munif Mohammed Abou Rish was a Palestinian journalist, who in 1974 planned to assassinate a politician born in which year ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"journalist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the journalist who planned the assassination.\"\n    },\n    \"target_politician\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the politician targeted for assassination.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the targeted politician.\"\n        },\n        \"role_at_time_of_plan\": {\n          \"type\": \"string\",\n          \"description\": \"The political role of the target at the time the assassination was planned.\"\n        },\n        \"later_role\": {\n          \"type\": \"string\",\n          \"description\": \"A significant later political role of the target.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\",\n        \"role_at_time_of_plan\",\n        \"later_role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"plan_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the assassination was planned.\"\n    }\n  },\n  \"required\": [\n    \"journalist_name\",\n    \"target_politician\",\n    \"plan_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "journalist_name": {
        "type": "string",
        "description": "The name of the journalist who planned the assassination."
      },
      "target_politician": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the politician targeted for assassination."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the targeted politician."
          },
          "role_at_time_of_plan": {
            "type": "string",
            "description": "The political role of the target at the time the assassination was planned."
          },
          "later_role": {
            "type": "string",
            "description": "A significant later political role of the target."
          }
        },
        "required": [
          "name",
          "birth_year",
          "role_at_time_of_plan",
          "later_role"
        ],
        "additionalProperties": false
      },
      "plan_year": {
        "type": "integer",
        "description": "The year the assassination was planned."
      }
    },
    "required": [
      "journalist_name",
      "target_politician",
      "plan_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
