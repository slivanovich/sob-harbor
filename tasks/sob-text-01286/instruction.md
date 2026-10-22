Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Battle Royale II: Requiem: Battle Royale II: Requiem (バトル・ロワイアルＩＩ　【鎮魂歌】 , "Batoru rowaiaru tsū: "Rekuiemu"" ) , abbreviated as BRII ("Bii āru tsū"), is a 2003 Japanese dystopian action film.  It is a sequel to the 2000 film, "Battle Royale", which in turn was based upon a controversial 1999 novel of the same title by Koushun Takami.  An extended version of the film is titled Battle Royale II: Revenge.

Ryo Kimura: Ryo Kimura (木村 了 , Kimura Ryō , born September 23, 1988) is a Japanese actor who debuted in 2002.  His first movie was Moonlight Jellyfish, in which he co-starred with Tatsuya Fujiwara.  He played the role of Michio, a mentally challenged 15-year-old boy diagnosed with an incurable skin disease called XP (Xeroderma Pigmentosum).

Kaiji (manga): Tobaku Mokushiroku Kaiji (賭博黙示録カイジ , lit.  "Gambling Apocalypse Kaiji" ) , also known as "Ultimate Survivor Kaiji", is a Japanese manga series about the art of gambling, written by Nobuyuki Fukumoto.  It is published by Kodansha in "Young Magazine".  The first part of the manga (13 volumes), was adapted as a 26-episode anime television series called Gyakkyō Burai Kaiji: Ultimate Survivor (逆境無頼カイジ Ultimate Survivor , lit.  "Suffering Outcast Kaiji: Ultimate Survivor" ) , which began airing October 2007.  A live-action 'Kaiji' movie was released October 10, 2009 in Japan with Tatsuya Fujiwara playing the role of Kaiji.

Tatsuya Fujiwara: Tatsuya Fujiwara (藤原 竜也 , Fujiwara Tatsuya , born May 15, 1982) is a Japanese actor.  Internationally, he is best known for his leading roles as Shuya Nanahara in the "Battle Royale" films, Light Yagami in the "Death Note" films, Kaiji Ito in the "Kaiji" films, and Rikuhiko Yuki in Hideo Nakata's "The Incite Mill".  In 2014, he portrayed the villain Shishio Makoto in the live action "Rurouni Kenshin" films.

Erased (2016 film): Boku Dake ga Inai Machi (僕だけがいない街 , lit.  "The Town Where Only I Am Missing") is a 2016 Japanese thriller fantasy mystery film adaptation of the manga series of the same name featuring Tatsuya Fujiwara as Satoru Fujinuma.  It premiered in cinemas throughout Japan on March 19, 2016.  The theme song is "Hear ~Shinjiaeta Akashi~" (Hear 〜信じあえた証〜 , lit.  Hear ~A proof that you could trust~ ) by Chise Kanna.  The trailer was released on 14 January 2016.

Battle Royale: Battle Royale (Japanese: バトル・ロワイアル , Hepburn: Batoru Rowaiaru ) is a novel by Japanese writer Koushun Takami.  Originally completed in 1996, it was not published until 1999.  The story tells of junior high school students who are forced to fight each other to the death in a program run by the authoritarian Japanese government, now known as the Republic of Greater East Asia.

Koushun Takami: Kōshun Takami (高見 広春 , Takami Kōshun , born 10 January 1969) is a Japanese author and journalist.  Best known for his 1999 novel "Battle Royale", which was later adapted into two live-action films, directed by Kinji Fukasaku, and three manga series.

Arrietty: Arrietty, titled The Borrower Arrietty (Japanese: 借りぐらしのアリエッティ , Hepburn: Kari-gurashi no Arietti ) in Japan and The Secret World of Arrietty in North America, is a 2010 Japanese animated fantasy film produced by Studio Ghibli and directed by Hiromasa Yonebayashi as his feature film debut as a director.  The novel was adapted as a screenplay by Hayao Miyazaki and Keiko Niwa, based on "The Borrowers" by Mary Norton, an English author of children's books, about a family of tiny people who live secretly in the walls and floors of a typical household, borrowing items from humans to survive.  The film stars the voices of Mirai Shida, Ryunosuke Kamiki, Shinobu Otake, Keiko Takeshita, Tatsuya Fujiwara, Tomokazu Miura, and Kirin Kiki, and tells the story of a young Borrower (Shida) befriending a human boy (Kamiki), while trying to avoid being detected by the other humans.

Battle Royale (film): Battle Royale (バトル・ロワイアル , Batoru Rowaiaru ) is a 2000 Japanese dystopian film adapted from the 1999 novel of the same name by Koushun Takami.  It is the final film directed by Kinji Fukasaku, the screenplay written by his son Kenta, and stars Takeshi Kitano.  The film takes place in a dystopian Japan and it follows the story of Shuya Nanahara, a high-school student, and his classmates.  Their class has been chosen by the government to take part in an annual game where all the students of the class must fight to the death until only one remains alive.  The film aroused both domestic and international controversy and was either banned outright or deliberately excluded from distribution in several countries.

Battle Royale (manga): Battle Royale (Japanese: バトル・ロワイアル , Hepburn: Batoru Rowaiaru ) is a Japanese manga series written by Koushun Takami and illustrated by Masayuki Taguchi.  It is based on Takami's novel of the same name, telling the story of a class of junior high school children who are forced to fight each other to the death.  It was serialized by Akita Shoten in "Young Champion" from 2000 to 2005, and later combined into 15 volumes, which were released in English by Tokyopop from 2003 to 2006.  In October 2007, a special edition of the manga began being released.

Question: Tatsuya Fujiwara is a Japanese actor, internationally, he is best known for his leading roles as Shuya Nanahara in which 2000 Japanese dystopian film adapted from the 1999 novel of the same name by Koushun Takami?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor."
        },
        "character_played": {
          "type": "string",
          "description": "The name of the character played by the actor."
        }
      },
      "required": [
        "actor_name",
        "character_played"
      ],
      "additionalProperties": false
    },
    "source_novel": {
      "type": "object",
      "properties": {
        "novel_title": {
          "type": "string",
          "description": "The title of the novel the film was adapted from."
        },
        "novel_author": {
          "type": "string",
          "description": "The author of the novel."
        },
        "novel_publication_year": {
          "type": "integer",
          "description": "The publication year of the novel."
        }
      },
      "required": [
        "novel_title",
        "novel_author",
        "novel_publication_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_year",
    "film_genre",
    "actor_details",
    "source_novel"
  ],
  "additionalProperties": false
}
