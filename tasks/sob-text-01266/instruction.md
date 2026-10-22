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
Will Kemp (actor, born 1977): William "Will" Kemp (born 29 June 1977) is an English actor and dancer.

Slumber (film): Slumber is an upcoming American-British supernatural horror-thriller film directed by Jonathan Hopkins and co-written by Richard Hobley and Hopkins.  The film stars Maggie Q, Will Kemp, Sylvester McCoy and William Hope.  Principal photography began on February 11, 2016 in UK.

Allegra Fuller Snyder: Allegra Fuller Snyder is a dance ethnologist (ethnochoreologist), choreographer, professor and author specializing on dance and culture.  Her research focuses on dances among Native American tribes particularly the Yaqui, and on dance among several ethnic groups in Africa and Asia.  She is Professor Emerita of dance ethnology from the University of California at Los Angeles (UCLA).

Ohangla dance: Ohangla is a traditional dance among the Luo community.  It was used to celebrate weddings and also in funeral ceremony as part of Tero Buru.  Ohangla consists of more than 8 drums hit by a stick and a cylindrical shoulder slung drum played normally to the accompaniment of flute, Nyatiti or kinanda.Tony Nyadundo, Osogo Winyo and Onyi Papa Jey are among the best known Ohangla musicians.The original Ohangla has very fast tempo nature and vulgar messages convey in the music.  Local elders used to ban ohangla music in the early 80’s.  Because the music was meant for adults.  “the songs can only be interpreted by very intelligent or mature people, but not children or teenagers” says Juma Oketch a ohangala band vocalist based in Nairobi.

Egg dance: An egg dance is a traditional Easter game in which eggs are laid on the ground or floor and the goal is to dance among them damaging as few as possible.  The egg was a symbol of the rebirth of the earth in Pagan celebrations of spring and was adopted by early Christians as a symbol of the rebirth of man at Easter.

Bulbul Chowdhury: Rashid Ahmed Chowdhury (January 1, 1919 – May 17, 1954; known by his stage name Bulbul Chowdhury) was a Bengali dancer of British India, and later East Pakistan.  He is primarily regarded as a pioneer of modern dance in Bangladesh, as a founding figure of dance among the conservative Muslim community.

Delta Chi Xi: Delta Chi Xi Honorary Dance Fraternity (ΔΧΞ), more commonly referred to as Delta Chi Xi, is a co-ed honorary professional fraternity and member of the Professional Fraternity Association organized to acknowledge academic excellence, serve the community, and share the art of dance among fellow students.

Electronic markets: Electronic markets (or electronic marketplaces) are information systems (IS) which are used by multiple separate organizational entities within one or among multiple tiers in economic value chains.  In analogy to the market concept which can be viewed from a macroeconomic (describing relationships among actors in an economic systems, e.g. a monopoly) as well as from a microeconomic (describing different allocation mechanisms, e.g. public auctions of telephone frequencies) perspective, electronic markets denote networked forms of business with many possible configurations:

National innovation system: The National Innovation System (also NIS, National System of Innovation) is the flow of technology and information among people, enterprises and institutions which is key to the innovative process on the national level.  According to innovation system theory, innovation and technology development are results of a complex set of relationships among actors in the system, which includes enterprises, universities and government research institutes.

Nabichum: Nabichum (literally 'butterfly dance') is a Korean Buddhist dance ("Jakbeop") for ritual service.  The dance is named after its choreography and costume which resemble the appearance of butterfly ("nabi" in Korean).  Some people regard nabichum as the most representative and important dance among Korean Buddhist dances.  Dancers wear "jangsam" (장삼: monks robe) and white "gokkal" (꼬깔: a peaked hat).

Question: who is a dance among actors of Slumber?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who is also a dancer."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film the actor is associated with."
    },
    "actor_profession": {
      "type": "string",
      "description": "A description of the actor's profession, including their dance background."
    },
    "is_dancer": {
      "type": "boolean",
      "description": "Indicates whether the identified person is a dancer."
    }
  },
  "required": [
    "actor_name",
    "film_title",
    "actor_profession",
    "is_dancer"
  ],
  "additionalProperties": false
}
