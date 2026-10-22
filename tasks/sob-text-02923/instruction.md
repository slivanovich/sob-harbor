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
List of I, Claudius episodes: This is a list of the 13 episodes of "I, Claudius", a 1976 BBC Television adaptation of Robert Graves' "I, Claudius" and "Claudius the God".  Written by Jack Pulman, it was one of the corporation's most successful drama serials of all time.  It also provided popular initial exposure for several actors who would eventually become well known, such as Derek Jacobi, Patrick Stewart, John Rhys-Davies and John Hurt.

Barbara Young (actress): Barbara Young (born 9 February 1936, Brighouse, West Riding of Yorkshire) is an English actress.  She is known for her role as the future Emperor Nero's mother, Agrippina, in the landmark 1976 BBC serial "I, Claudius".

Robert Craig-Morgan: Robert Craig-Morgan (born 1964 in Bromley, Kent) is an English actor who first appeared on television in the 1976 BBC production of "I Claudius" playing the Young Caligula, although he was best known for his character Justin Bennett in the children's drama series "Grange Hill" which he played for five years from the beginning of the series.

I, Claudius (radio adaptation): I, Claudius is a six-part 2010 radio adaptation of the novels "I, Claudius" and "Claudius the God" by Robert Graves.  Broadcast as part of the "Classic Serial" strand on BBC Radio 4, it was adapted by Robin Brooks and directed by Jonquil Panting, with music composed by David Pickvance.  Claudius was played by Tom Goodman-Hill and the series' cast is also notable for including Derek Jacobi, who played Claudius in the 1976 BBC TV adaptation of the same works.  The series was released as a BBC Audiobook on 6 January 2011.  It won the 2012 Audie Award in the "Audio Dramatization" category.

Derek Jacobi: Sir Derek George Jacobi, ( ; born 22 October 1938) is an English actor and stage director.

John Castle: John Castle (born 14 January 1940) is an English actor.  Castle has acted in theatre, film and television.  He is known for his role as Agrippa Postumus in the BBC television adaptation of "I, Claudius" (1976) and for playing Geoffrey II, Duke of Brittany, in the film "The Lion in Winter" (1968).  He also played Dr Carrasco as well as the prisoner called "The Duke" in the film "Man of La Mancha" (1972), and the villainous Paul McDagget in "RoboCop 3" (1993).

I, Claudius (TV series): I, Claudius is a 1976 BBC Television adaptation of Robert Graves' "I, Claudius" and "Claudius the God".  Written by Jack Pulman, it starred Derek Jacobi as Claudius, with Siân Phillips, Brian Blessed, George Baker, Margaret Tyzack, John Hurt, Patricia Quinn, Ian Ogilvy, Kevin McNally, Patrick Stewart, and John Rhys-Davies.

Jack Pulman: Jack Pulman (11 July 1925 – 29 May 1979) was an award-winning British television screenwriter, most famous for the critically acclaimed 1976 BBC television series, "I, Claudius", based on the novels "I Claudius" and "Claudius the God" by Robert Graves.

The Signalman (film): The Signalman is a 1976 BBC television adaptation of "The Signal-Man", an 1866 short story by Charles Dickens.  The story was adapted by Andrew Davies as the BBC's sixth "Ghost Story for Christmas", with Denholm Elliott starring as the signalman and Bernard Lloyd as the traveller, an unnamed character who acts as a plot device in place of the short story's narrator.

The Picnic: The Picnic (full title The Two Ronnies Present - The Picnic), is a 1976 BBC television film starring The Two Ronnies, and written by Ronnie Barker under the pseudonyms "Dave Huggett and Larry Keith".

Question: What English actor starred as Claudius in the 1976 BBC Television adaptation I, Claudius?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tv_series_title": {
      "type": "string",
      "description": "The title of the television series."
    },
    "adaptation_year": {
      "type": "integer",
      "description": "The year the television adaptation was released."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character played in the series."
    },
    "actor_information": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor."
        },
        "actor_nationality": {
          "type": "string",
          "description": "The nationality of the actor."
        }
      },
      "required": [
        "actor_name",
        "actor_nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "tv_series_title",
    "adaptation_year",
    "character_name",
    "actor_information"
  ],
  "additionalProperties": false
}
