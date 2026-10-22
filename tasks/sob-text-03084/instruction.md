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
Soo Bahk Do: Soo Bahk Do is a martial art founded and taught by Kwan Jang Nim Hwang Kee, his successor Hwang Hyun Chul, known as H.C. Hwang, and instructors who are certified by member organizations of the World Moo Duk Kwan, Inc.  This martial art was originally the ancient martial art of Korea.  Hwang Kee created Moo Duk Kwan with influence from "Soo Bahk Do"

Vidyut Jammwal: Vidyut Jammwal (born 10 December 1980) is an Indian film actor who predominantly works in Hindi films.  He is also a trained martial artist, having learned Kalaripayattu (a martial art of Kerala) since the age of three.  He is popularly known as "The New Age Action Hero of Bollywood".  He has also worked in Kollywood and Tollywood films.

Hee Il Cho: Cho Hee Il (born October 13, 1940) is a prominent Korean-American master of taekwondo, holding the rank of 9th "dan" in the martial art.  He has written 11 martial art books, produced 70 martial art training videos, and has appeared on more than 70 martial arts magazine covers.  Cho won several national and international competitions as a taekwondo competitor, and has appeared in several films, including "Fight to Win", "Best of the Best", "Bloodsport II", and "Bloodsport III".  He founded the Action International Martial Arts Association (AIMAA) in 1980, and is its President.  Cho is a member of both "Black Belt" magazine's Hall of Fame and "Tae Kwon Do Times" magazine's Hall of Fame.

Budo: The Art of Killing: Budo: The Art of Killing is an award winning 1978 Japanese martial arts documentary created and produced by Hisao Masuda and financed by The Arthur Davis Company.  Considered a cult classic, the film is a compilation of various Japanese martial art demonstrations by several famous Japanese instructors such as Gozo Shioda, Taizaburo Nakamura and Teruo Hayashi.  Martial arts featured in the film include: karate, aikido, kendo, sumo, and judo among others.  The only modern Japanese martial art not featured in the film is kyudo.

Kumdo: Kumdo is a modern Korean martial art derived from Japanese Kendo. its origin is the Japanese kendo.  Though romanized in a number ways when written Kǒmdo or Geomdo the meaning remains "the way of the sword" and is cognate with the Japanese term.  As a martial art, Kumdo has become accepted in Korean culture and society since its introduction from Japan to the degree that the term "Kumdo" has, in recent history, become a generic label for other Korean martial arts based upon swordsmanship.  As a result, caution should be exercised to avoid confusion among practices espousing martial (i.e., Hankumdo) rather than sporting and competitive goals.  Although related to Japanese Kendo, minor differences exist in Korean Kumdo due to appropriation and acculturation.  Such differences include, but are not limited to, the use of native terminology, the use of blue flags rather than red flags for the referees and minor modifications to the uniform.

Taijutsu: Taijutsu (体術 , literally "body technique" or "body skill") is a Japanese blanket term for any combat skill, technique or system of martial art using body movements that are described as an empty-hand combat skill or system.  The term is commonly used when referring to a traditional Japanese martial art but has also been used in the naming of modern martial arts such as Bujinkan Budo Taijutsu.  Taijutsu is similar to Karate but is more focused on the body techniques.  More specific names than taijutsu are typically used when describing a martial art, such as jujutsu (focusing on throwing, grappling, and submission), judo (focusing on throwing and grappling), aikido (focusing on throwing and joint locks) as well as karate and kenpō (focusing on striking).

Ji Jike: Ji Jike (; 1588–1662) was a highly accomplished martial artist from Yongji, Shanxi Province.  He was also known as Ji Longfeng ().  According to accepted theory, he is widely considered to be the originator of the internal martial art of Xingyiquan.  (Other, less credible, theories consider Bodhidharma or Yue Fei as the originators of this art.)  Ji Jike created the martial art of Xinyiquan (Heart and Intention Boxing), which is the precursor of Xingyiquan (Form and Intention Boxing).  He based the fundamentals of Xinyi on the spear techniques for which he was also famous.  It was Li Luo Neng, a most famous descendant of Ji Jike, who modified Xinyi and called it Xingyi.

Hélio Gracie: Hélio Gracie (] ; October 1, 1913 – January 29, 2009) was a Brazilian martial artist who, together with his brother Carlos Gracie, founded the martial art of Gracie jiu-jitsu and with Luiz França and Oswaldo Fadda the martial art of Brazilian jiu-jitsu (BJJ).  According to Rorion Gracie, his father Hélio is one of the first sports heroes in Brazilian history; he was named Man of the Year in 1997 by the American martial arts publication "Black Belt" magazine.  A patriarch of the Gracie family, he was the father of Rickson, Royler, Royce, Relson, and Ultimate Fighting Championship (UFC) co-founder Rorion Gracie, among other sons and daughters.

Thuppakki: Thuppakki ("The Gun") is a 2012 Tamil-language Indian action-thriller film written and directed by AR Murugadoss.  It features Vijay and Kajal Aggarwal in the lead roles, Vidyut Jammwal as the antagonist, as well as Jayaram and Sathyan in supporting roles.  The film, produced by S. Thanu, features background score and soundtrack composed by Harris Jayaraj with cinematography handled by Santosh Sivan.  The story revolves around an Indian Army officer from a Mumbai-based Tamil family on a mission to track down and destroy a terrorist group and deactivate the sleeper cells under its command, after witnessing and barely escaping a bomb blast executed by them.

Angampora: Angampora (Sinhalese: අංගම්පොර , is a form of martial art from Sri Lanka that combines combat techniques, self-defense, sport, exercise, and meditation.  A key component of angampora is the namesake "angam", which incorporates hand-to-hand fighting, and "illangam", involving the use of indigenous weapons such as the ethunu kaduwa, staves, knives and swords.  Another component known as "maya angam", which uses spells and incantations for combat, is also said to have existed.  Angampora's distinct feature lies in the use of pressure point attacks to inflict pain or permanently paralyze the opponent.  Fighters usually make use of both striking and grappling techniques, and fight until the opponent is caught in a submission lock that they cannot escape.  Usage of weapons is discretionary.  Perimeters of fighting are defined in advance, and in some of the cases is a pit.  With the advent of colonialism over the entirety of the island in 1815, Angampora fell into disuse and was very nearly lost as a part of the country's heritage.  The British administration prohibited its practice due to the dangers posed by a civilian populace versed in a martial art, burning down any "angan madu" (practice huts devoted to the martial art) found: flouting of the law was punished by a gunshot to the knee, effectively crippling practitioners; Angampora nevertheless survived within a few families, allowing it to emerge into mainstream Sri Lankan culture post-independence.

Question: What martial art has the actor who played the antagonist in Thuppakki learned since the age of three?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "antagonist_actor_name": {
          "type": "string",
          "description": "The name of the actor who played the antagonist in the film."
        }
      },
      "required": [
        "title",
        "antagonist_actor_name"
      ],
      "additionalProperties": false
    },
    "actor_martial_art_training": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor."
        },
        "martial_art_learned": {
          "type": "string",
          "description": "The name of the martial art the actor learned."
        },
        "age_started_learning_years": {
          "type": "integer",
          "description": "The age at which the actor started learning the martial art."
        },
        "martial_art_origin_region": {
          "type": "string",
          "description": "The region of origin for the martial art."
        }
      },
      "required": [
        "actor_name",
        "martial_art_learned",
        "age_started_learning_years",
        "martial_art_origin_region"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the martial art that the antagonist actor learned since the age of three."
    }
  },
  "required": [
    "film_details",
    "actor_martial_art_training",
    "final_answer"
  ],
  "additionalProperties": false
}
