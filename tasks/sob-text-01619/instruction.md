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
Magician (fantasy): An enchanter, enchantress, mage, magician, sorcerer, sorceress, warlock, witch, or wizard, is someone who uses or practices magic derived from supernatural or occult sources.  Magicians are common figures in works of fantasy, such as fantasy literature and role-playing games, and enjoy a rich history in mythology, legends, fiction, and folklore.

Heathkit H11: The Heathkit H11 Computer was an early kit-format personal computer introduced in 1978.  It was essentially a Digital Equipment PDP-11 in a small-form-factor case, designed by Heathkit.  The H11 was one of the first 16-bit personal computers, at a list price of US$1,295, but was too expensive for most Heathkit customers and was discontinued in 1982.

Polycera atra: Polycera atra, common name orange-spike polycera or sorcerer's sea slug, is a species of sea slug, a nudibranch, a marine gastropod mollusk in the family Polyceridae.

Tulip System-1: The Tulip system I was a 16-bit personal computer based on the Intel 8086 and made by Tulip Computers, formerly an import company for the Exidy Sorcerer, called "CompuData Systems".

Exidy Sorcerer: The Sorcerer is one of the early home computer systems, released in 1978 by the videogame company Exidy.  It was comparatively advanced when released, especially when compared to the contemporary more commercially successful Commodore PET and TRS-80, but due to a number of problems, including a lack of marketing, the machine remained relatively unknown.  Exidy eventually pulled it from the market in 1980, and today they are a coveted collector's item.

La figlia del mago: La figlia del mago ("The Sorcerer's Daughter") is a children's opera in two acts by Lorenzo Ferrero set to an Italian-language libretto by Marco Ravasini.  It was completed in 1981 and subtitled "giocodramma melodioso ", a wordplay on "melodramma giocoso ".  The libretto, inspired by Mario Lavagetto's book "Quei più modesti romanzi: il libretto nel melodramma di Verdi", is written in an imaginary language which emphasises the element of play.  The music is a sequence of closed numbers "which spoof the most common operatic conventions."  The aim of the opera is to show children how Italian opera functions.  Alongside professional singers, children take mime roles.

Resurrection (song): "Resurrection" is the second single from rapper Common's 1994 album "Resurrection".  Its piano-led beat, produced by No I.D., contains samples from "The Signs Pt.  II" by David Axelrod, "Dolphin Dance" by Ahmad Jamal, "Sorcerer of Isis" by Power of Zeus, "Ice" by Spirit and both "Why Can't People Be Colors Too?"  and "Help Is on the Way" by The Whatnauts.  The song contains free-associative lyrics by Common and scratches by DJ Sinister that "blend harmoniously with the jazzy melody."  Nick Quested directed the "Resurrection" music video.

Question: what does Exidy Sorcerer and Heathkit H11 have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_category": {
      "type": "string",
      "description": "The general category that both items belong to."
    },
    "shared_characteristics": {
      "type": "array",
      "description": "A list of common attributes or features shared by both items.",
      "items": {
        "type": "string"
      }
    },
    "release_year": {
      "type": "integer",
      "description": "The year both items were introduced or released."
    },
    "entities_involved": {
      "type": "array",
      "description": "Details about each entity mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "type": {
            "type": "string",
            "description": "The type or classification of the entity."
          }
        },
        "required": [
          "name",
          "type"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "common_category",
    "shared_characteristics",
    "release_year",
    "entities_involved"
  ],
  "additionalProperties": false
}
