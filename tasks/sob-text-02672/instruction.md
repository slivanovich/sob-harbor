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
Dinesh D'Souza: Dinesh Joseph D'Souza ( ; born April 25, 1961) is an Indian American conservative political commentator, author and filmmaker.  From 2010 to 2012, he was president of The King's College, a Christian school in New York City.

George Will: George Frederick Will (born May 4, 1941) is an American conservative political commentator.  Will writes regular columns for "The Washington Post" and provides commentary for NBC News and MSNBC.  In 1986, "The Wall Street Journal" called him "perhaps the most powerful journalist in America", in a league with Walter Lippmann (1889–1974).  His numerous awards include the Pulitzer Prize for commentary in 1977.

Dana Loesch: Dana Loesch ( , née Eaton, born September 28, 1978) is an American conservative political commentator.  She is a talk radio host, a television host for The Blaze, an author, and a spokesperson for the National Rifle Association.  Loesch has appeared as a guest on television networks such as Fox News, CNN, CBS, ABC, and HBO.

America: Imagine the World Without Her: America: Imagine the World Without Her is a 2014 American political documentary film by Dinesh D'Souza based on his book of the same name.  It is a follow-up to his film "" (2012).  In the film, D'Souza contends that parts of United States history are improperly and negatively highlighted by liberals, which he seeks to counter with positive highlights.  Topics addressed include appropriation of Native American and Mexican lands, slavery, and matters relating to foreign policy and capitalism.  D'Souza collaborated with John Sullivan and Bruce Schooley to adapt his book of the same name into a screenplay.  D'Souza produced the film with Gerald R. Molen and directed it with Sullivan.  The film combined historical reenactments with interviews with different political figures.

Ben Ferguson: Benjamin Grant Ferguson (born August 28, 1981) is an American radio host, CNN conservative political commentator, and author.  His nationally syndicated radio show, "The Ben Ferguson Show", formerly aired throughout the United States on Radio America and is now syndicated by ICON Radio Network, of which Ben is the founder and owner, on Sundays from 6 - 9 PM CT.  He is also a regular political commentator on CNN.

Ben Shapiro: Benjamin Aaron Shapiro (born January 15, 1984) is an American conservative political commentator, columnist, author, radio talk show host, and lawyer.

Derek Khanna: Derek Khanna (born Derek Satya Khanna sometime after 1984), is a Washington, D.C.-based Indian American conservative political commentator and columnist.  He has written for the "Washington Post" and "The Guardian", maintains a blog with Forbes, and is a regular contributor with The Atlantic, National Review Online, Human Events and Politix.  He is also an adviser and Board member to several technology start-ups.  He was listed on Forbes's 2014 list of 30 under 30 for law in policy for his work on technology policy and the successful phone unlocking campaign which resulted in the Unlocking Consumer Choice and Wireless Competition Act (S. 517/ P.L. 113-144) passing Congress and being signed into law by President Obama on August 1, 2014.

Bay Buchanan: Angela Marie "Bay" Buchanan (born December 23, 1948) is a prominent conservative political commentator who served as Treasurer of the United States under President Ronald Reagan.  She is also the sister of conservative political commentator Pat Buchanan.

Tomi Lahren: Tomi Lahren ( ; born August 11, 1992) is an American conservative political commentator, political operative, and former television host.  She is best known for hosting "Tomi" on TheBlaze.  She previously hosted "On Point with Tomi Lahren" on One America News Network (OANN).  In August 2017 Lahren joined Fox News as a contributor.

Pat Buchanan: Patrick Joseph Buchanan ( ; born November 2, 1938) is an American conservative political commentator, author, syndicated columnist, politician and broadcaster.  Buchanan was a senior advisor to U.S. Presidents Richard Nixon, Gerald Ford and Ronald Reagan, and was an original host on CNN's "Crossfire".  He sought the Republican presidential nomination in 1992 and 1996.  He ran on the Reform Party ticket in the 2000 presidential election.

Question: When was the Indian American conservative political commentator, author and filmmaker born who's documentary film is America: Imagine the World Without Her? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the person."
        },
        "occupations": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of the person's occupations."
        },
        "birth_date": {
          "type": "object",
          "properties": {
            "year": {
              "type": "integer",
              "description": "The birth year of the person."
            },
            "month": {
              "type": "string",
              "description": "The birth month of the person."
            },
            "day": {
              "type": "integer",
              "description": "The birth day of the person."
            }
          },
          "required": [
            "year",
            "month",
            "day"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "nationality",
        "occupations",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "associated_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the documentary film associated with the person."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The complete birth date of the person."
    }
  },
  "required": [
    "person_details",
    "associated_film",
    "final_answer"
  ],
  "additionalProperties": false
}
