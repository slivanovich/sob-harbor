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
Boğaziçi University: Boğaziçi University (also known as Bosphorus University, Turkish: "Boğaziçi Üniversitesi" , "Boğaziçi" literally meaning Bosphorus in Turkish) is a major research university located on the European side of the Bosphorus strait in Istanbul, Turkey.  It has four faculties and two schools offering undergraduate degrees, and six institutes offering graduate degrees.  The language of instruction is English.

Kegham Kavafyan: Kegham Kavafyan (Գեղամ Գաւաֆեան, born 1888 Istanbul, Ottoman Turkey – November 30, 1959 Switzerland) was an Ottoman Armenian architect.  He is noted for his construction plans for the Süreyya Opera House in the Kadıköy district of Istanbul, Turkey.

Fatih Sultan Mehmet Bridge: The Fatih Sultan Mehmet Bridge ("Sultan Mehmed the Conqueror Bridge"), also known as the Second Bosphorus Bridge (in Turkish: "Fatih Sultan Mehmet Köprüsü", "F.S.M. Köprüsü" or "2.  Köprü"), is a bridge in Istanbul, Turkey spanning the Bosphorus strait (Turkish: "Boğaziçi").  When completed in 1988, it was the 5th-longest suspension bridge span in the world; today it is the 24th.

Bosporus Water Tunnel: The Bosphorus Water Tunnel (Turkish: "Boğaziçi Su Tüneli" ) or Bosporus aqueduct is an under sea aqueduct in Istanbul, Turkey, crossing the Bosphorus strait.  It was constructed in 2012 to transfer water from the Melen Creek in Düzce Province to the European side of Istanbul.

Bosphorus Bridge: The 15 July Martyrs Bridge (Turkish: "15 Temmuz Şehitler Köprüsü" ) or unofficially the Bosphorus Bridge (Turkish: "Boğaziçi Köprüsü" ), also called the First Bridge (Turkish: "Birinci Köprü" ), is one of the three suspension bridges spanning the Bosphorus strait (Turkish: "Boğaziçi") in Istanbul, Turkey, thus connecting Europe and Asia (alongside Fatih Sultan Mehmet Bridge and Yavuz Sultan Selim Bridge).  The bridge extends between Ortaköy (in Europe) and Beylerbeyi (in Asia).

Yavuz Sultan Selim Bridge: The Yavuz Sultan Selim Bridge (Turkish: "Yavuz Sultan Selim Köprüsü" ) is a bridge for rail and motor vehicle transit over the Bosphorus strait, to the north of two existing suspension bridges in Istanbul, Turkey.  It was initially named the Third Bosphorus Bridge (with Bosphorus Bridge being the First Bosphorus Bridge and Fatih Sultan Mehmet Bridge the Second Bosphorus Bridge).  It is about 5 km north of the Bosphorus Bridge.  The bridge is located near the Black Sea entrance of the Bosphorus strait, between Garipçe in Sarıyer on the European side and Poyrazköy in Beykoz on the Asian side.

Süreyya Opera House: Süreyya Opera House, also called Süreyya Cultural Center (Turkish: "Süreyya Operası or Süreyya Kültür Merkezi" ), is an opera hall located in Kadıköy district of Istanbul, Turkey.  The building is designed by Armenian architect Kegam Kavafyan by order of a Deputy for Istanbul Süreyya İlmen, it was originally established in 1927 as the first musical theatre on the Anatolian part of Istanbul.  However, due to lack of appropriate facilities and equipment in the theatre, operettas were never staged.  The venue was rather used as a movie theatre until the building underwent a functional restoration and reopened as an opera house by the end of 2007.

Bosphorus: The Bosphorus ( or ) or Bosporus ( ; Ancient Greek: Βόσπορος , "Bósporos"; Turkish: "Boğaziçi" , ] ) is a narrow, natural strait and an internationally significant waterway located in northwestern Turkey.  It forms part of the continental boundary between Europe and Asia, and separates Asian Turkey from European Turkey.  The world's narrowest strait used for international navigation, the Bosphorus connects the Black Sea with the Sea of Marmara, and, by extension via the Dardanelles, the Aegean and Mediterranean Seas.

Feza Gürsey Institute: Feza Gürsey Institute (Turkish: "Feza Gürsey Enstitüsü" ) is a joint institute of Boğaziçi University and TÜBİTAK (Scientific and Technological Research Council of Turkey) on physics research, founded in 1983 by Erdal İnönü with the name "Research Institute for Basic Sciences".  It now continues as the "Feza Gürsey Institute", having been renamed in honor of Feza Gürsey, a distinguished Turkish physicist.  The institute is located within the Kandilli Campus of the Boğaziçi University in Istanbul, Turkey.  Currently it hosts researchers in mathematics and theoretical physics.

Boğaziçi Üniversitesi (Istanbul Metro): Boğaziçi Üniversitesi, formerly named Hisarüstü, is an underground rapid transit station on the M6 line of the Istanbul Metro.  It is located in northeast Beşiktaş under Hisar Üstü Nispetiye Avenue.  The station is named after the Boğaziçi University which is located right next to it.  An aerial tramway is planned between Hisarüstü and Aşiyan, on the Bosphorus.

Question: Are Boğaziçi University and the Süreyya Opera House located on the same side of Bosphorus strait?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entities_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "location_side": {
            "type": "string",
            "enum": [
              "European",
              "Asian"
            ]
          }
        },
        "required": [
          "name",
          "location_side"
        ],
        "additionalProperties": false
      }
    },
    "strait_name": {
      "type": "string"
    },
    "are_on_same_side": {
      "type": "boolean"
    }
  },
  "required": [
    "entities_compared",
    "strait_name",
    "are_on_same_side"
  ],
  "additionalProperties": false
}
