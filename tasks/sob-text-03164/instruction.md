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
LE (rapper): Ahn Hyo-jin (born December 10, 1991), better known by her stage name LE ( ), is a South Korean rapper, singer, songwriter, and record producer.  She is the main rapper of the K-pop girl group EXID.

Yezi: Lee Ye-ji (born August 26, 1994), better known by her stage name Yezi, is a South Korean rapper and singer.  She debuted as a member of South Korean girl group Fiestar in 2012.  Yezi was a semi-finalist on "Unpretty Rapstar 2" in 2015, during which she released several singles.  Her debut solo maxi single, "Foresight Dream", was released on January 28, 2016.

Paper (magazine): Paper, stylized as PAPER, is a New York City-based independent magazine focusing on fashion, popular culture, nightlife, music, art and film.  Past cover models include Kim Kardashian, Demi Lovato, Katy Perry, Miley Cyrus, Prince, CL, and Jennifer Lopez.

CL (singer): Lee Chae-rin (born February 26, 1991), better known by her stage name CL, is a South Korean singer-songwriter and rapper.  Born in Seoul, South Korea, she spent much of her early life in Japan and France.  She was trained in JYP Entertainment before joining YG Entertainment, and became a member of the girl group 2NE1.  She is currently working on an English-language album.

Jeon Ji-yoon: Jeon Ji-yoon (born October 15, 1990), better known mononymously as Jiyoon or by her stage name Jenyer, is a South Korean rapper, singer-songwriter and actress.  She was previously a member of South Korean girl group 4Minute and its sub-group 2Yoon.  She debuted as a solo artist on November 2, 2016, under the stage name Jenyer, with the release of her debut digital single, "I Do".

Miryo: Jo Mi-hye (born November 2, 1981), better known by her stage name Miryo, is a South Korean rapper, songwriter and record producer.  She is currently the rapper of girl group Brown Eyed Girls, and is a former member of rap group Honey Family.  Miryo debuted as a soloist in 2012, after appearing as a producer in the first season of Show Me the Money.

Gwiyomi: The Gwiyomi Song, or Kwiyomi Song (귀요미 송), is a K-pop single by South Korean singer Hari and was released on February 18, 2013.  It was inspired by a gesture from South Korean rapper Jung Ilhoon of boy group BtoB.  The gesture is called 'Gwiyomi Player', that was popularized by South Korean variety show "Weekly Idol" through a segment called "The Aegyo Battle" (Battle of Cuteness) following Ilhoon's guest appearance on the show in October 2012.  The song went on to be a viral success and an Internet meme after Korean Media outlet "Sports Seoul" uploaded a clip of Hari performing the gestures and singing the song.  This video has since inspired many Asian netizens to upload their own versions onto the internet.

GP Basic: GP Basic (Korean: 지피 베이직 ) was a South Korean girl group who debuted on August 15, 2010.  At the time of their debut, they were considered to be the "youngest" South Korean girl group with an average age of below 13.5.  The age of their youngest member, Janey, caused controversy followed by the debut of a much younger girl group, G-story, who were all below 10 years old.  This led to new broadcasting regulations in South Korea.

Beenzino: Lim Sung-bin (Hangul: 임성빈; born September 12, 1987), better known by the stage name Beenzino (Hangul: 빈지노), is a South Korean rapper currently signed under Illionaire Records.  His stage name is a play on that of Boston rapper Benzino, combined with "빈" (pronounced "been") from his birth name.  Beenzino made his first official public appearance at Dok2's Hustle Real Hard Concert on June 5, 2011 and has since released three solo albums, as well as other works in collaboration with hip hop producers Primary and Shimmy Twice, and as the duo Hot Clip with South Korean rapper Beatbox DG.  He is noted for his melodic style of rapping.

Cover model: A cover model is a male or female whose photograph appears on the front cover of a magazine.  The cover model is generally a fashion model, celebrity, or contest winner.  Generally, cover models are depicted solitarily; however, on occasion magazines will present a front cover with multiple cover models.  Female cover models are often referred to as cover girls.

Question: Paper is a magazine that has had, as a cover model, a South Korean rapper who was part of what girl group?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_name": {
      "type": "string",
      "description": "The name of the magazine."
    },
    "cover_model_details": {
      "type": "object",
      "properties": {
        "model_name": {
          "type": "string",
          "description": "The stage name of the cover model."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the cover model."
        },
        "occupation": {
          "type": "string",
          "description": "The primary occupation of the cover model."
        },
        "girl_group_name": {
          "type": "string",
          "description": "The name of the girl group the cover model was a member of."
        }
      },
      "required": [
        "model_name",
        "nationality",
        "occupation",
        "girl_group_name"
      ],
      "additionalProperties": false
    },
    "question_answer": {
      "type": "string",
      "description": "The name of the girl group that the South Korean rapper cover model was part of."
    }
  },
  "required": [
    "magazine_name",
    "cover_model_details",
    "question_answer"
  ],
  "additionalProperties": false
}
