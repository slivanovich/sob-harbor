{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLychee Light Club: Lychee Light Club (Japanese: ライチ☆光クラブ , Hepburn: Raichi☆Hikari Kurabu ) , also commonly known as \"Litchi Hikari Club\", is a Japanese horror manga series written and illustrated by Usamaru Furuya and based on a play of the same name.  It was serialized in Ohta Publishing's \"Manga Erotics F\" magazine between May 2005 and May 2006.  A prequel to the original story, \"Our Light Club\" (ぼくらの☆ひかりクラブ , Bokura no☆Hikari Kurabu ) , was serialized in Ohta Publishing's online \"pocopoco\" magazine between April 2011 and March 2012.\n\nJunji Ito: Junji Ito (伊藤 潤二 , Itō Junji , born July 31, 1963) is a Japanese horror manga artist.  Some of his most notable works include \"Tomie\", a series chronicling an immortal girl who drives her stricken admirers to madness, \"Uzumaki\", a three-volume series about a town obsessed with spirals, and \"Gyo\", a two-volume story where fish are controlled by a strain of sentient bacteria called \"the death stench.\"  His other works are \"Itou Junji Kyoufu Manga Collection\", a collection of different short stories including a series of stories named \"Souchi's Journal of Delights\", and \"Itou Junji No Neko Nikki: Yon and Mu\", a light-hearted, but still terrifying, story about moving in a new house with his cats.\n\nYōsuke Takahashi: Yōsuke Takahashi (高橋 葉介 , Takahashi Yōsuke , born 15 March 1956) is a Japanese horror manga artist who is known for his works \"Mugen Shinsi\" and \"Gakkō no Kaidan\".  He graduated from Komazawa University.  He made his professional manga debut in 1977, and has had stories published in the manga anthology series \"Petit Apple Pie\".\n\nPupa (manga): Pupa (Japanese: ピューパ , Hepburn: Pyūpa ) is a 20112013 Japanese horror manga series written and illustrated by Sayaka Mogi.  An anime television series adaptation produced by Studio Deen premiered on January 9, 2014.\n\nOpus (manga): Opus is a Japanese \"seinen\" manga series written and illustrated by Satoshi Kon.  The story is about a manga artist who is pulled into the world of the manga he is concluding and forced to confront his characters.  The manga was serialized in the manga magazine \"Comic Guys\" from October 1995 until the magazine's cancellation in June 1996.  It was collected into two volumes by Tokuma Shoten on December 13, 2010 and included a missing ending found after Kon's death.  Dark Horse Comics licensed the manga in North America and released it in an omnibus edition on December 9, 2014.  The french edition of the manga won the 2013 Asia Critics Prize from the \"Association des Critiques et des journalistes de Bande Dessinée\" and was nominated for the \"Sélection Officiele\" at the 2014 Angoulême International Comics Festival.  \"Opus\" was Kon's final manga before he debuted in the anime industry with \"Perfect Blue\".\n\nTomie: Tomie (富江 ) is a Japanese horror manga series written and illustrated by Junji Ito.  \"Tomie\" was Ito's first published work he originally submitted to \"Monthly Halloween\", a \"shōjo\" magazine in 1987, which led to him winning the Kazuo Umezu award.\n\nFuan no Tane: Fuan no Tane (不安の種 ) is a Japanese horror manga series written and illustrated by Masaaki Nakayama.  It was adapted into a live-action film released in July 2013.\n\nUzumaki: Uzumaki (Japanese: うずまき ) is a \"seinen\" horror manga series written and illustrated by Junji Ito.  Appearing as a serial in the weekly manga magazine \"Big Comic Spirits\" from 1998 to 1999, the chapters were compiled into three bound volumes by Shogakukan and published from August 1998 to September 1999.  In March 2000, Shogakukan released an omnibus edition, followed by a second omnibus version in August 2010.  In North America, Viz Media serialized an English-language translation of the series in its monthly magazine \"Pulp\" from February 2001 to August 2002.  Viz Media then published the volumes from October 2001 to October 2002, with a re-release from October 2007 to February 2008, and published a hardcover omnibus edition in October 2013.\n\nGhost Sweeper Mikami: Ghost Sweeper Mikami: The Great Paradise Battle!!  (Japanese: GS美神 極楽大作戦!!  , Hepburn: Gōsuto Suīpā Mikami Gokuraku Daisakusen!! )  is a Japanese comedic horror manga series written and illustrated by Takashi Shiina.  It was published by the weekly manga magazine \"Shōnen Sunday\" from 1991 to 1999.  In 1993, it won the Shogakukan Manga Award for best \"shōnen\" manga.  The series explores some folk religion themes such as possession, exorcism, shamanism, Yurei, and Yōkai.\n\nSanta Inoue: Santa Inoue (井上 三太 , Inoue Santa , born 1968 in Paris, France) is a Japanese manga artist and entrepreneur.  His most notable manga was the \"Tokyo Tribe\" series of which the manga installment \"Tokyo Tribe2\" (also known as \"Tokyo Tribes\") ran from 1997 to 2005, and was made into an anime series as well as a live-action film.  He wrote the horror manga \"The Neighbor No.  Thirteen\" which was also adapted into a live-action film.  His manga series have been influenced by hip hop culture, with some of the characters being modeled after rappers.  He owns a clothing and accessories business called Santastic! , and has done artwork on several music album covers.\n\nQuestion: Uzumaki, is a \"seinen\" horror manga series written and illustrated, by which Japanese horror manga artist?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"manga_series_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the manga series.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the manga series.\"\n    },\n    \"author_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"author_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the manga artist.\"\n        },\n        \"author_profession\": {\n          \"type\": \"string\",\n          \"description\": \"The profession of the manga artist.\"\n        }\n      },\n      \"required\": [\n        \"author_name\",\n        \"author_profession\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"manga_series_title\",\n    \"genre\",\n    \"author_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "manga_series_title": {
        "type": "string",
        "description": "The title of the manga series."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the manga series."
      },
      "author_details": {
        "type": "object",
        "properties": {
          "author_name": {
            "type": "string",
            "description": "The name of the manga artist."
          },
          "author_profession": {
            "type": "string",
            "description": "The profession of the manga artist."
          }
        },
        "required": [
          "author_name",
          "author_profession"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "manga_series_title",
      "genre",
      "author_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
