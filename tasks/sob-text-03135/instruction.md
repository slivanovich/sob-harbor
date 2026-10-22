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
4 the Tears in Your Eyes: "4 the Tears in Your Eyes" is a song by Prince and The Revolution.  Prince donated this song for the album "We Are the World" after he decided not to participate in the song "We Are the World".  A rare live version of the song, used for Live Aid, was included on the album "The Hits/The B-Sides".

Crying: Crying is the shedding of tears (or welling of tears in the eyes) in response to an emotional state.  This includes anger, happiness, or sadness.  The act of crying has been defined as "a complex secretomotor phenomenon characterized by the shedding of tears from the lacrimal apparatus, without any irritation of the ocular structures", instead, giving a relief which protects from conjunctivitis.  A related medical term is lacrimation, which also refers to non-emotional shedding of tears.  Various forms of crying are known as "sobbing", "weeping", "wailing", "whimpering", "bawling", and "blubbering".

Open Your Eyes (Alter Bridge song): "Open Your Eyes" is a song by the hard rock band Alter Bridge.  The song, which is one of the band's biggest hits to date, was released as the first single off their debut album "One Day Remains" and peaked at No. 2 on the US Mainstream Rock Tracks chart in 2004, the band's highest charting single on that chart until "Isolation" reached No. 1 in 2011.  The song, "Save Me", which appears on the soundtrack for "Elektra", is also on the "Open Your Eyes" single as a b-side.  Like many songs on the album, "Open Your Eyes" is about regrets and is one of the six songs on the record co-written by singer Myles Kennedy.  The chorus seems to be encouraging peace.  Lead guitarist Mark Tremonti originally wanted "Down to My Last" to be the first single, but the record company rejected it, saying it sounded too much like Creed, the then-former band of Tremonti, bassist Brian Marshall, and drummer Scott Phillips.  "Open Your Eyes" was chosen instead.

Workingman's Savings Bank &amp; Trust Co.: The Workingman's Savings Bank & Trust Co.  Building, located at 800 East Ohio Street in the East Allegheny neighborhood of Pittsburgh, Pennsylvania, was built in 1901.  It was added to the List of City of Pittsburgh historic designations on March 10, 2009.  Formerly a Mellon Bank until 1971, the building was sold to the Catholic Diocese of Pittsburgh with plans to convert it to a church.  However, the expense of the project proved too costly and it was instead donated to the ARC House rehabilitation center network.  The building remained their headquarters from 1976 to 2006.  It is currently vacant.

26th Awit Awards: The 26th Awit Awards were held in Sequoia Hotel, Quezon City.  They honored the best of Filipino music for the year 2012.  The Philippine Association of the Record Industry decided to hold a small event, where only the winners were invited, due to the tragic Typhoon Yolanda (Haiyan) that affected the country last month.  The money to be used for the planned extravagant awards ceremony was instead donated to the calamity fund.  Being a simple ceremony, no performances occurred.

The Screen Guild Theater: The Screen Guild Theater is a radio anthology series broadcast from 1939 until 1952 during the Golden Age of Radio.  Leading Hollywood stars performed adaptations of popular motion pictures.  Originating on CBS Radio, it aired under several different titles including The Gulf Screen Guild Show, The Gulf Screen Guild Theater, The Lady Esther Screen Guild Theater and The Camel Screen Guild Players.  Fees that would ordinarily have been paid to the stars and studios were instead donated to the Motion Picture Relief Fund, and were used for the construction and maintenance of the Motion Picture Country House.

We Are the World: "We Are the World" is a song and charity single originally recorded by the supergroup United Support of Artists (USA) for Africa in 1985.  It was written by Michael Jackson and Lionel Richie (with arrangements by Michael Omartian) and produced by Quincy Jones for the album "We Are the World".  With sales in excess of 20 million copies, it is one of the fewer than 30 all-time physical singles to have sold at least 10 million copies worldwide.

Portrait of Captain Thomas Coram: Portrait of Captain Thomas Coram is a 1740 portrait of philanthropist Thomas Coram painted by William Hogarth.  The portrait, which represents Hogarth’s highest achievement in direct portraiture, was not created as a commission and was instead donated to Coram's Foundling Hospital.  The portrait is divided into two sections: The left side represents Coram's sea ventures, a major source of his wealth.  The right side shows a curtain pulled over a mother figure with a child/

With Tears in My Eyes: "With Tears in My Eyes" is a 1945 song by Wesley Tuttle and His Texas Stars.  The song was Wesley Tuttle's first and most successful entry on the Juke Box Folk Chart.  "With Tears in My Eyes" went number one for four weeks with a total of fourteen weeks on the chart.  The Paul Howard composition was also released as a posthumous Hank Williams single on MGM Records in 1957.  The late singer had recorded it in Shreveport in 1948 or 1949 as a demo or as part of a radio show at KWKH studio

Caplan Collection: The Caplan Collection of folk art and childhood artifacts is held by The Children's Museum of Indianapolis; in 1984 it was donated by Frank and Theresa Caplan, owners of the Creative Playthings toy company.  The museum began accessioning the collection in January 1985.  The collection consists of nearly 32,000 objects, from toys to dolls to games to musical instruments to masks to clothing to folk art from over 120 different countries.  The museum created a specific exhibit for the collection, entitled "Passport to the World," which opened in 1986.  Initially the Caplans had intended for the collection to be the basis of a new Museum of Fantasy and Play, but this never materialized and they donated their collection to the Children's Museum instead.  The Caplans spent about US$1 million acquiring the objects from around 1965 to 1985; some of the countries strongly represented are Japan, Mexico, Russia, Germany, Indonesia, and India.

Question: Which singer did not participate in the song "We Are the World" for Africa in 1985 but instead donated "4 the Tears in Your Eyes"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "singer_name": {
      "type": "string",
      "description": "The name of the singer who made the donation."
    },
    "song_donated": {
      "type": "string",
      "description": "The title of the song that was donated."
    },
    "donation_details": {
      "type": "object",
      "properties": {
        "album_name": {
          "type": "string",
          "description": "The name of the album the song was donated for."
        },
        "reason_for_donation": {
          "type": "string",
          "description": "The reason the song was donated instead of direct participation."
        },
        "event_year": {
          "type": "integer",
          "description": "The year the 'We Are the World' event took place."
        }
      },
      "required": [
        "album_name",
        "reason_for_donation",
        "event_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "singer_name",
    "song_donated",
    "donation_details"
  ],
  "additionalProperties": false
}
