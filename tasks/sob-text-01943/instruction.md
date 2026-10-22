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
John Emil Augustine: John Emil Augustine (born March 12, 1975) is an American novelist, short story writer, singer-songwriter, multi-instrumentalist, mental health advocate, and teacher.  Augustine’s literary works are best known for their emphasis on the author’s own spousal abuse at the hands of a mentally unstable wife and the effects of that abuse on subsequent relationships.  Less than a year after its release, his first novel, "From the Abyss" (2013), was recognized as one of the "50 Self-Published Books Worth Reading" by Indie Author Land, 2013/14.  His musical career spans four decades (1987–present); however, little information has been released by Augustine himself regarding his career in music.  His participation in the Minneapolis music scene is alluded to in his memoir-oriented novels as well as in subsequent interviews.

John E. Berninger: John Emil Berninger (December 13, 1896 – July 1981) was an American landscape painter and Pennsylvania impressionist.  He lived and painted in Allentown, Pennsylvania, in the United States.

Richard Djerf: Richard Kenneth Djerf (born November 6, 1969) is an American mass murderer, currently on death row in Florence, Arizona.  His case is often compared with that of John List, with the exception that Djerf killed someone else’s family.

Emil Frisk: John Emil Frisk (October 15, 1874 – January 27, 1922) was a pitcher and outfielder in Major League Baseball.  He played for the Cincinnati Reds, Detroit Tigers, and St. Louis Browns.  Frisk also had a long career in the minor leagues, where he won three batting titles and became the first minor league baseball player to accumulate over 2,000 career hits.

Frank Bender: Francis Augustus "Frank" Bender (June 16, 1941 – July 28, 2011) was a autodidact forensic artist and fine artist.  He made facial reconstructions of the dead based on their skeletons, and of fugitives based on out of date photographs, with his reconstructions showing how they might look in the present day.  He primarily worked in clay and then cast his pieces into plaster and painted them, but he also created age-progression drawings of fugitives using pastels.  His most famous facial reconstruction case was that of John Emil List, whose case was shown on "America's Most Wanted".  Bender's work led to List's capture.

John Jaha: John Emil Jaha (born May 27, 1966) is a former first baseman in Major League Baseball who had a 10-year career from 1992 to 2001.  He played for the Milwaukee Brewers and Oakland Athletics, playing in both the American League and National League.  He was elected to the American League All-Star team in 1999.

John List: John Emil List (September 17, 1925 – March 21, 2008) was an American multiple murderer and long-time fugitive.  On November 9, 1971, he killed his wife, mother, and three children in their home in Westfield, New Jersey, then disappeared.  He had planned the murders so meticulously that nearly a month passed before anyone suspected that anything was amiss.

John Sörenson: John Emil Sörenson (September 15, 1889 – October 25, 1976) was a Swedish gymnast who competed in the 1920 Summer Olympics.

John Peurifoy: John Emil Peurifoy (August 9, 1907 – August 12, 1955) was an American diplomat, an ambassador in the early years of the Cold War.  He served as United States ambassador in Greece and Thailand and was the United States Ambassador to Guatemala during the 1954 coup that overthrew the democratic government of Jacobo Arbenz.

John Halver: John Emil Halver (April 21, 1922 – October 24, 2012) was an American biochemist known for his research into the nutritional biochemistry, physiology, cellular biochemistry of fish.  His work on the nutritional needs of fish led to modern methods of fish farming and fish feed production around the world.  He held a position with the United States Fish and Wildlife Service as director of the Western Fish Nutrition Laboratory in Cook, Washington, where Halver and his staff carried out reseaerch on the nutrient requirements for Pacific salmon."

Question: Who was born earlier, Richard Djerf or John Emil List?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "person_b": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "earlier_born_person_name": {
      "type": "string"
    },
    "earlier_birth_year": {
      "type": "integer"
    },
    "comparison_summary": {
      "type": "string"
    }
  },
  "required": [
    "person_a",
    "person_b",
    "earlier_born_person_name",
    "earlier_birth_year",
    "comparison_summary"
  ],
  "additionalProperties": false
}
