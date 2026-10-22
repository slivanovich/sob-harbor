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
Alexa Meade: Alexa Meade (born 1986) is an American installation artist best known for her portraits painted directly onto the human body and inanimate objects in a way that collapses depth and makes her models appear two-dimensional when photographed.  What remains is "a photo of a painting of a person, and the real person hidden somewhere underneath."  She takes a classical concept — trompe l'oeil, the art of making a two-dimensional representational painting look like a real three-dimensional space — and turns it on its head by doing the opposite, making real life appear to be a painting.

Kasongo Ilunga: Andre Kasongo Ilunga (allegedly born 20 October 1972) was supposedly the Vice-President of the UNAFEC party and the Minister for Foreign Trade of the Democratic Republic of the Congo for much of 2007, despite doubts on whether or not he ever actually existed as a real person.  Although a member of the UNAFEC party selected by Prime Minister Antoine Gizenga, he failed to appear at the opening of the new Government, and never claimed his office.  As a result, Kasongo Ilunga is now considered by the local media and the international community to have been an imaginary person, most likely created by Kisimba Ngoy, leader of the UNAFEC party, as a part of a plan to win the lucrative role for himself.

Real person fiction: Real person fiction or real people fiction (RPF) is a genre of writing similar to fan fiction, but featuring celebrities or other real people.  In the past, terms such as actorfic were used to distinguish such stories from those based on fictional characters from movies or television series.

Political decoy: A political decoy is a person employed to impersonate a politician, to draw attention away from the real person or to take risks on that person's behalf.  This can also apply to military figures, or civilians impersonated for political or espionage purposes.

Nefermaat: Nefermaat I was an Egyptian prince, a son of pharaoh Sneferu.  He was a vizier possessing the titles of the king's eldest son, royal seal bearer, and prophet of Bastet.  His name means "Maat is beautiful" or "With perfect justice".

Angular house: The first house, of which the cusp is often (but not always) the Ascendant, signifies the person in the chart, his or her personality, and his or her behaviour.  Quite often, the Ascendant can overshadow a person's Sun sign.  For example, a person who has Leo on the cusp of his or her first house and Virgo as his or her Sun sign can be quite dynamic and dramatic, but the fastidious, efficient, self-effacing part of him- or herself will not be readily apparent until people are able to pierce through the persona and see the real person.

Creed Bratton (character): Creed Rowland Bratton, also known as "William Charles Schneider" (claims to have been born November 1, 1925) is a fictional character from the U.S. television series "The Office".  Confusion may arise from the fact that the character is played by the musician of the same name, Creed Bratton.  The fictional Creed is partially based on the experiences and former flower child lifestyle of the real one; however, the character is an embellished version of the real person.  Unlike most characters of this version of "The Office", he has no equivalent in the original BBC series despite sharing similar lines in the pilot episode with the character of Ryan Howard.  Series writer B. J. Novak has said that the actual Creed Bratton is exactly like the character he plays, except that the real Creed is a good-hearted and likable person, while his fictional alter ego has a very dark side to him.  His resourcefulness and duplicity are his defining traits along with his senile behavior and ignorance of the modern world.

Bastet: Bastet was a goddess in ancient Egyptian religion, worshiped as early as the 2nd Dynasty (2890 BCE).  As Bast, she was the goddess of warfare in Lower Egypt, the Nile River delta region, before the unification of the cultures of ancient Egypt.  Her name is also translated as Baast, Ubaste, and Baset.  In Greek mythology, she is also known as Ailuros (Greek for "cat", αἴλουρος).

Actor: An actor (often actress for females; see terminology) is a person who portrays a character in a performance.  The actor performs "in the flesh" in the traditional medium of the theatre, or in modern mediums such as film, radio, and television.  The analogous Greek term is ( ), literally "one who answers".  The actor's interpretation of their role pertains to the role played, whether based on a real person or fictional character.  Interpretation occurs even when the actor is "playing themselves", as in some forms of experimental performance art, or, more commonly; to act, is to create, a character in performance.

Sgt. Slaughter (G.I. Joe): Sgt. Slaughter is a fictional character from the toyline series.  G.I. Joe used the persona of the professional wrestler of the same name as a model for their character.  Though the original G.I. Joe was based on the real life Sgt. Alvin York, Sgt. Slaughter was the first G.I. Joe figure accurately based on a real person (Chicago Bears defensive tackle William "The Refrigerator" Perry was the second).  Sgt. Slaughter was also the most successful toy character, with several versions of his toy action figure being released.  Unlike other real-person action figures, Sgt. Slaughter's toy version makes no reference to its real-life inspiration, although the figure does have wrestling moves.  The real-life Sgt. Slaughter also did the voice for the cartoon character, and appeared in person for introductions to the episodes that were originally "".  He was also the spokesman for the G.I. Joe toys from 1989 to early 1990, introducing the new vehicles and figures.

Question: Which of these Egyptians was a real person, Nefermaat or Bastet?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "real_person_identified": {
      "type": "string",
      "description": "The name of the Egyptian identified as a real person."
    },
    "is_real_person": {
      "type": "boolean",
      "description": "True if the identified entity is a real person, false otherwise."
    },
    "identified_person_role": {
      "type": "string",
      "description": "The primary role or status of the real person as described in the context."
    },
    "other_entity_name": {
      "type": "string",
      "description": "The name of the other entity mentioned in the question."
    },
    "other_entity_nature": {
      "type": "string",
      "description": "The nature of the other entity (e.g., deity, fictional character) explaining why it is not a real person."
    }
  },
  "required": [
    "real_person_identified",
    "is_real_person",
    "identified_person_role",
    "other_entity_name",
    "other_entity_nature"
  ],
  "additionalProperties": false
}
