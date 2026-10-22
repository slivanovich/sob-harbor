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
Kalantaka: Kalantaka (Sanskrit: कालान्तक, "ender of death and time") is an aspect of the Hindu god Shiva as the Conqueror of Time and Death, itself personified by the god Yama.  He is depicted as defeating or killing Yama when the latter comes to take the life of Shiva's devotee Markandeya.  Shiva is often depicted as dancing on Death, personified by Yama.  This incident is believed as happened at Triprangode, Tirur, Malappuram district, Kerala where the Kalasamharamurthy Temple is situated.  Another chief temple dedicated to Kalantaka is situated at Thirukkadavoor, Tamil Nadu of South India, however the Kalantaka icon is found sculpted in many Shiva temples in the South.

Vahana: Vahana (Sanskrit: वाहन , Vāhana , literally "that which carries, that which pulls") denotes the being, typically an animal or mythical entity, a particular Hindu deity is said to use as a vehicle.  In this capacity, the vahana is often called the deity's "mount".  Upon the partnership between the deity and his vahana is woven much iconography and mythology.  Deities are often depicted riding (or simply mounted upon) the vahana.  Other times, the vahana is depicted at the deity's side or symbolically represented as a divine attribute.  The vahana may be considered an accoutrement of the deity: though the vahana may act independently, they are still functionally emblematic or even syntagmatic of their "rider".  The deity may be seen sitting or standing on the vahana.  They may be sitting on a small platform called a "howdah", or riding on a saddle or bareback.  "Vah" in Sanskrit means "to carry" or "to transport".

Han Xiangzi: Han Xiangzi, courtesy name Qingfu or Beizhu, is a Chinese mythological figure and one of the Eight Immortals in the Taoist pantheon.  He studied Taoist magical arts under the tutelage of Lü Dongbin, another of the Eight Immortals.  Han Xiangzi is often depicted carrying a "dizi" (Chinese flute), so he is also regarded as the patron deity of flutists.  He is also believed to be the composer of the Taoist musical piece "Tian Hua Yin" (天花引).

Shaneshwar Sansthan: Shaneshwar Sansthan is the open temple of Lord Shree Shani in Dombivli near Mumbai city.  Here Shani Sansthan means a spiritual organisation established for Lord Shree Shani.  This Sansthan was established by the spiritual master Sadguru Shree Omkar Maharaj on 15 January 2008.  Thousands of devotees from all over Mumbai city daily visit this temple to get blessings of the Lord Shree Shani.

Marundeeswarar temple, Thirukachur: Marundeeswarar Temple is a Hindu temple dedicated to the deity Shiva, located in Thirukachur, a village in Kanchipuram district in the South Indian state of Tamil Nadu.  Shiva is worshipped as Marundeeswarar, and is represented by the "lingam".  His consort Parvati is depicted as Balambigai.  The presiding deity is associated with the 7th century Tamil Saiva Nayanars Sundarar.  The temple is counted as a twin temple along with Kachabeswarar temple located in the same village.

Kachabeswarar temple, Thirukachur: Kachabeswarar Temple, Thirukachur (கச்சபேஸ்வரர் கோயில், திருக்கச்சூர்) is a Hindu temple dedicated to the deity Shiva, located in Thirukachur, a village in Kanchipuram district in the South Indian state of Tamil Nadu.  Shiva is worshipped as Kachabeswarar, and is represented by the "lingam".  His consort Parvati is depicted as Antanatchi and Kanniyumaiyal.  The presiding deity is revered in the 7th century Tamil Saiva canonical work, the "Tevaram", written by Tamil saint poets known as the Nayanars and classified as "Paadal Petra Sthalam".  The temple is counted as a twin temple along with Marundeeswarar Temple located in the same village.

Bhaktajaneswarar temple: Bhaktajaneswarar Temple (பக்தஜனேஸ்வரர் கோயில்) (also called Thirunavalur Temple) is a Hindu temple dedicated to the deity Shiva, located in Poondi, a village in Viluppuram district in the South Indian state of Tamil Nadu.  Shiva is worshiped as Bhaktajaneswarar, and is represented by the "lingam".  His consort Parvati is depicted as Manonmani Amman.  The temple is located on the Panruti - Kedilam road.  The presiding deity is revered in the 7th century Tamil Saiva canonical work, the "Tevaram", written by Tamil saint poets known as the nayanmars and classified as "Paadal Petra Sthalam".  The temple is closely associated with Sundarar, whos is believed to have attained grace at this place.

Shani: Shani (Sanskrit: शनि , Śani ) refers to planet Saturn, and is one of the 9 heavenly objects known as Navagraha in Hindu astrology.  Shani is also a male deity in the Puranas, whose iconography consists of a handsome dark (black) figure carrying a sword (or another weapon) and sitting on a buffalo (or crow or vulture).

Infant Jesus Church, Dombivli: Infant Jesus Church, Dombivli is church dedicated to Infant Jesus, and situated in Dombivli in Kalyan taluka of Thane district, near Mumbai.

Tejashree Pradhan: Tejashri Pradhan is a Marathi television and film actress.  She is Originally from the town of Dombivli near Mumbai, she debuted in TV Serial by Hya Gojirvanya Gharat, later She played lead role in Lek Ladki.  However, she truly found big fame with the role of Janhvi in super-hit serial on Zee Honar Sun Me Hya Gharchi, in which she paired with Shashank Ketkar, who played the role of Shree.  she worked in several movies like Zenda, Sharyat, Lagna Pahave Karun, Dr. Prakash Baba Amte - The Real Hero and Ti Saddhya Kay Karte.

Question: Which deity, who is often depicted carrying a sword and sitting on a buffalo, has a temple dedicated to them in Dombivli near Mumbai?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "deity_name": {
      "type": "string",
      "description": "The name of the deity."
    },
    "deity_iconography": {
      "type": "object",
      "properties": {
        "main_weapon": {
          "type": "string",
          "description": "The primary weapon carried by the deity."
        },
        "main_mount": {
          "type": "string",
          "description": "The primary animal or entity the deity sits on."
        },
        "other_mounts": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other possible mounts for the deity."
        }
      },
      "required": [
        "main_weapon",
        "main_mount"
      ],
      "additionalProperties": false
    },
    "temple_details": {
      "type": "object",
      "properties": {
        "temple_name": {
          "type": "string",
          "description": "The name of the temple dedicated to the deity."
        },
        "temple_location": {
          "type": "string",
          "description": "The specific location of the temple."
        },
        "nearby_city": {
          "type": "string",
          "description": "The major city near the temple's location."
        }
      },
      "required": [
        "temple_name",
        "temple_location",
        "nearby_city"
      ],
      "additionalProperties": false
    },
    "is_temple_in_specified_location": {
      "type": "boolean",
      "description": "Indicates if a temple for the deity is found in the specified location (Dombivli near Mumbai)."
    }
  },
  "required": [
    "deity_name",
    "deity_iconography",
    "temple_details",
    "is_temple_in_specified_location"
  ],
  "additionalProperties": false
}
