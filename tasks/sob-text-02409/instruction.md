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
NGC 5713: NGC 5713 is a peculiar, asymmetric galaxy in the constellation Virgo.  Although classified as a spiral galaxy by most galaxy catalogs, NGC 5713 galaxy is very different from most normal spiral galaxies.  While most spiral galaxies either have either two well-defined spiral arms or a filamentary spiral-like structure, this spiral galaxy has only one visible spiral arm in its disk.  This makes it a galaxy of the Magellanic type.  Gravitational interactions with the nearby spiral galaxy NGC 5719 may be responsible for producing the disturbed, asymmetric structure including the single spiral arm.

Francis Preserved Leavenworth: Francis Preserved Leavenworth (born September 3, 1858 in Mount Vernon, Indiana; died November 12, 1928; a.k.a. "Frank Leavenworth") was an American astronomer.  He discovered many New General Catalogue objects together with Frank Muller and Ormond Stone.  They used a telescope with a 66-cm aperture at the Leander McCormick Observatory at the University of Virginia in Charlottesville, Virginia.

NGC 7331: NGC 7331 (also known as Caldwell 30) is a unbarred spiral galaxy about 40 e6ly away in the constellation Pegasus.  It was discovered by William Herschel in 1784.  NGC 7331 is the brightest member of the NGC 7331 Group of galaxies.  The other members of the group are the lenticular or unbarred spirals NGC 7335 and 7336, the barred spiral galaxy NGC 7337 and the elliptical galaxy NGC 7340.  These galaxies lie at distances of approximately 332, 365, 348 and 294 million light years, respectively.  In both visible light and infrared photos of the NGC 7331, the core of the galaxy appears to be slightly off-center, with one side of the disk appearing to extend further away from the core than the opposite side.

NGC 4244: NGC 4244, also Caldwell 26, is an edge-on loose Spiral galaxy and Caldwell object in the constellation Canes Venatici.  It is part of the M94 Group (the Canes Venatici I Group), a galaxy group relatively close to the Local Group containing the Milky Way.  It shines at magnitude +10.2/+10.6.  Its celestial cooridinates are RA 12 17.5 , dec +37 ° 49′ .  It is located near a naked-eye G-class star Beta Canum Venaticorum, barred spiral galaxy NGC 4151, and irregular galaxy NGC 4214.  The galaxy lies approximately 6.5 million/14 million light years away, with a redshift of +243/493 km/s.  A nuclear star cluster and halo is located at the centre of this galaxy.

NGC 1234: NGC 1234 is a peculiar barred spiral galaxy exhibiting a ring structure in the constellation Eridanus, discovered by Francis Preserved Leavenworth in 1886.

NGC 4633: NGC 4633 is an spiral galaxy located about 70 million light-years away in the constellation of Coma Berenices.  It is interacting with the nearby galaxy NGC 4634.  NGC 4633 was discovered by astronomer Edward Swift on April 27, 1887.  It was rediscovered on November 23, 1900 by astronomer Arnold Schwassmann and was later listed as IC 3688.  NGC 4633 is a member of the Virgo Cluster.

NGC 4606: NGC 4606 is a spiral galaxy located about 55 million light-years away in the constellation of Virgo.  NGC 4606 was discovered by astronomer William Herschel on March 15, 1784.  NGC 4606 appears to be in a pair with the galaxy NGC 4607.  The galaxy is a member of the Virgo Cluster.

NGC 1614: NGC 1614 is the "New General Catalogue" identifier for a spiral galaxy in the equatorial constellation of Eridanus.  It was discovered on December 29, 1885 by American astronomer Lewis Swift, who described it in a shorthand notation as: pretty faint, small, round, a little brighter middle.  The nebula was then catalogued by Danish-Irish astronomer J. L. E. Drayer in 1888.  When direct photography became available, it was noted that this galaxy displayed some conspicuous peculiarities.  American astronomer Halton Arp included it in his 1966 "Atlas of Peculiar Galaxies".  In 1971, Swiss astronomer Fritz Zwicky described it as a "blue post-eruptive galaxy, compact patchy core, spiral plumes, long blue jet SSW".

NGC 2276: NGC 2276 is an intermediate spiral galaxy in the constellation Cepheus.  The galaxy lies 105 million light-years away from Earth.  NGC 2276 has an asymmetrical appearance, most likely caused by gravitational interactions with its neighbor, elliptical galaxy NGC 2300.  One of the many starburst spiral arms contains an intermediate mass black hole with 50,000 times the mass of the Sun, named NGC 2276-3c.  NGC 2276-3c has produced two jets: a large-scale radio jet, approximately 2,000 light years long, and an "inner jet" about 6 light years long.  The galaxy shows an enhanced rate of star formation that may have been triggered by a collision with a dwarf galaxy, or by the gravitational interaction with its neighbor compressing gas and dust.

NGC 7004: NGC 7004 is a spiral galaxy around 330 million light-years away from Earth in the constellation Indus.  NGC 7004 has an estimated diameter of 166,980 light-years.  NGC 7004 was discovered by astronomer John Herschel on October 2, 1834.  NGC 7004 is also part of a group of galaxies that contains the nearby galaxy NGC 7002.

Question: In which state was the American astronomer who discovered spiral galaxy NGC 1234 born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "astronomer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the astronomer."
        },
        "birth_location": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city where the astronomer was born."
            },
            "state": {
              "type": "string",
              "description": "The state where the astronomer was born."
            }
          },
          "required": [
            "city",
            "state"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "birth_location"
      ],
      "additionalProperties": false
    },
    "galaxy_discovered": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the galaxy discovered."
        },
        "discovery_year": {
          "type": "integer",
          "description": "The year the galaxy was discovered."
        }
      },
      "required": [
        "name",
        "discovery_year"
      ],
      "additionalProperties": false
    },
    "answer_birth_state": {
      "type": "string",
      "description": "The state where the American astronomer was born."
    }
  },
  "required": [
    "astronomer",
    "galaxy_discovered",
    "answer_birth_state"
  ],
  "additionalProperties": false
}
