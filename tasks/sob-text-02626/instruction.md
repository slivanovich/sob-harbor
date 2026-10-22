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
Holy Water (Madonna song): "Holy Water" is a song recorded by American singer and songwriter Madonna for her thirteenth studio album, "Rebel Heart" (2015).  The song was written by Madonna, Martin Kierszenbaum, Natalia Keery-Fisher, Mike Dean, Kanye West and Tommy Brown.  It was produced by Madonna, Dean and West, with Charlie Heat serving as co-producer.  The demo of "Holy Water" leaked on the internet in late December 2014 and later its full version leaked in February 2015, a month prior to the album's release.  "Holy Water" is an electronica and technopop song, and it features minimalist bass stutter, ricocheting synths and "martial beats" in its instrumentation.

Tony Iommi: Anthony Frank "Tony" Iommi ( ; born 19 February 1948) is an English guitarist, songwriter and producer.  He is best known as the lead guitarist and one of the four founder members of the pioneering heavy metal band Black Sabbath, and has been the band's sole continual member and primary composer for nearly five decades.

Out of My Mind / Holy Water: "Out of My Mind / Holy Water" is a fund-raising two-track CD single from the supergroup WhoCares, a Tony Iommi and Ian Gillan collaboration, a direct continuation of the Rock Aid Armenia project.  The CD contains the single "Out of My Mind" and the song "Holy Water" with the latter using the traditional Armenian instrument, the duduk by two Armenian musicians Arshak Sahakyan and Ara Gevorgyan.

Holy Water (Bad Company album): Holy Water is the ninth studio album by the English hard rock band Bad Company, and their third with Brian Howe as lead vocalist.  The album was released on June 12, 1990.  It went platinum, selling over 1,000,000 units, and climbed to #35 on The Billboard Top Pop Albums Chart.  The first single "Holy Water", was a #1 Billboard Album Rock Track for two weeks during the Summer of '90 as the band toured the U.S. with Damn Yankees.  The single "If You Needed Somebody" became a major hit in early 1991, reaching # 16 on Billboards Hot 100 chart and #2 (for two weeks) on the Album Rock chart.  "Boys Cry Tough"(#3), "Stranger, Stranger"(#9) and "Walk Through Fire"(#28 Hot 100 chart / #14 Album Rock chart) also received substantial airplay.

Aspergillum: An aspergillum (less commonly, aspergilium or aspergil) is a liturgical implement used to sprinkle holy water.  It comes in two common forms: a brush that is dipped in the water and shaken, and a silver ball on a stick.  Some have sponges or internal reservoirs that dispense holy water when shaken, while others must periodically be dipped in an aspersorium (holy water bucket, known to art historians as a situla).

Holy water: Holy water is water that has been blessed by a member of the clergy or a religious figure.  The use for cleansing prior to a baptism and spiritual cleansing is common in several religions, from Christianity to Sikhism.  The use of holy water as a sacramental for protection against evil is common among Anglicans and Roman Catholics.

Lourdes water: Lourdes water is water which flows from a spring in the Grotto of Massabielle in the Sanctuary of Our Lady of Lourdes, France.  The location of the spring was described to Bernadette Soubirous by an apparition of Our Lady of Lourdes on 25 February 1858.  Since that time many thousands of pilgrims to Lourdes have followed the instruction of Our Lady of Lourdes to "drink at the spring and bathe in it".  Lourdes water is considered non-liturgical holy water.

Holy water font: A holy water font or stoup is a vessel containing holy water generally placed near the entrance of a church.  It is used in the Catholic Church, Anglican Church, and some Lutheran churches to make the Sign of the Cross using the holy water upon entrance of the church.  Holy water is blessed by a priest or a deacon, and many Christians believe it to be a reminder of the baptismal promises.

Bhumchu: Bhumchu (Bhum is a pot, Chum is water) is a Buddhist festival, which on the Tibetan lunar calendar is held on the 14th and 15th day of the first month, which is between February and March on the Gregorian calendar.  The Bhum or Sacred vase, according to Zigpo Lingpa, is made out of various kinds of sacred soil, water and five kinds of precious jewels found in sacred lands of India, Odiyana and Zahor.  In Sikkim the Tashiding Monastery is recognized as a sacred place.  It is believed that this place, Dakkar Tashiding in the center of four sacred caves, Sharchog Bephug in the east, Khandozangphu in the south, Dechenphug in the west and Lhari Nyingphug in the north, is meant to free you from the suffering of hell.  At the start of the year the vase is opened and the Lama or monk determines the future.  “If the water is to the brim, it foretells a year in which peace and prosperity will prevail.  If the water is over the brim and is spilling, it signifies a year with natural disaster and disturbances.  If the water level is low or almost dry it signifies famine.”  The celebration of “The Holy Water Vase” started under the rule of King Trisong Deutsonin Tibet, Guru Padmasambhava.”  It is believed that the water overflowed from the vase as a sign of a good omen and there was an earthquake.  The four guardian deities of Dharma and the gods of thirty three heavens showered flowers from the sky.”  This ritual is one of the holiest in Sikkim.  From midnight until the next day thousands are seen waiting to receive the holy water.  “A part of the holy water is distributed amongst the gathering of devotes and the pot is replenished with river water and sealed at the end of the festival to be opened only in the during next Bumchu festival.”  It is said that by taking a drop of the Bumchu water enlightenment is achieved and all of the evil spirits and distress are removed.  It is said one would somehow attain a form of Buddhahood or be born at a higher ranking in the next life.  In 2016, it will be on March 19-20.

Shivagange: Sri Honnammadevi Temple is inside the cave.  Sri Gavi Gangadhareshwara Temple is also inside the cave.  Gavi means Cave, Gangadhareshwara means Parameshwara having Gange on the top.  Every year in the month of January on the day of Sankranthi festival, the marriage function of Sri Gangadhareshwara and Sri Honnammadevi (Parvathi) is conducted.  At that time Ganga holy water will come from the rock at the top of hill and that holy water is used for the dhare ritual (solemnise) of the marriage function.

Question: What English guitarist worked on "Out of My Mind / Holy Water"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist."
    },
    "artist_role": {
      "type": "string",
      "description": "The primary role of the artist in the context of the question."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the artist."
    },
    "work_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the work the artist contributed to."
        },
        "type": {
          "type": "string",
          "description": "The type of the work (e.g., CD single)."
        }
      },
      "required": [
        "title",
        "type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_name",
    "artist_role",
    "nationality",
    "work_details"
  ],
  "additionalProperties": false
}
