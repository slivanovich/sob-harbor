{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMeri Pyaari Bindu: Meri Pyaari Bindu (English: My Lovely Bindu) is an Indian Hindi romantic drama film, written by Suprotim Sengupta and directed by Akshay Roy.  It features Ayushmann Khurrana and Parineeti Chopra in the lead roles.\n\nSalt N' Pepper: Salt N' Pepper is a 2011 Indian Malayalam romantic comedy film directed by Aashiq Abu and produced for Lucsam Creations.  The film stars Lal, Asif Ali, Shweta Menon and Mythili in the lead roles while Baburaj and Vijayaraghavan play supporting roles.  Cinematography is by Shyju Kahild, whose debut was \"Traffic\" (2011).  The screenplay was written by Syam Pushkaran and Dileesh Nair.\n\nPasanga 2: Pasanga 2 : Haiku is a 2015 Indian Tamil children's film written, co produced and directed by Pandiraj.  A thematic sequel to \"Pasanga\" (2009), the film focuses on the issue of attention deficit hyperactivity disorder (ADHD) amongst children and is set in the city, unlike \"Pasanga\".  The film, starring debutante child actors Nishesh and Vaishnavi in lead alongside Karthik Kumar, Bindu Madhavi, Ramdoss and Vidya Pradeep, is produced by Suriya, who also appears in an supporting role along with Amala Paul.  The film was the last film of year 2015 and was declared as a \"year end blockbuster\".  The film will mark Pandiraj's last of the \"trilogy for children\", following \"Pasanga\" and \"Marina\".  A Telugu dubbed version, titled Memu, was released simultaneously in Andhra Pradesh and Telangana on 8 July 2016.\n\nMere Jeevan Saathi (1972 film): Mere Jeevan Saathi (\"My Life Partner\") is a 1972 Indian Hindi-language romantic comedy film produced by Harish and Vinod Shah.  It is directed by Ravikant Nagaich, and it stars Rajesh Khanna, Tanuja, Sujit Kumar, Bindu, Helen, Utpal Dutt, Nazir Hussain and Rajindranath.\n\nMeri Pyaari Bahania Banegi Dulhania: Meri Pyaari Bahania Banegi Dulhania is a 2001 Hindi-language Indian feature film directed by Jayant Gilatar, starring Mithun Chakraborty, Rajeshwari Sachdev and Vishwajeet Pradhan.  The film is the remake of the 1997 successful Tamil film \"Porkkaalam\".\n\nAyushmann Khurrana: Ayushmann Khurrana (born 14 September 1984) is an Indian film actor and singer.  He is the recipient of two Filmfare awards.  In 2012, Khurrana made his film debut in Shoojit Sircar's romantic comedy \"Vicky Donor\", which touched on the topic of sperm donation in India.  Upon release, the film was a critical and commercial success.\n\nSitaram Kattel: Sita Ram Kattel (Nepali: सीता राम कट्टेल ), popularly known by his serial name \"Dhurmus\" is a Nepali comedian, actor, script writer, and director.  He was one of the main characters of the Nepali TV series \"Meri Bassai\".  He is considered as one of the Nepal's most talented and best comedian ever because he alone had played more than 24 roles in his own sitcom Meri Bassai.  He also acted in the 2013 Nepali box office hit \"Chha Ekan Chha\" in a lead role along with Deepak Raj Giri, Kedar Ghimire, Neeta Dhungana, and Jeetu Nepal.  His another movie wada number chha was also blockbuster.  He is highly active in social work too.\n\nPorkkaalam: Porkaalam (Tamil: பொற்காலம் English: Golden Age ) is a 1997 Indian Tamil drama film written and directed by Cheran.  The film has Murali, Meena, Sanghavi, Rajeshwari and Vadivelu in key roles.  It was later remade in Telugu as \"Manikyam\" with Meka Srikanth, in Kannada as \"Odahuttidavalu\" with Ravichandran in 2006 and in Bollywood as \"Meri Pyaari Bahania Banegi Dulhania\" with Mithun Chakraborty in 2001.  \"Porkaalam\" was one among 1997 Deepavali releases and became a huge success.\n\nMatthew Goode: Matthew William Goode (born 3 April 1978) is an English actor.  He made his screen debut in 2002 with ABC's TV movie feature \"Confessions of an Ugly Stepsister\".  His breakthrough role was in romantic comedy \"Chasing Liberty\" (2004), for which he received a nomination at Teen Choice Awards.  He then appeared in supporting roles in Woody Allen's \"Match Point\" (2005), the German-British romantic comedy \"Imagine Me and You\" (2006), the period drama \"Copying Beethoven\" (2006).  He gained praise for his performance as an aspiring artist in Julian Jarrold's drama \"Brideshead Revisited\" (2008) and as Ozymandias in the American neo-noir-superhero film \"Watchmen\" (2009), based on DC Comics' limited series of the same name.  He then starred in romantic comedy \"Leap Year\" (2010) and Australian drama \"Burning Man\" (2011), the latter earning him a nomination for Best Actor at the Film Critics Circle of Australia Awards.\n\nAdam Hicks: Hicks had a recurring role on \"Titus\", and had roles in various movies and television series, before playing the lead in \"How to Eat Fried Worms\".  He then appeared in \"Mostly Ghostly\" alongside many other Disney Channel stars.  In 2009, he grabbed the co lead role of Luther on \"Zeke & Luther\".  In 2011, he starred in \"Lemonade Mouth\" as Wendell \"Wen\" Gifford.  He co starred on \"Pair of Kings\" as King Boz, replacing Mitchel Musso's character King Brady.  Hicks portrayed so Jason Zimmer, in the erotic thriller \"The Boy Next Door\".\n\nQuestion: What is the name of the romantic comedy that debuted the male co lead of Meri Pyaari Bindu?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_identified\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the male co-lead of Meri Pyaari Bindu.\"\n        },\n        \"role_in_meri_pyaari_bindu\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the actor in Meri Pyaari Bindu.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_in_meri_pyaari_bindu\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"debut_film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the actor's debut film.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the debut film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the debut film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"genre\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the romantic comedy film that was the debut of the male co-lead of Meri Pyaari Bindu.\"\n    }\n  },\n  \"required\": [\n    \"actor_identified\",\n    \"debut_film_details\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_identified": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the male co-lead of Meri Pyaari Bindu."
          },
          "role_in_meri_pyaari_bindu": {
            "type": "string",
            "description": "The role of the actor in Meri Pyaari Bindu."
          }
        },
        "required": [
          "name",
          "role_in_meri_pyaari_bindu"
        ],
        "additionalProperties": false
      },
      "debut_film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the actor's debut film."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the debut film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the debut film."
          }
        },
        "required": [
          "title",
          "genre",
          "release_year"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "string",
        "description": "The name of the romantic comedy film that was the debut of the male co-lead of Meri Pyaari Bindu."
      }
    },
    "required": [
      "actor_identified",
      "debut_film_details",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
