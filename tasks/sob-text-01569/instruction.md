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
Symkaria: Symkaria is a fictional Eastern European country appearing in American comic books published by Marvel Comics.  The country was created by Tom DeFalco for the Marvel Universe.  It is one of several fictional countries in Eastern Europe created for Marvel Comics.  The fictional country is mostly known as being the home of Silver Sable and the Wild Pack team though it is used throughout the Marvel Universe.  The country has appeared in issues of "Silver Sable", "Silver Sable and the Wild Pack", "The Amazing Spider-Man", "Thunderbolts", "Citizen V and the V-Battalion", and other comics published by Marvel Comics.

List of Inhumans: The following is a list of known fictional characters who are Inhumans, a race of superhumans appearing in Marvel Comics and media inspired by them.

Deviant (comics): The Deviants are a fictional race of superhumans appearing in American comic books published by Marvel Comics.

Makkari (comics): Makkari ( ), formerly known as Hurricane and Mercury, is a fictional character appearing in American comic books published by Marvel Comics.  The character is depicted as a member of the Eternals, a race of superhumans in the Marvel Universe.  He was created by writer-artist Jack Kirby in the 1976-1978 comic book series "The Eternals", where the name was spelled Makarri.

Delphyne Gorgon: Delphyne Gorgon is a fictional character appearing in American comic books published by Marvel Comics.  A Gorgon member of the Amazon nation, she is a love interest of Amadeus Cho.  She first appeared in "Incredible Hercules" #121, and was created by Greg Pak, Fred Van Lente, and Clayton Henry.

Gorgon (Inhuman): Gorgon is a fictional character appearing in American comic books published by Marvel Comics.  Gorgon is also a member of the Royal Family of the Inhumans, a race of superpowered beings that inhabit the hidden city of Attilan.

Terrigen Mist: The Terrigen Mist is a fictional substance appearing in American comic books published by Marvel Comics.  Terrigen Mist is featured particularly in stories that feature the Inhumans, a fictional race of superhumans.

Eternals (comics): The Eternals are a fictional race of superhumans appearing in American comic books published by Marvel Comics.  They are described as an offshoot of the evolutionary process that created sentient life on Earth.  The original instigators of this process, the alien Celestials, intended the Eternals to be the defenders of Earth, which leads to the inevitability of war against their destructive counterparts, the Deviants.  The Eternals were created by Jack Kirby and made their first appearance in "The Eternals" #1 (July 1976).

Inhumans: The Inhumans are a fictional race of superhumans appearing in American comic books published by Marvel Comics.

Cipher (newuniversal): Cipher (Jennifer Swann) is a fictional character appearing in American comic books published by Marvel Comics.  The character appears in the newuniversal imprint of Marvel Comics, and is one of the four initial superhumans created by the White Event in 2006 (the others being Justice, Nightmask, and Star Brand).  "newuniversal", designated Earth-555 in the Marvel Comics multiverse, is a re-imagining of the New Universe imprint from the late 1980s.  The name Cipher actually refers to two things: a powerful extra-dimensional glyph (tattoo) that confers superhuman powers on a sentient being, and the name of the being that wields the glyph.  Cipher is a new superhuman created by Warren Ellis and Salvador Larroca who were inspired by the original Spitfire and the nature of the Star Brand itself (as an extra-dimensional tool of near-unlimited power), combined with strong conceptual ties to Iron Man.

Question: What is the name given to a fictional race of superhumans appearing in comics published by Marvel and which includes a Royal Family with the fictional character Gorgon in it?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "superhuman_race_name": {
      "type": "string",
      "description": "The name of the fictional superhuman race."
    },
    "publisher": {
      "type": "string",
      "description": "The publisher of the comic books featuring this race."
    },
    "royal_family_members": {
      "type": "array",
      "description": "A list of characters identified as members of the race's Royal Family.",
      "items": {
        "type": "string"
      }
    },
    "race_description": {
      "type": "string",
      "description": "A brief description of the superhuman race."
    }
  },
  "required": [
    "superhuman_race_name",
    "publisher",
    "royal_family_members",
    "race_description"
  ],
  "additionalProperties": false
}
