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
The Flamingo Kid: The Flamingo Kid is a 1984 American comedy film directed by Garry Marshall and written by Marshall, Neal Marshall and Bo Goldman.  It stars Matt Dillon, Richard Crenna, Hector Elizondo, and Janet Jones.  It tells the story of a working class boy who takes a summer job at a beach resort and learns valuable life lessons.  It was the first movie to receive a PG-13 rating, although it was the fifth to be released with that rating, after "Red Dawn", "The Woman in Red", "Dreamscape", and "Dune".

Melendez Films: Melendez Films is a film animation studio.  It was founded in 1969 as a London subsidiary of Bill Melendez Productions (best known for producing the Peanuts specials) by Steven C. Melendez (son of animator Bill Melendez).

Ronny Hallin: Ronny Hallin (born Ronelle L. Marshall on January 2, 1938) is an American television producer and actress, and sister of Penny Marshall and Garry Marshall, she is best known for her work on the television shows "Happy Days", "Mork & Mindy", and "Step by Step".

Cathy's Valentine: Cathy's Valentine is a 1989 animated television special based on the "Cathy" comic strip by Cathy Guisewite.  It features Kathleen Wilhoite as the voice of Cathy Andrews, and was written by Guisewite, executive-produced by Lee Mendelson, produced by Bill Melendez, and directed by Evert Brown.

Bill Melendez: José Cuauhtémoc Meléndez (November 15, 1916 – September 2, 2008), known as Bill Melendez, was a Mexican American character animator, film director, voice artist and producer, known for his cartoons for Walt Disney Productions (working on four Disney films "Pinocchio", "Fantasia", "Dumbo" and "Bambi"), Warner Bros.  Cartoons, UPA and the "Peanuts" series.  Melendez provided the voices of Snoopy and Woodstock in the latter as well.

Happiness Is a Warm Blanket, Charlie Brown: Happiness Is a Warm Blanket, Charlie Brown is a "Peanuts" television special that was released in 2011.  The special is the 45th "Peanuts" special and the first produced without Bill Melendez on the production team.  It is also the first special without the direct involvement of "Peanuts" creator Charles M. Schulz, Lee Mendelson Productions or Bill Melendez Productions (it is unknown, though, if Lee Mendelson also worked on this special).  In addition, it is the first "Peanuts" special produced in part under Warner Bros.  Television, which holds the home media distribution rights to the Peanuts specials.

Garry Marshall: Garry Kent Marshall (November 13, 1934 – July 19, 2016) was an American actor, director, producer, writer, and voice artist best known for creating "Happy Days" and its various spin-offs, developing Neil Simon's 1965 play "The Odd Couple" for television, and directing "Pretty Woman", "Runaway Bride", "Valentine's Day", "New Year's Eve", "Mother's Day", ""The Princess Diaries", and "".  He provided the voice of Buck Cluck in "Chicken Little".

Steven C. Melendez: Steven Cuitlahuac Melendez is an American film and television director, producer and animator.  He is the second son of "Peanuts" animator Bill Melendez.

The Peanuts Movie: The Peanuts Movie (known in some countries as Snoopy and Charlie Brown: The Peanuts Movie) is a 2015 American 3D computer-animated comedy film produced by Blue Sky Studios and distributed by 20th Century Fox, based on Charles M. Schulz's comic strip "Peanuts".  The film is directed by Steve Martino and written by Craig and Bryan Schulz (Schulz's son and grandson, respectively), and Cornelius Uliano, and stars the voices of Noah Schnapp as Charlie Brown and, via archival recordings, Bill Melendez as Snoopy and Woodstock.  It is the fifth full-length "Peanuts" film, and the first feature film in 35 years.  It commemorates the 65th anniversary of the comic strip and the 50th anniversary of the TV special "A Charlie Brown Christmas", and was released on November 6, 2015.

Hank Smith (animator): Henry "Hank" Smith was a cartoon animator, who worked for many Hollywood animation studios during the 1950s, 1960s, 1970s and 1980s.  His work includes numerous cartoons for television, including many featuring "Mr. Magoo", "The Road Runner", "Fat Albert", and many of the "Peanuts" television specials with Bill Melendez.  He was the brother of Frank Smith and Paul J. Smith.

Question: Who has more work to be known for, Bill Melendez or Garry Marshall?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_subject_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person being compared."
        },
        "roles_and_works": {
          "type": "array",
          "description": "A list of distinct roles and works attributed to this person in the context.",
          "items": {
            "type": "string"
          }
        },
        "work_count": {
          "type": "integer",
          "description": "The total count of distinct roles and works for this person."
        }
      },
      "required": [
        "name",
        "roles_and_works",
        "work_count"
      ],
      "additionalProperties": false
    },
    "comparison_subject_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person being compared."
        },
        "roles_and_works": {
          "type": "array",
          "description": "A list of distinct roles and works attributed to this person in the context.",
          "items": {
            "type": "string"
          }
        },
        "work_count": {
          "type": "integer",
          "description": "The total count of distinct roles and works for this person."
        }
      },
      "required": [
        "name",
        "roles_and_works",
        "work_count"
      ],
      "additionalProperties": false
    },
    "person_with_more_work": {
      "type": "string",
      "description": "The name of the person who has more work to be known for, based on the context."
    },
    "more_work_count": {
      "type": "integer",
      "description": "The count of works for the person identified as having more work."
    }
  },
  "required": [
    "comparison_subject_1",
    "comparison_subject_2",
    "person_with_more_work",
    "more_work_count"
  ],
  "additionalProperties": false
}
