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
Mansour bin Muqrin: Mansour bin Muqrin bin Abdulaziz Al Saud is a Saudi businessman, member of the House of Saud, and Advisor at the Court of the Crown Prince of Saudi Arabia.  In April 2015, he was appointed Advisor to the Custodian of the Two Holy Mosques with the rank of minister.  He is the son of Prince Muqrin al-Saud, former Crown Prince of Saudi Arabia.

King of Saudi Arabia: The King of Saudi Arabia is Saudi Arabia's head of state and absolute monarch (i.e. head of government).  He serves as the head of the Saudi royal family, the House of Saud.  The King is called the Custodian of the Two Holy Mosques (خادم الحرمين الشريفين ).  The title, which signifies Saudi Arabia's jurisdiction over the mosques of Masjid al Haram in Mecca and Al-Masjid an-Nabawi in Medina, replaced His Majesty (صاحب الجلالة ) in 1986.

Abdulaziz bin Saud Al Saud: Abdulaziz bin Saud bin Nayef bin Abdulaziz Al Saud (Arabic: عبد العزيز بن سعود بن نايف بن عبد العزيز آل سعود‎ ‎ ; born November 4, 1983) is the Minister of Interior of Saudi Arabia since 21 June 2017.  Prince Saud is a graduate of the Dhahran Ahliyyah School and King Saud University.  After King Salman came to power, Abdulaziz was appointed as an adviser to the Royal Court in various departments and later served as an adviser in the Defense Ministry.  He is the eldest son of Prince Saud bin Nayef (former Head of the Saudi Crown Prince Court) who is the eldest son of the former Crown Prince Nayef bin Abdulaziz.

Hussa bint Ahmed Al Sudairi: Hussa bint Ahmed Al Sudairi (1900–1969) was one of King Abdulaziz many spouses and the mother of King Fahd and King Salman, monarchs of Saudi Arabia.

Hamoud bin Abdulaziz Al Saud: Hamoud bin Abdulaziz al Saud was the only child of Futaimah Al-Yamania and the youngest son to live to adulthood of the founder of Saudi Arabia, King Abdulaziz ibn Saud.  Born in 1947, he died on 26 February 1994 at the age of 47 years.  He is the only one not represented in the Allegiance Council originally (later joined in similar circumstances by Prince Fawwaz upon his death) because he died without sons, only having one daughter.  Some sources say that he died in Saudi Arabia while talking with King Fahd.  He was also sometimes threatened by his brothers because he was the youngest of all his siblings.  He had a younger half-brother Jiluwi (II) who was born in 1952, but died the same year.  He was the youngest surviving son of Abdulaziz until his death in 1994, Thus, making Muqrin bin Abdulaziz the youngest-surviving son of King Abdulaziz.

Bader bin Saud bin Mohammed Al Saud: Prince Bader bin Saud bin Mohammed bin Abdulaziz bin Saud bin Faisal bin Turki Al Saud (born 27 November 1969), is a Saudi Public Affairs Writer under the nom de plume Bader bin Saud, Paratrooper Colonel at the Saudi Arabian Ministry of Interior, and previously president of the Saudi Students Clubs in the UK & Ireland.  He is now the Deputy Commander of the Public Security Training City in Al Madinah Region, Kingdom of Saudi Arabia.  His father is Prince Saud bin Mohammed Al Saud, and his mother Princess Alanoud bint Abdullah bin Abdulmohsen Alfirm.  Two of his siblings are known poets, Prince and Dr Saad Al Saud, known as “Munadi,” (the caller).  The other is Prince Abdulaziz bin Saud Al Saud, known as “Alsamir”, (the one who stays up all night) Prince Bader has six children - Prince Faisal, Prince Saud, Prince Khalid, Prince Fahad, Princess Reem and Princess Aljohara.

Abdullah of Saudi Arabia: Abdullah bin Abdulaziz Al Saud (Arabic: عبدالله بن عبدالعزيز آل سعود‎ ‎ , "‘Abd Allāh ibn ‘Abd al-‘Azīz Āl Sa‘ūd ", ] ; 1 August 1924 – 23 January 2015) was King of Saudi Arabia and Custodian of the Two Holy Mosques from 2005 to his death in 2015.

Islam in Saudi Arabia: Islam is the state religion of Saudi Arabia.  The connection between Islam and Saudi Arabia (or at least the western Hejaz region of the country) is uniquely strong.  The kingdom, which sometimes is called the "home of Islam", is the location of the cities of Mecca and Medina, where Muhammad, the messenger of the Islamic faith, lived and died, and attracts millions of Muslim Hajj pilgrims annually, and thousands of clerics and students who come from across the Muslim world to study.  The official title of the King of Saudi Arabia is "Custodian of the Two Holy Mosques"—the two being Al-Masjid al-Haram in Mecca and Al-Masjid al-Nabawi in Medina—which are considered the holiest in Islam.

Fahd of Saudi Arabia: Fahd bin Abdulaziz Al Saud, Custodian of the Two Holy Mosques (Arabic: فهد بن عبد العزيز آل سعود‎ ‎ "Fahd ibn ‘Abd al-‘Azīz Āl Sa‘ūd "; 1921 – 1 August 2005) was King of Saudi Arabia from 1982 to 2005.

Salman of Saudi Arabia: Salman bin Abdulaziz Al Saud (Arabic: ‎ ‎ , "Salmān ibn ‘Abd al-‘Azīz Āl Sa‘ūd "; born 31 December 1935) is King of Saudi Arabia, Custodian of the Two Holy Mosques, and head of the House of Saud.

Question: Who was the son of one of King Abdulaziz many spouses who's brother  is King of Saudi Arabia, Custodian of the Two Holy Mosques, and head of the House of Saud ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "identified_person_name": {
      "type": "string",
      "description": "The full name of the person identified as the answer to the question."
    },
    "person_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the identified person."
        },
        "relationship_to_king_abdulaziz": {
          "type": "string",
          "description": "The direct relationship of the identified person to King Abdulaziz."
        }
      },
      "required": [
        "name",
        "relationship_to_king_abdulaziz"
      ],
      "additionalProperties": false
    },
    "mother_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the identified person's mother."
        },
        "relationship_to_king_abdulaziz": {
          "type": "string",
          "description": "The relationship of the mother to King Abdulaziz."
        }
      },
      "required": [
        "name",
        "relationship_to_king_abdulaziz"
      ],
      "additionalProperties": false
    },
    "brother_king_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the identified person's brother who is the current King."
        },
        "relationship_to_identified_person": {
          "type": "string",
          "description": "The relationship of the King to the identified person."
        },
        "titles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The official titles held by the brother who is the current King."
        }
      },
      "required": [
        "name",
        "relationship_to_identified_person",
        "titles"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "identified_person_name",
    "person_details",
    "mother_details",
    "brother_king_details"
  ],
  "additionalProperties": false
}
