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
William H. Ray House: The William H. Ray House is a historic house located at 415 South University Avenue in Provo, Utah.  A prominent non-Mormon in Provo, Utah, William H. Ray was one of the founders of the State Bank of Provo.  A financier, banker, and broker, Ray organized the Ray Investment Company as an insurance and real estate brokerage firm.  The William Ray House, which was built around 1898, "Combines Romanesque Revival elements with classical detailing in a personalized manner (Historic Provo 2002)."  The William H. Ray House was added to the National Register of Historic Places in 1982 and was designated to the Provo City Historic Landmark Register on April 28, 1995.

Hector: In Greek mythology and Roman Mythology, Hector (Ἕκτωρ "Hektōr", ] ) was a Trojan prince and the greatest fighter for Troy in the Trojan War.  As the first-born son of King Priam and Queen Hecuba, who was a descendant of Dardanus and Tros, the founder of Troy, he was a prince of the royal house and the heir apparent to his father's throne.  He was married to Andromache, with whom he had an infant son, Scamandrius (whom the people of Troy called Astyanax).  He acted as leader of the Trojans and their allies in the defense of Troy, "killing 31,000 Greek fighters", offers Hyginus.  During the European Middle Ages, Hector figures as one of the Nine Worthies noted by Jacques de Longuyon, known not only for his courage but also for his noble and courtly nature.  Indeed, Homer places Hector as peace-loving, thoughtful as well as bold, a good son, husband and father, and without darker motives.  James Redfield writes of Hector as a "martyr to loyalties, a witness to the things of this world, a hero ready to die for the precious imperfections of ordinary life."

William H. Gass: William Howard Gass (born July 30, 1924) is an American novelist, short-story writer, essayist, critic, and former philosophy professor.  He has written three novels, three collections of short stories, a collection of novellas, and seven volumes of essays, three of which have won National Book Critics Circle Award prizes and one of which, "A Temple of Texts" (2006), won the Truman Capote Award for Literary Criticism.  His 1995 novel "The Tunnel" received the American Book Award.  His 2013 novel "Middle C" won the 2015 William Dean Howells Medal.

James Redfield (Iowa): James Redfield (March 27, 1824 – October 6, 1864) may have been an American politician and Civil War officer.  He might have died at the Battle of Allatoona.

The Celestine Prophecy: The Celestine Prophecy is a 1993 novel by James Redfield that discusses various psychological and spiritual ideas rooted in multiple ancient Eastern traditions and New Age spirituality.  The main character undertakes a journey to find and understand a series of nine spiritual insights in an ancient manuscript in Peru.  The book is a first-person narrative of the narrator's spiritual awakening as he goes through a transitional period of his life.

William Henry Seward (Brooks): William Henry Seward, also known as Let Us Make the Treaty Tonight, the Monument to William H. Seward, and William H. Seward, is an outdoor bronze sculpture of William H. Seward by Richard Brooks, located in Volunteer Park in Seattle, Washington, United States.  The statue was unveiled at the Alaska–Yukon–Pacific Exposition in 1909 and relocated to the park the following year.  It cost $15,000 and was funded by private donors.

William H. Bell (fl. 1860s): William H. Bell was an African-American servant of William Seward, who is best known for being the servant who greeted William Seward's assassin the night of April 14, 1865, and for giving testimony against Lewis Powell during the Abraham Lincoln military tribunal.  William H. Bell was born sometime around 1845.  William H. Bell's occupation at the Seward's house at the time of the assassination was "second waiter".  He later went on to practice law.

The Tenth Insight: Holding the Vision: The Tenth Insight: Holding the Vision is the second novel in "The Celestine Series", beginning with "The Celestine Prophecy", by James Redfield.  It was published in 1996.

James Redfield: James Redfield (born March 19, 1950) is an American author, lecturer, screenwriter and film producer.  He is notable for his novel "The Celestine Prophecy".

The Celestine Prophecy (film): The Celestine Prophecy is a 2006 American film directed by Armand Mastroianni and starring Matthew Settle, Thomas Kretschmann, and Sarah Wayne Callies.  The film is based on James Redfield's best-selling novel of the same name.

Question: William H. Gass and James Redfield, both are Americans, that have which occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_occupation": {
      "type": "string",
      "description": "The occupation shared by both individuals."
    },
    "individuals_sharing_occupation": {
      "type": "array",
      "description": "Details about the individuals who share the common occupation.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the individual."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the individual."
          },
          "listed_occupations": {
            "type": "array",
            "description": "All occupations explicitly listed for this individual in the context.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "nationality",
          "listed_occupations"
        ],
        "additionalProperties": false
      }
    },
    "number_of_individuals": {
      "type": "integer",
      "description": "The count of individuals identified as sharing this occupation."
    }
  },
  "required": [
    "common_occupation",
    "individuals_sharing_occupation",
    "number_of_individuals"
  ],
  "additionalProperties": false
}
