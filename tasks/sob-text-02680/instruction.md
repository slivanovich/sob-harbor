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
Syra Shehroz: Syra Yousuf Khan, better known as Syra Shehroz (Urdu: ‎ ), is a Pakistani model and actress and former VJ who works in Pakistani serials and telefilms.  She is best known for her role in Hum TV serial "Mera Naseeb" (2011).

Geo Entertainment: Geo Entertainment or Geo Drama is a Pakistani entertainment television channel owned by Geo Television Network was established in May 2002.  Its test transmission started on 14 August 2002 on the PAS 10 digital satellite whereas on 1 October 2002 the regular transmission of Geo Entertainment was started.

Geo Kahani: GEO Kahani (Urdu:) is an entertainment channel of GEO network, broadcasting in Urdu Language.  Title song of channel is sung by Rahat Fateh Ali Khan.  The most popular dramas are the "Kumkum Bhagya", "Muhteşem Yüzyıl" (Urdu dub title: "Mera Sultan") and "Jodha Akbar".  Geo Kahani began its transmission in the U.K. from 11 August 2017, ending the 4 year run of Geo Tez.

AAG TV: AAG TV (Urdu: ‎ "lit."  fire is a youth entertainment channel in Pakistan, owned by Independent Media Corporation.  Launched in 2006 by Geo Television Network, it was associated with Fire Records, a now defunct record label in Pakistan.  Certain notable artists within the Pakistani music industry were signed by Fire Records.  In 2013, Aag TV shut down in the United Kingdom and Ireland, and was replaced by Geo Tez.  Now it is only available in the USA.

Geo Films: Geo Films is a film distribution company owned by Geo Television Network based in Karachi, Pakistan.  Geo films distribute Hollywood, Bollywood and Lollywood films in cinemas across Pakistan.

Geo TV: Geo TV (trademarked "GEO TV") or Geo Television is a Pakistani television channel established in May 2002 and owned by the Independent Media Corporation.  The channel began test transmission on 14 August 2002, with regular transmission beginning 1 October 2002.  It was later renamed Geo Entertainment.  "Geo" is an Urdu word meaning "Live".

Bikhra Mera Naseeb: Bikhra Mera Naseeb is a 2014 Pakistani drama serial directed by Furqan Khan, produced by A&B Entertainment and written by Saima Younus.  The drama stars Ayeza Khan, Sami Khan, Alizey Rasool and Emaad Irfani in lead roles.  The drama was first aired 2 May 2014 on Geo Entertainment.

Imran Abbas: Imran Abbas Naqvi is a Pakistani actor and former model.  He is known for his leading roles in television serials including "Meri Zaat Zarra-e-Benishan" (2011), "Khuda Aur Muhabbat" (2011), "Mera Naseeb" (2011), "Piya Kay Ghar Jana Hai" (2012), "Dil-e-Muztar" (2013), "Shadi Aur Tum Say? " (2013), "Alvida" (2015), and "Mera Naam Yusuf Hai" (2015).  Abbas made his film debut with a leading role in the 2013 romantic drama "Anjuman".  The following year, he appeared in Bollywood's monster horror film "Creature 3D", which earned him Filmfare Award for Best Male Debut nomination.

The Awaien Show: The Awaien Show (pronounced Ay-Ween), created by Omer Ikram, is a Pakistani parody show than ran on GEO Television Network during 2008.  It initially started as a sports commentary show, coinciding with the Indian Premier League.  The episodes were a success, and there were calls for the show's continuation.  On 13 November, the first episode was aired on GEO TV.  The show went on to air on three channels owned by the GEO Television Network, GEO Entertainment, GEO News And AAG TV.  The show consists of different skits, poking fun at public figures and current affairs, though it has a constantly changing format.  The recurrent crew consists of Omer Ikram, who acts as a host, and Mir Muhammad Ali, a versatile actor who does every parody on the show, and a special guest in each episode.  The show was canceled in 7 June 2009.

Mera Naseeb: Mera Naseeb (Urdu: , English: My Fate‎ ) is a Hum TV drama which aired from 1 April 2011 to 26 August 2011.  The drama featured a huge ensemble star cast including Samina Peerzada, Sakina Samoo, Rubina Ashraf, Bushra Ansari, Shagufta Ejaz, Durdana Butt, Sajid Hassan, Adeel Hussain, Imran Abbas, Imran Aslam, Syra Yousuf, Sanam Saeed, Rehan Sheikh, Ali Afzal and Sabahat Bukhari.  Indian-American author Chitra Banerjee Divakaruni has accused the writers of the show of plagiarizing her novel "Sister of My Heart" for the story of the serial.  She has also threatened to take legal action against the writers of the show.  However the screenplay writer had mentioned earlier before the show's original run that it is a drama adaptation of a story provided to them.  Only recently it was mentioned the screenplay writers had no prior knowledge a plagiarized work was being provided to them to work with.

Question: The serial drama Bikhra Mera Naseeb, written by Saima Youmkus, made it's debut on what Pakastani television channel, which is owned by Geo Television Network?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "drama_serial_title": {
      "type": "string",
      "description": "The title of the drama serial."
    },
    "writer": {
      "type": "string",
      "description": "The writer of the drama serial."
    },
    "debut_channel": {
      "type": "string",
      "description": "The name of the television channel where the drama serial debuted."
    },
    "channel_owner": {
      "type": "string",
      "description": "The network that owns the debut channel."
    },
    "debut_date": {
      "type": "string",
      "description": "The date when the drama serial was first aired."
    }
  },
  "required": [
    "drama_serial_title",
    "writer",
    "debut_channel",
    "channel_owner",
    "debut_date"
  ],
  "additionalProperties": false
}
