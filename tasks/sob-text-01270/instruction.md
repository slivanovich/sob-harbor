{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAleksandr Revva: Aleksandr Vladimirovich Revva (Russian: Александр Владимирович Ревва ; born 10 September 1974) is a Russian stand-up comedian, TV host and voice actor.  A former KVN player, in 2006 Revva became a \"resident\" of the Russian Comedy Club show on TNT.  As of 2009 hosts a TV show on NTV.  Stage name: Arthur Pirozhkov, Alex Nowacki, Grandma Batman, Don Digidon.\n\nInexplicable, yet a Fact: Inexplicable, yet a Fact (Russian: Необъяснимо, но факт, often abbreviated as ННФ and has also been translated as Inexplicable, but Factual) was a popular TV show on TNT (Russian TV channel).  \"Inexplicable, yet a Fact\" is among the earliest pseudo-documentary projects on the Russian television and has influenced several similar projects on other Russian TV channels: \"Fantastical Stories\" (REN TV), \"Cannot Be!\"  (STS (TV channel)), \"X Files\" (DTV), and others.  The series has begun shortly after Syfy's \"Ghost Hunters\", possibly influenced by the success of the series, and before Discovery Channel's \"A Haunting\".  \"Inexplicable, yet a Fact\", as well as the aforementioned pseudo-documentaries, root in \"Chariots of the Gods (film)\", with \"Inexplicable, yet a Fact\" heavily using the footage and ideas from the film in several episodes.\n\nKsenia Sobchak: Ksenia Anatolyevna Sobchak (Russian: Ксе́ния Анато́льевна Собча́к , born November 5, 1981) is a Russian TV anchor, journalist, socialite, and actress.  Sobchak became known to the wider public as a host of the reality show \"Dom-2\" on the Russian channel TNT.  She is sometimes described as \"Russia's Paris Hilton\".  She is an anchor at an independent TV channel Dozhd.\n\nGarik Martirosyan: Garik Martirosyan (Armenian: Գարիկ Մարտիրոսյան , born February 13, 1974 in Yerevan, Soviet Union) is a Moscow-based Armenian entertainer, comedian, TV host, actor and singer.  He's the co-producer and host of the Comedy Club Russia which airs on Russian TV channel TNT.  He was also one of 4 hosts of \"Prozhektorperiskhilton\" broadcast on Channel One from 2008 until 2012.\n\nUniver. New Dorm: Univer.  New Dorm (Russian: Униве́р.  Новая общага ) is a Russian comedy sitcom which airs on the TNT channel since October 10, 2011.  The show is a spin-off of the popular Russian TV Series \"Univer\".\n\nNasha Russia: Nasha Russia (Russian: Наша Russia , literally \"Our Russia\") is a Russian sketch show based on the British comedy show \"Little Britain\", created by Comedy Club Production.  It was written by former KVN players and producers Semyon Slepakov and Garik Martirosyan.\n\nKVN: KVN (Russian: КВН , an abbreviation of Клуб весёлых и находчивых , \"Klub vesyólykh i nakhódchivykh\" or \"Ka-Ve-En\", \"Club of the Funny and Inventive People\") is a Russian humour TV show and competition where teams (usually college students) compete by giving funny answers to questions and showing prepared sketches, that originated in the Soviet Union.  The programme was first aired by the First Soviet Channel on November 8, 1961.  Eleven years later, in 1972, when few programmes were being broadcast live, Soviet censors found the students' impromptu jokes offensive and anti-Soviet and banned \"KVN\".  The show was revived fourteen years later during the Perestroika era in 1986, with Alexander Maslyakov as its host.  It is one of the longest-running TV programmes on Russian Television.  It also has its own holiday on November 8, the birthday of the game, which \"KVN\" players celebrate every year since it was announced and widely celebrated for the first time in 2001.\n\nMikhail Galustyan: Mikhail Sergeyevich Galustyan (Russian: Михаи́л Серге́евич Галустя́н , born 25 October 1979) is a Russian-Armenian showman, comedian, screenwriter, and producer.  Mikhail Galustyan was also a former participant in KVN and a show called \"Comedy Club (Russia)\".  Awards Champion League KVN 2003, Winner of the Summer Cup of KVN 2004, 2005, 2009.\n\nThe Best Movie: The Best Movie (Russian: Самый лучший фильм , \"Samy luchshiy film\") is a 2008 Russian comedy film from TNT and Comedy Club Russia, spoofing such famous Russian films as \"Night Watch\" and \"Day Watch\", \"The 9th Company\", \"Heat\" and TV series: \"My Fair Nanny\", \"Dalnoboyshchiki\" and \"Brigada\".  The movie includes numerous cameos by Russian celebrities, some of them involving a humorous touch on their public image.  For instance, socialite Kseniya Sobchak appears as a luxury prostitute, and gay icon Boris Moiseev plays a rough-and-tumble policeman, his only line being: \"You gonna sign it all, you faggot!\"\n\nPavel Volya: Pavel Alekseevich Volya (Russian: Павел Алексеевич Воля , born 14 March 1979) is a Russian TV host, actor and singer.  A former KVN player, he first came to prominence as the \"\"resident\"\" of the Russian Comedy Club show, co-produced by Garik Martirosyan and aired on TNT channel.  In 2007, Volya released his first studio album.  As of 2008, hosts a TV Show on TNT.\n\nQuestion: Pavel Alekseevich Volya, is a Russian TV host, actor and singer, a ormer KVN player, he first came to prominence as the \"\"resident\"\" of the Russian Comedy Club show, co-produced by Garik Martirosyan, a Moscow-based Armenian entertainer, comedian, TV host, actor and singer, the co-producer and host of the Comedy Club Russia which airs on which Russian TV channel ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"tv_show_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the TV show.\"\n        },\n        \"broadcasting_channel\": {\n          \"type\": \"string\",\n          \"description\": \"The TV channel on which the show airs.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"broadcasting_channel\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"key_personalities\": {\n      \"type\": \"array\",\n      \"description\": \"A list of key individuals associated with the TV show.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The full name of the personality.\"\n          },\n          \"roles\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"A list of roles or professions of the personality related to the show or generally.\"\n          },\n          \"is_former_kvn_player\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the personality was a former KVN player.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"roles\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"answer_channel\": {\n      \"type\": \"string\",\n      \"description\": \"The direct answer to the question: the Russian TV channel where Comedy Club Russia airs.\"\n    }\n  },\n  \"required\": [\n    \"tv_show_details\",\n    \"key_personalities\",\n    \"answer_channel\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "tv_show_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the TV show."
          },
          "broadcasting_channel": {
            "type": "string",
            "description": "The TV channel on which the show airs."
          }
        },
        "required": [
          "name",
          "broadcasting_channel"
        ],
        "additionalProperties": false
      },
      "key_personalities": {
        "type": "array",
        "description": "A list of key individuals associated with the TV show.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The full name of the personality."
            },
            "roles": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "A list of roles or professions of the personality related to the show or generally."
            },
            "is_former_kvn_player": {
              "type": "boolean",
              "description": "Indicates if the personality was a former KVN player."
            }
          },
          "required": [
            "name",
            "roles"
          ],
          "additionalProperties": false
        }
      },
      "answer_channel": {
        "type": "string",
        "description": "The direct answer to the question: the Russian TV channel where Comedy Club Russia airs."
      }
    },
    "required": [
      "tv_show_details",
      "key_personalities",
      "answer_channel"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
