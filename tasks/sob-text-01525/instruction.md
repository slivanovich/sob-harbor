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
Monolith of Phobos: Monolith of Phobos is the debut studio album by 'The Claypool Lennon Delirium' consisting of American multi-instrumentalists Sean Lennon and Primus' Les Claypool, released on 3 June 2016.

Purple Onion (album): Purple Onion is the only studio album by The Les Claypool Frog Brigade, released on September 24, 2002.  It followed two live releases by the band, and is the first release of the Frog Brigade's original compositions.  While the Brigade regulars are consistent on much of the record such as Jay Lane, Eenor, Skerik and new percussionist Mike "Tree Frog" Dillon, many special guests appear on the album as well.  Guests on multiple tracks include Ben Barnes and Sam Bass (then both from Deadweight).  "D's Diner," a tribute to a Sebastopol, California restaurant, features sitar player Gabby La La in addition to the triple-bass onslaught of Claypool, Norwood Fisher (Fishbone) and Lonnie Marshall (Weapon of Choice).  Warren Haynes (Allman Brothers Band) adds slide guitar on the "Buzzards of Green Hill" and Fish Fisher (Fishbone drummer) guests on "Whamola."  "Whamola" was a live show staple named after the unique instrument Les employs—a one-string bass played with a drumstick.  The song later appeared as a remix for the theme of "South Park Season 10". " Barrington Hall" is a tribute to the UC Berkeley student housing known in the 1960s-1980s for counterculture.

Les Claypool: Leslie Edward "Les" Claypool (born September 29, 1963) is an American musician, singer, songwriter, composer, author and actor best known as the bassist and lead vocalist of the band Primus.  Claypool's playing style on the electric bass mixes tapping, flamenco-like strumming, whammy bar bends, and slapping.

Colonel Claypool's Bucket of Bernie Brains: Colonel Claypool's Bucket of Bernie Brains (C2B3) was an experimental supergroup featuring bassist Les Claypool, guitarist Buckethead, keyboardist Bernie Worrell and drummer Bryan "Brain" Mantia.

Mike McColgan: Michael "Mike" McColgan is best known as the original lead singer of the American outfit Dropkick Murphys and the lead singer of the Street Dogs.

Highball with the Devil: Highball with the Devil is a studio album by Les Claypool and the Holy Mackerel, released in 1996.  "Les Claypool and the Holy Mackerel" is Claypool's first solo effort.  In addition to his usual bass guitar and vocals, he also plays most of the drums and some guitar.  He also self produced and engineered the album at his own studio, "Rancho Relaxo".  Credited musicians include Charlie Hunter on guitar for "Me and Chuck;" Marc "Mirv" Haggard on guitar on songs such as "El Sobrante Fortnight" and "Hendershot," as well as on the saw for "Precipitation"; Adam "Bob Cock" Gates on vocal; Jay Lane on drums; and Henry Rollins narrating "Delicate Tendrils."

Of Fungi and Foe: Of Fungi and Foe is the second solo album by Les Claypool.  The album was released on the March 17, 2009.  The album featured Eugene Hütz, Paulo Baldi, Mike Dillon, Lapland Miclovik, Sam Bass, Cage Claypool, and Bryonn Bain.

Of Whales and Woe: Of Whales And Woe is a solo album by Les Claypool, the bassist/vocalist of Primus.  The album was released on the May 30, 2006.  The album features Skerik (saxophonist of the Les Claypool's Fearless Flying Frog Brigade), Mike Dillon (percussionist, also of the Frog Brigade), and Gabby La La (multi-instrumentalist).  "Back off Turkey" also features Les' children, Cage and Lena.  The track "Iowan Gal" is a love song for his wife, Chaney Claypool.

Les Claypool's Fancy Band: Les Claypool's Fancy Band was a lineup of musicians on tour with Les Claypool from 2005 to 2007.  The band consisted of Claypool on bass, Skerik on tenor and baritone saxophone, Mike Dillon on vibraphone, marimba, tabla, cuíca and percussion, Gabby La La on sitar, ukulele and theremin and Paulo Baldi on drums.  The Fancy Band's first appearance was 2005.  They toured nationally in 2006 promoting the album "Of Whales and Woe".  They toured the early Summer of 2007 with the release of the DVD "Fancy".

Four Foot Shack: Four Foot Shack is the debut album of Duo de Twang, a country music duo formed by Primus bassist and vocalist Les Claypool and M.I.R.V. guitarist Bryan Kehoe.  This album contains one original song and fourteen cover songs (although many of the "covers" are Primus or Les Claypool songs).  It was released on February 4, 2014 by ATO Records.

Question: What do Mike McColgan and Les Claypool have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_names": {
      "type": "array",
      "description": "The names of the individuals being compared.",
      "items": {
        "type": "string"
      },
      "minItems": 2,
      "maxItems": 2
    },
    "common_attributes": {
      "type": "array",
      "description": "A list of attributes or roles that both individuals share.",
      "items": {
        "type": "string"
      },
      "minItems": 1
    },
    "attribute_category": {
      "type": "string",
      "description": "The category of the shared attributes (e.g., 'musical role', 'profession')."
    }
  },
  "required": [
    "person_names",
    "common_attributes",
    "attribute_category"
  ],
  "additionalProperties": false
}
