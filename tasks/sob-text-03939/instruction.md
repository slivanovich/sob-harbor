{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGinza Cosmetics: Ginza Cosmetics (銀座化粧 , Ginza Keshō ) is a 1951 black-and-white Japanese film directed by Mikio Naruse.  It follows the life of a quiet geisha, single mother of a young boy, in the lively Tokyo quarter of Ginza.  The film is based on a novel by Tomoichiro Igami and also on screenwriter Matsuo Kishi and director Mikio Naruse's personal knowledge of Tokyo's Ginza district.\n\nTadao Ikeda: Tadao Ikeda (池田忠雄 , Ikeda Tadao ) (5 February 1905 - 5 May 1964) was a Japanese screenwriter and film director.  After graduating from Waseda University, he joined the Shochiku studio and came to prominence writing screenplays for such directors as Yasujirō Ozu, Mikio Naruse, Kōzaburō Yoshimura, and Yasujirō Shimazu.  He also directed a few films.\n\nWife (film): Wife (\"妻 Tsuma\") is a film directed by Japanese director Mikio Naruse originally released in 1953.  It is based on the novel \"Chairo no me\", written by Fumiko Hayashi in 1950.  Like other Naruse films from this period, such as \"Repast\" and \"Husband and Wife\", the theme of \"Wife\" involves a couple trapped with each other.  Another theme common to several Naruse films of the period is the way loving relationships dissipate as a result of economic pressures.  And like two other Naruse films based on novels by Hayashi, \"Repast\" and \"Lightning\", the story involves a stale marriage and unhappy family.\n\nMikio Naruse: Mikio Naruse (成瀬 巳喜男 , Naruse Mikio , August 20, 1905 – July 2, 1969) was a Japanese filmmaker, screenwriter, and producer who directed some 89 films spanning the period 1930 (towards the end of the silent period in Japan) to 1967.\n\nShochiku: Shochiku Company Limited (松竹株式会社 , Shōchiku Kabushiki gaisha ) () is a Japanese movie studio and production company for kabuki.  It also produces and distributes anime films.  Its best remembered directors include Yasujirō Ozu, Kenji Mizoguchi, Mikio Naruse, Keisuke Kinoshita and Yōji Yamada.  Shochiku has also produced films by highly regarded independent and \"loner\" directors such as Takashi Miike, Takeshi Kitano, Akira Kurosawa and Taiwanese New Wave director Hou Hsiao-hsien.  It is a member of the Motion Picture Producers Association of Japan (MPPAJ), and is one of Japan's Big Four film studios.\n\nMatsuo Kishi: Matsuo Kishi (岸松雄 , Kishi Matsuo ) (18 September 1906 – 17 August 1985) was a Japanese film critic, director, screenwriter, producer, and biographer.  His real name was Aji Shūichirō.  Born in Tokyo, he became interested in film from his days in high school and, continuing on to Keio University, began submitting reviews to magazines such as \"Kinema Junpo\" and editing theater programs.  Starting a dōjinshi \"Eiga kaihō\" with Tsuneo Hazumi, Kishi became involved in the left-wing film movement of the late 1920s, eventually becoming a member of the Proletarian Film League of Japan (Prokino).  He soon left out of dissatisfaction with such a political approach to film.  In 1932, he became the first critic to champion the work of Sadao Yamanaka, and later was a strong supporter of the films of Hiroshi Shimizu.  In 1937, he gave up being a film critic and became an assistant director at Toho, where he directed one film— \"Kazaguruma\", in 1938— before concentrating on screenwriting.  After the war, he mainly worked at Shintoho, serving as producer on a few films, and wrote scripts for such directors as Shimizu and Mikio Naruse.  All along he continued writing on film, especially penning numerous biographical accounts of the many people he knew in the Japanese film world.\n\nSadao Yamanaka: Sadao Yamanaka (山中 貞雄 , Yamanaka Sadao , November 7, 1909 – September 17, 1938) was a Japanese film director and screenwriter who directed 26 films between 1932 and 1938.  He was a contemporary of Yasujirō Ozu, Mikio Naruse and Kenji Mizoguchi and one of the primary figures in the development of the \"jidaigeki\", or historical film.  Yamanaka died of dysentery in Manchuria after being drafted into the Imperial Japanese Army.  He is the uncle of the Japanese film director Tai Kato, who wrote a book about Yamanaka, \"Eiga kantoku Yamanaka Sadao\".\n\nSumie Tanaka: Sumie Tanaka (\"田中澄江\"; April 11, 1908—March 1, 2000) was a Japanese screenwriter and playwright born in Tokyo.  She was most well known for her long collaboration with film director Mikio Naruse and for writing screenplays for Japan's first major female director Kinuyo Tanaka.  Member of the Bungakuza theatre company, she was married to playwright and dramatist Chikao Tanaka.  The screenplays she wrote for Repast (\"めし\", Meshi; 1951), Home Sweet Home (\"我が家は楽し \", Wa ga ya wa tanoshi; 1951), and Record of Youth (\"少年期 \", Shonenki; 1951) won her the Blue Ribbon Award for Best Screenplay in 1951.\n\nSōjirō Motoki: Sōjirō Motoki (本木 荘二郎 , Motoki Sōjirō ) was a Japanese filmmaker who served primarily as a film producer, but also as a writer and director.  He was most famous for producing several films for Akira Kurosawa, including \"Seven Samurai\", \"Ikiru\" and \"Throne of Blood\".  He also produced films for other directors, including Mikio Naruse, for whom he produced \"Spring Awakens\" and \"Battle of Roses\", and Kazuo Mori, for whom he produced \"Vendetta for a Samurai\".  As a writer, he provided the story for Kei Kumai's 1968 film \"The Sands of Kurobe\", starring Kurosawa favorite Toshiro Mifune.\n\nRon Underwood: Ronald Brian \"Ron\" Underwood (born November 6, 1953) is an American film director, producer and television director.\n\nQuestion: Which film director was born first, Mikio Naruse or Ron Underwood?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"directors_compared\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\"\n          },\n          \"birth_year\": {\n            \"type\": \"integer\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"birth_year\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"earliest_born_director_name\": {\n      \"type\": \"string\"\n    },\n    \"earliest_birth_year\": {\n      \"type\": \"integer\"\n    }\n  },\n  \"required\": [\n    \"directors_compared\",\n    \"earliest_born_director_name\",\n    \"earliest_birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "directors_compared": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "birth_year": {
              "type": "integer"
            }
          },
          "required": [
            "name",
            "birth_year"
          ],
          "additionalProperties": false
        }
      },
      "earliest_born_director_name": {
        "type": "string"
      },
      "earliest_birth_year": {
        "type": "integer"
      }
    },
    "required": [
      "directors_compared",
      "earliest_born_director_name",
      "earliest_birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
