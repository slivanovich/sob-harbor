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
Crooks Anonymous: Crooks Anonymous is a British comedy film from 1962.  Directed by Ken Annakin, it starred Leslie Phillips and Stanley Baxter and was notable for one of the earliest appearances of Julie Christie.

Value for Money: Value for Money is a 1955 British comedy film directed by Ken Annakin and starring John Gregson, Donald Pleasence, Leslie Phillips, Joan Hickson, Derek Farr and Diana Dors.

Very Important Person (film): Very Important Person (retitled A Coming Out Party in the United States) is a 1961 British comedy film, directed by Ken Annakin and written by Jack Davies and Henry Blyth.  The cast includes several well-known British comedy and character actors, including James Robertson Justice, Stanley Baxter in a dual role as a dour Scottish prisoner and a German prisoner-of-war camp officer, Eric Sykes, John Le Mesurier, Leslie Phillips and Richard Wattis.

Loser Takes All (film): Loser Takes All is a 1956 British comedy film directed by Ken Annakin, starring Glynis Johns, Rossano Brazzi, and Robert Morley, and based on a screenplay by Graham Greene.

Those Magnificent Men in their Flying Machines: Those Magnificent Men in their Flying Machines; Or, How I Flew from London to Paris in 25 Hours 11 Minutes is a 1965 British comedy film starring Stuart Whitman, Sarah Miles, Robert Morley, Terry-Thomas, James Fox and Alberto Sordi, directed and co-written by Ken Annakin.

Three Men in a Boat (1956 film): Three Men in a Boat is a 1956 British CinemaScope colour comedy film directed by Ken Annakin and starring Laurence Harvey, Jimmy Edwards, Shirley Eaton and David Tomlinson.  It is based on the 1889 novel "Three Men in a Boat" by Jerome K. Jerome.  The film received mixed reviews, but was a commercial success.

Glynis Johns: Glynis Johns (born 5 October 1923) is a retired Welsh stage, television and film actress, dancer, pianist, and singer.  Born in Pretoria, South Africa of Welsh origin, she is best known for creating the role of Desiree Armfeldt in "A Little Night Music" on Broadway, for which she won a Tony Award, and for playing Winifred Banks in Walt Disney's musical motion picture box office smash "Mary Poppins."  In both roles, she originated songs written specifically for her, including "Send in the Clowns", composed by Stephen Sondheim, and "Sister Suffragette", written by the Sherman Brothers.  She was nominated for an Oscar for her work in the 1960 film "The Sundowners".

Holiday Camp (film): Holiday Camp is a 1947 British comedy drama film directed by Ken Annakin, starring Jack Warner, Jimmy Hanley, Kathleen Harrison and Dennis Price set at the then popular Butlin's holiday camps.

You Know What Sailors Are (1954 film): You Know What Sailors Are is a 1954 British comedy film directed by Ken Annakin from a screenplay by Peter Rogers.  It starred Donald Sinden, Michael Hordern, Bill Kerr, Dora Bryan and Akim Tamiroff.

Miranda (1948 film): Miranda is a 1948 British comedy film, directed by Ken Annakin and written by Peter Blackmore, who also wrote the play of the same name from which the film was adapted.  Denis Waldock provided additional dialogue.  A light comedy, the film is about a beautiful and playful mermaid played by Glynis Johns and her effect on Griffith Jones' character.  Googie Withers and Margaret Rutherford are also featured in the film.  Glynis Johns and Margaret Rutherford reprised their roles in the 1954 sequel, "Mad About Men".

Question: Where was the star of Ken Annakin's 1956 British comedy born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the British comedy film directed by Ken Annakin in 1956."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "star_details": {
      "type": "object",
      "properties": {
        "star_name": {
          "type": "string",
          "description": "The name of the star whose birthplace is being identified."
        },
        "star_birthplace": {
          "type": "string",
          "description": "The city and country where the star was born."
        },
        "star_origin": {
          "type": "string",
          "description": "The origin or nationality of the star."
        }
      },
      "required": [
        "star_name",
        "star_birthplace",
        "star_origin"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The final answer to the question: the birthplace of the star."
    }
  },
  "required": [
    "film_title",
    "film_year",
    "director",
    "star_details",
    "answer"
  ],
  "additionalProperties": false
}
