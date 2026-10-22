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
Deben (unit): Stone weights from the Old Kingdom have been found, weighing about 13.6 grams. Similar weights from the Middle Kingdom were discovered at Lisht.  From the Middle Kingdom date also "deben" weight units used for metals, referred to as copper deben and gold deben, the former being about twice as heavy (c. 23.7 grams) as the latter.

Harageh: Harageh (also el-Harageh or Haraga) is a modern village in Egypt at the entrance to the river oasis of the Fayum, close to El-Lahun.  In archaeology Harageh is mainly known for a series of cemeteries dating to several periods of Egyptian history.  Reginald Engelbach excavated these cemeteries in 1913.  The cemeteries belong to the Naqada-Period, to the First Intermediate Period, to the late Middle Kingdom and to the New Kingdom, a few Coptic stelae were discovered too.  Especially the burials of the late Middle Kingdom belonged to wealthy people.  Perhaps the people of El-Lahun were buried here.  Engelbach found stelae, inscribed coffins, canopic boxes and jars and many statues.

Round Eyes in the Middle Kingdom: Round Eyes in the Middle Kingdom is a 1995 documentary directed by Ronald Levaco, an American filmmaker who journeyed back to China, the nation of his boyhood days, to discover what became of an old friend of his family, Israel Epstein.

Middle Kingdom of Egypt: The Middle Kingdom of Egypt (also known as The Period of Reunification) is the period in the history of ancient Egypt between circa 2050 BC and 1800 BC, stretching from the reunification of Egypt under the impulse of Mentuhotep II of the Eleventh Dynasty to the end of the Twelfth Dynasty.  Some scholars also include the Thirteenth Dynasty of Egypt wholly into this period as well, in which case the Middle Kingdom would finish c. 1650, while others only include it until Merneferre Ay c. 1700 BC, last king of this dynasty to be attested in both Upper and Lower Egypt.  During the Middle Kingdom period, Osiris became the most important deity in popular religion.

In the Shadow of the Moon (film): In the Shadow of the Moon is a 2007 British documentary film about the United States' manned missions to the Moon.  It premiered at the 2007 Sundance Film Festival, where it won the World Cinema Audience Award.  In March 2008, it was the first film to win the Sir Arthur Clarke Award for Best Film Presentation.  It was given a limited release in the United States on 7 September 2007, and in Canada on 19 October 2007.  It was released on DVD in the United States on 22 February 2008, and 31 March 2008, in the United Kingdom.  It is also notable for giving Gareth Edwards (who would go on to direct "Godzilla") an early credit in visual effects.

Rifeh: Rifeh or Deir Rifeh (also known as Rifa) is a village in Egypt.  The name refers today most often to a series of Ancient Egyptian cemeteries nearby.  These are the burial grounds of the ancient town Shashotep.  The cemeteries date from the end of the First Intermediate Period to the Roman Period.  Especially important are the burials of the Middle Kingdom.  In this period Shashotep was the capital of the 11th Upper Egyptian province.  Several decorated rock cut tombs were carved into the rocky hills.  They belong to the local governors of the period.  Nakht-Khnum and Nefer-Khnum are the two whose names survived.  In front of these tombs were burials of lower officials that were working for these local governors.  One of them is the Tomb of two Brothers, that was found undisturbed and still contained an array of important artcfacts.  Further away and closer to the Nile were the burials of the more common people.  Typical for many of these burials dating to the Middle Kingdom model clay houses, once placed on top of the burial.  They are called in Egyptology "soul houses".  Further burials belong to the Second Intermediate Period and to the New Kingdom, when Shashotep was no longer the capital of a province.

Pyramidion: A pyramidion (plural pyramidia) is the uppermost piece or capstone of an Egyptian pyramid or obelisk, in archaeological parlance.  They were called "benbenet" in the Ancient Egyptian language, which associated the pyramid as a whole with the sacred benben stone.  During Egypt's Old Kingdom, pyramidia were generally made of diorite, granite, or fine limestone, which were then covered in gold or electrum; during the Middle Kingdom and through the end of the pyramid-building era, they were built from granite.  A pyramidion was "covered in gold leaf to reflect the rays of the sun"; during Egypt's Middle Kingdom, they were often "inscribed with royal titles and religious symbols."

Sheshi: Maaibre Sheshi (also Sheshy) was a ruler of areas of Egypt during the Second Intermediate Period.  The dynasty, chronological position, duration and extent of his reign are uncertain and subject to ongoing debate.  The difficulty of identification is mirrored by problems in determining events from the end of the Middle Kingdom to the arrival of the Hyksos in Egypt.  Nonetheless, Sheshi is, in terms of the number of artefacts attributed to him, the best attested king of the period spanning the end of the Middle Kingdom and the Second Intermediate period; roughly from c. 1800 BC until 1550 BC.  Hundreds of scaraboid seals bearing his name have been found throughout Canaan, Egypt, Nubia and as far away as Carthage where some were still in use 1500 years after his death.

Ameny (vizier): Ameny was an Ancient Egyptian vizier under Middle Kingdom king Amenemhat II, around 1900 BC, in the Twelfth Dynasty.  Ameny appears on the fragment of an annal stone of the king.  The fragment was found by Flinders Petrie in Memphis and mentions a statue of this vizier.  Ameny is perhaps also known from an offering table.  However, the name Ameny belongs to the most common names of the Middle Kingdom.  Therefore, the identity of both people on these objects is far from certain.

Fane of Shadows: The Fane of Shadows is a temple that journeys the worlds on the currents of the secret Weave, in the fictional setting of the Forgotten Realms campaign in "Dungeons & Dragons".  The place has many names in many tongues, and is also known as the Temple of Night or the Umbral Shrine.  Created by Shar, it serves as many dark gods of many worlds, and as a gift of the god of shadows to their faithful—a sanctuary that journeys through time and worlds.  It also serves as a bastion/armory for the servants of the twilight.  It is located within the Lightless Lake (The Moonmere) in the Gulthmere Forest, but it only materializes during a certain date at midnight, and stays only temporarily in each world for a short time.  Upon its arrival onto Toril, the Fane appeared within the depths of the Lightless Lake in a diffuse, ochre light.  The entirety of the temple is situated on an invisible platform encapsulated within a dome of air.  The architecture includes black-veined columns, graceful arches, and thick pillars all crafted from marble, basalt, obsidian, or ebony.  The Fane of Shadows is guarded by a host of shadows inside the courtyard area.  They are only hostile to those not subservient to shadow.  The courtyard contains a statue garden of hundreds of obsidian sculptures, all of them depicting the innumerable world's gods of shadow.  Statues of Toril's deities of night and shadow, Shar and Mask, are among the collection.  Beyond its doors it contains a long, wide hallway, the Grand Hall, filled with shadows and bathed in a low, green light.  Painting and mosaics line the walls, while tables and pedestals are hidden inside alcoves along it.  These alcoves usually hold an item of great power, one of the many gifts of shadow found within.  Only one gift may be taken from the Fane of Shadows.  A husky, female voice tries to persuade its guests in a perceived, familiar tongue into taking an item of power.  The Grand Hall also contains the caretaker of the temple, who materializes from the shadows.  He is an elderly man, with solid black eyes, and his duty is to serve his calling into the shadow.  The hallway ends at a pair of double doors, which leads into the inner sanctum.  The inner sanctum contains a skydome ceiling of black encrusted in gems, representing the night sky of the world in which it currently exists in.  The inner sanctum itself has a polished slate floor inlaid with an amethyst border, and in its center lies a black sphere bordered in purple, Shar's symbol.  A horsehoe-shaped altar lies in the center of the symbol on some kind of black crystalline substance, under an area of ceiling of the blackest black, depicting Shar's moon.  It is underneath this symbol where a host receives the transforming energy of the greatest gifts offered by the Shadow Weave: the transformation into a shade.  Black curtains line the walls of the inner sanctum, as well as a mosaic of the Weave Tap.  Entrance into the Fane of Shadows requires either being adept in the Shadow Weave, or reverence to a god or goddess of shadow.

Question: What do Round Eyes in the Middle Kingdom and In the Shadow of the Moon have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_media_type": {
      "type": "string",
      "description": "The common media type shared by both entities."
    },
    "entity_1_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first entity."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the first entity."
        },
        "director": {
          "type": "string",
          "description": "The director of the first entity."
        }
      },
      "required": [
        "name",
        "release_year",
        "director"
      ],
      "additionalProperties": false
    },
    "entity_2_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second entity."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the second entity."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country of origin for the second entity."
        }
      },
      "required": [
        "name",
        "release_year",
        "country_of_origin"
      ],
      "additionalProperties": false
    },
    "reason_for_commonality": {
      "type": "string",
      "description": "Explanation of why the entities are considered common."
    }
  },
  "required": [
    "common_media_type",
    "entity_1_details",
    "entity_2_details",
    "reason_for_commonality"
  ],
  "additionalProperties": false
}
