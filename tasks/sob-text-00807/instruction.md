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
Why Must I Die?: Why Must I Die?  is a 1960 neo noir film directed by Roy Del Ruth, and starring Terry Moore and Debra Paget.  It was released by American International Pictures as a double feature with "The Jailbreakers".  This was director Roy Del Ruth's final film.

Glee (season 4): The fourth season of the Fox musical comedy-drama television series "Glee" was commissioned on April 9, 2012.  It premiered on September 13, 2012 and is produced by 20th Century Fox Television, Ryan Murphy Television and Brad Falchuk Teley-Vision with executive producers Dante Di Loreto and series co-creators Ryan Murphy, Brad Falchuk and Ian Brennan.

Glee (season 2): The second season of the musical comedy-drama television series "Glee" originally aired between September 21, 2010 and May 24, 2011 on Fox in the United States.  The 22-episode season was produced by 20th Century Fox Television and Ryan Murphy Television, with executive producers Dante Di Loreto and series co-creators Ryan Murphy and Brad Falchuk, with the other series co-creator, Ian Brennan, as co-executive producer.

Scream Queens (2015 TV series): Scream Queens is an American comedy horror television series that aired on Fox from September 22, 2015 to December 20, 2016.  The series was created by Ryan Murphy, Brad Falchuk, and Ian Brennan and produced by Murphy, Falchuk, Brennan, and Alexis Martin Woodall.  "Scream Queens" is produced by 20th Century Fox Television, Ryan Murphy Productions, Brad Falchuck Teley-vision, and Prospect Films.  The first season takes place at the fictional Wallace University, being produced in New Orleans, Louisiana.  One of the sororities, Kappa Kappa Tau, becomes plagued by a serial killer, who uses the university's Red Devil mascot as a disguise.

Girl Crazy (1929 film): Girl Crazy was a 1929 comedy film directed by Mack Sennett and starring Andy Clyde as "a girl-crazy sexagenarian".  The film's story is credited to Hampton Del Ruth, Alfred J. Goulding, Harry McCoy, Earle Rodney, and Mack Sennett.

The Alligator People: The Alligator People is a 1959 CinemaScope science fiction horror film directed by Roy Del Ruth.  It stars Beverly Garland, Bruce Bennett and Lon Chaney Jr. This film was the penultimate feature directed by Del Ruth and quite different than those of his days at Warner Bros.

Hampton Del Ruth: Hampton Del Ruth (September 7, 1879 – May 15, 1958) was an American film actor, director, screenwriter, and film producer.  Among other work, he wrote the intertitles for the final American studio-made silent film "" (1935).

Ryan Murphy (writer): Ryan Patrick Murphy (born November 30, 1965) is an American screenwriter, director and producer.  Murphy is best known for creating/co-creating/producing a number of successful television series, including the FX medical drama "Nip/Tuck" (2003–10), the Fox musical comedy-drama "Glee" (2009–15), and the FX anthology series "American Horror Story" (2011–present), "American Crime Story" (2016–present) and "Feud" (2017–present).  He is also known for directing the 2010 film adaptation of Elizabeth Gilbert's bestselling memoir "Eat, Pray, Love" and the 2014 HBO film adaptation of Larry Kramer's "The Normal Heart", which earned a Primetime Emmy Award for Outstanding Television Movie.

List of Scream Queens (2015 TV series) episodes: "Scream Queens" is an American comedy horror television series created for Fox by Ryan Murphy, Brad Falchuk and Ian Brennan and produced by Murphy, Falchuk, Brennan and Alexis Martin Woodall.  The series is produced by 20th Century Fox Television, Ryan Murphy Productions, Brad Falchuck Teley-vision and Prospect Films.  The series premiered on September 22, 2015.  The second season premiered on September 20, 2016.

Glee (season 3): The third season of the musical comedy-drama television series "Glee" was commissioned on May 23, 2010 by Fox while the first season aired.  It aired between September 20, 2011 and May 22, 2012, and was produced by 20th Century Fox Television and Ryan Murphy Television, with executive producers Dante Di Loreto and series co-creators Ryan Murphy, Brad Falchuk and Ian Brennan.

Question: Which director is also an actor, Hampton Del Ruth or Ryan Murphy?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_director_name": {
      "type": "string",
      "description": "The name of the person who is both an actor and a director."
    },
    "is_director": {
      "type": "boolean",
      "description": "True if the person is identified as a director."
    },
    "is_actor": {
      "type": "boolean",
      "description": "True if the person is identified as an actor."
    },
    "other_known_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of other professions known for this person."
    },
    "compared_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person being compared against."
        },
        "is_director": {
          "type": "boolean",
          "description": "True if the compared person is identified as a director."
        },
        "is_actor": {
          "type": "boolean",
          "description": "True if the compared person is identified as an actor."
        },
        "other_known_professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of other professions known for the compared person."
        }
      },
      "required": [
        "name",
        "is_director",
        "is_actor",
        "other_known_professions"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_director_name",
    "is_director",
    "is_actor",
    "other_known_professions",
    "compared_person"
  ],
  "additionalProperties": false
}
