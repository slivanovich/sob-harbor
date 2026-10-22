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
Boris Delaunay: Boris Nikolaevich Delaunay or Delone (Russian: Бори́с Никола́евич Делоне́ ; March 15, 1890 – July 17, 1980) was one of the first Russian mountain climbers and a Soviet/Russian mathematician, and the father of physicist Nikolai Borisovich Delone.

Nikolai Borisovich Delone: Nikolai Delaunay, Jr. (aka Delone, Nikolai Borisovich) (22 May 1926 – 11 September 2008) was a born in Leningrad, USSR (now Saint Petersburg, Russia).

Delaunay triangulation: In mathematics and computational geometry, a Delaunay triangulation for a given set P of discrete points in a plane is a triangulation DT(P) such that no point in P is inside the circumcircle of any triangle in DT(P).  Delaunay triangulations maximize the minimum angle of all the angles of the triangles in the triangulation; they tend to avoid sliver triangles.  The triangulation is named after Boris Delaunay for his work on this topic from 1934.

Nikolay Yusupov: Prince Nikolai Borisovich Yusupov (Russian: Князь Никола́й Бори́сович Юсу́пов ; 26 October [O.S. 15 October] 1750 – 15 July 1831) was a Russian nobleman and art collector of the House of Yusupov.

Nikolai Kolesov: Nikolai Borisovich Kolesov (Russian: Николай Борисович Колесов ; born February 16, 1956; died August 23, 1998) was a Russian professional footballer.  He made his professional debut in the Soviet Top League in 1976 for FC Dynamo Moscow.

Trachtenberg system: The Trachtenberg system is a system of rapid mental calculation.  The system consists of a number of readily memorized operations that allow one to perform arithmetic computations very quickly.  It was developed by the Russian Jewish engineer Jakow Trachtenberg in order to keep his mind occupied while being held in a Nazi concentration camp.

Nikolai Borisovich Galitzine: Prince Nikolai Borisovich Golitsyn (Russian: Николай Борисович Голицын , alternatively spelled Galitzin; 8 December/19 December 1794 – 22 October/3 November 1866) was a Russian aristocrat, of the Galitzine family.  He was an amateur musician, and is known particularly for his commissioning three string quartets — opp.  127, 130 and 132 — from Ludwig van Beethoven, which are among the composer's group of late string quartets.  His parents were Boris Andreevich Golitsyn and his wife Ana, whilst one of his sisters was the philanthropist Tatiana Potemkina.

Jakow Trachtenberg: Jakow Trachtenberg (17 June 1888 – 1953) was a Jewish mathematician who developed the mental calculation techniques called the Trachtenberg system.

Nikolai B. Kopnin: Nikolai Borisovich Kopnin (May 17, 1946 – October 20, 2013) was a Russian physicist specializing in superconductivity.

Nikolai Obukhov: Nikolai Borisovich Obukhov (Russian: Николай Борисович Обухов ; Nicolai, Nicolas, Nikolay; Obukhow, Obouhow, Obouhov, Obouhoff) (22 April 189213 June 1954) was a modernist and mystic Russian composer, active mainly in France.  An avant-garde figure who took as his point of departure the late music of Scriabin, he fled Russia along with his family after the Bolshevik Revolution, settling in Paris.  His music is notable for its religious mysticism, its unusual notation, its use of an idiosyncratic 12-tone chromatic language, and its pioneering use of electronic musical instruments in the era of their earliest development.

Question: Which mathematician was the father of physicist Nikolai Borisovich Delone: Jakow Trachtenberg or Boris Delaunay?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mathematician": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the mathematician."
        },
        "occupation": {
          "type": "string",
          "description": "The primary occupation of the mathematician mentioned in the context."
        }
      },
      "required": [
        "name",
        "occupation"
      ],
      "additionalProperties": false
    },
    "physicist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the physicist."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "relationship": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "description": "The type of relationship between the mathematician and the physicist (e.g., 'father_of')."
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The name of the mathematician who is the father of the physicist."
    }
  },
  "required": [
    "mathematician",
    "physicist",
    "relationship",
    "answer"
  ],
  "additionalProperties": false
}
