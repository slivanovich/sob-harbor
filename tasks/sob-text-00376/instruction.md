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
Bad Moon Rising (Grimm): "Bad Moon Rising" is the 3rd episode of the supernatural drama television series "Grimm" of season 2 and the 25th overall, which premiered on August 27, 2012, on NBC.  The episode was written by Richard Hatem, and was directed by David Solomon.

Loner (The Secret Circle): "Loner" is the 3rd episode of the first season of the CW television series "The Secret Circle", and the series' 3rd episode overall.  It aired on September 29, 2011.  The episode was written by Richard Hatem and it was directed by Colin Bucksey.

One Angry Fuchsbau: "One Angry Fuchsbau" is the 17th episode and of the supernatural drama television series "Grimm" of season 2 and the 39th overall, which premiered on April 5, 2013, on NBC.  The episode was written by Richard Hatem, and was directed by Terrence O'Hara.

Big Feet: "Big Feet" is the 21st episode of the supernatural drama television series "Grimm" of season 1, which premiered on May 11, 2012, on NBC.  The episode was written by Richard Hatem from a story by Alan DiFiore and Dan E. Fesman, and was directed by Omar Madha.

University of California, Los Angeles: The University of California, Los Angeles (UCLA) is a public research university in the Westwood district of Los Angeles, California, United States.  It became the Southern Branch of the University of California in 1919, making it the second-oldest undergraduate campus of the ten-campus University of California system.  It offers 337 undergraduate and graduate degree programs in a wide range of disciplines.  UCLA enrolls about 31,000 undergraduate and 13,000 graduate students, and had 119,000 applicants for Fall 2016, including transfer applicants, the most applicants for any American university.

Richard Hatem: Richard Hatem (born November 2, 1966) is an American television and film screenwriter and producer.  He is a member of the Writers Guild of America (WGA).  He is also a professor on staff with the University of California, Los Angeles (UCLA), teaching a television writing class.

List of The Gates characters: This is a list of the characters featured on "The Gates" created by Grant Scharbo and Richard Hatem developed by ABC.

Miracles (TV series): Miracles is an American drama television program starring Skeet Ulrich and Angus Macfadyen.  Created by Richard Hatem and Michael Petroni, the series has sometimes been dubbed a "spiritual version of "The X-Files"" by its creators.  Following the pilot, David Greenwalt, co-creator of "Angel" (the spin-off of "Buffy the Vampire Slayer") served as the show's executive producer and head writer for the remaining twelve episodes.

The Mothman Prophecies (film): The Mothman Prophecies is a 2002 U.S. supernatural horror mystery film directed by Mark Pellington, based on the 1975 book of the same name by parapsychologist and Fortean author John Keel.  The screenplay was written by Richard Hatem.  The film stars Richard Gere as John Klein, a reporter who researches the legend of the Mothman.

The Thing with Feathers: "The Thing with Feathers" is the 16th episode of the supernatural drama television series "Grimm" of season 1, which premiered on April 6, 2012, on NBC.  The episode was written by Richard Hatem, and was directed by Darnell Martin.

Question: How many applicants did the university, for which Richard Hatem is a professor on staff, have for the Fall of 2016?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "university_name": {
      "type": "string",
      "description": "The name of the university where Richard Hatem is a professor."
    },
    "professor_name": {
      "type": "string",
      "description": "The name of the professor in question."
    },
    "application_year": {
      "type": "integer",
      "description": "The academic year for which the applicant data is provided."
    },
    "number_of_applicants": {
      "type": "integer",
      "description": "The total number of applicants for the specified year."
    },
    "applicant_details": {
      "type": "object",
      "properties": {
        "includes_transfer_applicants": {
          "type": "boolean",
          "description": "Indicates if transfer applicants are included in the total count."
        }
      },
      "required": [
        "includes_transfer_applicants"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "university_name",
    "professor_name",
    "application_year",
    "number_of_applicants",
    "applicant_details"
  ],
  "additionalProperties": false
}
