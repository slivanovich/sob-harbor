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
Moon Chae-won: Moon Chae-won (born November 13, 1986) is a South Korean actress.  Moon first attracted attention in 2008 in her supporting role as a gisaeng in "Painter of the Wind".  She was next cast in "Brilliant Legacy", one of the top-rated Korean dramas of 2009.  2011 marked Moon's career breakthrough, with leading roles in the television period drama "The Princess' Man" and the action blockbuster "War of the Arrows"; both were critical and commercial hits.  For her performance in the latter, Moon won Best New Actress at the Grand Bell Awards and the Blue Dragon Film Awards.  Moon's other notable television series include the revenge melodrama "The Innocent Man" (2012) and the humanistic medical drama "Good Doctor" (2013).

Hope (2013 film): Hope (), also known as Wish, is a 2013 South Korean film directed by Lee Joon-ik, starring Sol Kyung-gu, Uhm Ji-won and Lee Re.  It won Best Film at the 34th Blue Dragon Film Awards.

30th Blue Dragon Film Awards: The 30th Blue Dragon Film Awards ceremony was held on December 2, 2009 at the KBS Hall in Yeouido, Seoul, South Korea.  Hosted by actors Kim Hye-soo and Lee Beom-soo, it was presented by Sports Chosun and was broadcast on KBS starting at 8PM KST.

Park Jung-min (actor): Park Jung-min (born February 25, 1987) is a South Korean actor.  He is best known for starring in the critically acclaimed indie film "Bleak Night" (2011) and "" (2015), for which he won "Best New Actor" at the 52nd Baeksang Arts Awards and the 37th Blue Dragon Film Awards.

34th Blue Dragon Film Awards: The 34th Blue Dragon Film Awards ceremony was held at Kyung Hee University's Peace Palace Hall in Seoul on November 22, 2013.  It was broadcast on SBS and was hosted by Kim Hye-soo and Yoo Jun-sang.

29th Blue Dragon Film Awards: The 29th Blue Dragon Film Awards ceremony was held on November 20, 2008 at the KBS Hall in Yeouido, Seoul, South Korea.  Hosted by actors Jung Joon-ho and Kim Hye-soo, it was presented by Sports Chosun and broadcast on KBS.

35th Blue Dragon Film Awards: The 35th Blue Dragon Film Awards ceremony was held on December 17, 2014 at the Sejong Center for the Performing Arts in Seoul.  It was broadcast on SBS and hosted by Kim Hye-soo and Yoo Jun-sang.

Lee Eun-woo: Lee Eun-woo (born August 22, 1980) is a South Korean actress.  She has worked on films such as "Moebius" and "Kabukicho Love Hotel".  In 2013, she was nominated for Best New Actress at the 34th Blue Dragon Film Awards.

Moebius (2013 film): Moebius is a 2013 South Korean horror drama film written and directed by Kim Ki-duk.  It was screened out of competition at the 70th Venice International Film Festival.  It was initially banned in South Korea, before the Korea Media Rating Board reviewed the film and changed the rating.

Han Hyo-joo: Han Hyo-joo (born February 22, 1987) is a South Korean film and television actress.  She is best known for her leading roles in television drama series: "Brilliant Legacy" (2009); "Dong Yi" (2010) and "W - Two Worlds" (2016); as well as the film "Cold Eyes" (2013), for which she won Best Actress at the 34th Blue Dragon Film Awards.

Question: In what year did Lee Eun-woo both star in the intially banned film Mobius and get nominate for Best New Actress at the 34th Blue Dragon Film Awards?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_year": {
      "type": "integer",
      "description": "The year in which both events occurred."
    },
    "person_name": {
      "type": "string",
      "description": "The name of the actress involved."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film."
        },
        "initial_status": {
          "type": "string",
          "description": "The initial status or notable characteristic of the film."
        }
      },
      "required": [
        "film_title",
        "initial_status"
      ],
      "additionalProperties": false
    },
    "award_nomination_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the award ceremony."
        },
        "award_edition": {
          "type": "integer",
          "description": "The edition number of the award ceremony."
        },
        "nomination_category": {
          "type": "string",
          "description": "The category for which the person was nominated."
        }
      },
      "required": [
        "award_name",
        "award_edition",
        "nomination_category"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "event_year",
    "person_name",
    "film_details",
    "award_nomination_details"
  ],
  "additionalProperties": false
}
