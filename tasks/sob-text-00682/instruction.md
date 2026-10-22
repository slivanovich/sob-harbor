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
The Pleasure Garden (1953 film): The Pleasure Garden is a short film written and directed by James Broughton in 1953.  Among its crew was Peter Price as sound editor.  Cast members included the subsequent director Lindsay Anderson and Broughton's artistic collaborator Kermit Sheets.

All Killer, No Filler: The Anthology: All Killer, No Filler: The Anthology (also called The Jerry Lee Lewis Anthology: All Killer, No Filler!)  is a 1993 box set collecting 42 songs by rock and roll and rockabilly pioneer Jerry Lee Lewis from the mid-1950s to the 1980s, including 27 charting hits.  The album has been critically well received.  In 2003, "Rolling Stone" listed the album at #245 in its list of "Rolling Stone's 500 Greatest Albums of All Time".  "Country Music: The Rough Guide" indicated that "[t]his is the kind of full-bodied, decades-spanning treatment that Lewis's long, diverse career more than well deserves."

The Adventures of Jimmy: The Adventures of Jimmy (1950) is an early, short experimental film directed by, and starring, James Broughton.  It was Broughton's second film as sole director, following Mother's Day (1948), and was filmed by Art in Cinema founder Frank Stauffacher with an original musical score by Weldon Kees.

Smile (musical): Smile is a musical with music by Marvin Hamlisch and book and lyrics by Howard Ashman.  It was originally produced on Broadway in 1986.  The musical is based loosely on the 1975 comedy film of the same title, from a screenplay by Jerry Belson.

Smile (1975 film): Smile is a 1975 DeLuxe Color satirical comedy-drama film directed by Michael Ritchie with a screenplay by Jerry Belson about a beauty pageant in Santa Rosa, California.

James Broughton: James Broughton (November 10, 1913 – May 17, 1999) was an American poet and poetic filmmaker.  He was part of the San Francisco Renaissance, a precursor to the Beat poets.  He was an early bard of the Radical Faeries as well as a member of The Sisters of Perpetual Indulgence, serving the community as Sister Sermonetta.

Surrender (1987 film): Surrender is a 1987 American comedy film that was written and directed by Jerry Belson.  It stars Sally Field, Michael Caine, Steve Guttenberg, Peter Boyle and Iman.  Caine, Field and Boyle previously collaborated together in "Beyond the Poseidon Adventure".

Luchita Hurtado: Luchita Hurtado (Caracas, Venezuela, October 28, 1920) is a painter from Santa Monica, California and Arroyo Seco, New Mexico.  Her second husband was artist and collector Wolfgang Paalen.  She lived and traveled in Mexico with Paalen, encountering Rufino Tamayo, Frida Kahlo, Remedios Varo, Leonora Carrington, Edward James, Giles Healey and Sheila Healey.  Moving to San Francisco, her contacts with artists and collectors included Isamu Noguchi, Gordon Onslow Ford, Jacqueline Johnson, Lucienne Bloch, James Broughton, Rene d'Harnoncourt and Robert Motherwell.

The End (1978 film): The End is a 1978 American black comedy directed by and starring Burt Reynolds, written by Jerry Belson, and with music composed by Paul Williams.  The film also stars Dom DeLuise, Sally Field, Strother Martin, David Steinberg, Joanne Woodward, Norman Fell, Myrna Loy, Kristy McNichol, Pat O'Brien, Robby Benson and Carl Reiner.

Jerry Belson: Jerry Belson (July 8, 1938 – October 10, 2006) was a writer, director, and producer of Hollywood films for over forty years.

Question: Between Jerry Belson and James Broughton, who had a more diverse career?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a_name": {
      "type": "string",
      "description": "The name of the first person being compared."
    },
    "person_a_career_details": {
      "type": "object",
      "properties": {
        "primary_professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Main professional roles of the first person."
        },
        "artistic_mediums": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Artistic mediums or industries the first person worked in."
        }
      },
      "required": [
        "primary_professions",
        "artistic_mediums"
      ],
      "additionalProperties": false
    },
    "person_b_name": {
      "type": "string",
      "description": "The name of the second person being compared."
    },
    "person_b_career_details": {
      "type": "object",
      "properties": {
        "primary_professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Main professional roles of the second person."
        },
        "artistic_mediums": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Artistic mediums or industries the second person worked in."
        },
        "other_affiliations": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other significant groups or movements the second person was part of."
        }
      },
      "required": [
        "primary_professions",
        "artistic_mediums"
      ],
      "additionalProperties": false
    },
    "person_with_more_diverse_career": {
      "type": "string",
      "description": "The name of the person identified as having a more diverse career."
    },
    "diversity_reasoning": {
      "type": "string",
      "description": "Explanation for why one person's career is considered more diverse."
    }
  },
  "required": [
    "person_a_name",
    "person_a_career_details",
    "person_b_name",
    "person_b_career_details",
    "person_with_more_diverse_career",
    "diversity_reasoning"
  ],
  "additionalProperties": false
}
