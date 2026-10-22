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
Dentist in the Chair: Dentist in the Chair is a 1960 British comedy film, directed by Don Chaffey and starring Bob Monkhouse, Ronnie Stevens, Eric Barker and Vincent Ball.  The screenplay was written by Val Guest, and based on a novel by Matthew Finch.  Additional scenes were written by Bob Monkhouse and George Wadmore.

The Golden Shot: The Golden Shot was a British television game show produced by ATV for ITV between 1 July 1967 and 13 April 1975, based on the German TV show "Der goldene Schuß".  It is most commonly associated with host Bob Monkhouse, though, three other presenters also hosted the show during its lifetime.  Hostess Anne Aston was on hand to read out the scores achieved by the contestants, and each month a "Maid of the Month", usually a glamour model of the era, would demonstrate the prizes and announce the contestants.  When Bob Monkhouse returned to present the show in 1974, he was joined by co-hostess (to Anne Aston) Wei Wei Wong, recently seen in "The Man with the Golden Gun" and an ex-member of the "Young Generation" and "Second Generation" dance troupes.  This was one of the earliest regular appearances by an East Asian woman on British TV.

The Bob Monkhouse Show: The Bob Monkhouse Show was an entertainment, variety and talk show presented by Bob Monkhouse.

The Mysterious Mr. Wong: The Mysterious Mr. Wong is a tongue-in-cheek 1934 mystery film starring Bela Lugosi as a powerful Fu Manchu type criminal mastermind of the Chinatown underworld, and Wallace Ford as a wisecracking reporter.  The film is based on Harry Stephen Keeler's 1928 short story "The Strange Adventure of the Twelve Coins of Confucius" one of three stories in Keeler's book "Sing Sing Nights".  Despite the name of the title character and being directed by William Nigh, it has no relation to Monogram Pictures later Mr Wong film series.  The character of Mr. Wong does not appear in the original story.

The Bob Monkhouse Hour: The Bob Monkhouse Hour was a British televised variety show from 1958 which was fronted by the comedian Bob Monkhouse, and featured musical stars of the day, contemporary comedians, and various other variety acts.

Celebrity Squares: Celebrity Squares is a British comedy game show based on the American comedy game show "Hollywood Squares".  It first ran from 20 July 1975 to 7 July 1979 and was hosted by Bob Monkhouse, then from 8 January 1993 to 3 January 1997 and was also hosted by Monkhouse.

Harry Stephen Keeler: Harry Stephen Keeler (November 3, 1890 – January 22, 1967) was a prolific but little-known American author of mysteries and science fiction.

Bob Monkhouse: Robert Alan "Bob" Monkhouse, OBE (1 June 1928 – 29 December 2003) was an English entertainer and comedian.

My Pal Bob: My Pal Bob was a United Kingdom television sitcom originally shown in ten episodes from 1957 to 1958.  Written by Bob Monkhouse and Denis Goodwin, the show starred Bob Monkhouse and narrated by Denis Goodwin.  All recording of the episodes was thought be destroyed until it was discovered that Monkhouse had kept a number episodes from shows including "My Pal Bob" in his own private archive.

Sing Sing Nights (film): Sing Sing Nights is a 1934 American film directed by Lewis D. Collins, based on the 1927 novel by American Author Harry Stephen Keeler (Hutchinson 1927, Dutton 1928, Ward & Lock 1929).

Question: Which man was a comedian, Harry Stephen Keeler or Bob Monkhouse?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "identified_comedian": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person identified as the comedian."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the comedian."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions for the comedian."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the comedian."
        },
        "death_date": {
          "type": "string",
          "description": "The death date of the comedian."
        }
      },
      "required": [
        "name",
        "nationality",
        "professions",
        "birth_date",
        "death_date"
      ],
      "additionalProperties": false
    },
    "other_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the other person mentioned in the question."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the other person."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions for the other person."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the other person."
        },
        "death_date": {
          "type": "string",
          "description": "The death date of the other person."
        }
      },
      "required": [
        "name",
        "nationality",
        "professions",
        "birth_date",
        "death_date"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The name of the man who was a comedian."
    }
  },
  "required": [
    "identified_comedian",
    "other_person",
    "answer"
  ],
  "additionalProperties": false
}
