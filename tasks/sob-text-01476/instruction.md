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
Jonah Jenkins: Jonah Jenkins is/was the vocalist in the following bands:

Scrotum Grinder: Scrotum Grinder was an American hardcore punk band from Tampa, Florida.  The band consisted of people who also were/are members of the following bands: Assück, Slap Of Reality, Failure Face, Hankshaw, Watermark 6000 and In/humanity, to name a few.

Piedra Roja: Piedra Roja was a music festival in Chile noted as an expression of the hippie counterculture in South America.  Following the success of Woodstock, a similar music festival was held in Chile between 10 and 12 October 1970 in the eastern area of Santiago.  Among others, the following bands performed in the festival: Aguaturbia, Los Blops, Lágrima Seca and Los Jaivas.  Similarly to Woodstock, chaos marked the festival, involving problems with sound, drugs and delinquency.  The festival showed for the first time that the young population in Chile during that time was a group to reckon with.  It also showed the increasing social tension that would end in the ascension of Pinochet.

LostAlone: LostAlone were a British rock band from Derby, Derbyshire formed in 2005.  The band consisted of Steven Battelle (lead vocals, guitar), Alan Williamson (bass guitar, backing vocals), and Mark Gibson (drums, percussion, backing vocals).

Ricky Ball: Ricky Ball is a musician from New Zealand.  He played drums in the following bands: the Beatboys, the Courtiers, Challenge, Ticket, Jimmy Sloggett Band, Tommy Ferguson's Goodtime Band, Rainbow, Hello Sailor, Woody, the Pink Flamingos (briefly, at the beginning) and Beaver.

G.a.s. Drummers: G.a.s. Drummers was a melodic hardcore band formed in Jerez de la Frontera, Spain at the end of 1997 by three teenagers who stood out from their other students due to their colourful hair dies and their taste in the california punk rock bands such as Bad Religion, Operation Ivy, NOFX, Lagwagon, The Descendents etc.  Original members from other small local bands Dani Llamas (guitar and vocals), Pakomoto (Bass and vocals) and Rafa Camison (Drums) started playing together and composing their own music and after one year of sending demos around the country they got put as the opening act for Swedish Punk Rock band Randy on their Spanish tour.  A tour that took the band through the whole country helping a lot of Spanish kids discover that there were actually Spanish bands capable of sounding as good as some of their favorite American bands.  This lead immediately the band to sign to a young record label called Slide Chorus Records a young emerging record label from Madrid which would start releasing albums for other Spanish Punk Rock bands.  This first release titled Proud To Be Nothing hit the streets at the end of 1999 and was presented on their first European tour which covered Spain, Great Britain, France and the Netherlands amongst Spanish punk rock legend[P.P.M.

Everclear (band): Everclear is an American rock band formed in Portland, Oregon in 1991.  The band was formed by Art Alexakis, the band's lead songwriter, vocalist, and guitarist; and for most of the band's height of popularity, consisted of Craig Montoya on bass guitar and Greg Eklund on drums.  After the limited release of their independently released debut album, "World of Noise", the band found success with their first three albums on Capitol Records: "Sparkle and Fade", "So Much for the Afterglow", and "", which were all certified platinum in sales.  However, the following two albums "" and "Slow Motion Daydream", were not as well received, and as sales suffered, Montoya and Eklund left the band shortly after in 2003.

Lisle Kinney: Lisle Kinney is a musician from New Zealand.  His full name is David Lisle Kinney.  From 1967 onwards he was a semi-professional musician, playing mainly in cabaret bands.  He played bass in the following bands: October while at the University of Auckland (Graham Brazier was also in October); Brown Street, the resident band at the Great Northern Hotel; Hello Sailor and DD Smash.  He had to leave DD Smash after a road accident.  After this however, Lisle played Bass with Sonny Day in the Coromandel "Better start saving up" tour of '87.

The Lost Tapes of Cogumelo: The Lost Tapes of Cogumelo is a seminal compilation released by the Brazilian label Cogumelo Records in 1990 which includes the following bands: Overdose, Holocausto, Sarcófago, Sepultura, Mutilator, and Chakal.

Tore Stjerna: Tore Gunnar Stjerna (a.k.a. Necromorbus) has played guitar and drums in the following bands; Watain, Chaos Omen, Corpus Christii, Funeral Mist, Ofermod, Zavorash, Desolation, In Aeternum.  He is also a producer who owns Necromorbus Studio.

Question: Which of the following bands ; Everclear or LostAlone, were formed in Britain in 2005?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_bands": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Bands mentioned in the question for comparison."
    },
    "formation_criteria": {
      "type": "object",
      "properties": {
        "country": {
          "type": "string",
          "description": "The country criterion for band formation."
        },
        "year": {
          "type": "integer",
          "description": "The year criterion for band formation."
        }
      },
      "required": [
        "country",
        "year"
      ],
      "additionalProperties": false,
      "description": "Criteria specified in the question for band formation."
    },
    "matching_band_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the band that matches the criteria."
        },
        "formation_country": {
          "type": "string",
          "description": "The country where the matching band was formed."
        },
        "formation_year": {
          "type": "integer",
          "description": "The year when the matching band was formed."
        }
      },
      "required": [
        "name",
        "formation_country",
        "formation_year"
      ],
      "additionalProperties": false,
      "description": "Details of the band that satisfies the given criteria."
    },
    "match_found": {
      "type": "boolean",
      "description": "Indicates whether a band matching the criteria was found."
    }
  },
  "required": [
    "question_bands",
    "formation_criteria",
    "matching_band_details",
    "match_found"
  ],
  "additionalProperties": false
}
